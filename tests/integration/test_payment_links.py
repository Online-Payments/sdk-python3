import unittest
import uuid
from datetime import datetime, timezone, timedelta

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.paymentlinks.create_payment_link_request_builder import CreatePaymentLinkRequestBuilder
from tests.integration.sdk_test_helper import create_payment_link_and_get_id
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.reference_exception import ReferenceException
from onlinepayments.sdk.validation_exception import ValidationException

UNKNOWN_PAYMENT_LINK_ID = "00000000-0000-0000-0000-000000000000"
INVALID_PAYMENT_LINK_ID = "invalid-id"


class PaymentLinksIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test create payment link - valid input"""

    def test_create_payment_link_returns_payment_link(self):
        request = CreatePaymentLinkRequestBuilder().build()

        response = self.client.merchant(MERCHANT_ID).payment_links().create_payment_link(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_link_id)
        self.assertIsNotNone(response.status)
        self.assertIsNotNone(response.redirection_url)

    def test_create_payment_link_with_call_context_returns_payment_link(self):
        request = CreatePaymentLinkRequestBuilder().build()
        context = CallContext(idempotence_key="test-payment-links-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).payment_links().create_payment_link(request, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_link_id)
        self.assertIsNotNone(response.status)
        self.assertIsNotNone(response.redirection_url)

    def test_create_payment_link_with_qr_code_returns_qr_code_base64(self):
        request = CreatePaymentLinkRequestBuilder() \
            .with_display_qr_code(True) \
            .build()

        response = self.client.merchant(MERCHANT_ID).payment_links().create_payment_link(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_link_id)
        self.assertIsNotNone(response.qr_code_base64)

    def test_create_payment_link_with_reusable_link_returns_reusable_flag(self):
        request = CreatePaymentLinkRequestBuilder() \
            .with_reusable_link(True) \
            .build()

        response = self.client.merchant(MERCHANT_ID).payment_links().create_payment_link(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_link_id)
        self.assertEqual(True, response.is_reusable_link)

    """Test create payment link - invalid input"""

    def test_create_payment_link_invalid_amount_raises_validation_exception(self):
        request = CreatePaymentLinkRequestBuilder() \
            .with_amount(-1000) \
            .with_currency("EUR") \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payment_links().create_payment_link(request)

    def test_create_payment_link_expired_expiration_date_raises_validation_exception(self):
        past_date = datetime.now(timezone.utc) - timedelta(days=1)
        request = CreatePaymentLinkRequestBuilder() \
            .with_expiration_date(past_date) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payment_links().create_payment_link(request)

    """Test get payment link"""

    def test_get_payment_link_valid_id_returns_payment_link(self):
        payment_link_id = create_payment_link_and_get_id(self.client)

        response = self.client.merchant(MERCHANT_ID).payment_links().get_payment_link_by_id(payment_link_id)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment_link_id)
        self.assertEqual(payment_link_id, response.payment_link_id)
        self.assertIsNotNone(response.status)

    def test_get_payment_link_unknown_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).payment_links().get_payment_link_by_id(UNKNOWN_PAYMENT_LINK_ID)

    def test_get_payment_link_invalid_id_format_raises_validation_exception(self):
        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payment_links().get_payment_link_by_id(INVALID_PAYMENT_LINK_ID)

    """Test cancel payment link"""

    def test_cancel_payment_link_valid_id_cancels_link(self):
        payment_link_id = create_payment_link_and_get_id(self.client)

        self.client.merchant(MERCHANT_ID).payment_links().cancel_payment_link_by_id(payment_link_id)

        response = self.client.merchant(MERCHANT_ID).payment_links().get_payment_link_by_id(payment_link_id)

        self.assertIsNotNone(response)
        self.assertEqual(payment_link_id, response.payment_link_id)
        self.assertIsNotNone(response.payment_link_events)
        self.assertEqual("CANCELLED", response.payment_link_events[1].type)

    def test_cancel_payment_link_unknown_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).payment_links().cancel_payment_link_by_id(UNKNOWN_PAYMENT_LINK_ID)

    def test_cancel_payment_link_invalid_id_format_raises_validation_exception(self):
        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).payment_links().cancel_payment_link_by_id(INVALID_PAYMENT_LINK_ID)

    def test_cancel_payment_link_already_cancelled_raises_reference_exception(self):
        payment_link_id = create_payment_link_and_get_id(self.client)

        self.client.merchant(MERCHANT_ID).payment_links().cancel_payment_link_by_id(payment_link_id)

        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).payment_links().cancel_payment_link_by_id(payment_link_id)


if __name__ == "__main__":
    unittest.main()