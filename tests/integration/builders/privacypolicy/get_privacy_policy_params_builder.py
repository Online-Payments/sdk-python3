from onlinepayments.sdk.merchant.privacypolicy.get_privacy_policy_params import GetPrivacyPolicyParams


class GetPrivacyPolicyParamsBuilder:

    def __init__(self):
        self._locale = "en_US"
        self._payment_product_id = None

    def with_locale(self, locale):
        self._locale = locale
        return self

    def with_payment_product_id(self, payment_product_id):
        self._payment_product_id = payment_product_id
        return self

    def with_english_locale(self):
        self._locale = "en_US"
        return self

    def with_dutch_locale(self):
        self._locale = "nl_NL"
        return self

    def with_french_locale(self):
        self._locale = "fr_FR"
        return self

    def with_german_locale(self):
        self._locale = "de_DE"
        return self

    def with_visa_product(self):
        self._payment_product_id = 1
        return self

    def with_american_express_product(self):
        self._payment_product_id = 2
        return self

    def with_master_card_product(self):
        self._payment_product_id = 3
        return self

    def build(self):
        params = GetPrivacyPolicyParams()
        params.locale = self._locale

        if self._payment_product_id is not None:
            params.payment_product_id = self._payment_product_id

        return params
