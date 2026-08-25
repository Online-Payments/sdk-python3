import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.common.create_payment_request_builder import CreatePaymentRequestBuilder
from tests.integration.builders.merchant_batch.submit_batch_request_body_builder import SubmitBatchRequestBodyBuilder
from tests.integration.builders.merchant_batch.get_payments_report_params_builder import GetPaymentsReportParamsBuilder
from tests.integration.sdk_test_helper import submit_batch_and_get_reference, submit_and_process_batch_and_get_reference
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.validation_exception import ValidationException
from onlinepayments.sdk.reference_exception import ReferenceException

NON_EXISTING_MERCHANT_BATCH_REFERENCE = "non-existing-batch-reference"
INVALID_MERCHANT_BATCH_REFERENCE = ""
INVALID_CURSOR = "invalid-cursor-value"
CURSOR_VALUE = "cursor-value"
LIMIT_BELOW_MINIMUM = 0
LIMIT_ABOVE_MAXIMUM = 1001

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

    """Test get payments report"""

    def test_get_payments_report_params_getters_return_correct_values(self):
        params = GetPaymentsReportParamsBuilder() \
            .with_cursor(CURSOR_VALUE) \
            .with_limit(50) \
            .build()

        self.assertEqual(CURSOR_VALUE, params.cursor)
        self.assertEqual(50, params.limit)

    def test_get_payments_report_valid_reference_returns_report(self):
        create_payment_request = CreatePaymentRequestBuilder().build()

        merchant_batch_reference = submit_and_process_batch_and_get_reference(
            self.client,
            "CreatePayment",
            1,
            [create_payment_request])

        params = GetPaymentsReportParamsBuilder().build()

        response = self.client.merchant(MERCHANT_ID).merchant_batch().get_payments_report(merchant_batch_reference, params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payments)
        self.assertIsNotNone(response.pagination)

    def test_get_payments_report_with_cursor_and_limit_returns_response(self):
        create_payment_request = CreatePaymentRequestBuilder().build()

        merchant_batch_reference = submit_and_process_batch_and_get_reference(
            self.client,
            "CreatePayment",
            1,
            [create_payment_request])

        first_page_params = GetPaymentsReportParamsBuilder().with_limit(1).build()
        first_page = self.client.merchant(MERCHANT_ID).merchant_batch().get_payments_report(merchant_batch_reference, first_page_params)

        self.assertIsNotNone(first_page)
        self.assertIsNotNone(first_page.payments)
        self.assertIsNotNone(first_page.pagination)

        second_page_params = GetPaymentsReportParamsBuilder() \
            .with_limit(1) \
            .with_cursor(first_page.pagination.next_cursor) \
            .build()
        second_page = self.client.merchant(MERCHANT_ID).merchant_batch().get_payments_report(merchant_batch_reference, second_page_params)

        self.assertIsNotNone(second_page)
        self.assertIsNotNone(second_page.payments)
        self.assertIsNotNone(second_page.pagination)

    def test_get_payments_report_with_call_context_returns_report(self):
        create_payment_request = CreatePaymentRequestBuilder().build()
        merchant_batch_reference = submit_and_process_batch_and_get_reference(
            self.client,
            "CreatePayment",
            1,
            [create_payment_request])

        params = GetPaymentsReportParamsBuilder().build()
        context = CallContext(idempotence_key="test-merchant-batch-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).merchant_batch().get_payments_report(merchant_batch_reference, params, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payments)
        self.assertIsNotNone(response.pagination)

    def test_get_payments_report_invalid_reference_raises_reference_exception(self):
        params = GetPaymentsReportParamsBuilder().build()

        with self.assertRaises(ReferenceException) as raised:
            self.client.merchant(MERCHANT_ID).merchant_batch().get_payments_report(NON_EXISTING_MERCHANT_BATCH_REFERENCE, params)

        self.assertEqual(404, raised.exception.status_code)

    def test_get_payments_report_invalid_cursor_raises_validation_exception(self):
        create_payment_request = CreatePaymentRequestBuilder().build()
        merchant_batch_reference = submit_batch_and_get_reference(
            self.client,
            "CreatePayment",
            1,
            [create_payment_request])

        params = GetPaymentsReportParamsBuilder().with_cursor(INVALID_CURSOR).build()

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).merchant_batch().get_payments_report(merchant_batch_reference, params)

        self.assertEqual(400, raised.exception.status_code)

    def test_get_payments_report_limit_below_minimum_raises_validation_exception(self):
        create_payment_request = CreatePaymentRequestBuilder().build()
        merchant_batch_reference = submit_batch_and_get_reference(
            self.client,
            "CreatePayment",
            1,
            [create_payment_request])

        params = GetPaymentsReportParamsBuilder().with_limit(LIMIT_BELOW_MINIMUM).build()

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).merchant_batch().get_payments_report(merchant_batch_reference, params)

        self.assertEqual(400, raised.exception.status_code)

    def test_get_payments_report_limit_above_maximum_raises_validation_exception(self):
        create_payment_request = CreatePaymentRequestBuilder().build()
        merchant_batch_reference = submit_batch_and_get_reference(
            self.client,
            "CreatePayment",
            1,
            [create_payment_request])

        params = GetPaymentsReportParamsBuilder().with_limit(LIMIT_ABOVE_MAXIMUM).build()

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).merchant_batch().get_payments_report(merchant_batch_reference, params)

        self.assertEqual(400, raised.exception.status_code)

if __name__ == "__main__":
    unittest.main()
