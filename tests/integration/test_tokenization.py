import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.tokenization.csr_request_builder import CsrRequestBuilder
from tests.integration.builders.tokenization.get_card_data_by_tokens_params_builder import GetCardDataByTokensParamsBuilder
from tests.integration.builders.tokenization.get_card_data_by_payments_params_builder import GetCardDataByPaymentsParamsBuilder
from tests.integration.builders.common.create_payment_request_builder import CreatePaymentRequestBuilder
from tests.integration.sdk_test_helper import create_token_and_get_id
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.reference_exception import ReferenceException
from onlinepayments.sdk.validation_exception import ValidationException


class TokenizationIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test create certificate"""

    @unittest.skip("Test is skipped because the Tokenization endpoint features are not enabled for the test merchant.")
    def test_create_certificate_returns_certificate_response(self):
        request = CsrRequestBuilder().build()

        response = self.client.merchant(MERCHANT_ID).tokenization().create_certificate(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.signed_certificate)
        self.assertIsNotNone(response.certificate_id)

    @unittest.skip("Test is skipped because the Tokenization endpoint features are not enabled for the test merchant.")
    def test_create_certificate_with_call_context_returns_certificate_response(self):
        request = CsrRequestBuilder().build()
        context = CallContext(idempotence_key="test-tokenization-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).tokenization().create_certificate(request, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.signed_certificate)
        self.assertIsNotNone(response.certificate_id)

    def test_create_certificate_invalid_csr_raises_validation_exception(self):
        request = CsrRequestBuilder() \
            .with_csr(None) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).tokenization().create_certificate(request)

    """Test get card data by tokens"""

    @unittest.skip("Test is skipped because the Tokenization endpoint features are not enabled for the test merchant.")
    def test_get_card_data_by_tokens_valid_token_returns_detokenized_data(self):
        token_id = create_token_and_get_id(self.client)

        params = GetCardDataByTokensParamsBuilder() \
            .with_tokens([token_id]) \
            .build()

        response = self.client.merchant(MERCHANT_ID).tokenization().get_card_data_by_tokens(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.tokens)

    @unittest.skip("Test is skipped because the Tokenization endpoint features are not enabled for the test merchant.")
    def test_get_card_data_by_tokens_non_existent_token_raises_reference_exception(self):
        params = GetCardDataByTokensParamsBuilder() \
            .with_tokens(["non-existent-token-xyz"]) \
            .build()

        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).tokenization().get_card_data_by_tokens(params)

    def test_get_card_data_by_tokens_invalid_tokens_raises_validation_exception(self):
        params = GetCardDataByTokensParamsBuilder() \
            .with_tokens(None) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).tokenization().get_card_data_by_tokens(params)

    """Test get card data by payments"""

    @unittest.skip("Test is skipped because the Tokenization endpoint features are not enabled for the test merchant.")
    def test_get_card_data_by_payments_valid_payment_id_returns_detokenized_data(self):
        token_id = create_token_and_get_id(self.client)

        payment_request = CreatePaymentRequestBuilder().with_token(token_id).build()
        payment_response = self.client.merchant(MERCHANT_ID).payments().create_payment(payment_request)

        params = GetCardDataByPaymentsParamsBuilder() \
            .with_payments([payment_response.payment.id]) \
            .build()

        response = self.client.merchant(MERCHANT_ID).tokenization().get_card_data_by_payments(params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.tokens)

    @unittest.skip("Test is skipped because the Tokenization endpoint features are not enabled for the test merchant.")
    def test_get_card_data_by_payments_non_existent_payment_id_raises_reference_exception(self):
        params = GetCardDataByPaymentsParamsBuilder() \
            .with_payments(["non-existent-payment"]) \
            .build()

        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).tokenization().get_card_data_by_payments(params)

    def test_get_card_data_by_payments_invalid_payment_ids_raises_validation_exception(self):
        params = GetCardDataByPaymentsParamsBuilder() \
            .with_payments(None) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).tokenization().get_card_data_by_payments(params)


if __name__ == "__main__":
    unittest.main()
