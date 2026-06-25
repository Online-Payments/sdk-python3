import unittest

from onlinepayments.sdk.communication.not_found_exception import NotFoundException


class NotFoundExceptionTest(unittest.TestCase):

    def test_CreatingWithException_DefaultScenario_InitializeExceptionWithCause(self):
        cause = ValueError("Invalid path parameter")
        exception = NotFoundException(cause, "Resource not found")
        self.assertIsNotNone(exception)
        self.assertIs(cause, exception.cause)

    def test_CreatingWithMessageAndException_DefaultScenario_InitializeExceptionWithMessageAndCause(self):
        cause = ValueError("Invalid path parameter")
        exception = NotFoundException(cause, "Resource not found")
        self.assertIsNotNone(exception)
        self.assertEqual("Resource not found", exception.args[0])
        self.assertIs(cause, exception.cause)


if __name__ == '__main__':
    unittest.main()
