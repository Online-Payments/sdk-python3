import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.common.create_payment_request_builder import CreatePaymentRequestBuilder
from tests.integration.builders.payments.cancel_payment_request_builder import CancelPaymentRequestBuilder
from tests.integration.builders.payments.capture_payment_request_builder import CapturePaymentRequestBuilder
from tests.integration.builders.payments.refund_request_builder import RefundRequestBuilder
from tests.integration.sdk_test_helper import create_payment_and_get_id
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.declined_payment_exception import DeclinedPaymentException
from onlinepayments.sdk.reference_exception import ReferenceException
from onlinepayments.sdk.validation_exception import ValidationException

NON_EXISTING_PAYMENT_ID = "9999999999_0"
CURRENCY_CODE = "EUR"


class PaymentsIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test create payment"""

    def test_create_payment_valid_request_returns_payment(self):
        request = CreatePaymentRequestBuilder().build()

        response = self.client.merchant(MERCHANT_ID).payments().create_payment(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment)
        self.assertIsNotNone(response.payment.id)
        self.assertIsNotNone(response.payment.status)

    def test_create_payment_with_call_context_returns_payment(self):
        request = CreatePaymentRequestBuilder().build()
        context = CallContext(idempotence_key="test-payments-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).payments().create_payment(request, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment)
        self.assertIsNotNone(response.payment.id)
        self.assertIsNotNone(response.payment.status)

    def test_create_payment_invalid_card_number_raises_validation_exception(self):
        request = CreatePaymentRequestBuilder() \
            .with_card_number("123") \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payments().create_payment(request)

    def test_create_payment_unsupported_card_number_raises_declined_payment_exception(self):
        request = CreatePaymentRequestBuilder() \
            .with_card_number("4321456998744563") \
            .build()

        with self.assertRaises(DeclinedPaymentException):
            self.client.merchant(MERCHANT_ID).payments().create_payment(request)

    def test_create_payment_with_auto_capture_returns_payment(self):
        request = CreatePaymentRequestBuilder() \
            .with_auto_capture(True) \
            .build()

        response = self.client.merchant(MERCHANT_ID).payments().create_payment(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment)
        self.assertIsNotNone(response.payment.id)

    """Test get payment"""

    def test_get_payment_existing_id_returns_payment(self):
        payment_id = create_payment_and_get_id(self.client)

        response = self.client.merchant(MERCHANT_ID).payments().get_payment(payment_id)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertEqual(payment_id, response.id)
        self.assertIsNotNone(response.status)

    def test_get_payment_details_existing_id_returns_payment_details(self):
        payment_id = create_payment_and_get_id(self.client)

        response = self.client.merchant(MERCHANT_ID).payments().get_payment_details(payment_id)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertIsNotNone(response.payment_output)
        self.assertIsNotNone(response.status)

    def test_get_payment_invalid_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).payments().get_payment(NON_EXISTING_PAYMENT_ID)

    def test_get_payment_details_invalid_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).payments().get_payment_details(NON_EXISTING_PAYMENT_ID)

    """Test cancel payment"""

    def test_cancel_payment_valid_request_returns_cancelled_payment(self):
        payment_id = create_payment_and_get_id(self.client)

        response = self.client.merchant(MERCHANT_ID).payments().cancel_payment(
            payment_id, CancelPaymentRequestBuilder().build()
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment)
        self.assertIsNotNone(response.payment.id)
        self.assertIsNotNone(response.payment.status)

    def test_cancel_payment_partial_amount_returns_cancelled_payment(self):
        payment_id = create_payment_and_get_id(self.client, amount=800)

        request = CancelPaymentRequestBuilder() \
            .with_amount(300) \
            .with_currency(CURRENCY_CODE) \
            .with_is_final(False) \
            .build()

        response = self.client.merchant(MERCHANT_ID).payments().cancel_payment(payment_id, request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment)
        self.assertIsNotNone(response.payment.id)
        self.assertIsNotNone(response.payment.status)

    def test_cancel_payment_twice_remaining_valid_returns_cancelled_payment(self):
        payment_id = create_payment_and_get_id(self.client, amount=800)

        first_cancel_request = CancelPaymentRequestBuilder() \
            .with_amount(300) \
            .with_currency(CURRENCY_CODE) \
            .with_is_final(False) \
            .build()

        first_response = self.client.merchant(MERCHANT_ID).payments().cancel_payment(
            payment_id, first_cancel_request
        )

        self.assertIsNotNone(first_response)
        self.assertIsNotNone(first_response.payment)
        self.assertIsNotNone(first_response.payment.id)

        second_cancel_request = CancelPaymentRequestBuilder() \
            .with_amount(500) \
            .with_currency(CURRENCY_CODE) \
            .with_is_final(True) \
            .build()

        second_response = self.client.merchant(MERCHANT_ID).payments().cancel_payment(
            payment_id, second_cancel_request
        )

        self.assertIsNotNone(second_response)
        self.assertIsNotNone(second_response.payment)
        self.assertIsNotNone(second_response.payment.id)

    def test_cancel_payment_second_amount_exceeds_remaining_raises_validation_exception(self):
        payment_id = create_payment_and_get_id(self.client, amount=800)

        first_cancel_request = CancelPaymentRequestBuilder() \
            .with_amount(300) \
            .with_currency(CURRENCY_CODE) \
            .with_is_final(False) \
            .build()

        self.client.merchant(MERCHANT_ID).payments().cancel_payment(payment_id, first_cancel_request)

        second_cancel_request = CancelPaymentRequestBuilder() \
            .with_amount(600) \
            .with_currency(CURRENCY_CODE) \
            .with_is_final(False) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payments().cancel_payment(payment_id, second_cancel_request)

    def test_cancel_payment_invalid_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).payments().cancel_payment(
                NON_EXISTING_PAYMENT_ID, CancelPaymentRequestBuilder().build()
            )

    def test_cancel_payment_after_capture_raises_validation_exception(self):
        payment_id = create_payment_and_get_id(self.client)

        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payments().cancel_payment(
                payment_id, CancelPaymentRequestBuilder().build()
            )

    def test_cancel_payment_partial_exceeds_remaining_uncaptured_raises_validation_exception(self):
        payment_id = create_payment_and_get_id(self.client, amount=800)

        capture_request = CapturePaymentRequestBuilder() \
            .with_amount(600) \
            .with_is_final(False) \
            .build()

        self.client.merchant(MERCHANT_ID).payments().capture_payment(payment_id, capture_request)

        cancel_request = CancelPaymentRequestBuilder() \
            .with_amount(400) \
            .with_currency(CURRENCY_CODE) \
            .with_is_final(False) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payments().cancel_payment(payment_id, cancel_request)

    def test_cancel_payment_after_refund_raises_validation_exception(self):
        payment_id = create_payment_and_get_id(self.client)

        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )
        self.client.merchant(MERCHANT_ID).payments().refund_payment(
            payment_id, RefundRequestBuilder().build()
        )

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payments().cancel_payment(
                payment_id, CancelPaymentRequestBuilder().build()
            )

    def test_cancel_payment_after_previous_cancel_raises_validation_exception(self):
        payment_id = create_payment_and_get_id(self.client)

        self.client.merchant(MERCHANT_ID).payments().cancel_payment(
            payment_id, CancelPaymentRequestBuilder().build()
        )

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payments().cancel_payment(
                payment_id, CancelPaymentRequestBuilder().build()
            )

    """Test capture payment"""

    def test_capture_payment_valid_request_returns_captured_payment(self):
        payment_id = create_payment_and_get_id(self.client)

        response = self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertIsNotNone(response.status)

    def test_capture_payment_partial_amount_returns_captured_payment(self):
        payment_id = create_payment_and_get_id(self.client, amount=800)

        capture_request = CapturePaymentRequestBuilder() \
            .with_amount(300) \
            .with_is_final(False) \
            .build()

        response = self.client.merchant(MERCHANT_ID).payments().capture_payment(payment_id, capture_request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertIsNotNone(response.status)

    def test_capture_payment_remaining_amount_returns_captured_payment(self):
        payment_id = create_payment_and_get_id(self.client, amount=800)

        first_capture_request = CapturePaymentRequestBuilder() \
            .with_amount(300) \
            .with_is_final(False) \
            .build()

        first_response = self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, first_capture_request
        )

        self.assertIsNotNone(first_response)
        self.assertIsNotNone(first_response.id)

        second_capture_request = CapturePaymentRequestBuilder() \
            .with_amount(500) \
            .with_is_final(True) \
            .build()

        second_response = self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, second_capture_request
        )

        self.assertIsNotNone(second_response)
        self.assertIsNotNone(second_response.id)

    def test_capture_payment_second_amount_exceeds_remaining_raises_validation_exception(self):
        payment_id = create_payment_and_get_id(self.client, amount=800)

        first_capture_request = CapturePaymentRequestBuilder() \
            .with_amount(300) \
            .with_is_final(False) \
            .build()

        self.client.merchant(MERCHANT_ID).payments().capture_payment(payment_id, first_capture_request)

        second_capture_request = CapturePaymentRequestBuilder() \
            .with_amount(600) \
            .with_is_final(False) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payments().capture_payment(payment_id, second_capture_request)

    def test_capture_payment_after_partial_cancel_returns_captured_payment(self):
        payment_id = create_payment_and_get_id(self.client, amount=800)

        cancel_request = CancelPaymentRequestBuilder() \
            .with_amount(600) \
            .with_currency(CURRENCY_CODE) \
            .with_is_final(False) \
            .build()

        self.client.merchant(MERCHANT_ID).payments().cancel_payment(payment_id, cancel_request)

        capture_request = CapturePaymentRequestBuilder() \
            .with_amount(200) \
            .with_is_final(True) \
            .build()

        response = self.client.merchant(MERCHANT_ID).payments().capture_payment(payment_id, capture_request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertIsNotNone(response.status)

    def test_capture_payment_invalid_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).payments().capture_payment(
                NON_EXISTING_PAYMENT_ID, CapturePaymentRequestBuilder().build()
            )

    def test_capture_payment_after_previous_capture_raises_validation_exception(self):
        payment_id = create_payment_and_get_id(self.client)

        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payments().capture_payment(
                payment_id, CapturePaymentRequestBuilder().build()
            )

    def test_capture_payment_after_cancel_raises_validation_exception(self):
        payment_id = create_payment_and_get_id(self.client)

        self.client.merchant(MERCHANT_ID).payments().cancel_payment(
            payment_id, CancelPaymentRequestBuilder().build()
        )

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payments().capture_payment(
                payment_id, CapturePaymentRequestBuilder().build()
            )

    def test_capture_payment_after_refund_raises_validation_exception(self):
        payment_id = create_payment_and_get_id(self.client)

        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )
        self.client.merchant(MERCHANT_ID).payments().refund_payment(
            payment_id, RefundRequestBuilder().build()
        )

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payments().capture_payment(
                payment_id, CapturePaymentRequestBuilder().build()
            )

    """Test refund payment"""

    def test_refund_payment_valid_request_returns_refunded_payment(self):
        payment_id = create_payment_and_get_id(self.client)

        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        response = self.client.merchant(MERCHANT_ID).payments().refund_payment(
            payment_id, RefundRequestBuilder().build()
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertIsNotNone(response.status)

    def test_refund_payment_partial_amounts_returns_refunded_payment(self):
        payment_id = create_payment_and_get_id(self.client, amount=1500)

        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        first_refund_request = RefundRequestBuilder() \
            .with_amount(300) \
            .with_currency(CURRENCY_CODE) \
            .with_is_final(False) \
            .build()

        self.client.merchant(MERCHANT_ID).payments().refund_payment(payment_id, first_refund_request)

        second_refund_request = RefundRequestBuilder() \
            .with_amount(400) \
            .with_currency(CURRENCY_CODE) \
            .with_is_final(False) \
            .build()

        response = self.client.merchant(MERCHANT_ID).payments().refund_payment(payment_id, second_refund_request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertNotEqual("REJECTED", response.status)

    def test_refund_payment_total_exceeds_captured_raises_validation_exception(self):
        payment_id = create_payment_and_get_id(self.client, amount=800)

        capture_request = CapturePaymentRequestBuilder() \
            .with_amount(400) \
            .with_is_final(True) \
            .build()

        self.client.merchant(MERCHANT_ID).payments().capture_payment(payment_id, capture_request)

        refund_request = RefundRequestBuilder() \
            .with_amount(600) \
            .with_currency(CURRENCY_CODE) \
            .build()

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).payments().refund_payment(payment_id, refund_request)

        self.assertEqual("ACTION_NOT_ALLOWED_ON_TRANSACTION", raised.exception.errors[0].message)

    def test_refund_payment_single_refund_exceeds_captured_raises_validation_exception(self):
        payment_id = create_payment_and_get_id(self.client, amount=800)

        capture_request = CapturePaymentRequestBuilder() \
            .with_amount(300) \
            .with_is_final(True) \
            .build()

        self.client.merchant(MERCHANT_ID).payments().capture_payment(payment_id, capture_request)

        refund_request = RefundRequestBuilder() \
            .with_amount(600) \
            .with_currency(CURRENCY_CODE) \
            .build()

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).payments().refund_payment(payment_id, refund_request)

        self.assertEqual("ACTION_NOT_ALLOWED_ON_TRANSACTION", raised.exception.errors[0].message)

    def test_refund_payment_invalid_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).payments().refund_payment(
                NON_EXISTING_PAYMENT_ID, RefundRequestBuilder().build()
            )

    def test_refund_payment_without_capture_raises_validation_exception(self):
        payment_id = create_payment_and_get_id(self.client)

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payments().refund_payment(
                payment_id, RefundRequestBuilder().build()
            )

    def test_refund_payment_after_cancel_raises_validation_exception(self):
        payment_id = create_payment_and_get_id(self.client)

        self.client.merchant(MERCHANT_ID).payments().cancel_payment(
            payment_id, CancelPaymentRequestBuilder().build()
        )

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payments().refund_payment(
                payment_id, RefundRequestBuilder().build()
            )

    def test_refund_payment_already_refunded_raises_validation_exception(self):
        payment_id = create_payment_and_get_id(self.client)

        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )
        self.client.merchant(MERCHANT_ID).payments().refund_payment(
            payment_id, RefundRequestBuilder().build()
        )

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).payments().refund_payment(
                payment_id, RefundRequestBuilder().build()
            )

        self.assertEqual("ACTION_NOT_ALLOWED_ON_TRANSACTION", raised.exception.errors[0].message)


if __name__ == '__main__':
    unittest.main()
