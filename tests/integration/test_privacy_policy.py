import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.privacypolicy.get_privacy_policy_params_builder import GetPrivacyPolicyParamsBuilder
from onlinepayments.sdk.call_context import CallContext


class PrivacyPolicyIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test get privacy policy"""

    def test_get_privacy_policy_valid_params_returns_response(self):
        params = GetPrivacyPolicyParamsBuilder().build()

        response = self.client.merchant(MERCHANT_ID).privacy_policy().get_privacy_policy(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.html_content)

    def test_get_privacy_policy_with_call_context_returns_response(self):
        params = GetPrivacyPolicyParamsBuilder().build()
        context = CallContext(idempotence_key="test-privacy-policy-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).privacy_policy().get_privacy_policy(params, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.html_content)

    def test_get_privacy_policy_specific_payment_product_returns_response(self):
        params = GetPrivacyPolicyParamsBuilder() \
            .with_visa_product() \
            .build()

        response = self.client.merchant(MERCHANT_ID).privacy_policy().get_privacy_policy(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.html_content)
        self.assertEqual(1, params.payment_product_id)

    def test_get_privacy_policy_english_locale_returns_response(self):
        params = GetPrivacyPolicyParamsBuilder() \
            .with_english_locale() \
            .build()

        response = self.client.merchant(MERCHANT_ID).privacy_policy().get_privacy_policy(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.html_content)
        self.assertEqual("en_US", params.locale)

    def test_get_privacy_policy_dutch_locale_returns_response(self):
        params = GetPrivacyPolicyParamsBuilder() \
            .with_dutch_locale() \
            .build()

        response = self.client.merchant(MERCHANT_ID).privacy_policy().get_privacy_policy(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.html_content)
        self.assertEqual("nl_NL", params.locale)

    def test_get_privacy_policy_french_locale_returns_response(self):
        params = GetPrivacyPolicyParamsBuilder() \
            .with_french_locale() \
            .build()

        response = self.client.merchant(MERCHANT_ID).privacy_policy().get_privacy_policy(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.html_content)
        self.assertEqual("fr_FR", params.locale)

    def test_get_privacy_policy_german_locale_returns_response(self):
        params = GetPrivacyPolicyParamsBuilder() \
            .with_german_locale() \
            .build()

        response = self.client.merchant(MERCHANT_ID).privacy_policy().get_privacy_policy(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.html_content)
        self.assertEqual("de_DE", params.locale)

    def test_get_privacy_policy_visa_product_returns_response(self):
        params = GetPrivacyPolicyParamsBuilder() \
            .with_visa_product() \
            .build()

        response = self.client.merchant(MERCHANT_ID).privacy_policy().get_privacy_policy(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.html_content)
        self.assertEqual(1, params.payment_product_id)

    def test_get_privacy_policy_american_express_product_returns_response(self):
        params = GetPrivacyPolicyParamsBuilder() \
            .with_american_express_product() \
            .build()

        response = self.client.merchant(MERCHANT_ID).privacy_policy().get_privacy_policy(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.html_content)
        self.assertEqual(2, params.payment_product_id)

    def test_get_privacy_policy_master_card_product_returns_response(self):
        params = GetPrivacyPolicyParamsBuilder() \
            .with_master_card_product() \
            .build()

        response = self.client.merchant(MERCHANT_ID).privacy_policy().get_privacy_policy(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.html_content)
        self.assertEqual(3, params.payment_product_id)

    def test_get_privacy_policy_visa_product_french_locale_returns_response(self):
        params = GetPrivacyPolicyParamsBuilder() \
            .with_visa_product() \
            .with_french_locale() \
            .build()

        response = self.client.merchant(MERCHANT_ID).privacy_policy().get_privacy_policy(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.html_content)
        self.assertEqual(1, params.payment_product_id)
        self.assertEqual("fr_FR", params.locale)

    def test_get_privacy_policy_amex_product_german_locale_returns_response(self):
        params = GetPrivacyPolicyParamsBuilder() \
            .with_american_express_product() \
            .with_german_locale() \
            .build()

        response = self.client.merchant(MERCHANT_ID).privacy_policy().get_privacy_policy(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.html_content)
        self.assertEqual(2, params.payment_product_id)
        self.assertEqual("de_DE", params.locale)


if __name__ == '__main__':
    unittest.main()