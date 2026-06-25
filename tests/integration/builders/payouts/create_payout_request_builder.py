from onlinepayments.sdk.domain.create_payout_request import CreatePayoutRequest
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.card_payout_method_specific_input import CardPayoutMethodSpecificInput
from onlinepayments.sdk.domain.card import Card


class CreatePayoutRequestBuilder:

    def __init__(self):
        self._amount = 1000
        self._currency_code = "EUR"
        self._card_number = "4012000033330026"
        self._cardholder_name = "Wile E. Coyote"
        self._cvv = "123"
        self._expiry_date = "1230"
        self._payment_product_id = 1
        self._payout_reason = "Refund"

    def with_amount(self, amount):
        self._amount = amount
        return self

    def with_currency(self, currency_code):
        self._currency_code = currency_code
        return self

    def with_card_number(self, card_number):
        self._card_number = card_number
        return self

    def with_cardholder_name(self, cardholder_name):
        self._cardholder_name = cardholder_name
        return self

    def with_cvv(self, cvv):
        self._cvv = cvv
        return self

    def with_expiry_date(self, expiry_date):
        self._expiry_date = expiry_date
        return self

    def with_payment_product_id(self, payment_product_id):
        self._payment_product_id = payment_product_id
        return self

    def with_payout_reason(self, payout_reason):
        self._payout_reason = payout_reason
        return self

    def build(self):
        amount_of_money = AmountOfMoney()
        amount_of_money.amount = self._amount
        amount_of_money.currency_code = self._currency_code

        card = Card()
        card.card_number = self._card_number
        card.cardholder_name = self._cardholder_name
        card.cvv = self._cvv
        card.expiry_date = self._expiry_date

        card_input = CardPayoutMethodSpecificInput()
        card_input.card = card
        card_input.payment_product_id = self._payment_product_id
        card_input.payout_reason = self._payout_reason

        request = CreatePayoutRequest()
        request.amount_of_money = amount_of_money
        request.card_payout_method_specific_input = card_input

        return request
