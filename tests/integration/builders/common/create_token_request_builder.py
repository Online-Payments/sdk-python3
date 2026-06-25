from onlinepayments.sdk.domain.create_token_request import CreateTokenRequest
from onlinepayments.sdk.domain.token_card_specific_input import TokenCardSpecificInput
from onlinepayments.sdk.domain.token_data import TokenData
from onlinepayments.sdk.domain.card import Card


class CreateTokenRequestBuilder:

    def __init__(self):
        self._card_number = "4567350000427977"
        self._cvv = "123"
        self._expiry_date = "1230"
        self._cardholder_name = "John Doe"
        self._payment_product_id = 1
        self._encrypted_customer_input = None
        self._cobrand_selection_indicator = None

    def with_card_number(self, card_number):
        self._card_number = card_number
        return self

    def with_cvv(self, cvv):
        self._cvv = cvv
        return self

    def with_expiry_date(self, expiry_date):
        self._expiry_date = expiry_date
        return self

    def with_cardholder_name(self, cardholder_name):
        self._cardholder_name = cardholder_name
        return self

    def with_payment_product_id(self, payment_product_id):
        self._payment_product_id = payment_product_id
        return self

    def with_encrypted_customer_input(self, encrypted_customer_input):
        self._encrypted_customer_input = encrypted_customer_input
        return self

    def with_cobrand_selection_indicator(self, cobrand_selection_indicator):
        self._cobrand_selection_indicator = cobrand_selection_indicator
        return self

    def build(self):
        request = CreateTokenRequest()
        request.payment_product_id = self._payment_product_id

        if self._encrypted_customer_input is not None:
            request.encrypted_customer_input = self._encrypted_customer_input
        else:
            request.card = self._build_card_token()

        return request

    def _build_card_token(self):
        card = Card()
        card.card_number = self._card_number
        card.cvv = self._cvv
        card.expiry_date = self._expiry_date
        card.cardholder_name = self._cardholder_name

        token_data = TokenData()
        token_data.card = card

        card_input = TokenCardSpecificInput()
        card_input.data = token_data

        if self._cobrand_selection_indicator is not None:
            card_input.cobrand_selection_indicator = self._cobrand_selection_indicator

        return card_input

