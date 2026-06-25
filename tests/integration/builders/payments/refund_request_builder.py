from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.refund_request import RefundRequest


class RefundRequestBuilder:

    def __init__(self):
        self._amount = 1000
        self._currency = "EUR"
        self._is_final = None

    def with_amount(self, amount):
        self._amount = amount
        return self

    def with_currency(self, currency):
        self._currency = currency
        return self

    def with_is_final(self, is_final):
        self._is_final = is_final
        return self

    def build(self):
        amount_of_money = AmountOfMoney()
        amount_of_money.amount = self._amount
        amount_of_money.currency_code = self._currency

        request = RefundRequest()
        request.amount_of_money = amount_of_money

        if self._is_final is not None:
            request.is_final = self._is_final

        return request
