from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.increment_authorization_request import IncrementAuthorizationRequest


class IncrementAuthorizationRequestBuilder:

    def __init__(self):
        self._amount = 1500
        self._currency = "EUR"

    def with_amount(self, amount):
        self._amount = amount
        return self

    def with_currency(self, currency):
        self._currency = currency
        return self

    def build(self):
        amount_of_money = AmountOfMoney()
        amount_of_money.amount = self._amount
        amount_of_money.currency_code = self._currency

        request = IncrementAuthorizationRequest()
        request.amount_of_money = amount_of_money

        return request
