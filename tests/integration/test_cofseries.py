import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.cofseries.import_cof_series_request_builder import ImportCofSeriesRequestBuilder
from tests.integration.sdk_test_helper import create_token_and_get_id, create_payment_and_get_id
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.validation_exception import ValidationException


class CofSeriesIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test import cof series"""

    @unittest.skip("Test is skipped because the Import COF Series endpoint features are not enabled for the test merchant.")
    def test_import_cof_series_valid_request_returns_response(self):
        request = ImportCofSeriesRequestBuilder().build()

        response = self.client.merchant(MERCHANT_ID).cof_series().import_cof_series(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_id)

    @unittest.skip(
    "Test is skipped because the Import COF Series endpoint features are not enabled for the test merchant.")
    def test_import_cof_series_with_call_context_returns_response(self):
        request = ImportCofSeriesRequestBuilder().build()
        context = CallContext(idempotence_key="test-cof-series-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).cof_series().import_cof_series(request, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_id)

    @unittest.skip("Test is skipped because the Import COF Series endpoint features are not enabled for the test merchant.")
    def test_import_cof_series_valid_token_id_returns_response(self):
        token_id = create_token_and_get_id(self.client)
        request = ImportCofSeriesRequestBuilder() \
            .with_token_id(token_id) \
            .build()

        response = self.client.merchant(MERCHANT_ID).cof_series().import_cof_series(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_id)

    def test_import_cof_series_invalid_input_raises_validation_exception(self):
        request = ImportCofSeriesRequestBuilder() \
            .with_scheme_reference_data(None) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).cof_series().import_cof_series(request)

    @unittest.skip("Test is skipped because the Import COF Series endpoint features are not enabled for the test merchant.")
    def test_import_cof_series_with_transaction_link_identifier_returns_response(self):
        payment_id = create_payment_and_get_id(self.client)
        request = ImportCofSeriesRequestBuilder() \
            .with_transaction_link_identifier(payment_id) \
            .build()

        response = self.client.merchant(MERCHANT_ID).cof_series().import_cof_series(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_id)


if __name__ == '__main__':
    unittest.main()
