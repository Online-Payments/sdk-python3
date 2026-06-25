import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.services.get_iin_details_request_builder import GetIINDetailsRequestBuilder
from tests.integration.builders.services.currency_conversion_request_builder import CurrencyConversionRequestBuilder
from tests.integration.builders.services.calculate_surcharge_request_builder import CalculateSurchargeRequestBuilder
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.validation_exception import ValidationException

INVALID_BIN = "123"


class ServicesIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test connection"""

    def test_connection_valid_request_returns_result(self):
        response = self.client.merchant(MERCHANT_ID).services().test_connection()

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.result)

    def test_connection_with_call_context_returns_result(self):
        context = CallContext(idempotence_key="test-services-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).services().test_connection(context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.result)

    """Test get IIN details"""

    def test_get_iin_details_valid_request_returns_iin_details(self):
        request = GetIINDetailsRequestBuilder().build()

        response = self.client.merchant(MERCHANT_ID).services().get_iin_details(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.card_type)
        self.assertIsNotNone(response.payment_product_id)
        self.assertIsNotNone(response.card_scheme)

    def test_get_iin_details_invalid_bin_raises_validation_exception(self):
        request = GetIINDetailsRequestBuilder() \
            .with_bin(INVALID_BIN) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).services().get_iin_details(request)

    """Test currency conversion"""

    @unittest.skip("Test is skipped because the Currency Conversion feature is not enabled for the test merchant.")
    def test_get_dcc_rate_inquiry_valid_request_returns_currency_conversion_response(self):
        request = CurrencyConversionRequestBuilder() \
            .with_card_number("4012000033330026") \
            .build()

        response = self.client.merchant(MERCHANT_ID).services().get_dcc_rate_inquiry(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.result)

    def test_get_dcc_rate_inquiry_missing_card_source_raises_validation_exception(self):
        request = CurrencyConversionRequestBuilder() \
            .with_amount(1000) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).services().get_dcc_rate_inquiry(request)

    def test_get_dcc_rate_inquiry_invalid_amount_raises_validation_exception(self):
        request = CurrencyConversionRequestBuilder() \
            .with_amount(-1000) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).services().get_dcc_rate_inquiry(request)

    """Test surcharge calculation"""

    @unittest.skip("Test is skipped because the Surcharge Calculation feature is not enabled for the test merchant.")
    def test_surcharge_calculation_valid_request_returns_surcharge_response(self):
        request = CalculateSurchargeRequestBuilder() \
            .with_card_number("5425233430109903") \
            .build()

        response = self.client.merchant(MERCHANT_ID).services().surcharge_calculation(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.surcharges)

    def test_surcharge_calculation_missing_card_source_raises_validation_exception(self):
        request = CalculateSurchargeRequestBuilder().build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).services().surcharge_calculation(request)

    def test_surcharge_calculation_invalid_amount_raises_validation_exception(self):
        request = CalculateSurchargeRequestBuilder() \
            .with_amount(-1000) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).services().surcharge_calculation(request)


if __name__ == "__main__":
    unittest.main()
