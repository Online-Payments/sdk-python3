import logging
import time

from onlinepayments.sdk.api_exception import ApiException
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.communication.communication_exception import CommunicationException
from onlinepayments.sdk.declined_payment_exception import DeclinedPaymentException
from onlinepayments.sdk.domain.create_payment_request import CreatePaymentRequest
from onlinepayments.sdk.idempotence_exception import IdempotenceException
from onlinepayments.sdk.merchant.i_merchant_client import IMerchantClient
from onlinepayments.sdk.validation_exception import ValidationException

from app_types import OrderPaymentState, OrderStore, PaymentStep
from create_payment_response_handler import handle_create_payment_response
from payment_attempt import start_payment_attempt
from payment_status_example import PaymentStatusExample

logger = logging.getLogger(__name__)


class ErrorHandlingExample:

    def __init__(self, merchant: IMerchantClient, orders: OrderStore):
        self.__merchant = merchant
        self.__orders = orders

    # [START error-handling]
    # idempotence_key is the stored key of the payment attempt (payment_attempt_key). Reuse it when a request
    # got no answer; replace it, stored again, only when the platform answered with an error marked retriable.
    def create_payment(self, order_id: str, request: CreatePaymentRequest, idempotence_key: str) -> PaymentStep:
        context = CallContext(idempotence_key=idempotence_key)
        attempt = 1
        while True:
            try:
                response = self.__merchant.payments().create_payment(request, context)
                break
            except DeclinedPaymentException as e:
                # Declined: the payment exists. Read its status before deciding anything.
                return self.__handle_declined(order_id, e)
            except IdempotenceException:
                # The first request with this key is still running. Wait, then send the same request again.
                if attempt >= 3:
                    raise
            except ValidationException as e:
                # 400: the request is invalid. Fix the request; retrying does not help.
                # Log the error codes and the error ID, never the request (it can hold card data).
                codes = "; ".join(f"{error.error_code} {error.property_name}" for error in e.errors)
                logger.error("create_payment rejected, error_id %s: %s", e.error_id, codes)
                raise
            except ApiException as e:
                # A technical error marked retriable (PlatformException for 500, 502 or 503): the request was not
                # processed. Send it again with a new key. Other errors are not retried: AuthorizationException (403)
                # for a wrong API key, secret or merchant ID, ReferenceException (404, 409, 410) for an object not
                # found, and server errors without a retriable error.
                if attempt >= 3 or not any(error.retriable is True for error in e.errors):
                    raise
                # The new key is stored before the call, like the first one.
                context = CallContext(idempotence_key=start_payment_attempt(order_id, self.__orders))
            except CommunicationException:
                # No answer: timeout or connection error. The payment may or may not exist.
                # Retry with the same key; the platform returns the original result instead of creating a second
                # payment.
                if attempt >= 3:
                    raise
            time.sleep(2 * attempt)
            attempt += 1

        return handle_create_payment_response(response, order_id, self.__orders)

    def __handle_declined(self, order_id: str, e: DeclinedPaymentException) -> PaymentStep:
        declined = e.create_payment_response
        payment = declined.payment if declined is not None else None
        if payment is None or payment.id is None:
            self.__orders.save_state(order_id, OrderPaymentState.FAILED)
            return PaymentStep(state=OrderPaymentState.FAILED)
        self.__orders.save_payment_id(order_id, payment.id)
        details = self.__merchant.payments().get_payment_details(payment.id)
        state = PaymentStatusExample.to_order_state(details.status, details.status_output)
        self.__orders.save_state(order_id, state)
        return PaymentStep(state=state)
    # [END error-handling]
