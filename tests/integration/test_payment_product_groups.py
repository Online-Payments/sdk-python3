import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.product_groups.get_product_groups_params_builder import GetProductGroupsParamsBuilder
from tests.integration.builders.product_groups.get_product_group_params_builder import GetProductGroupParamsBuilder
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.validation_exception import ValidationException
from onlinepayments.sdk.reference_exception import ReferenceException

COUNTRY_CODE = "NL"
CURRENCY_CODE = "EUR"
VALID_PAYMENT_PRODUCT_GROUP_ID = "cards"
INVALID_PAYMENT_PRODUCT_GROUP_ID = "invalid-group-id"


class ProductGroupsIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test get product groups"""

    def test_get_product_groups_valid_params_returns_product_groups(self):
        params = GetProductGroupsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .build()

        response = self.client.merchant(MERCHANT_ID).product_groups().get_product_groups(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_product_groups)
        self.assertGreater(len(response.payment_product_groups), 0)
        self.assertIsNotNone(response.payment_product_groups[0])

    def test_get_product_groups_with_call_context_returns_product_groups(self):
        params = GetProductGroupsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .build()

        context = CallContext(idempotence_key="test-product-groups-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).product_groups().get_product_groups(params, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_product_groups)
        self.assertGreater(len(response.payment_product_groups), 0)
        self.assertIsNotNone(response.payment_product_groups[0])

    def test_get_product_groups_with_amount_returns_product_groups(self):
        params = GetProductGroupsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_amount(1000) \
            .build()

        response = self.client.merchant(MERCHANT_ID).product_groups().get_product_groups(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_product_groups)

    def test_get_product_groups_with_is_recurring_returns_product_groups(self):
        params = GetProductGroupsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_is_recurring(True) \
            .build()

        response = self.client.merchant(MERCHANT_ID).product_groups().get_product_groups(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_product_groups)

    def test_get_product_groups_with_add_hide_returns_product_groups(self):
        params = GetProductGroupsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_add_hide_list(["fields", "accountsOnFile"]) \
            .build()

        response = self.client.merchant(MERCHANT_ID).product_groups().get_product_groups(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_product_groups)
        self.assertIsNotNone(params.hide)
        self.assertEqual(2, len(params.hide))
        self.assertIn("fields", params.hide)
        self.assertIn("accountsOnFile", params.hide)

    def test_get_product_groups_with_hide_list_returns_product_groups(self):
        hide_fields = ["fields", "translations"]
        params = GetProductGroupsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_hide_list(hide_fields) \
            .build()

        response = self.client.merchant(MERCHANT_ID).product_groups().get_product_groups(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_product_groups)
        self.assertEqual(hide_fields, params.hide)

    def test_get_product_groups_with_null_hide_element_returns_product_groups(self):
        params = GetProductGroupsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_add_hide_list(["fields", None]) \
            .build()

        response = self.client.merchant(MERCHANT_ID).product_groups().get_product_groups(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_product_groups)
        self.assertEqual(2, len(params.hide))
        self.assertIn(None, params.hide)

    def test_get_product_groups_params_getters_return_correct_values(self):
        params = GetProductGroupsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_amount(1000) \
            .with_is_recurring(True) \
            .build()

        self.assertEqual(COUNTRY_CODE, params.country_code)
        self.assertEqual(CURRENCY_CODE, params.currency_code)
        self.assertEqual(1000, params.amount)
        self.assertTrue(params.is_recurring)

    def test_get_product_groups_missing_country_code_raises_validation_exception(self):
        params = GetProductGroupsParamsBuilder() \
            .with_currency_code(CURRENCY_CODE) \
            .build()

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).product_groups().get_product_groups(params)

        self.assertEqual(400, raised.exception.status_code)

    """Test get product group"""

    def test_get_product_group_valid_id_returns_product_group(self):
        params = GetProductGroupParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .build()

        response = self.client.merchant(MERCHANT_ID).product_groups().get_product_group(VALID_PAYMENT_PRODUCT_GROUP_ID, params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertEqual(VALID_PAYMENT_PRODUCT_GROUP_ID, response.id.lower())

    def test_get_product_group_with_amount_returns_product_group(self):
        params = GetProductGroupParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_amount(2500) \
            .build()

        response = self.client.merchant(MERCHANT_ID).product_groups().get_product_group(VALID_PAYMENT_PRODUCT_GROUP_ID, params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertEqual(VALID_PAYMENT_PRODUCT_GROUP_ID, response.id.lower())

    def test_get_product_group_with_is_recurring_returns_product_group(self):
        params = GetProductGroupParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_is_recurring(True) \
            .build()

        response = self.client.merchant(MERCHANT_ID).product_groups().get_product_group(VALID_PAYMENT_PRODUCT_GROUP_ID, params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertEqual(VALID_PAYMENT_PRODUCT_GROUP_ID, response.id.lower())

    def test_get_product_group_with_add_hide_returns_product_group(self):
        params = GetProductGroupParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_add_hide_list(["accountsOnFile"]) \
            .build()

        response = self.client.merchant(MERCHANT_ID).product_groups().get_product_group(VALID_PAYMENT_PRODUCT_GROUP_ID, params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertEqual(VALID_PAYMENT_PRODUCT_GROUP_ID, response.id.lower())
        self.assertIsNotNone(params.hide)
        self.assertEqual(1, len(params.hide))
        self.assertIn("accountsOnFile", params.hide)

    def test_get_product_group_with_hide_list_returns_product_group(self):
        hide_fields = ["fields"]
        params = GetProductGroupParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_hide_list(hide_fields) \
            .build()

        response = self.client.merchant(MERCHANT_ID).product_groups().get_product_group(VALID_PAYMENT_PRODUCT_GROUP_ID, params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertEqual(VALID_PAYMENT_PRODUCT_GROUP_ID, response.id.lower())
        self.assertEqual(hide_fields, params.hide)

    def test_get_product_group_with_null_hide_element_returns_product_group(self):
        params = GetProductGroupParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_add_hide_list(["accountsOnFile", None]) \
            .build()

        response = self.client.merchant(MERCHANT_ID).product_groups().get_product_group(VALID_PAYMENT_PRODUCT_GROUP_ID, params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertEqual(VALID_PAYMENT_PRODUCT_GROUP_ID, response.id.lower())
        self.assertEqual(2, len(params.hide))
        self.assertIn(None, params.hide)

    def test_get_product_group_params_getters_return_correct_values(self):
        params = GetProductGroupParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_amount(2500) \
            .with_is_recurring(False) \
            .build()

        self.assertEqual(COUNTRY_CODE, params.country_code)
        self.assertEqual(CURRENCY_CODE, params.currency_code)
        self.assertEqual(2500, params.amount)
        self.assertFalse(params.is_recurring)

    def test_get_product_group_invalid_id_raises_reference_exception(self):
        params = GetProductGroupParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .build()

        with self.assertRaises((ReferenceException, ValueError)):
            self.client.merchant(MERCHANT_ID).product_groups().get_product_group(INVALID_PAYMENT_PRODUCT_GROUP_ID, params)


if __name__ == "__main__":
    unittest.main()