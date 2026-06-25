import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.payments.capture_payment_request_builder import CapturePaymentRequestBuilder
from tests.integration.sdk_test_helper import create_payment_and_get_id
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.reference_exception import ReferenceException

NON_EXISTING_PAYMENT_ID = "9999999999_0"


class CapturesIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test get captures"""

    def test_get_captures_valid_payment_id_returns_captures(self):
        payment_id = create_payment_and_get_id(self.client)
        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        response = self.client.merchant(MERCHANT_ID).captures().get_captures(payment_id)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.captures)
        self.assertGreater(len(response.captures), 0)
        self.assertIsNotNone(response.captures[0])
        self.assertIsNotNone(response.captures[0].id)
        self.assertIsNotNone(response.captures[0].status)

    def test_get_captures_valid_payment_id_with_call_context_returns_captures(self):
        payment_id = create_payment_and_get_id(self.client)
        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        context = CallContext(idempotence_key="test-captures-" + str(uuid.uuid4()))
        response = self.client.merchant(MERCHANT_ID).captures().get_captures(payment_id, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.captures)
        self.assertGreater(len(response.captures), 0)
        self.assertIsNotNone(response.captures[0])
        self.assertIsNotNone(response.captures[0].id)
        self.assertIsNotNone(response.captures[0].status)

    def test_get_captures_valid_payment_id_returns_capture_details(self):
        payment_id = create_payment_and_get_id(self.client)
        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        response = self.client.merchant(MERCHANT_ID).captures().get_captures(payment_id)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.captures)
        self.assertGreater(len(response.captures), 0)
        self.assertIsNotNone(response.captures[0].id)
        self.assertIsNotNone(response.captures[0].status)
        self.assertIsNotNone(response.captures[0].capture_output)
        self.assertIsNotNone(response.captures[0].status_output)

    def test_get_captures_valid_payment_id_returns_multiple_captures_if_exists(self):
        payment_id = create_payment_and_get_id(self.client)
        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        response = self.client.merchant(MERCHANT_ID).captures().get_captures(payment_id)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.captures)
        self.assertGreater(len(response.captures), 0)

        for capture in response.captures:
            self.assertIsNotNone(capture.id)
            self.assertIsNotNone(capture.status)

    def test_get_captures_invalid_payment_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException) as raised:
            self.client.merchant(MERCHANT_ID).captures().get_captures(NON_EXISTING_PAYMENT_ID)

        self.assertEqual(404, raised.exception.status_code)


if __name__ == "__main__":
    unittest.main()