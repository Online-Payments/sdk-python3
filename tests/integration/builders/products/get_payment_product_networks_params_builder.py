from onlinepayments.sdk.merchant.products.get_payment_product_networks_params import GetPaymentProductNetworksParams


class GetPaymentProductNetworksParamsBuilder:

    def __init__(self):
        self._country_code = None
        self._currency_code = None
        self._amount = None
        self._is_recurring = None

    def with_country_code(self, country_code):
        self._country_code = country_code
        return self

    def with_currency_code(self, currency_code):
        self._currency_code = currency_code
        return self

    def with_amount(self, amount):
        self._amount = amount
        return self

    def with_is_recurring(self, is_recurring):
        self._is_recurring = is_recurring
        return self

    def build(self):
        params = GetPaymentProductNetworksParams()
        params.country_code = self._country_code
        params.currency_code = self._currency_code

        if self._amount is not None:
            params.amount = self._amount
        if self._is_recurring is not None:
            params.is_recurring = self._is_recurring

        return params
