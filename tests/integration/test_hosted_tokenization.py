import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.hostedtokenization.create_hosted_tokenization_request_builder import CreateHostedTokenizationRequestBuilder
from tests.integration.sdk_test_helper import create_hosted_tokenization_and_get_id
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.reference_exception import ReferenceException
from onlinepayments.sdk.validation_exception import ValidationException

INVALID_TOKENIZATION_ID = "invalid_id_12345"


class HostedTokenizationIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test create hosted tokenization - valid input"""

    def test_create_hosted_tokenization_returns_id_and_url(self):
        request = CreateHostedTokenizationRequestBuilder().build()

        response = self.client.merchant(MERCHANT_ID).hosted_tokenization().create_hosted_tokenization(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_tokenization_id)
        self.assertIsNotNone(response.hosted_tokenization_url)

    def test_create_hosted_tokenization_with_call_context_returns_id_and_url(self):
        request = CreateHostedTokenizationRequestBuilder().build()
        context = CallContext(idempotence_key="test-hosted-tokenization-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).hosted_tokenization().create_hosted_tokenization(request, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_tokenization_id)
        self.assertIsNotNone(response.hosted_tokenization_url)

    """Test create hosted tokenization - invalid locale"""

    def test_create_hosted_tokenization_invalid_locale_raises_validation_exception(self):
        request = CreateHostedTokenizationRequestBuilder() \
            .with_locale("invalid_locale") \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).hosted_tokenization().create_hosted_tokenization(request)

    """Test create hosted tokenization - tokens"""

    def test_create_hosted_tokenization_with_single_invalid_token_returns_invalid_tokens(self):
        request = CreateHostedTokenizationRequestBuilder() \
            .with_token("firstInvalidToken") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_tokenization().create_hosted_tokenization(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_tokenization_id)
        self.assertIsNotNone(response.hosted_tokenization_url)
        self.assertIsNotNone(response.invalid_tokens)
        self.assertEqual(1, len(response.invalid_tokens))
        self.assertIn("firstInvalidToken", response.invalid_tokens)

    def test_create_hosted_tokenization_with_multiple_invalid_tokens_returns_invalid_tokens(self):
        request = CreateHostedTokenizationRequestBuilder() \
            .with_tokens("firstInvalidToken", "secondInvalidToken") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_tokenization().create_hosted_tokenization(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_tokenization_id)
        self.assertIsNotNone(response.hosted_tokenization_url)
        self.assertIsNotNone(response.invalid_tokens)
        self.assertEqual(2, len(response.invalid_tokens))
        self.assertIn("firstInvalidToken", response.invalid_tokens)
        self.assertIn("secondInvalidToken", response.invalid_tokens)

    def test_create_hosted_tokenization_with_chained_tokens_returns_invalid_tokens(self):
        request = CreateHostedTokenizationRequestBuilder() \
            .with_token("firstChainedToken") \
            .with_token("secondChainedToken") \
            .with_token("thirdChainedToken") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_tokenization().create_hosted_tokenization(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_tokenization_id)
        self.assertIsNotNone(response.hosted_tokenization_url)
        self.assertIsNotNone(response.invalid_tokens)
        self.assertEqual(3, len(response.invalid_tokens))
        self.assertIn("firstChainedToken", response.invalid_tokens)
        self.assertIn("secondChainedToken", response.invalid_tokens)
        self.assertIn("thirdChainedToken", response.invalid_tokens)

    def test_create_hosted_tokenization_with_empty_token_list_returns_empty_invalid_tokens(self):
        request = CreateHostedTokenizationRequestBuilder() \
            .with_tokens() \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_tokenization().create_hosted_tokenization(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_tokenization_id)
        self.assertIsNotNone(response.hosted_tokenization_url)
        self.assertEqual(0, len(response.invalid_tokens or []))

    def test_create_hosted_tokenization_with_special_character_tokens_returns_invalid_tokens(self):
        request = CreateHostedTokenizationRequestBuilder() \
            .with_tokens("token-with-dashes", "token_with_underscores", "token.with.dots") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_tokenization().create_hosted_tokenization(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_tokenization_id)
        self.assertIsNotNone(response.hosted_tokenization_url)
        self.assertIsNotNone(response.invalid_tokens)
        self.assertEqual(3, len(response.invalid_tokens))

    def test_create_hosted_tokenization_with_ten_tokens_returns_invalid_tokens(self):
        request = CreateHostedTokenizationRequestBuilder() \
            .with_tokens(
                "firstToken", "secondToken", "thirdToken", "fourthToken", "fifthToken",
                "sixthToken", "seventhToken", "eighthToken", "ninthToken", "tenthToken"
            ) \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_tokenization().create_hosted_tokenization(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_tokenization_id)
        self.assertIsNotNone(response.hosted_tokenization_url)
        self.assertIsNotNone(response.invalid_tokens)
        self.assertEqual(10, len(response.invalid_tokens))

    def test_create_hosted_tokenization_with_duplicate_tokens_returns_invalid_tokens(self):
        request = CreateHostedTokenizationRequestBuilder() \
            .with_tokens("duplicateToken", "duplicateToken", "uniqueToken") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_tokenization().create_hosted_tokenization(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_tokenization_id)
        self.assertIsNotNone(response.hosted_tokenization_url)
        self.assertIsNotNone(response.invalid_tokens)
        self.assertGreater(len(response.invalid_tokens), 0)

    """Test get hosted tokenization"""

    def test_get_hosted_tokenization_valid_id_returns_details(self):
        hosted_tokenization_id = create_hosted_tokenization_and_get_id(self.client)

        response = self.client.merchant(MERCHANT_ID).hosted_tokenization().get_hosted_tokenization(hosted_tokenization_id)

        self.assertIsNotNone(response)

    def test_get_hosted_tokenization_invalid_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).hosted_tokenization().get_hosted_tokenization(INVALID_TOKENIZATION_ID)


if __name__ == "__main__":
    unittest.main()