import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.products.get_payment_products_params_builder import GetPaymentProductsParamsBuilder
from tests.integration.builders.products.get_payment_product_params_builder import GetPaymentProductParamsBuilder
from tests.integration.builders.products.get_payment_product_networks_params_builder import GetPaymentProductNetworksParamsBuilder
from tests.integration.builders.products.get_product_directory_params_builder import GetProductDirectoryParamsBuilder
from tests.integration.builders.products.payment_product_session_request_builder import PaymentProductSessionRequestBuilder
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.validation_exception import ValidationException
from onlinepayments.sdk.reference_exception import ReferenceException

COUNTRY_CODE = "NL"
CURRENCY_CODE = "EUR"
VALID_PAYMENT_PRODUCT_ID = 1
VALID_PAYMENT_PRODUCT_NETWORKS_ID = 302
VALID_PAYMENT_PRODUCT_DIRECTORY_ID = 809
INVALID_PAYMENT_PRODUCT_ID = -1


class ProductsIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test get payment products"""

    def test_get_payment_products_valid_params_returns_payment_products(self):
        params = GetPaymentProductsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_products(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_products)
        self.assertGreater(len(response.payment_products), 0)
        self.assertIsNotNone(response.payment_products[0])
        self.assertGreater(response.payment_products[0].id, 0)

    def test_get_payment_products_with_call_context_returns_payment_products(self):
        params = GetPaymentProductsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .build()

        context = CallContext(idempotence_key="test-products-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).products().get_payment_products(params, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_products)
        self.assertGreater(len(response.payment_products), 0)
        self.assertIsNotNone(response.payment_products[0])
        self.assertGreater(response.payment_products[0].id, 0)

    def test_get_payment_products_with_locale_returns_payment_products(self):
        params = GetPaymentProductsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_locale("en_US") \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_products(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_products)
        self.assertGreater(len(response.payment_products), 0)
        self.assertIsNotNone(response.payment_products[0])
        self.assertGreater(response.payment_products[0].id, 0)

    def test_get_payment_products_with_amount_returns_payment_products(self):
        params = GetPaymentProductsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_amount(1000) \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_products(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_products)
        self.assertGreater(len(response.payment_products), 0)
        self.assertIsNotNone(response.payment_products[0])
        self.assertGreater(response.payment_products[0].id, 0)

    def test_get_payment_products_with_is_recurring_returns_payment_products(self):
        params = GetPaymentProductsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_is_recurring(True) \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_products(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_products)
        self.assertGreater(len(response.payment_products), 0)
        self.assertIsNotNone(response.payment_products[0])
        self.assertGreater(response.payment_products[0].id, 0)

    def test_get_payment_products_with_add_hide_returns_payment_products(self):
        params = GetPaymentProductsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_add_hide_list(["fields", "accountsOnFile"]) \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_products(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_products)
        self.assertIsNotNone(params.hide)
        self.assertEqual(2, len(params.hide))
        self.assertIn("fields", params.hide)
        self.assertIn("accountsOnFile", params.hide)

    def test_get_payment_products_with_hide_list_returns_payment_products(self):
        hide_fields = ["fields", "translations"]
        params = GetPaymentProductsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_hide_list(hide_fields) \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_products(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_products)
        self.assertEqual(hide_fields, params.hide)

    def test_get_payment_products_params_getters_return_correct_values(self):
        params = GetPaymentProductsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_locale("en_US") \
            .with_amount(1000) \
            .with_is_recurring(True) \
            .build()

        self.assertEqual(COUNTRY_CODE, params.country_code)
        self.assertEqual(CURRENCY_CODE, params.currency_code)
        self.assertEqual("en_US", params.locale)
        self.assertEqual(1000, params.amount)
        self.assertTrue(params.is_recurring)

    def test_get_payment_products_missing_country_code_raises_validation_exception(self):
        params = GetPaymentProductsParamsBuilder() \
            .with_currency_code(CURRENCY_CODE) \
            .build()

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).products().get_payment_products(params)

        self.assertEqual(400, raised.exception.status_code)

    def test_get_payment_products_with_operation_type_returns_payment_products(self):
        params = GetPaymentProductsParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_operation_type("Authorization") \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_products(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_products)
        self.assertGreater(len(response.payment_products), 0)
        self.assertEqual("Authorization", params.operation_type)

    """Test get payment product"""

    def test_get_payment_product_valid_id_returns_payment_product(self):
        params = GetPaymentProductParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_product(VALID_PAYMENT_PRODUCT_ID, params)

        self.assertIsNotNone(response)
        self.assertEqual(VALID_PAYMENT_PRODUCT_ID, response.id)

    def test_get_payment_product_with_locale_returns_payment_product(self):
        params = GetPaymentProductParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_locale("nl_NL") \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_product(VALID_PAYMENT_PRODUCT_ID, params)

        self.assertIsNotNone(response)
        self.assertEqual(VALID_PAYMENT_PRODUCT_ID, response.id)

    def test_get_payment_product_with_amount_returns_payment_product(self):
        params = GetPaymentProductParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_amount(2500) \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_product(VALID_PAYMENT_PRODUCT_ID, params)

        self.assertIsNotNone(response)
        self.assertEqual(VALID_PAYMENT_PRODUCT_ID, response.id)

    def test_get_payment_product_with_is_recurring_returns_payment_product(self):
        params = GetPaymentProductParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_is_recurring(False) \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_product(VALID_PAYMENT_PRODUCT_ID, params)

        self.assertIsNotNone(response)
        self.assertEqual(VALID_PAYMENT_PRODUCT_ID, response.id)

    def test_get_payment_product_with_add_hide_returns_payment_product(self):
        params = GetPaymentProductParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_add_hide_list(["accountsOnFile"]) \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_product(VALID_PAYMENT_PRODUCT_ID, params)

        self.assertIsNotNone(response)
        self.assertEqual(VALID_PAYMENT_PRODUCT_ID, response.id)
        self.assertIsNotNone(params.hide)
        self.assertEqual(1, len(params.hide))
        self.assertIn("accountsOnFile", params.hide)

    def test_get_payment_product_with_hide_list_returns_payment_product(self):
        hide_fields = ["fields"]
        params = GetPaymentProductParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_hide_list(hide_fields) \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_product(VALID_PAYMENT_PRODUCT_ID, params)

        self.assertIsNotNone(response)
        self.assertEqual(VALID_PAYMENT_PRODUCT_ID, response.id)
        self.assertEqual(hide_fields, params.hide)

    def test_get_payment_product_params_getters_return_correct_values(self):
        params = GetPaymentProductParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_locale("nl_NL") \
            .with_amount(2500) \
            .with_is_recurring(False) \
            .build()

        self.assertEqual(COUNTRY_CODE, params.country_code)
        self.assertEqual(CURRENCY_CODE, params.currency_code)
        self.assertEqual("nl_NL", params.locale)
        self.assertEqual(2500, params.amount)
        self.assertFalse(params.is_recurring)

    def test_get_payment_product_invalid_id_raises_reference_exception(self):
        params = GetPaymentProductParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .build()

        with self.assertRaises(ReferenceException) as raised:
            self.client.merchant(MERCHANT_ID).products().get_payment_product(INVALID_PAYMENT_PRODUCT_ID, params)

        self.assertEqual(404, raised.exception.status_code)

    def test_get_payment_product_with_operation_type_returns_payment_product(self):
        params = GetPaymentProductParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_operation_type("Authorization") \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_product(VALID_PAYMENT_PRODUCT_ID, params)

        self.assertIsNotNone(response)
        self.assertEqual(VALID_PAYMENT_PRODUCT_ID, response.id)
        self.assertEqual("Authorization", params.operation_type)

    """Test get payment product networks"""

    def test_get_payment_product_networks_valid_id_returns_networks(self):
        params = GetPaymentProductNetworksParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_product_networks(VALID_PAYMENT_PRODUCT_NETWORKS_ID, params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.networks)
        self.assertGreater(len(response.networks), 0)
        self.assertIsNotNone(response.networks[0])

    def test_get_payment_product_networks_with_amount_returns_networks(self):
        params = GetPaymentProductNetworksParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_amount(3000) \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_product_networks(VALID_PAYMENT_PRODUCT_NETWORKS_ID, params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.networks)

    def test_get_payment_product_networks_with_is_recurring_returns_networks(self):
        params = GetPaymentProductNetworksParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_is_recurring(True) \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_payment_product_networks(VALID_PAYMENT_PRODUCT_NETWORKS_ID, params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.networks)

    def test_get_payment_product_networks_params_getters_return_correct_values(self):
        params = GetPaymentProductNetworksParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .with_amount(3000) \
            .with_is_recurring(True) \
            .build()

        self.assertEqual(COUNTRY_CODE, params.country_code)
        self.assertEqual(CURRENCY_CODE, params.currency_code)
        self.assertEqual(3000, params.amount)
        self.assertTrue(params.is_recurring)

    def test_get_payment_product_networks_invalid_id_raises_reference_exception(self):
        params = GetPaymentProductNetworksParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .build()

        with self.assertRaises(ReferenceException) as raised:
            self.client.merchant(MERCHANT_ID).products().get_payment_product_networks(INVALID_PAYMENT_PRODUCT_ID, params)

        self.assertEqual(404, raised.exception.status_code)

    """Test get product directory"""

    @unittest.skip("Test is skipped because no payment method supports directory fot the test merchant.")
    def test_get_product_directory_valid_id_returns_directory(self):
        params = GetProductDirectoryParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .build()

        response = self.client.merchant(MERCHANT_ID).products().get_product_directory(VALID_PAYMENT_PRODUCT_DIRECTORY_ID, params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.entries)
        self.assertGreater(len(response.entries), 0)
        self.assertIsNotNone(response.entries[0])

    def test_get_product_directory_invalid_id_raises_reference_exception(self):
        params = GetProductDirectoryParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .build()

        with self.assertRaises(ReferenceException) as raised:
            self.client.merchant(MERCHANT_ID).products().get_product_directory(INVALID_PAYMENT_PRODUCT_ID, params)

        self.assertEqual(404, raised.exception.status_code)

    def test_get_product_directory_params_getters_return_correct_values(self):
        params = GetProductDirectoryParamsBuilder() \
            .with_country_code(COUNTRY_CODE) \
            .with_currency_code(CURRENCY_CODE) \
            .build()

        self.assertEqual(COUNTRY_CODE, params.country_code)
        self.assertEqual(CURRENCY_CODE, params.currency_code)

    """Test create payment product session"""

    def test_create_payment_product_session_invalid_id_raises_validation_exception(self):
        request = PaymentProductSessionRequestBuilder().build()

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).products().create_payment_product_session(INVALID_PAYMENT_PRODUCT_ID, request)

        self.assertEqual(400, raised.exception.status_code)


if __name__ == "__main__":
    unittest.main()
