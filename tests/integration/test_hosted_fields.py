import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.hostedfields.create_hosted_fields_session_request_builder import CreateHostedFieldsSessionRequestBuilder
from tests.integration.sdk_test_helper import create_token_and_get_id
from onlinepayments.sdk.api_exception import ApiException
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.problem_details_exception import ProblemDetailsException
from onlinepayments.sdk.validation_exception import ValidationException

INVALID_LOCALE = "invalid-locale"


class HostedFieldsIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test create hosted fields session - valid input"""

    def test_create_hosted_fields_session_returns_session_data_with_session_id(self):
        request = CreateHostedFieldsSessionRequestBuilder().build()

        response = self.client.merchant(MERCHANT_ID).hosted_fields().create_hosted_fields_session(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.session_data)
        self.assertIsNotNone(response.session_data.hosted_fields_session_id)
        self.assertIsNotNone(response.sdk_url)
        self.assertIsNotNone(response.sdk_sri)

    def test_create_hosted_fields_session_with_call_context_returns_session_data_with_session_id(self):
        request = CreateHostedFieldsSessionRequestBuilder().build()
        context = CallContext(idempotence_key="test-hosted-fields-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).hosted_fields().create_hosted_fields_session(request, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.session_data)
        self.assertIsNotNone(response.session_data.hosted_fields_session_id)
        self.assertIsNotNone(response.sdk_url)
        self.assertIsNotNone(response.sdk_sri)

    """Test create hosted fields session - invalid locale"""

    def test_create_hosted_fields_session_missing_locale_raises_validation_exception(self):
        request = CreateHostedFieldsSessionRequestBuilder() \
            .with_locale(None) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).hosted_fields().create_hosted_fields_session(request)

    def test_create_hosted_fields_session_empty_locale_raises_validation_exception(self):
        request = CreateHostedFieldsSessionRequestBuilder() \
            .with_locale("") \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).hosted_fields().create_hosted_fields_session(request)

    def test_create_hosted_fields_session_invalid_locale_format_raises_api_exception(self):
        request = CreateHostedFieldsSessionRequestBuilder() \
            .with_locale(INVALID_LOCALE) \
            .build()

        with self.assertRaises(ApiException) as raised:
            self.client.merchant(MERCHANT_ID).hosted_fields().create_hosted_fields_session(request)

        self.assertEqual(422, raised.exception.status_code)

    def test_create_hosted_fields_session_with_tokens_returns_session_data(self):
        token_id = create_token_and_get_id(self.client)
        request = CreateHostedFieldsSessionRequestBuilder() \
            .with_tokens([token_id]) \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_fields().create_hosted_fields_session(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.session_data)
        self.assertIsNotNone(response.session_data.hosted_fields_session_id)

    """Test get hosted fields session"""

    def test_get_hosted_fields_session_with_valid_session_id_returns_session(self):
        create_request = CreateHostedFieldsSessionRequestBuilder().build()
        create_response = self.client.merchant(MERCHANT_ID).hosted_fields().create_hosted_fields_session(create_request)
        session_id = create_response.session_data.hosted_fields_session_id

        response = self.client.merchant(MERCHANT_ID).hosted_fields().get_hosted_fields_session(session_id)

        self.assertIsNotNone(response)
        self.assertEqual(session_id, response.session_id)

    def test_get_hosted_fields_session_with_invalid_session_id_raises_problem_details_exception(self):
        with self.assertRaises(ProblemDetailsException) as raised:
            self.client.merchant(MERCHANT_ID).hosted_fields().get_hosted_fields_session("invalid-session-id")

        self.assertIsNotNone(raised.exception)


if __name__ == "__main__":
    unittest.main()