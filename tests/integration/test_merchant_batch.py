import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.common.create_payment_request_builder import CreatePaymentRequestBuilder
from tests.integration.builders.merchant_batch.submit_batch_request_body_builder import SubmitBatchRequestBodyBuilder
from tests.integration.sdk_test_helper import submit_batch_and_get_reference
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.validation_exception import ValidationException
from onlinepayments.sdk.reference_exception import ReferenceException

NON_EXISTING_MERCHANT_BATCH_REFERENCE = "non-existing-batch-reference"
INVALID_MERCHANT_BATCH_REFERENCE = ""


class MerchantBatchIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test submit batch"""

    def test_submit_batch_valid_request_returns_submitted_batch(self):
        create_payment_request = CreatePaymentRequestBuilder().build()
        request = SubmitBatchRequestBodyBuilder() \
            .with_operation_type("CreatePayment") \
            .with_item_count(1) \
            .with_create_payment_requests([create_payment_request]) \
            .build()

        merchant_batch_reference = request.header.merchant_batch_reference

        response = self.client.merchant(MERCHANT_ID).merchant_batch().submit_batch(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.merchant_batch_reference)
        self.assertEqual(merchant_batch_reference, response.merchant_batch_reference)
        self.assertIsNotNone(response.total_count)
        self.assertEqual(1, response.total_count)

    def test_submit_batch_with_call_context_returns_submitted_batch(self):
        create_payment_request = CreatePaymentRequestBuilder().build()
        request = SubmitBatchRequestBodyBuilder() \
            .with_operation_type("CreatePayment") \
            .with_item_count(1) \
            .with_create_payment_requests([create_payment_request]) \
            .build()

        merchant_batch_reference = request.header.merchant_batch_reference
        context = CallContext(idempotence_key="test-merchant-batch-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).merchant_batch().submit_batch(request, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.merchant_batch_reference)
        self.assertEqual(merchant_batch_reference, response.merchant_batch_reference)
        self.assertIsNotNone(response.total_count)
        self.assertEqual(1, response.total_count)

    def test_submit_batch_invalid_reference_raises_validation_exception(self):
        create_payment_request = CreatePaymentRequestBuilder().build()
        request = SubmitBatchRequestBodyBuilder() \
            .with_merchant_batch_reference(INVALID_MERCHANT_BATCH_REFERENCE) \
            .with_operation_type("CreatePayment") \
            .with_item_count(1) \
            .with_create_payment_requests([create_payment_request]) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).merchant_batch().submit_batch(request)

    """Test process batch"""

    def test_process_batch_valid_reference_updates_batch_status(self):
        create_payment_request = CreatePaymentRequestBuilder().build()
        merchant_batch_reference = submit_batch_and_get_reference(
            self.client,
            "CreatePayment",
            1,
            [create_payment_request])

        self.client.merchant(MERCHANT_ID).merchant_batch().process_batch(merchant_batch_reference)

        status_response = self.client.merchant(MERCHANT_ID).merchant_batch().get_batch_status(merchant_batch_reference)
        self.assertIsNotNone(status_response)
        self.assertIsNotNone(status_response.status)

    def test_process_batch_invalid_reference_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).merchant_batch().process_batch(NON_EXISTING_MERCHANT_BATCH_REFERENCE)

    """Test get batch status"""

    def test_get_batch_status_valid_reference_returns_batch_status(self):
        create_payment_request = CreatePaymentRequestBuilder().build()
        merchant_batch_reference = submit_batch_and_get_reference(
            self.client,
            "CreatePayment",
            1,
            [create_payment_request])

        response = self.client.merchant(MERCHANT_ID).merchant_batch().get_batch_status(merchant_batch_reference)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.merchant_batch_reference)
        self.assertEqual(merchant_batch_reference, response.merchant_batch_reference)

        self.assertIsNotNone(response.item_count)
        self.assertEqual(1, response.item_count)
        self.assertIsNotNone(response.operation_type)
        self.assertIsNotNone(response.status)

    def test_get_batch_status_invalid_reference_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).merchant_batch().get_batch_status(NON_EXISTING_MERCHANT_BATCH_REFERENCE)


if __name__ == "__main__":
    unittest.main()
