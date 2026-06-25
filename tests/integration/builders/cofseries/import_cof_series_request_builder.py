from onlinepayments.sdk.domain.import_cof_series_request import ImportCofSeriesRequest
from onlinepayments.sdk.domain.card_data_without_cvv import CardDataWithoutCvv


class ImportCofSeriesRequestBuilder:

    def __init__(self):
        self._card_number = "4567350000427977"
        self._cardholder_name = "John Doe"
        self._expiry_date = "1230"
        self._currency_code = "EUR"
        self._payment_product_id = 1
        self._scheme_reference_data = "test_scheme_reference"
        self._token_id = None
        self._transaction_link_identifier = None

    def with_card_number(self, card_number):
        self._card_number = card_number
        return self

    def with_cardholder_name(self, cardholder_name):
        self._cardholder_name = cardholder_name
        return self

    def with_expiry_date(self, expiry_date):
        self._expiry_date = expiry_date
        return self

    def with_currency_code(self, currency_code):
        self._currency_code = currency_code
        return self

    def with_payment_product_id(self, payment_product_id):
        self._payment_product_id = payment_product_id
        return self

    def with_scheme_reference_data(self, scheme_reference_data):
        self._scheme_reference_data = scheme_reference_data
        return self

    def with_token_id(self, token_id):
        self._token_id = token_id
        return self

    def with_transaction_link_identifier(self, transaction_link_identifier):
        self._transaction_link_identifier = transaction_link_identifier
        return self

    def build(self):
        request = ImportCofSeriesRequest()
        request.currency_code = self._currency_code
        request.payment_product_id = self._payment_product_id
        request.scheme_reference_data = self._scheme_reference_data

        if self._token_id is not None:
            request.token_id = self._token_id
        else:
            card = CardDataWithoutCvv()
            card.card_number = self._card_number
            card.cardholder_name = self._cardholder_name
            card.expiry_date = self._expiry_date
            request.card = card

        if self._transaction_link_identifier is not None:
            request.transaction_link_identifier = self._transaction_link_identifier

        return request
