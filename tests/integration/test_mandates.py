import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.mandates.create_mandate_request_builder import CreateMandateRequestBuilder
from tests.integration.builders.mandates.revoke_mandate_request_builder import RevokeMandateRequestBuilder
from tests.integration.sdk_test_helper import create_mandate_and_get_reference
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.validation_exception import ValidationException
from onlinepayments.sdk.reference_exception import ReferenceException

INVALID_IBAN = "INVALID"
INVALID_MANDATE_REFERENCE = "INVALID123456"


class MandatesIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test create mandate"""

    def test_create_mandate_valid_request_returns_unique_mandate_reference(self):
        request = CreateMandateRequestBuilder() \
            .with_unique_mandate_reference(uuid.uuid4().hex[:35]) \
            .build()

        response = self.client.merchant(MERCHANT_ID).mandates().create_mandate(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.mandate)
        self.assertIsNotNone(response.mandate.unique_mandate_reference)

    def test_create_mandate_with_call_context_returns_unique_mandate_reference(self):
        request = CreateMandateRequestBuilder() \
            .with_unique_mandate_reference(uuid.uuid4().hex[:35]) \
            .build()

        context = CallContext(idempotence_key="test-mandates-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).mandates().create_mandate(request, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.mandate)
        self.assertIsNotNone(response.mandate.unique_mandate_reference)

    def test_create_mandate_invalid_iban_raises_validation_exception(self):
        request = CreateMandateRequestBuilder() \
            .with_customer_iban(INVALID_IBAN) \
            .with_unique_mandate_reference(uuid.uuid4().hex[:35]) \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).mandates().create_mandate(request)

    """Test get mandate"""

    def test_get_mandate_valid_reference_returns_mandate(self):
        mandate_reference = create_mandate_and_get_reference(self.client)

        response = self.client.merchant(MERCHANT_ID).mandates().get_mandate(mandate_reference)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.mandate)
        self.assertIsNotNone(response.mandate.unique_mandate_reference)

    def test_get_mandate_invalid_reference_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).mandates().get_mandate(INVALID_MANDATE_REFERENCE)

    """Test block mandate"""

    def test_block_mandate_valid_reference_returns_mandate(self):
        mandate_reference = create_mandate_and_get_reference(self.client)

        response = self.client.merchant(MERCHANT_ID).mandates().block_mandate(mandate_reference)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.mandate)
        self.assertIsNotNone(response.mandate.unique_mandate_reference)

    def test_block_mandate_already_blocked_raises_validation_exception(self):
        mandate_reference = create_mandate_and_get_reference(self.client)
        self.client.merchant(MERCHANT_ID).mandates().block_mandate(mandate_reference)

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).mandates().block_mandate(mandate_reference)

    def test_block_mandate_already_revoked_raises_validation_exception(self):
        mandate_reference = create_mandate_and_get_reference(self.client)
        self.client.merchant(MERCHANT_ID).mandates().revoke_mandate(
            mandate_reference, RevokeMandateRequestBuilder().build()
        )

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).mandates().block_mandate(mandate_reference)

    def test_block_mandate_invalid_reference_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).mandates().block_mandate(INVALID_MANDATE_REFERENCE)

    """Test unblock mandate"""

    def test_unblock_mandate_blocked_returns_mandate(self):
        mandate_reference = create_mandate_and_get_reference(self.client)
        self.client.merchant(MERCHANT_ID).mandates().block_mandate(mandate_reference)

        response = self.client.merchant(MERCHANT_ID).mandates().unblock_mandate(mandate_reference)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.mandate)
        self.assertIsNotNone(response.mandate.unique_mandate_reference)

    def test_unblock_mandate_not_blocked_raises_validation_exception(self):
        mandate_reference = create_mandate_and_get_reference(self.client)

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).mandates().unblock_mandate(mandate_reference)

    def test_unblock_mandate_revoked_raises_validation_exception(self):
        mandate_reference = create_mandate_and_get_reference(self.client)
        self.client.merchant(MERCHANT_ID).mandates().revoke_mandate(
            mandate_reference, RevokeMandateRequestBuilder().build()
        )

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).mandates().unblock_mandate(mandate_reference)

    def test_unblock_mandate_invalid_reference_raises_reference_exception(self):
        with self.assertRaises(ReferenceException):
            self.client.merchant(MERCHANT_ID).mandates().unblock_mandate(INVALID_MANDATE_REFERENCE)

    """Test revoke mandate"""

    def test_revoke_mandate_valid_request_returns_mandate(self):
        mandate_reference = create_mandate_and_get_reference(self.client)
        request = RevokeMandateRequestBuilder().build()

        response = self.client.merchant(MERCHANT_ID).mandates().revoke_mandate(mandate_reference, request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.mandate)
        self.assertIsNotNone(response.mandate.unique_mandate_reference)

    def test_revoke_mandate_blocked_returns_mandate(self):
        mandate_reference = create_mandate_and_get_reference(self.client)
        self.client.merchant(MERCHANT_ID).mandates().block_mandate(mandate_reference)
        request = RevokeMandateRequestBuilder().build()

        response = self.client.merchant(MERCHANT_ID).mandates().revoke_mandate(mandate_reference, request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.mandate)
        self.assertIsNotNone(response.mandate.unique_mandate_reference)

    def test_revoke_mandate_previously_unblocked_returns_mandate(self):
        mandate_reference = create_mandate_and_get_reference(self.client)
        self.client.merchant(MERCHANT_ID).mandates().block_mandate(mandate_reference)
        self.client.merchant(MERCHANT_ID).mandates().unblock_mandate(mandate_reference)
        request = RevokeMandateRequestBuilder().build()

        response = self.client.merchant(MERCHANT_ID).mandates().revoke_mandate(mandate_reference, request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.mandate)
        self.assertIsNotNone(response.mandate.unique_mandate_reference)

    def test_revoke_mandate_already_revoked_raises_validation_exception(self):
        mandate_reference = create_mandate_and_get_reference(self.client)
        revoke_request = RevokeMandateRequestBuilder().build()
        self.client.merchant(MERCHANT_ID).mandates().revoke_mandate(mandate_reference, revoke_request)

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).mandates().revoke_mandate(mandate_reference, revoke_request)

    def test_revoke_mandate_invalid_reference_raises_validation_exception(self):
        request = RevokeMandateRequestBuilder().build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).mandates().revoke_mandate(INVALID_MANDATE_REFERENCE, request)


if __name__ == '__main__':
    unittest.main()