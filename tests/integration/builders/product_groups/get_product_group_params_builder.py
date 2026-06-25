from onlinepayments.sdk.merchant.productgroups.get_product_group_params import GetProductGroupParams


class GetProductGroupParamsBuilder:

    def __init__(self):
        self._country_code = None
        self._currency_code = None
        self._amount = None
        self._is_recurring = None
        self._add_hide_list = None
        self._hide_list = None

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

    def with_add_hide_list(self, add_hide_list):
        self._add_hide_list = add_hide_list
        return self

    def with_hide_list(self, hide_list):
        self._hide_list = hide_list
        return self

    def build(self):
        params = GetProductGroupParams()
        params.country_code = self._country_code
        params.currency_code = self._currency_code

        if self._amount is not None:
            params.amount = self._amount
        if self._is_recurring is not None:
            params.is_recurring = self._is_recurring
        if self._add_hide_list is not None:
            for item in self._add_hide_list:
                params.add_hide(item)
        if self._hide_list is not None:
            params.hide = self._hide_list

        return params
