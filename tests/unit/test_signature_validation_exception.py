import traceback
import unittest

from onlinepayments.sdk.webhooks.signature_validation_exception import SignatureValidationException


class SignatureValidationExceptionTest(unittest.TestCase):

    def test_ConstructingWithMessage_DefaultScenario_CreateInstanceWithMessage(self):
        exception = SignatureValidationException("Signature validation failed")
        self.assertIsNotNone(exception)

    def test_ConstructingWithMessage_DefaultScenario_StoreMessageFromConstructor(self):
        exception = SignatureValidationException("Invalid signature provided")
        self.assertEqual("Invalid signature provided", str(exception))

    def test_ConstructingWithMessage_DefaultScenario_BeRuntimeException(self):
        exception = SignatureValidationException("Signature validation failed")
        self.assertIsInstance(exception, RuntimeError)

    def test_ConstructingWithMessage_DefaultScenario_NotHaveCauseWhenNotProvided(self):
        exception = SignatureValidationException("Signature validation failed")
        self.assertEqual(1, len(exception.args))
        self.assertEqual("Signature validation failed", exception.args[0])

    def test_ConstructingWithCause_DefaultScenario_CreateInstanceWithCause(self):
        cause = RuntimeError("Cryptographic error")
        exception = SignatureValidationException(cause=cause)
        self.assertIsNotNone(exception)

    def test_ConstructingWithCause_DefaultScenario_StoreCauseFromConstructor(self):
        cause = RuntimeError("Cryptographic error")
        exception = SignatureValidationException(cause=cause)
        self.assertIs(cause, exception.args[0])

    def test_ConstructingWithCause_DefaultScenario_HaveCauseMessage(self):
        cause = Exception("Invalid key format")
        exception = SignatureValidationException(cause=cause)
        # equivalent of Java getCause().getMessage()
        self.assertEqual("Invalid key format", exception.args[0].args[0])

    def test_ConstructingWithCause_DefaultScenario_HaveNullMessageWhenOnlyCallWithCause(self):
        cause = RuntimeError("Cryptographic error")
        exception = SignatureValidationException(cause=cause)
        self.assertEqual(1, len(exception.args))
        self.assertIs(cause, exception.args[0])

    def test_ConstructingWithMessageAndCause_DefaultScenario_CreateInstanceWithBothParameters(self):
        cause = RuntimeError("Cryptographic error")
        exception = SignatureValidationException("Signature validation failed", cause)
        self.assertIsNotNone(exception)

    def test_ConstructingWithMessageAndCause_DefaultScenario_StoreMessageFromConstructor(self):
        cause = RuntimeError("Cryptographic error")
        exception = SignatureValidationException("Invalid signature: expected ABC but got DEF", cause)
        self.assertIn("Invalid signature", str(exception))

    def test_ConstructingWithMessageAndCause_DefaultScenario_StoreCauseFromConstructor(self):
        cause = RuntimeError("Cryptographic error")
        exception = SignatureValidationException("Signature validation failed", cause)
        self.assertIs(cause, exception.args[1])

    def test_ConstructingWithMessageAndCause_DefaultScenario_HaveBothMessageAndCause(self):
        cause = Exception("Underlying crypto error")
        exception = SignatureValidationException("Failed to validate webhook signature", cause)
        self.assertEqual("Failed to validate webhook signature", exception.args[0])
        self.assertIs(cause, exception.args[1])

    def test_ThrowingException_DefaultScenario_BeThrowableAndCatchable(self):
        with self.assertRaises(SignatureValidationException) as ctx:
            raise SignatureValidationException("Signature mismatch")
        self.assertEqual("Signature mismatch", str(ctx.exception))

    def test_ThrowingException_DefaultScenario_BeCatchableAsRuntimeException(self):
        with self.assertRaises(RuntimeError):
            raise SignatureValidationException("Signature mismatch")

    def test_ThrowingException_DefaultScenario_BeCatchableAsException(self):
        with self.assertRaises(Exception):
            raise SignatureValidationException("Signature mismatch")

    def test_ThrowingException_DefaultScenario_BeCatchableAsThrowable(self):
        with self.assertRaises(BaseException):
            raise SignatureValidationException("Signature mismatch")

    def test_HandlingExceptionMessages_DefaultScenario_HandleEmptyMessage(self):
        exception = SignatureValidationException("")
        self.assertEqual("", str(exception))

    def test_HandlingExceptionMessages_DefaultScenario_HandleNullMessage(self):
        exception = SignatureValidationException(None)
        self.assertIsNotNone(exception)

    def test_HandlingExceptionMessages_DefaultScenario_HandleMultilineMessage(self):
        message = "Signature validation failed:\nExpected: sig1\nActual: sig2"
        exception = SignatureValidationException(message)
        self.assertEqual(message, str(exception))
        self.assertIn("\n", str(exception))

    def test_HandlingExceptionMessages_DefaultScenario_HandleSpecialCharactersInMessage(self):
        message = "Signature!@#$%^&*() validation failed"
        exception = SignatureValidationException(message)
        self.assertEqual(message, str(exception))

    def test_HandlingExceptionMessages_DefaultScenario_HandleLongMessage(self):
        message = "A" * 10000
        exception = SignatureValidationException(message)
        self.assertEqual(message, str(exception))
        self.assertEqual(10000, len(str(exception)))

    def test_HandlingExceptionChains_DefaultScenario_ChainWithMultipleCauses(self):
        root_cause = Exception("Root cause")
        intermediate = RuntimeError("Intermediate")
        intermediate.__cause__ = root_cause
        exception = SignatureValidationException("Signature failed", intermediate)
        self.assertEqual("Intermediate", exception.args[1].args[0])
        self.assertEqual("Root cause", exception.args[1].__cause__.args[0])

    def test_HandlingExceptionChains_DefaultScenario_PreserveStackTrace(self):
        try:
            raise SignatureValidationException("Signature validation failed", Exception("Crypto error"))
        except SignatureValidationException as exception:
            self.assertIsNotNone(exception.__traceback__)

    def test_HandlingExceptionChains_DefaultScenario_BePrintableWithStackTrace(self):
        try:
            raise SignatureValidationException("Signature failed", Exception("Cryptographic error"))
        except SignatureValidationException as exception:
            formatted = "".join(
                traceback.format_exception(type(exception), exception, exception.__traceback__))
            self.assertIn("SignatureValidationException", formatted)

    def test_UsingDifferentConstructors_DefaultScenario_CreateInstanceWithEachConstructor(self):
        e1 = SignatureValidationException("Message only")
        e2 = SignatureValidationException(cause=Exception("Cause only"))
        e3 = SignatureValidationException("Message", Exception("Cause"))
        self.assertIsNotNone(e1)
        self.assertIsNotNone(e2)
        self.assertIsNotNone(e3)

    def test_UsingDifferentConstructors_DefaultScenario_HaveMessageWhenProvidedInConstructor(self):
        exception = SignatureValidationException("My message")
        self.assertEqual("My message", exception.args[0])

    def test_UsingDifferentConstructors_DefaultScenario_HaveCauseWhenProvidedInConstructor(self):
        cause = Exception("Cause")
        exception = SignatureValidationException(cause=cause)
        self.assertIs(cause, exception.args[0])

    def test_UsingDifferentConstructors_DefaultScenario_HaveBothMessageAndCauseWhenBothProvided(self):
        cause = Exception("Cause")
        exception = SignatureValidationException("Message", cause)
        self.assertEqual("Message", exception.args[0])
        self.assertIs(cause, exception.args[1])


if __name__ == '__main__':
    unittest.main()
