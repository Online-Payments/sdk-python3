from onlinepayments.sdk.merchant.products.get_product_directory_params import GetProductDirectoryParams


class GetProductDirectoryParamsBuilder:

    def __init__(self):
        self._country_code = None
        self._currency_code = None

    def with_country_code(self, country_code):
        self._country_code = country_code
        return self

    def with_currency_code(self, currency_code):
        self._currency_code = currency_code
        return self

    def build(self):
        params = GetProductDirectoryParams()
        params.country_code = self._country_code
        params.currency_code = self._currency_code

        return params
