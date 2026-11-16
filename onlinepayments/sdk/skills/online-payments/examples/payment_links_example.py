from datetime import datetime, timedelta, timezone

from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.create_payment_link_request import CreatePaymentLinkRequest
from onlinepayments.sdk.domain.order import Order
from onlinepayments.sdk.domain.order_references import OrderReferences
from onlinepayments.sdk.domain.payment_link_response import PaymentLinkResponse
from onlinepayments.sdk.domain.payment_link_specific_input import PaymentLinkSpecificInput
from onlinepayments.sdk.merchant.i_merchant_client import IMerchantClient


class PaymentLinksExample:

    def __init__(self, merchant: IMerchantClient):
        self.__merchant = merchant

    # [START payment-link-create]
    # Returns the link to send to the customer (email, chat, invoice).
    def create_link(self, order_id: str, amount_in_cents: int, currency_code: str, description: str) -> PaymentLinkResponse:
        amount_of_money = AmountOfMoney()
        amount_of_money.amount = amount_in_cents
        amount_of_money.currency_code = currency_code

        references = OrderReferences()
        references.merchant_reference = order_id

        order = Order()
        order.amount_of_money = amount_of_money
        order.references = references

        link_input = PaymentLinkSpecificInput()
        link_input.description = description
        # Required. A datetime with a time zone, at most 6 months in the future.
        link_input.expiration_date = datetime.now(timezone.utc) + timedelta(days=7)

        request = CreatePaymentLinkRequest()
        request.order = order
        request.payment_link_specific_input = link_input

        # CreatePaymentLink does not support idempotent requests, so no idempotence key is sent.
        link = self.__merchant.payment_links().create_payment_link(request)

        # Store payment_link_id with the order. Send redirection_url exactly as returned.
        # The paymentlink.paid webhook (or get_payment_link_by_id) tells you when it is paid.
        # Once paid, the link's payment_id has no attempt suffix: use it with "_0" appended in
        # GetPaymentDetails, and read the payment's status.
        return link
    # [END payment-link-create]
