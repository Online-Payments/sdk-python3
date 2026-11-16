from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.create_hosted_checkout_request import CreateHostedCheckoutRequest
from onlinepayments.sdk.domain.hosted_checkout_specific_input import HostedCheckoutSpecificInput
from onlinepayments.sdk.domain.order import Order
from onlinepayments.sdk.domain.order_references import OrderReferences
from onlinepayments.sdk.domain.subsequent_card_payment_method_specific_input import \
    SubsequentCardPaymentMethodSpecificInput
from onlinepayments.sdk.domain.subsequent_payment_request import SubsequentPaymentRequest
from onlinepayments.sdk.merchant.i_merchant_client import IMerchantClient

from app_types import OrderPaymentState, OrderStore
from hosted_checkout_example import HostedCheckoutExample
from payment_status_example import PaymentStatusExample


class RecurringPaymentsExample:

    def __init__(self, merchant: IMerchantClient, orders: OrderStore, hosted_checkout: HostedCheckoutExample):
        self.__merchant = merchant
        self.__orders = orders
        self.__hosted_checkout = hosted_checkout

    # [START recurring-first]
    # First payment of a subscription, made by the customer on the Hosted Checkout Page.
    # The recurring flag marks it as the first payment of the series.
    # It follows the Hosted Checkout flow: the return URL is built from your configuration and the call goes
    # through the same retry helper. Handle the return as there.
    def start_subscription(self, order_id: str, amount_in_cents: int, currency_code: str) -> str:
        amount_of_money = AmountOfMoney()
        amount_of_money.amount = amount_in_cents
        amount_of_money.currency_code = currency_code

        references = OrderReferences()
        references.merchant_reference = order_id

        order = Order()
        order.amount_of_money = amount_of_money
        order.references = references

        hosted_checkout_input = HostedCheckoutSpecificInput()
        hosted_checkout_input.return_url = self.__hosted_checkout.build_return_url(order_id)
        hosted_checkout_input.is_recurring = True

        request = CreateHostedCheckoutRequest()
        request.order = order
        request.hosted_checkout_specific_input = hosted_checkout_input

        response = self.__hosted_checkout.create_with_retry(request)
        if response.hosted_checkout_id is None or response.returnmac is None or response.redirect_url is None:
            raise RuntimeError(f"Incomplete hosted checkout response for order {order_id}")
        self.__orders.save_hosted_checkout(order_id, response.hosted_checkout_id, response.returnmac)
        return response.redirect_url

    # When the first payment is authorised or captured, keep its payment ID: later charges refer to it.
    def on_first_payment_succeeded(self, customer_id: str, first_payment_id: str) -> None:
        self.__orders.save_recurring_payment_id(customer_id, first_payment_id)
    # [END recurring-first]

    # [START recurring-subsequent]
    # Later charge started by you, without the customer (merchant-initiated).
    # The caller creates ONE idempotence key per charge and stores it with the charge, before the first call:
    # save_idempotence_key(order_id, key). Retries reuse or replace the key as described in errors.md.
    def charge_renewal(self, customer_id: str, order_id: str, amount_in_cents: int, currency_code: str,
                       idempotence_key: str) -> OrderPaymentState:
        first_payment_id = self.__orders.get_recurring_payment_id(customer_id)

        amount_of_money = AmountOfMoney()
        amount_of_money.amount = amount_in_cents
        amount_of_money.currency_code = currency_code

        references = OrderReferences()
        references.merchant_reference = order_id

        order = Order()
        order.amount_of_money = amount_of_money
        order.references = references

        card_input = SubsequentCardPaymentMethodSpecificInput()
        # Recurring = fixed amount, regular intervals (at most one year), started by you.
        # Other allowed values: Unscheduled, Installment, NoShow, DelayedCharge, PartialShipment,
        # Resubmission, RecurringVariable, UnscheduledFixed.
        card_input.subsequent_type = "Recurring"
        # SALE: authorised and captured at once. Acquirers that do not support it ignore it.
        card_input.authorization_mode = "SALE"

        request = SubsequentPaymentRequest()
        request.order = order
        request.subsequentcard_payment_method_specific_input = card_input

        context = CallContext(idempotence_key=idempotence_key)
        # A declined charge raises DeclinedPaymentException, as for create_payment.
        response = self.__merchant.subsequent().subsequent_payment(first_payment_id, request, context)

        payment = response.payment
        if payment is None or payment.id is None:
            raise RuntimeError(f"The subsequent payment response for order {order_id} has no payment")
        self.__orders.save_payment_id(order_id, payment.id)
        state = PaymentStatusExample.to_order_state(payment.status, payment.status_output)
        self.__orders.save_state(order_id, state)
        return state
    # [END recurring-subsequent]
