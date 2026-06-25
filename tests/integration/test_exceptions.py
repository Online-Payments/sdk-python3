import threading
import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.common.create_payment_request_builder import CreatePaymentRequestBuilder
from tests.integration.builders.payments.capture_payment_request_builder import CapturePaymentRequestBuilder
from tests.integration.builders.payments.refund_request_builder import RefundRequestBuilder
from tests.integration.builders.payouts.create_payout_request_builder import CreatePayoutRequestBuilder
from tests.integration.sdk_test_helper import create_payment_and_get_id
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.api_exception import ApiException
from onlinepayments.sdk.platform_exception import PlatformException
from onlinepayments.sdk.authorization_exception import AuthorizationException
from onlinepayments.sdk.declined_payment_exception import DeclinedPaymentException
from onlinepayments.sdk.declined_payout_exception import DeclinedPayoutException
from onlinepayments.sdk.declined_refund_exception import DeclinedRefundException
from onlinepayments.sdk.declined_transaction_exception import DeclinedTransactionException
from onlinepayments.sdk.reference_exception import ReferenceException
from onlinepayments.sdk.validation_exception import ValidationException

NON_EXISTING_PAYMENT_ID = "9999999999_0"
INVALID_MERCHANT_ID = "000000"
DECLINED_CARD_NUMBER = "4321456998744563"
OVERSHOOT_PAYOUT_AMOUNT = 999999999
DECLINED_REFUND_AMOUNT = 1500


class ExceptionsTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test exception errors"""

    def test_create_payment_invalid_card_number_raises_validation_exception(self):
        request = CreatePaymentRequestBuilder() \
            .with_card_number("123") \
            .build()

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).payments().create_payment(request)

        exception = raised.exception
        self.assertIsNotNone(exception)
        self.assertIsNotNone(exception.error_id)
        self.assertNotEqual("", exception.error_id)
        self.assertIsNotNone(exception.errors)
        self.assertEqual(1, len(exception.errors))

        error = exception.errors[0]
        self.assertIsNotNone(error)
        self.assertIsNotNone(error.id)
        self.assertIsNotNone(error.http_status_code)

    """Test validation exception"""

    def test_create_payout_invalid_currency_raises_validation_exception(self):
        request = CreatePayoutRequestBuilder() \
            .with_amount(1000) \
            .with_currency("INVALID") \
            .build()

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).payouts().create_payout(request)

        exception = raised.exception
        self.assertIsNotNone(exception)
        self.assertEqual(400, exception.status_code)
        self.assertIsNotNone(exception.error_id)
        self.assertIsNotNone(exception.errors)
        self.assertGreater(len(exception.errors), 0)

        error = exception.errors[0]
        self.assertEqual("INVALID_VALUE", error.id)
        self.assertEqual(400, error.http_status_code)

    def test_create_payment_multiple_invalid_fields_raises_validation_exception(self):
        request = CreatePaymentRequestBuilder() \
            .with_card_number("123") \
            .with_cvv("") \
            .with_expiry_date("invalid") \
            .build()

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).payments().create_payment(request)

        exception = raised.exception
        self.assertIsNotNone(exception)
        self.assertEqual(400, exception.status_code)
        self.assertIsNotNone(exception.errors)
        self.assertGreater(len(exception.errors), 0)

        for error in exception.errors:
            self.assertIsNotNone(error.id)
            self.assertIsNotNone(error.http_status_code)
            self.assertEqual(400, error.http_status_code)

    """Test authorization exception"""

    def test_create_payment_invalid_merchant_id_raises_authorization_exception(self):
        request = CreatePaymentRequestBuilder().build()

        with self.assertRaises(AuthorizationException) as raised:
            self.client.merchant(INVALID_MERCHANT_ID).payments().create_payment(request)

        exception = raised.exception
        self.assertIsNotNone(exception)
        self.assertEqual(403, exception.status_code)
        self.assertIsNotNone(exception.response_body)
        self.assertIsNotNone(exception.error_id)
        self.assertNotEqual("", exception.error_id)
        self.assertIsNotNone(exception.errors)
        self.assertGreater(len(exception.errors), 0)

        error = exception.errors[0]
        self.assertIsNotNone(error.id)
        self.assertEqual(403, error.http_status_code)

    """Test declined payment exception"""

    def test_create_payment_declined_card_raises_declined_payment_exception(self):
        request = CreatePaymentRequestBuilder() \
            .with_card_number(DECLINED_CARD_NUMBER) \
            .build()

        with self.assertRaises(DeclinedPaymentException) as raised:
            self.client.merchant(MERCHANT_ID).payments().create_payment(request)

        exception = raised.exception
        self.assertIsNotNone(exception)
        self.assertGreaterEqual(exception.status_code, 400)
        self.assertIsNotNone(exception.response_body)

        payment_response = exception.create_payment_response
        assert payment_response is not None
        payment = payment_response.payment
        assert payment is not None
        self.assertIsNotNone(payment.id)
        self.assertIsNotNone(payment.status)
        self.assertEqual("REJECTED", payment.status)

    """Test declined payout exception"""

    def test_create_payout_declined_card_raises_declined_payout_exception(self):
        request = CreatePayoutRequestBuilder() \
            .with_card_number(DECLINED_CARD_NUMBER) \
            .build()

        with self.assertRaises(DeclinedPayoutException) as raised:
            self.client.merchant(MERCHANT_ID).payouts().create_payout(request)

        exception = raised.exception
        self.assertIsNotNone(exception)
        self.assertGreaterEqual(exception.status_code, 400)
        self.assertIsNotNone(exception.response_body)

        payout_result = exception.payout_result
        assert payout_result is not None
        self.assertIsNotNone(payout_result.id)
        self.assertIsNotNone(payout_result.status)
        self.assertEqual("REJECTED_CREDIT", payout_result.status)

    """Test api exception"""

    def test_create_payment_invalid_card_number_raises_api_exception(self):
        request = CreatePaymentRequestBuilder() \
            .with_card_number("123") \
            .build()

        with self.assertRaises(ApiException) as raised:
            self.client.merchant(MERCHANT_ID).payments().create_payment(request)

        exception = raised.exception
        self.assertIsNotNone(exception)
        self.assertGreaterEqual(exception.status_code, 400)
        self.assertIsNotNone(exception.response_body)
        self.assertIsNotNone(exception.error_id)
        self.assertIsNotNone(exception.errors)

    """Test declined transaction exception"""

    def test_create_payment_declined_card_raises_declined_transaction_exception(self):
        request = CreatePaymentRequestBuilder() \
            .with_card_number(DECLINED_CARD_NUMBER) \
            .build()

        with self.assertRaises(DeclinedTransactionException) as raised:
            self.client.merchant(MERCHANT_ID).payments().create_payment(request)

        exception = raised.exception
        self.assertIsNotNone(exception)
        self.assertIsInstance(exception, DeclinedPaymentException)
        self.assertIsNotNone(exception.response_body)

    """Test idempotence exception"""

    def test_create_payment_concurrent_duplicate_requests_raises_reference_exception(self):
        idempotence_key = str(uuid.uuid4())
        request = CreatePaymentRequestBuilder().build()

        errors: list[Exception | None] = [None, None]

        def send_request(index):
            try:
                context = CallContext(idempotence_key=idempotence_key)
                self.client.merchant(MERCHANT_ID).payments().create_payment(request, context)
            except Exception as e:
                errors[index] = e

        barrier = threading.Event()

        def run(index):
            barrier.wait()
            send_request(index)

        threads = [threading.Thread(target=run, args=(i,)) for i in range(2)]
        for t in threads:
            t.start()
        barrier.set()
        for t in threads:
            t.join()

        first_error, second_error = errors[0], errors[1]

        if first_error is None:
            self.assertIsNotNone(second_error)
            self.assertIsInstance(second_error, ReferenceException)
            self.assertIsNotNone(second_error.errors)
            self.assertIsNotNone(second_error.errors[0])
            self.assertEqual(409, second_error.errors[0].http_status_code)
            self.assertEqual("DUPLICATE_REQUEST_IN_PROGRESS", second_error.errors[0].id)

        if second_error is None:
            self.assertIsNotNone(first_error)
            self.assertIsInstance(first_error, ReferenceException)
            self.assertIsNotNone(first_error.errors)
            self.assertIsNotNone(first_error.errors[0])
            self.assertEqual(409, first_error.errors[0].http_status_code)
            self.assertEqual("DUPLICATE_REQUEST_IN_PROGRESS", first_error.errors[0].id)

    """Test declined refund exception"""

    @unittest.skip("Test is skipped because the action could not be triggered in the current merchant setup.")
    def test_refund_payment_declined_raises_declined_refund_exception(self):
        payment_id = create_payment_and_get_id(self.client, amount=DECLINED_REFUND_AMOUNT, currency="EUR")
        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        with self.assertRaises(DeclinedRefundException) as raised:
            self.client.merchant(MERCHANT_ID).payments().refund_payment(
                payment_id,
                RefundRequestBuilder().with_amount(DECLINED_REFUND_AMOUNT).with_currency("EUR").build()
            )

        exception = raised.exception
        self.assertIsNotNone(exception)
        self.assertGreaterEqual(exception.status_code, 400)
        self.assertIsNotNone(exception.response_body)

        refund_response = exception.refund_response
        self.assertIsNotNone(refund_response)
        self.assertIsNotNone(refund_response.id)
        self.assertIsNotNone(refund_response.status)

    """Test error id in all exceptions"""

    def test_validation_exception_has_error_id(self):
        request = CreatePaymentRequestBuilder() \
            .with_card_number("123") \
            .build()

        with self.assertRaises(ValidationException) as raised:
            self.client.merchant(MERCHANT_ID).payments().create_payment(request)

        exception = raised.exception
        self.assertIsNotNone(exception.error_id)
        self.assertNotEqual("", exception.error_id)

    def test_reference_exception_has_error_id(self):
        with self.assertRaises(ReferenceException) as raised:
            self.client.merchant(MERCHANT_ID).payments().get_payment(NON_EXISTING_PAYMENT_ID)

        exception = raised.exception
        self.assertIsNotNone(exception.error_id)
        self.assertNotEqual("", exception.error_id)

    def test_authorization_exception_has_error_id(self):
        request = CreatePaymentRequestBuilder().build()

        with self.assertRaises(AuthorizationException) as raised:
            self.client.merchant(INVALID_MERCHANT_ID).payments().create_payment(request)

        exception = raised.exception
        self.assertIsNotNone(exception.error_id)
        self.assertNotEqual("", exception.error_id)


if __name__ == "__main__":
    unittest.main()
