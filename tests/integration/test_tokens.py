import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.common.create_token_request_builder import CreateTokenRequestBuilder
from tests.integration.sdk_test_helper import create_token_and_get_id
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.reference_exception import ReferenceException
from onlinepayments.sdk.validation_exception import ValidationException

INVALID_TOKEN_ID = "invalid_token_12345"
EXPECTED_CARDHOLDER_NAME = "John Doe"
EXPECTED_EXPIRY_DATE = "1230"


class TokensIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test create token - valid input"""

    def test_create_token_returns_valid_response(self):
        request = CreateTokenRequestBuilder().build()

        response = self.client.merchant(MERCHANT_ID).tokens().create_token(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.token)
        self.assertIsNotNone(response.card)
        self.assertEqual(EXPECTED_CARDHOLDER_NAME, response.card.cardholder_name)
        self.assertEqual(EXPECTED_EXPIRY_DATE, response.card.expiry_date)
        self.assertIsNotNone(response.card.card_number)

    def test_create_token_with_call_context_returns_valid_response(self):
        request = CreateTokenRequestBuilder().build()
        context = CallContext(idempotence_key="test-tokens-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).tokens().create_token(request, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.token)
        self.assertIsNotNone(response.card)
        self.assertEqual(EXPECTED_CARDHOLDER_NAME, response.card.cardholder_name)
        self.assertEqual(EXPECTED_EXPIRY_DATE, response.card.expiry_date)
        self.assertIsNotNone(response.card.card_number)

    """Test create token - invalid input"""

    def test_create_token_invalid_card_number_raises_validation_exception(self):
        request = CreateTokenRequestBuilder() \
            .with_card_number("1234567890123456") \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).tokens().create_token(request)

    def test_create_token_invalid_expiry_date_raises_validation_exception(self):
        request = CreateTokenRequestBuilder() \
            .with_expiry_date("0000") \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).tokens().create_token(request)

    def test_create_token_invalid_cvv_raises_validation_exception(self):
        request = CreateTokenRequestBuilder() \
            .with_cvv("12345678") \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).tokens().create_token(request)

    """Test get token"""

    def test_get_token_valid_id_returns_token_details(self):
        token_id = create_token_and_get_id(self.client)

        response = self.client.merchant(MERCHANT_ID).tokens().get_token(token_id)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertEqual(token_id, response.id)
        self.assertIsNotNone(response.payment_product_id)

        self.assertIsNotNone(response.card)
        self.assertIsNotNone(response.card.data)
        self.assertIsNotNone(response.card.data.card_without_cvv)
        self.assertIsNotNone(response.card.data.card_without_cvv.card_number)

    def test_get_token_invalid_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).tokens().get_token(INVALID_TOKEN_ID)

    """Test delete token"""

    def test_delete_token_valid_id_deletes_token(self):
        token_id = create_token_and_get_id(self.client)

        self.client.merchant(MERCHANT_ID).tokens().delete_token(token_id)

        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).tokens().get_token(token_id)

    def test_delete_token_invalid_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).tokens().delete_token(INVALID_TOKEN_ID)


if __name__ == "__main__":
    unittest.main()
