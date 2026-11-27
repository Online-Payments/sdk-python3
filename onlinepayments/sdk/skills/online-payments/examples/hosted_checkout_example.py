import hmac
import logging
import time
from urllib.parse import urlencode

from onlinepayments.sdk.api_exception import ApiException
from onlinepayments.sdk.communication.communication_exception import CommunicationException
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.create_hosted_checkout_request import CreateHostedCheckoutRequest
from onlinepayments.sdk.domain.create_hosted_checkout_response import CreateHostedCheckoutResponse
from onlinepayments.sdk.domain.hosted_checkout_specific_input import HostedCheckoutSpecificInput
from onlinepayments.sdk.domain.order import Order
from onlinepayments.sdk.domain.order_references import OrderReferences
from onlinepayments.sdk.merchant.i_merchant_client import IMerchantClient
from onlinepayments.sdk.reference_exception import ReferenceException

from app_types import OrderPaymentState, OrderStore
from payment_status_example import PaymentStatusExample

logger = logging.getLogger(__name__)


class HostedCheckoutExample:

    # public_base_url: the absolute public URL of your shop, from configuration (see required_public_base_url).
    def __init__(self, merchant: IMerchantClient, orders: OrderStore, public_base_url: str):
        self.__merchant = merchant
        self.__orders = orders
        self.__public_base_url = public_base_url

    # [START hosted-checkout-create]
    # The base URL comes from configuration, never from the request's Host header, which the sender controls.
    # urlencode escapes the order reference, so it cannot add or change query parameters.
    def build_return_url(self, order_id: str) -> str:
        return f"{self.__public_base_url.rstrip('/')}/return?{urlencode({'orderId': order_id})}"

    # Returns the URL to redirect the customer to.
    def start_checkout(self, order_id: str, amount_in_cents: int, currency_code: str) -> str:
        amount_of_money = AmountOfMoney()
        amount_of_money.amount = amount_in_cents
        amount_of_money.currency_code = currency_code

        references = OrderReferences()
        references.merchant_reference = order_id

        order = Order()
        order.amount_of_money = amount_of_money
        order.references = references

        hosted_checkout_input = HostedCheckoutSpecificInput()
        hosted_checkout_input.return_url = self.build_return_url(order_id)
        hosted_checkout_input.locale = "en-GB"

        request = CreateHostedCheckoutRequest()
        request.order = order
        request.hosted_checkout_specific_input = hosted_checkout_input

        response = self.create_with_retry(request)
        if response.hosted_checkout_id is None or response.returnmac is None or response.redirect_url is None:
            raise RuntimeError(f"Incomplete hosted checkout response for order {order_id}")

        # Store both values with the order before the customer leaves your site.
        self.__orders.save_hosted_checkout(order_id, response.hosted_checkout_id, response.returnmac)

        # Redirect to this URL exactly as returned. Do not build it from partial_redirect_url.
        return response.redirect_url
    # [END hosted-checkout-create]

    # [START hosted-checkout-retry]
    # CreateHostedCheckout does not support idempotent requests: the platform ignores an idempotence key, so every
    # resend creates a new session. That is harmless until the customer pays in it; the unused session expires.
    # Send it again after no answer or after an error marked retriable. The waiting happens inside the customer's
    # request, so the browser waits too: keep the attempts few and the delays short, or move the call to a
    # background job.
    def create_with_retry(self, request: CreateHostedCheckoutRequest) -> CreateHostedCheckoutResponse:
        attempt = 1
        while True:
            try:
                return self.__merchant.hosted_checkout().create_hosted_checkout(request)
            except ApiException as e:
                # The error of a Hosted Checkout call is a plain error response (error ID and errors), so logging it
                # in full is fine here; log at least the error ID, status and error codes.
                codes = "; ".join(f"{error.error_code} {error.property_name}" for error in e.errors)
                logger.error("create_hosted_checkout failed, error_id %s, status %s: %s",
                             e.error_id, e.status_code, codes)
                # Only an error marked retriable is sent again: that request was not processed.
                # Other errors (400 invalid request, 403 wrong credentials, ...) reach the caller.
                if attempt >= 3 or not any(error.retriable is True for error in e.errors):
                    raise
            except CommunicationException:
                # No answer: timeout or connection error. The checkout may or may not exist.
                if attempt >= 3:
                    raise
            time.sleep(2 * attempt)
            attempt += 1
    # [END hosted-checkout-retry]

    # [START hosted-checkout-return]
    # Called when the customer comes back on your return URL, e.g. with request.args.get("RETURNMAC") in Flask.
    def handle_return(self, order_id: str, returnmac_from_query: str | None) -> OrderPaymentState:
        stored = self.__orders.get_hosted_checkout(order_id)

        # The platform appends RETURNMAC to the return URL. It identifies the returning customer:
        # a missing or different value means the request does not belong to this checkout.
        # compare_digest compares in constant time, so the comparison does not reveal the stored value.
        # It takes bytes here because it raises TypeError for a str with non-ASCII characters.
        if not returnmac_from_query or not hmac.compare_digest(stored.returnmac.encode(),
                                                               returnmac_from_query.encode()):
            raise RuntimeError(f"RETURNMAC does not match the stored value for order {order_id}")

        # Never trust the redirect alone: read the result from the platform.
        try:
            hosted_checkout = self.__merchant.hosted_checkout().get_hosted_checkout(stored.hosted_checkout_id)
        except ReferenceException as e:
            # The API reference documents a 404 for this call. If it fails with not found, read the payment
            # instead, with the payment ID that your webhook handler stored. Other errors reach the caller,
            # including the 409 and 410 that the SDK also raises as ReferenceException.
            if e.status_code != 404:
                raise
            # refresh_payment_state returns PENDING, not FAILED, when no payment ID is stored
            # yet: the webhook or your reconciliation job settles the order.
            logger.warning("get_hosted_checkout failed for order %s, error_id %s, status %s", order_id, e.error_id,
                           e.status_code)
            return PaymentStatusExample(self.__merchant, self.__orders).refresh_payment_state(order_id)

        output = hosted_checkout.created_payment_output
        payment = output.payment if output is not None else None
        if hosted_checkout.status == "PAYMENT_CREATED" and payment is not None and payment.id is not None:
            self.__orders.save_payment_id(order_id, payment.id)
            state = PaymentStatusExample.to_order_state(payment.status, payment.status_output)
            self.__orders.save_state(order_id, state)
            return state
        if hosted_checkout.status == "CANCELLED_BY_CONSUMER":
            # The customer cancelled, or the session expired (the created payment is then cancelled with the
            # error id CANCELLED_BY_EXPIRATION).
            self.__orders.save_state(order_id, OrderPaymentState.CANCELLED)
            return OrderPaymentState.CANCELLED
        # IN_PROGRESS: the customer has not finished. A webhook will report the result.
        return OrderPaymentState.PENDING
    # [END hosted-checkout-return]
