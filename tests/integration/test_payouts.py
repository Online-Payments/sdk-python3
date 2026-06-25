import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.payouts.create_payout_request_builder import CreatePayoutRequestBuilder
from tests.integration.sdk_test_helper import create_payout_and_get_id
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.validation_exception import ValidationException
from onlinepayments.sdk.reference_exception import ReferenceException

NON_EXISTING_PAYOUT_ID = "9999999999_0"


class PayoutsIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test create payout"""

    def test_create_payout_valid_card_input_returns_payout_id(self):
        request = CreatePayoutRequestBuilder().build()

        response = self.client.merchant(MERCHANT_ID).payouts().create_payout(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertGreater(len(response.id), 0)
        self.assertIsNotNone(response.status)
        self.assertIsNotNone(response.payout_output)
        self.assertIsNotNone(response.payout_output.amount_of_money)
        self.assertEqual(request.amount_of_money.amount, response.payout_output.amount_of_money.amount)
        self.assertEqual(request.amount_of_money.currency_code, response.payout_output.amount_of_money.currency_code)

    def test_create_payout_with_call_context_returns_payout_id(self):
        request = CreatePayoutRequestBuilder().build()
        context = CallContext(idempotence_key="test-payouts-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).payouts().create_payout(request, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertGreater(len(response.id), 0)
        self.assertIsNotNone(response.status)
        self.assertIsNotNone(response.payout_output)
        self.assertIsNotNone(response.payout_output.amount_of_money)
        self.assertEqual(request.amount_of_money.amount, response.payout_output.amount_of_money.amount)
        self.assertEqual(request.amount_of_money.currency_code, response.payout_output.amount_of_money.currency_code)

    def test_create_payout_invalid_amount_raises_validation_exception(self):
        request = CreatePayoutRequestBuilder() \
            .with_amount(-1000) \
            .with_currency("EUR") \
            .build()

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).payouts().create_payout(request)

        exception = raised.exception
        self.assertIsNotNone(exception.error_id)
        self.assertGreater(len(exception.errors), 0)

        error = exception.errors[0]
        self.assertEqual("INVALID_VALUE", error.id)
        self.assertEqual(400, error.http_status_code)

    def test_create_payout_invalid_currency_code_raises_validation_exception(self):
        request = CreatePayoutRequestBuilder() \
            .with_currency("INVALID") \
            .build()

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).payouts().create_payout(request)

        exception = raised.exception
        self.assertIsNotNone(exception.error_id)
        self.assertGreater(len(exception.errors), 0)

        error = exception.errors[0]
        self.assertEqual("INVALID_VALUE", error.id)
        self.assertEqual(400, error.http_status_code)

    def test_create_payout_invalid_card_number_raises_validation_exception(self):
        request = CreatePayoutRequestBuilder() \
            .with_card_number("123") \
            .build()

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).payouts().create_payout(request)

        exception = raised.exception
        self.assertIsNotNone(exception.error_id)
        self.assertGreater(len(exception.errors), 0)

        error = exception.errors[0]
        self.assertEqual("INVALID_VALUE", error.id)
        self.assertEqual(400, error.http_status_code)

    """Test get payout"""

    def test_get_payout_valid_id_returns_payout(self):
        payout_id = create_payout_and_get_id(self.client)

        response = self.client.merchant(MERCHANT_ID).payouts().get_payout(payout_id)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertGreater(len(response.id), 0)
        self.assertEqual(payout_id, response.id)
        self.assertIsNotNone(response.status)
        self.assertEqual("ACCOUNT_CREDITED", response.status)

        self.assertIsNotNone(response.payout_output)
        self.assertIsNotNone(response.status_output)
        self.assertEqual("REFUNDED", response.status_output.status_category)
        self.assertEqual(8, response.status_output.status_code)

    def test_get_payout_invalid_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).payouts().get_payout(NON_EXISTING_PAYOUT_ID)


if __name__ == '__main__':
    unittest.main()
