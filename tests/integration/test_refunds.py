import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.payments.capture_payment_request_builder import CapturePaymentRequestBuilder
from tests.integration.builders.payments.refund_request_builder import RefundRequestBuilder
from tests.integration.sdk_test_helper import create_payment_and_get_id
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.reference_exception import ReferenceException

NON_EXISTING_PAYMENT_ID = "9999999999_0"


class RefundsIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test get refunds"""

    def test_get_refunds_valid_payment_id_returns_refunds(self):
        payment_id = create_payment_and_get_id(self.client)
        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        self.client.merchant(MERCHANT_ID).payments().refund_payment(
            payment_id, RefundRequestBuilder().build()
        )

        response = self.client.merchant(MERCHANT_ID).refunds().get_refunds(payment_id)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.refunds)
        self.assertGreater(len(response.refunds), 0)
        self.assertIsNotNone(response.refunds[0])
        self.assertIsNotNone(response.refunds[0].id)
        self.assertIsNotNone(response.refunds[0].status)

    def test_get_refunds_valid_payment_id_with_call_context_returns_refunds(self):
        payment_id = create_payment_and_get_id(self.client)
        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        self.client.merchant(MERCHANT_ID).payments().refund_payment(
            payment_id, RefundRequestBuilder().build()
        )

        context = CallContext(idempotence_key="test-refunds-" + str(uuid.uuid4()))
        response = self.client.merchant(MERCHANT_ID).refunds().get_refunds(payment_id, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.refunds)
        self.assertGreater(len(response.refunds), 0)
        self.assertIsNotNone(response.refunds[0])
        self.assertIsNotNone(response.refunds[0].id)
        self.assertIsNotNone(response.refunds[0].status)

    def test_get_refunds_valid_payment_id_returns_refund_details(self):
        payment_id = create_payment_and_get_id(self.client)
        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        self.client.merchant(MERCHANT_ID).payments().refund_payment(
            payment_id, RefundRequestBuilder().build()
        )

        response = self.client.merchant(MERCHANT_ID).refunds().get_refunds(payment_id)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.refunds)
        self.assertGreater(len(response.refunds), 0)
        self.assertIsNotNone(response.refunds[0].id)
        self.assertIsNotNone(response.refunds[0].status)
        self.assertIsNotNone(response.refunds[0].refund_output)
        self.assertIsNotNone(response.refunds[0].status_output)

    def test_get_refunds_valid_payment_id_returns_multiple_refunds_if_exists(self):
        payment_id = create_payment_and_get_id(self.client)
        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        self.client.merchant(MERCHANT_ID).payments().refund_payment(
            payment_id, RefundRequestBuilder().build()
        )

        response = self.client.merchant(MERCHANT_ID).refunds().get_refunds(payment_id)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.refunds)
        self.assertGreater(len(response.refunds), 0)

        for refund in response.refunds:
            self.assertIsNotNone(refund.id)
            self.assertIsNotNone(refund.status)

    def test_get_refunds_invalid_payment_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException) as raised:
            self.client.merchant(MERCHANT_ID).refunds().get_refunds(NON_EXISTING_PAYMENT_ID)

        self.assertEqual(404, raised.exception.status_code)


if __name__ == "__main__":
    unittest.main()
