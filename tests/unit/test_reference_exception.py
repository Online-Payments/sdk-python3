import unittest

from onlinepayments.sdk.api_exception import ApiException
from onlinepayments.sdk.reference_exception import ReferenceException


class ReferenceExceptionTest(unittest.TestCase):

    def test_CreatedWithDefaultMessage_DefaultScenario_SetDefaultMessageAndProperties(self):
        errors = []
        exception = ReferenceException(404, '{"error":"not found"}', "error-id", errors)

        self.assertIsInstance(exception, ApiException)
        self.assertEqual(404, exception.status_code)
        self.assertEqual('{"error":"not found"}', exception.response_body)
        self.assertEqual("error-id", exception.error_id)
        self.assertIs(errors, exception.errors)
        self.assertIn("the payment platform returned a reference error response", str(exception))

    def test_CreatedWithCustomMessage_DefaultScenario_SetCustomMessageAndProperties(self):
        errors = []
        exception = ReferenceException(404, '{"error":"not found"}', "error-id", errors, "custom message")

        self.assertIsInstance(exception, ApiException)
        self.assertEqual(404, exception.status_code)
        self.assertEqual('{"error":"not found"}', exception.response_body)
        self.assertEqual("error-id", exception.error_id)
        self.assertIs(errors, exception.errors)
        self.assertIn("custom message", str(exception))


if __name__ == '__main__':
    unittest.main()
