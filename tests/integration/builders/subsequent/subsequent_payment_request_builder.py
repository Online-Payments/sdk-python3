from onlinepayments.sdk.domain.subsequent_payment_request import SubsequentPaymentRequest
from onlinepayments.sdk.domain.order import Order
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.subsequent_card_payment_method_specific_input import SubsequentCardPaymentMethodSpecificInput


class SubsequentPaymentRequestBuilder:

    def __init__(self):
        self._amount = 1000
        self._currency = "EUR"
        self._subsequent_type = "Recurring"
        self._authorization_mode = "FINAL_AUTHORIZATION"

    def with_amount(self, amount):
        self._amount = amount
        return self

    def with_currency(self, currency):
        self._currency = currency
        return self

    def with_subsequent_type(self, subsequent_type):
        self._subsequent_type = subsequent_type
        return self

    def with_authorization_mode(self, authorization_mode):
        self._authorization_mode = authorization_mode
        return self

    def build(self):
        amount_of_money = AmountOfMoney()
        amount_of_money.amount = self._amount
        amount_of_money.currency_code = self._currency

        order = Order()
        order.amount_of_money = amount_of_money

        card_input = SubsequentCardPaymentMethodSpecificInput()
        card_input.subsequent_type = self._subsequent_type
        card_input.authorization_mode = self._authorization_mode

        request = SubsequentPaymentRequest()
        request.order = order
        request.subsequentcard_payment_method_specific_input = card_input

        return request
