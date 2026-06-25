import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.subsequent.subsequent_payment_request_builder import SubsequentPaymentRequestBuilder
from tests.integration.sdk_test_helper import create_payment_and_get_id
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.validation_exception import ValidationException
from onlinepayments.sdk.reference_exception import ReferenceException

NON_EXISTING_PAYMENT_ID = "9999999999"


class SubsequentsIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test subsequent payment"""

    def test_subsequent_payment_valid_request_returns_payment_id(self):
        payment_id = create_payment_and_get_id(self.client)
        request = SubsequentPaymentRequestBuilder().build()

        response = self.client.merchant(MERCHANT_ID).subsequent().subsequent_payment(payment_id, request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment)
        self.assertIsNotNone(response.payment.id)
        self.assertIsNotNone(response.payment.status)

    def test_subsequent_payment_with_call_context_returns_payment_id(self):
        payment_id = create_payment_and_get_id(self.client)
        request = SubsequentPaymentRequestBuilder().build()
        context = CallContext(idempotence_key="test-subsequent-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).subsequent().subsequent_payment(payment_id, request, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment)
        self.assertIsNotNone(response.payment.id)
        self.assertIsNotNone(response.payment.status)

    def test_subsequent_payment_invalid_amount_raises_validation_exception(self):
        payment_id = create_payment_and_get_id(self.client)
        request = SubsequentPaymentRequestBuilder() \
            .with_amount(-1000) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).subsequent().subsequent_payment(payment_id, request)

    def test_subsequent_payment_invalid_payment_id_raises_reference_exception(self):
        request = SubsequentPaymentRequestBuilder().build()

        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).subsequent().subsequent_payment(NON_EXISTING_PAYMENT_ID, request)


if __name__ == "__main__":
    unittest.main()
