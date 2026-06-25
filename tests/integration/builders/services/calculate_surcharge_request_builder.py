from onlinepayments.sdk.domain.calculate_surcharge_request import CalculateSurchargeRequest
from onlinepayments.sdk.domain.card_source import CardSource
from onlinepayments.sdk.domain.surcharge_calculation_card import SurchargeCalculationCard
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney


class CalculateSurchargeRequestBuilder:

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
        card = SurchargeCalculationCard()
        card.card_number = self._card_number

        card_source = CardSource()
        card_source.card = card

        amount_of_money = AmountOfMoney()
        amount_of_money.amount = self._amount
        amount_of_money.currency_code = self._currency_code

        request = CalculateSurchargeRequest()
        request.card_source = card_source
        request.amount_of_money = amount_of_money

        return request
