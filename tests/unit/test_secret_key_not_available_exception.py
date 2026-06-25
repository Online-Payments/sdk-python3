import unittest

from onlinepayments.sdk.webhooks.secret_key_not_available_exception import SecretKeyNotAvailableException
from onlinepayments.sdk.webhooks.signature_validation_exception import SignatureValidationException


class SecretKeyNotAvailableExceptionTest(unittest.TestCase):

    def test_ConstructingWithMessageAndKeyId_DefaultScenario_CreateInstanceWithMessageAndKeyId(self):
        exception = SecretKeyNotAvailableException("api-key-123", message="Secret key not found")
        self.assertIsNotNone(exception)
        self.assertEqual("api-key-123", exception.key_id)

    def test_ConstructingWithMessageAndKeyId_DefaultScenario_StoreMessageFromConstructor(self):
        exception = SecretKeyNotAvailableException("api-key-123",
                                                   message="Secret key not found for key: api-key-123")
        self.assertEqual("Secret key not found for key: api-key-123", str(exception))

    def test_ConstructingWithMessageAndKeyId_DefaultScenario_StoreKeyIdFromConstructor(self):
        exception = SecretKeyNotAvailableException("api-key-123", message="Secret key not found")
        self.assertEqual("api-key-123", exception.key_id)

    def test_ConstructingWithMessageAndKeyId_DefaultScenario_BeRuntimeException(self):
        exception = SecretKeyNotAvailableException("api-key-123", message="Secret key not found")
        self.assertIsInstance(exception, RuntimeError)

    def test_ConstructingWithKeyIdAndCause_DefaultScenario_CreateInstanceWithKeyIdAndCause(self):
        cause = Exception("Database connection failed")
        exception = SecretKeyNotAvailableException("api-key-456", cause=cause)
        self.assertIsNotNone(exception)
        self.assertEqual("api-key-456", exception.key_id)

    def test_ConstructingWithKeyIdAndCause_DefaultScenario_StoreCauseFromConstructor(self):
        cause = Exception("Database connection failed")
        exception = SecretKeyNotAvailableException("api-key-456", cause=cause)
        self.assertIs(cause, exception.args[0])

    def test_ConstructingWithKeyIdAndCause_DefaultScenario_StoreKeyIdFromConstructor(self):
        cause = Exception("Database error")
        exception = SecretKeyNotAvailableException("api-key-456", cause=cause)
        self.assertEqual("api-key-456", exception.key_id)

    def test_ConstructingWithKeyIdAndCause_DefaultScenario_HaveCauseMessage(self):
        cause = Exception("Database error occurred")
        exception = SecretKeyNotAvailableException("api-key-456", cause=cause)
        self.assertEqual("Database error occurred", exception.args[0].args[0])

    def test_ConstructingWithMessageKeyIdAndCause_DefaultScenario_CreateInstanceWithAllParameters(self):
        cause = RuntimeError("Connection timeout")
        exception = SecretKeyNotAvailableException("api-key-789", message="Could not retrieve secret key",
                                                   cause=cause)
        self.assertIsNotNone(exception)
        self.assertEqual("api-key-789", exception.key_id)

    def test_ConstructingWithMessageKeyIdAndCause_DefaultScenario_StoreMessageFromConstructor(self):
        cause = RuntimeError("Connection timeout")
        exception = SecretKeyNotAvailableException(
            "api-key-789", message="Could not retrieve secret key for api-key-789", cause=cause)
        self.assertIn("Could not retrieve secret key for api-key-789", str(exception))

    def test_ConstructingWithMessageKeyIdAndCause_DefaultScenario_StoreKeyIdFromConstructor(self):
        cause = RuntimeError("Connection timeout")
        exception = SecretKeyNotAvailableException("api-key-789", message="Could not retrieve secret key",
                                                   cause=cause)
        self.assertEqual("api-key-789", exception.key_id)

    def test_ConstructingWithMessageKeyIdAndCause_DefaultScenario_StoreCauseFromConstructor(self):
        cause = RuntimeError("Connection timeout")
        exception = SecretKeyNotAvailableException("api-key-789", message="Could not retrieve secret key",
                                                   cause=cause)
        self.assertIs(cause, exception.args[1])

    def test_ConstructingWithMessageKeyIdAndCause_DefaultScenario_HaveCompleteExceptionChain(self):
        cause = Exception("Root error")
        exception = SecretKeyNotAvailableException("test-key", message="Secret key unavailable", cause=cause)
        self.assertEqual("test-key", exception.key_id)
        self.assertIn("Secret key unavailable", str(exception))
        self.assertEqual("Root error", exception.args[1].args[0])

    def test_GettingKeyId_DefaultScenario_ReturnCorrectKeyId(self):
        exception = SecretKeyNotAvailableException("production-key-001", message="Error")
        self.assertEqual("production-key-001", exception.key_id)

    def test_GettingKeyId_DefaultScenario_ReturnSameKeyIdStoredInConstructor(self):
        key_id = "webhook-secret-xyz"
        exception = SecretKeyNotAvailableException(key_id, message="Message")
        self.assertEqual(key_id, exception.key_id)

    def test_GettingKeyId_DefaultScenario_ReturnDifferentKeyIdForDifferentInstances(self):
        exception1 = SecretKeyNotAvailableException("key-1", message="Error")
        exception2 = SecretKeyNotAvailableException("key-2", message="Error")
        self.assertEqual("key-1", exception1.key_id)
        self.assertEqual("key-2", exception2.key_id)

    def test_GettingKeyId_DefaultScenario_ReturnNullWhenKeyIdIsNull(self):
        exception = SecretKeyNotAvailableException(None, message="Error")
        self.assertIsNone(exception.key_id)

    def test_ThrowingException_DefaultScenario_BeThrowableAsRuntimeException(self):
        with self.assertRaises(SecretKeyNotAvailableException) as ctx:
            raise SecretKeyNotAvailableException("test-key", message="Key not found")
        self.assertEqual("test-key", ctx.exception.key_id)

    def test_ThrowingException_DefaultScenario_BeCatchableAsSignatureValidationException(self):
        with self.assertRaises(SignatureValidationException):
            raise SecretKeyNotAvailableException("test-key", message="Key not found")

    def test_ThrowingException_DefaultScenario_BeCatchableAsRuntimeException(self):
        with self.assertRaises(RuntimeError):
            raise SecretKeyNotAvailableException("test-key", message="Key not found")

    def test_UsingDifferentKeyIdFormats_DefaultScenario_HandleSimpleKeyIds(self):
        exception = SecretKeyNotAvailableException("key1", message="Error")
        self.assertEqual("key1", exception.key_id)

    def test_UsingDifferentKeyIdFormats_DefaultScenario_HandleKeyIdsWithHyphens(self):
        exception = SecretKeyNotAvailableException("api-key-prod-001", message="Error")
        self.assertEqual("api-key-prod-001", exception.key_id)

    def test_UsingDifferentKeyIdFormats_DefaultScenario_HandleKeyIdsWithUnderscores(self):
        exception = SecretKeyNotAvailableException("api_key_prod_001", message="Error")
        self.assertEqual("api_key_prod_001", exception.key_id)

    def test_UsingDifferentKeyIdFormats_DefaultScenario_HandleKeyIdsWithNumbers(self):
        exception = SecretKeyNotAvailableException("key123456789", message="Error")
        self.assertEqual("key123456789", exception.key_id)

    def test_UsingDifferentKeyIdFormats_DefaultScenario_HandleUUIDStyleKeyIds(self):
        key_id = "550e8400-e29b-41d4-a716-446655440000"
        exception = SecretKeyNotAvailableException(key_id, message="Error")
        self.assertEqual(key_id, exception.key_id)


if __name__ == '__main__':
    unittest.main()
