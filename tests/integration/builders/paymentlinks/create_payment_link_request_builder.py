import uuid
from datetime import datetime, timezone, timedelta

from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.create_payment_link_request import CreatePaymentLinkRequest
from onlinepayments.sdk.domain.order import Order
from onlinepayments.sdk.domain.order_references import OrderReferences
from onlinepayments.sdk.domain.payment_link_specific_input import PaymentLinkSpecificInput


class CreatePaymentLinkRequestBuilder:

    def __init__(self):
        self._amount = 1000
        self._currency_code = "EUR"
        self._display_qr_code = True
        self._reusable_link = True
        self._expiration_date = datetime.now(timezone.utc) + timedelta(days=7)
        self._description = "Test payment link"
        self._recipient_name = "Wile E. Coyote"
        self._merchant_reference = "Ref-" + str(uuid.uuid4())

    def with_amount(self, amount):
        self._amount = amount
        return self

    def with_currency(self, currency_code):
        self._currency_code = currency_code
        return self

    def with_display_qr_code(self, display_qr_code):
        self._display_qr_code = display_qr_code
        return self

    def with_reusable_link(self, reusable_link):
        self._reusable_link = reusable_link
        return self

    def with_expiration_date(self, expiration_date):
        self._expiration_date = expiration_date
        return self

    def with_description(self, description):
        self._description = description
        return self

    def with_recipient_name(self, recipient_name):
        self._recipient_name = recipient_name
        return self

    def with_merchant_reference(self, merchant_reference):
        self._merchant_reference = merchant_reference
        return self

    def build(self):
        request = CreatePaymentLinkRequest()
        request.order = self._build_order()
        request.display_qr_code = self._display_qr_code
        request.is_reusable_link = self._reusable_link
        request.payment_link_specific_input = self._build_payment_link_specific_input()

        return request

    def _build_order(self):
        order = Order()
        order.amount_of_money = self._build_amount_of_money()
        order.references = self._build_order_references()

        return order

    def _build_amount_of_money(self):
        amount = AmountOfMoney()
        amount.amount = self._amount
        amount.currency_code = self._currency_code

        return amount

    def _build_order_references(self):
        references = OrderReferences()
        references.merchant_reference = self._merchant_reference

        return references

    def _build_payment_link_specific_input(self):
        specific_input = PaymentLinkSpecificInput()
        specific_input.description = self._description
        specific_input.expiration_date = self._expiration_date
        specific_input.recipient_name = self._recipient_name

        return specific_input
