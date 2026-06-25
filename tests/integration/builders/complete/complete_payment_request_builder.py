from onlinepayments.sdk.domain.complete_payment_request import CompletePaymentRequest
from onlinepayments.sdk.domain.complete_payment_card_payment_method_specific_input import CompletePaymentCardPaymentMethodSpecificInput
from onlinepayments.sdk.domain.card_without_cvv import CardWithoutCvv
from onlinepayments.sdk.domain.order import Order
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney


class CompletePaymentRequestBuilder:

    def __init__(self):
        self._amount = 1000
        self._currency = "EUR"
        self._card_number = None
        self._cardholder_name = None
        self._expiry_date = None
        self._order_override = None
        self._use_order_override = False

    def with_amount(self, amount):
        self._amount = amount
        return self

    def with_currency(self, currency):
        self._currency = currency
        return self

    def with_card_number(self, card_number):
        self._card_number = card_number
        return self

    def with_cardholder_name(self, cardholder_name):
        self._cardholder_name = cardholder_name
        return self

    def with_expiry_date(self, expiry_date):
        self._expiry_date = expiry_date
        return self

    def with_order(self, order):
        self._order_override = order
        self._use_order_override = True

        return self

    def build(self):
        request = CompletePaymentRequest()
        request.order = self._order_override if self._use_order_override else self._build_order()

        if self._card_number is not None or self._cardholder_name is not None or self._expiry_date is not None:
            request.card_payment_method_specific_input = self._build_card_payment_method_specific_input()

        return request

    def _build_order(self):
        amount = AmountOfMoney()
        amount.amount = self._amount
        amount.currency_code = self._currency

        order = Order()
        order.amount_of_money = amount

        return order

    def _build_card_payment_method_specific_input(self):
        card = CardWithoutCvv()

        if self._card_number is not None:
            card.card_number = self._card_number

        if self._cardholder_name is not None:
            card.cardholder_name = self._cardholder_name

        if self._expiry_date is not None:
            card.expiry_date = self._expiry_date

        input_ = CompletePaymentCardPaymentMethodSpecificInput()
        input_.card = card

        return input_
