import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.webhooks.validate_credentials_request_builder import ValidateCredentialsRequestBuilder
from tests.integration.builders.webhooks.send_test_request_builder import SendTestRequestBuilder
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.validation_exception import ValidationException

VALID_WEBHOOK_KEY = "test-key"
VALID_WEBHOOK_SECRET = "test-secret"
INVALID_WEBHOOK_URL = "invalid-url"
VALID_WEBHOOK_URL = "https://example.com/webhook"


class WebhooksIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test validate webhook credentials"""

    def test_validate_webhook_credentials_valid_credentials_returns_result(self):
        request = ValidateCredentialsRequestBuilder() \
            .with_key(VALID_WEBHOOK_KEY) \
            .with_secret(VALID_WEBHOOK_SECRET) \
            .build()

        response = self.client.merchant(MERCHANT_ID).webhooks().validate_webhook_credentials(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.result)

    def test_validate_webhook_credentials_with_call_context_returns_result(self):
        request = ValidateCredentialsRequestBuilder() \
            .with_key(VALID_WEBHOOK_KEY) \
            .with_secret(VALID_WEBHOOK_SECRET) \
            .build()

        context = CallContext(idempotence_key="test-webhooks-" + str(uuid.uuid4()))
        response = self.client.merchant(MERCHANT_ID).webhooks().validate_webhook_credentials(request, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.result)

    def test_validate_webhook_credentials_incorrect_secret_returns_invalid(self):
        request = ValidateCredentialsRequestBuilder() \
            .with_key(VALID_WEBHOOK_KEY) \
            .with_secret("incorrect-secret") \
            .build()

        response = self.client.merchant(MERCHANT_ID).webhooks().validate_webhook_credentials(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.result)
        self.assertEqual("Invalid", response.result)

    """Test send test webhook"""

    def test_send_test_webhook_missing_configuration_raises_validation_exception(self):
        request = SendTestRequestBuilder() \
            .with_url(VALID_WEBHOOK_URL) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).webhooks().send_test_webhook(request)

    def test_send_test_webhook_missing_url_raises_validation_exception(self):
        request = SendTestRequestBuilder().build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).webhooks().send_test_webhook(request)

    def test_send_test_webhook_invalid_url_raises_validation_exception(self):
        request = SendTestRequestBuilder() \
            .with_url(INVALID_WEBHOOK_URL) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).webhooks().send_test_webhook(request)


if __name__ == '__main__':
    unittest.main()
