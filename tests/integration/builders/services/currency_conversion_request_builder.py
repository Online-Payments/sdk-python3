from onlinepayments.sdk.domain.currency_conversion_request import CurrencyConversionRequest
from onlinepayments.sdk.domain.dcc_card_source import DccCardSource
from onlinepayments.sdk.domain.card_info import CardInfo
from onlinepayments.sdk.domain.transaction import Transaction
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney


class CurrencyConversionRequestBuilder:

    def __init__(self):
        self._card_number = None
        self._amount = 1000
        self._currency_code = "EUR"

    def with_card_number(self, card_number):
        self._card_number = card_number
        return self

    def with_amount(self, amount):
        self._amount = amount
        return self

    def with_currency_code(self, currency_code):
        self._currency_code = currency_code
        return self

    def build(self):
        card_info = CardInfo()
        card_info.card_number = self._card_number

        card_source = DccCardSource()
        card_source.card = card_info

        amount_of_money = AmountOfMoney()
        amount_of_money.amount = self._amount
        amount_of_money.currency_code = self._currency_code

        transaction = Transaction()
        transaction.amount = amount_of_money

        request = CurrencyConversionRequest()
        request.card_source = card_source
        request.transaction = transaction

        return request
