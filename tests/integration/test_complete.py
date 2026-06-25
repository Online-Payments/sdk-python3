import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.complete.complete_payment_request_builder import CompletePaymentRequestBuilder
from tests.integration.sdk_test_helper import _create_paypal_payment_and_get_id
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.platform_exception import PlatformException
from onlinepayments.sdk.reference_exception import ReferenceException
from onlinepayments.sdk.validation_exception import ValidationException

NON_EXISTING_PAYMENT_ID = "9999999999_0"


class CompleteIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test complete payment"""

    def test_complete_payment_valid_payment_id_raises_platform_exception(self):
        payment_id = _create_paypal_payment_and_get_id(self.client)
        request = CompletePaymentRequestBuilder().build()

        with self.assertRaises(PlatformException) as platform_exception_context:
            self.client.merchant(MERCHANT_ID).complete().complete_payment(payment_id, request)

        exception = platform_exception_context.exception
        self.assertIsNotNone(exception.errors)
        self.assertIsNotNone(exception.errors[0].http_status_code)
        self.assertEqual(500, exception.errors[0].http_status_code)

        self.assertIsNotNone(exception.errors[0].category)
        self.assertEqual("DIRECT_PLATFORM_ERROR", exception.errors[0].category)

    def test_complete_payment_valid_payment_id_and_call_context_raises_platform_exception(self):
        payment_id = _create_paypal_payment_and_get_id(self.client)
        request = CompletePaymentRequestBuilder().build()
        context = CallContext(idempotence_key="test-complete-" + str(uuid.uuid4()))

        with self.assertRaises(PlatformException) as platform_exception_context:
            self.client.merchant(MERCHANT_ID).complete().complete_payment(payment_id, request, context)

        exception = platform_exception_context.exception
        self.assertIsNotNone(exception.errors)
        self.assertIsNotNone(exception.errors[0].http_status_code)
        self.assertEqual(500, exception.errors[0].http_status_code)

        self.assertIsNotNone(exception.errors[0].category)
        self.assertEqual("DIRECT_PLATFORM_ERROR", exception.errors[0].category)

    def test_complete_payment_invalid_payment_id_raises_reference_exception(self):
        request = CompletePaymentRequestBuilder().build()

        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).complete().complete_payment(NON_EXISTING_PAYMENT_ID, request)

    def test_complete_payment_invalid_input_raises_validation_exception(self):
        payment_id = _create_paypal_payment_and_get_id(self.client)
        request = CompletePaymentRequestBuilder() \
            .with_order(None) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).complete().complete_payment(payment_id, request)


if __name__ == '__main__':
    unittest.main()
