import unittest

from onlinepayments.sdk.authorization_exception import AuthorizationException


class AuthorizationExceptionTest(unittest.TestCase):

    def test_CreatedWithDefaultMessage_DefaultScenario_SetDefaultMessageAndProperties(self):
        exception = AuthorizationException(403, "Forbidden", "ERR_403", [])
        self.assertIsNotNone(exception)
        self.assertEqual(403, exception.status_code)
        self.assertEqual("Forbidden", exception.response_body)
        self.assertEqual("ERR_403", exception.error_id)

    def test_CreatedWithDefaultMessage_DefaultScenario_ContainDefaultMessageInString(self):
        exception = AuthorizationException(403, "Forbidden", "ERR_403", [])
        self.assertIn("the payment platform returned an authorization error response", str(exception))

    def test_CreatedWithCustomMessage_DefaultScenario_SetCustomMessageAndProperties(self):
        exception = AuthorizationException(403, "Forbidden", "ERR_403", [],
                                           "Custom auth error")
        self.assertIn("Custom auth error", str(exception))


if __name__ == '__main__':
    unittest.main()
