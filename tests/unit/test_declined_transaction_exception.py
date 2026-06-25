import unittest

from onlinepayments.sdk.api_exception import ApiException
from onlinepayments.sdk.declined_transaction_exception import DeclinedTransactionException
from onlinepayments.sdk.domain.api_error import APIError


def _make_error(message):
    error = APIError()
    error.message = message
    return error


class DeclinedTransactionExceptionTest(unittest.TestCase):

    def test_ConstructingWithoutMessage_DefaultScenario_StoreStatusCode(self):
        exception = DeclinedTransactionException(402, '{"error":"declined"}',
                                                 "ERR_402", [])
        self.assertEqual(402, exception.status_code)

    def test_ConstructingWithMessage_DefaultScenario_StoreCustomMessage(self):
        exception = DeclinedTransactionException(402, "body", "err-id",
                                                 [],"declined transaction")
        self.assertIn("declined transaction", str(exception))

    def test_ConstructingWithoutMessage_DefaultScenario_StoreNullErrors(self):
        exception = DeclinedTransactionException(402, "body", "err-id", None)
        self.assertIsNotNone(exception.errors)
        self.assertEqual(0, len(exception.errors))

    def test_ConstructingWithMessage_DefaultScenario_StoreErrors(self):
        errors = [_make_error("Transaction declined")]
        exception = DeclinedTransactionException(402, "body",
                                                 "err-id", errors,"declined")
        self.assertEqual(1, len(exception.errors))
        self.assertEqual("Transaction declined", exception.errors[0].message)

    def test_ConstructingWithoutMessage_DefaultScenario_StoreNullErrorId(self):
        exception = DeclinedTransactionException(402, "body", None, [])
        self.assertIsNone(exception.error_id)

    def test_ConstructingWithoutMessage_DefaultScenario_AllowNullResponseBody(self):
        exception = DeclinedTransactionException(402, None, "err-id", [])
        self.assertIsNone(exception.response_body)

    def test_ConstructingWithoutMessage_DefaultScenario_ExtendApiException(self):
        exception = DeclinedTransactionException(402, "body", "err-id", [])
        self.assertIsInstance(exception, ApiException)

    def test_ConstructingWithoutMessage_DefaultScenario_StoreResponseBody(self):
        exception = DeclinedTransactionException(402, '{"error":"declined"}',
                                                 "ERR_402", [])
        self.assertEqual('{"error":"declined"}', exception.response_body)

    def test_ConstructingWithoutMessage_DefaultScenario_AllowVariousStatusCodes(self):
        for status_code in [400, 402, 500]:
            exception = DeclinedTransactionException(status_code, "body", "err-id", [])
            self.assertEqual(status_code, exception.status_code)

    def test_ConstructingWithoutMessage_DefaultScenario_StoreErrorIdWhenProvided(self):
        exception = DeclinedTransactionException(402, "body", "ERR_DECLINED", [])
        self.assertEqual("ERR_DECLINED", exception.error_id)

    def test_ConstructingWithoutMessage_DefaultScenario_StoreErrorsWhenProvided(self):
        errors = [_make_error("Transaction declined"), _make_error("Insufficient funds")]
        exception = DeclinedTransactionException(402, "body", "err-id", errors)

        self.assertEqual(2, len(exception.errors))
        self.assertEqual("Transaction declined", exception.errors[0].message)
        self.assertEqual("Insufficient funds", exception.errors[1].message)

    def test_ConstructingWithMessage_DefaultScenario_StoreErrorId(self):
        exception = DeclinedTransactionException(402, "body", "ERR_402",
                                                 [],"declined")
        self.assertEqual("ERR_402", exception.error_id)

    def test_ConstructingWithMessage_DefaultScenario_StoreStatusCodeWithMessage(self):
        exception = DeclinedTransactionException(402, "body", "err-id", [],
                                                 "declined")
        self.assertEqual(402, exception.status_code)

    def test_ConstructingWithMessage_DefaultScenario_StoreResponseBodyWithMessage(self):
        exception = DeclinedTransactionException(402, "response body", "err-id",
                                                 [], "declined")
        self.assertEqual("response body", exception.response_body)

    def test_ConstructingWithMessage_DefaultScenario_AllowNullMessage(self):
        exception = DeclinedTransactionException(402, "body", "err-id",
                                                 [], None)
        self.assertIn("the payment platform returned an error response", str(exception))

    def test_ConstructingWithMessage_DefaultScenario_AllowNullErrorId(self):
        exception = DeclinedTransactionException(402, "body", None,
                                                 [], "declined")
        self.assertIsNone(exception.error_id)

    def test_ConstructingWithMessage_DefaultScenario_AllowNullErrors(self):
        exception = DeclinedTransactionException(402, "body", "err-id",
                                                 None, "declined")
        self.assertIsNotNone(exception.errors)
        self.assertEqual(0, len(exception.errors))

    def test_ConstructingWithMessage_DefaultScenario_AllowEmptyErrorsList(self):
        exception = DeclinedTransactionException(402, "body", "err-id",
                                                 [], "declined")
        self.assertEqual(0, len(exception.errors))

    def test_ConstructingWithMessage_DefaultScenario_ExtendApiExceptionWhenConstructedWithMessage(self):
        exception = DeclinedTransactionException(402, "body", "err-id",
                                                 [], "declined")
        self.assertIsInstance(exception, ApiException)

    def test_ComparingDifferentInstances_DefaultScenario_HaveDifferentStatusCodes(self):
        first_exception = DeclinedTransactionException(402, "body", "err-id", [],
                                                       "Message")
        second_exception = DeclinedTransactionException(500, "body", "err-id", [],
                                                        "Message")
        self.assertEqual(402, first_exception.status_code)
        self.assertEqual(500, second_exception.status_code)

    def test_ComparingDifferentInstances_DefaultScenario_HaveDifferentErrorIds(self):
        first_exception = DeclinedTransactionException(402, "body", "ERR_001", [],
                                          "Message")
        second_exception = DeclinedTransactionException(402, "body", "ERR_002", [],
                                          "Message")
        self.assertEqual("ERR_001", first_exception.error_id)
        self.assertEqual("ERR_002", second_exception.error_id)

    def test_ComparingDifferentInstances_DefaultScenario_HaveDifferentMessages(self):
        first_exception = DeclinedTransactionException(402, "body", "err-id", [],
                                          "message one")
        second_exception = DeclinedTransactionException(402, "body", "err-id", [],
                                          "message two")
        self.assertIn("message one", str(first_exception))
        self.assertIn("message two", str(second_exception))


if __name__ == '__main__':
    unittest.main()
