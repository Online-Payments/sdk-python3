import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.sessions.session_request_builder import SessionRequestBuilder
from tests.integration.sdk_test_helper import create_token_and_get_id
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.validation_exception import ValidationException


class SessionsIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test create session"""

    def test_create_session_valid_request_returns_client_session_id(self):
        request = SessionRequestBuilder().build()

        response = self.client.merchant(MERCHANT_ID).sessions().create_session(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.client_session_id)
        self.assertIsNotNone(response.asset_url)
        self.assertIsNotNone(response.client_api_url)

    def test_create_session_with_call_context_returns_client_session_id(self):
        request = SessionRequestBuilder().build()
        context = CallContext(idempotence_key="test-session-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).sessions().create_session(request, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.client_session_id)
        self.assertIsNotNone(response.asset_url)
        self.assertIsNotNone(response.client_api_url)

    def test_create_session_valid_token_returns_session(self):
        token_id = create_token_and_get_id(self.client)
        request = SessionRequestBuilder() \
            .with_token(token_id) \
            .build()

        response = self.client.merchant(MERCHANT_ID).sessions().create_session(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.client_session_id)
        self.assertNotIn(token_id, response.invalid_tokens or [])

    def test_create_session_too_many_tokens_raises_validation_exception(self):
        request = SessionRequestBuilder() \
            .with_tokens(
                "firstToken", "secondToken", "thirdToken", "fourthToken", "fifthToken",
                "sixthToken", "seventhToken", "eighthToken", "ninthToken", "tenthToken", "eleventhToken"
            ) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).sessions().create_session(request)

    def test_create_session_invalid_token_values_returns_invalid_tokens(self):
        request = SessionRequestBuilder() \
            .with_tokens("65468465464646", "654646464", "easgudasdas") \
            .build()

        response = self.client.merchant(MERCHANT_ID).sessions().create_session(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.client_session_id)
        self.assertIsNotNone(response.invalid_tokens)
        self.assertGreater(len(response.invalid_tokens), 0)


if __name__ == "__main__":
    unittest.main()