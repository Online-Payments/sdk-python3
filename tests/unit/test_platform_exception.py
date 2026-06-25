import unittest

from onlinepayments.sdk.api_exception import ApiException
from onlinepayments.sdk.platform_exception import PlatformException
from onlinepayments.sdk.domain.api_error import APIError


def _make_error(message):
    error = APIError()
    error.message = message
    return error


class PlatformExceptionTest(unittest.TestCase):

    def test_CreatedWithDefaultMessage_DefaultScenario_SetDefaultMessageAndProperties(self):
        errors = []
        exception = PlatformException(500, '{"error":"platform error"}', "error-id", errors)

        self.assertIsInstance(exception, ApiException)
        self.assertEqual(500, exception.status_code)
        self.assertEqual('{"error":"platform error"}', exception.response_body)
        self.assertEqual("error-id", exception.error_id)
        self.assertIs(errors, exception.errors)
        self.assertIn("the payment platform returned an error response", str(exception))

    def test_CreatedWithDefaultMessage_DefaultScenario_NormalizeNullErrorsToEmptyList(self):
        exception = PlatformException(500, '{"error":"platform error"}', "error-id", None)
        self.assertIsNotNone(exception.errors)
        self.assertEqual(0, len(exception.errors))

    def test_CreatedWithDefaultMessage_DefaultScenario_PreserveNonEmptyErrors(self):
        errors = [_make_error("payment failed")]
        exception = PlatformException(500, '{"error":"platform error"}', "error-id", errors)

        self.assertIs(errors, exception.errors)
        self.assertEqual(1, len(exception.errors))
        self.assertEqual("payment failed", exception.errors[0].message)

    def test_CreatedWithCustomMessage_DefaultScenario_SetCustomMessageAndProperties(self):
        errors = []
        exception = PlatformException(500, '{"error":"platform error"}', "error-id", errors, "custom message")

        self.assertIsInstance(exception, ApiException)
        self.assertEqual(500, exception.status_code)
        self.assertEqual('{"error":"platform error"}', exception.response_body)
        self.assertEqual("error-id", exception.error_id)
        self.assertIs(errors, exception.errors)
        self.assertIn("custom message", str(exception))

    def test_CreatedWithCustomMessage_DefaultScenario_NormalizeNullErrorsToEmptyList(self):
        exception = PlatformException(500, '{"error":"platform error"}', "error-id", None, "custom message")
        self.assertIsNotNone(exception.errors)
        self.assertEqual(0, len(exception.errors))

    def test_CreatedWithCustomMessage_DefaultScenario_PreserveNonEmptyErrors(self):
        errors = [_make_error("payment failed")]
        exception = PlatformException(500, '{"error":"platform error"}', "error-id", errors, "custom message")

        self.assertIs(errors, exception.errors)
        self.assertEqual(1, len(exception.errors))
        self.assertEqual("payment failed", exception.errors[0].message)


if __name__ == '__main__':
    unittest.main()
