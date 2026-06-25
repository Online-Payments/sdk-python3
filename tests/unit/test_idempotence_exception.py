import unittest

from onlinepayments.sdk.api_exception import ApiException
from onlinepayments.sdk.idempotence_exception import IdempotenceException
from onlinepayments.sdk.domain.api_error import APIError


def _make_error(message):
    error = APIError()
    error.message = message
    return error


class IdempotenceExceptionTest(unittest.TestCase):

    def test_CreatedWithDefaultMessage_DefaultScenario_SetDefaultMessageAndProperties(self):
        errors = []
        exception = IdempotenceException(
            "idempotence-key", 123456789,
            409, '{"error":"duplicate request"}', "error-id", errors
        )

        self.assertIsInstance(exception, ApiException)
        self.assertEqual(409, exception.status_code)
        self.assertEqual('{"error":"duplicate request"}', exception.response_body)
        self.assertEqual("error-id", exception.error_id)
        self.assertIs(errors, exception.errors)
        self.assertEqual("idempotence-key", exception.idempotence_key)
        self.assertEqual(123456789, exception.idempotence_request_timestamp)
        self.assertIn(
            "the payment platform returned a duplicate request error response",
            str(exception)
        )

    def test_CreatedWithDefaultMessage_DefaultScenario_StoreNullIdempotenceKey(self):
        exception = IdempotenceException(
            None, 123456789,
            409, '{"error":"duplicate request"}', "error-id", []
        )
        self.assertIsNone(exception.idempotence_key)

    def test_CreatedWithDefaultMessage_DefaultScenario_StoreNullIdempotenceRequestTimestamp(self):
        exception = IdempotenceException(
            "idempotence-key", None,
            409, '{"error":"duplicate request"}', "error-id", []
        )
        self.assertIsNone(exception.idempotence_request_timestamp)

    def test_CreatedWithDefaultMessage_DefaultScenario_NormalizeNullErrorsToEmptyList(self):
        exception = IdempotenceException(
            "idempotence-key", 123456789,
            409, '{"error":"duplicate request"}', "error-id", None
        )
        self.assertIsNotNone(exception.errors)
        self.assertEqual(0, len(exception.errors))

    def test_CreatedWithDefaultMessage_DefaultScenario_PreserveNonEmptyErrors(self):
        errors = [_make_error("duplicate request detected")]
        exception = IdempotenceException(
            "idempotence-key", 123456789,
            409, '{"error":"duplicate request"}', "error-id", errors
        )
        self.assertIs(errors, exception.errors)
        self.assertEqual(1, len(exception.errors))
        self.assertEqual("duplicate request detected", exception.errors[0].message)

    def test_CreatedWithCustomMessage_DefaultScenario_SetCustomMessageAndProperties(self):
        errors = []
        exception = IdempotenceException(
            "idempotence-key", 123456789,
            409, '{"error":"duplicate request"}', "error-id", errors,
            "custom message"
        )

        self.assertIsInstance(exception, ApiException)
        self.assertEqual(409, exception.status_code)
        self.assertEqual('{"error":"duplicate request"}', exception.response_body)
        self.assertEqual("error-id", exception.error_id)
        self.assertIs(errors, exception.errors)
        self.assertEqual("idempotence-key", exception.idempotence_key)
        self.assertEqual(123456789, exception.idempotence_request_timestamp)
        self.assertIn("custom message", str(exception))

    def test_CreatedWithCustomMessage_DefaultScenario_StoreNullIdempotenceKey(self):
        exception = IdempotenceException(
            None, 123456789,
            409, '{"error":"duplicate request"}', "error-id", [],
            "custom message"
        )
        self.assertIsNone(exception.idempotence_key)

    def test_CreatedWithCustomMessage_DefaultScenario_StoreNullIdempotenceRequestTimestamp(self):
        exception = IdempotenceException(
            "idempotence-key", None,
            409, '{"error":"duplicate request"}', "error-id", [],
            "custom message"
        )
        self.assertIsNone(exception.idempotence_request_timestamp)

    def test_CreatedWithCustomMessage_DefaultScenario_NormalizeNullErrorsToEmptyList(self):
        exception = IdempotenceException(
            "idempotence-key", 123456789,
            409, '{"error":"duplicate request"}', "error-id", None,
            "custom message"
        )
        self.assertIsNotNone(exception.errors)
        self.assertEqual(0, len(exception.errors))


if __name__ == '__main__':
    unittest.main()
