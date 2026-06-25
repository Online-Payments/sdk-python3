import unittest

from onlinepayments.sdk.api_exception import ApiException
from onlinepayments.sdk.validation_exception import ValidationException


class ValidationExceptionTest(unittest.TestCase):

    def test_CreatedWithDefaultMessage_DefaultScenario_SetDefaultMessageAndProperties(self):
        errors = []
        exception = ValidationException(400, '{"error":"bad request"}', "error-id", errors)

        self.assertIsInstance(exception, ApiException)
        self.assertEqual(400, exception.status_code)
        self.assertEqual('{"error":"bad request"}', exception.response_body)
        self.assertEqual("error-id", exception.error_id)
        self.assertIs(errors, exception.errors)
        self.assertEqual(
            "the payment platform returned an incorrect request error response", exception.args[0])

    def test_CreatedWithCustomMessage_DefaultScenario_SetCustomMessageAndProperties(self):
        errors = []
        exception = ValidationException(400, '{"error":"bad request"}', "error-id", errors, "custom message")

        self.assertIsInstance(exception, ApiException)
        self.assertEqual(400, exception.status_code)
        self.assertEqual('{"error":"bad request"}', exception.response_body)
        self.assertEqual("error-id", exception.error_id)
        self.assertIs(errors, exception.errors)
        self.assertEqual("custom message", exception.args[0])


if __name__ == '__main__':
    unittest.main()
