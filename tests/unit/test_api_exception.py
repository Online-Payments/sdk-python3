import unittest

from onlinepayments.sdk.api_exception import ApiException
from onlinepayments.sdk.domain.api_error import APIError

def _make_error(message):
    error = APIError()
    error.message = message
    return error

class ApiExceptionTest(unittest.TestCase):

    def test_ConstructingWith4Parameters_DefaultScenario_CreateInstanceWithValidParameters(self):
        error = _make_error("Invalid input")
        exception = ApiException(400, "Bad Request", "ERR_400", [error])

        self.assertIsNotNone(exception)
        self.assertEqual(400, exception.status_code)
        self.assertEqual("Bad Request", exception.response_body)
        self.assertEqual("ERR_400", exception.error_id)
        self.assertEqual(1, len(exception.errors))

    def test_ConstructingWith4Parameters_DefaultScenario_ThrowExceptionWhenStatusCodeIsNegative(self):
        exception = ApiException(-1, "error", "ERR_001", [])
        self.assertEqual(-1, exception.status_code)

    def test_ConstructingWith4Parameters_DefaultScenario_ConvertNullErrorsListToEmptyList(self):
        exception = ApiException(400, "error", "ERR_001", None)
        self.assertIsNotNone(exception.errors)
        self.assertEqual(0, len(exception.errors))

    def test_ConstructingWith4Parameters_DefaultScenario_StoreNullResponseBody(self):
        exception = ApiException(400, None, "ERR_001", [])
        self.assertIsNone(exception.response_body)

    def test_ConstructingWith4Parameters_DefaultScenario_StoreNullErrorId(self):
        exception = ApiException(400, "error", None, [])
        self.assertIsNone(exception.error_id)

    def test_ConstructingWith4Parameters_DefaultScenario_SetDefaultMessage(self):
        exception = ApiException(400, "error", "ERR_001", [])
        self.assertIn("the payment platform returned an error response", str(exception))

    def test_ConstructingWith4Parameters_DefaultScenario_StoreZeroStatusCode(self):
        exception = ApiException(0, "error", "ERR_001", [])
        self.assertEqual(0, exception.status_code)

    def test_ConstructingWith4Parameters_DefaultScenario_StoreEmptyStringResponseBody(self):
        exception = ApiException(400, "", "ERR_001", [])
        self.assertEqual("", exception.response_body)

    def test_ConstructingWith4Parameters_DefaultScenario_StoreEmptyStringErrorId(self):
        exception = ApiException(400, "error", "", [])
        self.assertEqual("", exception.error_id)

    def test_ConstructingWith5Parameters_DefaultScenario_CreateInstanceWithCustomMessage(self):
        exception = ApiException(500, "Internal Server Error", "ERR_500", [],
                                 "Custom error message")
        self.assertIn("Custom error message", str(exception))

    def test_ConstructingWith5Parameters_DefaultScenario_StoreAllParametersCorrectly(self):
        error = _make_error("Resource not found")
        exception = ApiException(404, "Not Found", "ERR_404", [error],
                                 "Error occurred")

        self.assertIn("Error occurred", str(exception))
        self.assertEqual(404, exception.status_code)
        self.assertEqual("Not Found", exception.response_body)
        self.assertEqual("ERR_404", exception.error_id)
        self.assertEqual(1, len(exception.errors))

    def test_ConstructingWith5Parameters_DefaultScenario_ConvertNullErrorsListToEmptyList(self):
        exception = ApiException(400, "error", "ERR_001", None, "Error")
        self.assertIsNotNone(exception.errors)
        self.assertEqual(0, len(exception.errors))

    def test_ConstructingWith5Parameters_DefaultScenario_StoreNullResponseBody(self):
        exception = ApiException(400, None, "ERR_001", [], "Error")
        self.assertIsNone(exception.response_body)

    def test_ConstructingWith5Parameters_DefaultScenario_StoreNullErrorId(self):
        exception = ApiException(400, "error", None, [], "Error")
        self.assertIsNone(exception.error_id)

    def test_ConstructingWith5Parameters_DefaultScenario_StoreNullMessage(self):
        exception = ApiException(400, "error", "ERR_001", [], None)
        self.assertIsNone(exception.args[0])

    def test_ConstructingWith5Parameters_DefaultScenario_StoreEmptyStringMessage(self):
        exception = ApiException(400, "error", "ERR_001", [], "")
        self.assertEqual("", exception.args[0])

    def test_ConstructingWith5Parameters_DefaultScenario_StoreZeroStatusCode(self):
        exception = ApiException(0, "error", "ERR_001", [], "Error")
        self.assertEqual(0, exception.status_code)

    def test_GettingStatusCode_DefaultScenario_ReturnPositiveStatusCode(self):
        exception = ApiException(201, "Created", "ERR_201", [])
        self.assertEqual(201, exception.status_code)

    def test_GettingStatusCode_DefaultScenario_ReturnZeroStatusCode(self):
        exception = ApiException(0, "error", "ERR_001", [])
        self.assertEqual(0, exception.status_code)

    def test_GettingStatusCode_DefaultScenario_ReturnNegativeStatusCode(self):
        exception = ApiException(-1, "error", "ERR_001", [])
        self.assertEqual(-1, exception.status_code)

    def test_GettingStatusCode_DefaultScenario_ReturnStatusCodeFromSecondConstructor(self):
        exception = ApiException(503, "Service Unavailable", "ERR_503", [],
                                 "Message")
        self.assertEqual(503, exception.status_code)

    def test_GettingResponseBody_DefaultScenario_ReturnResponseBody(self):
        exception = ApiException(400, "Invalid request format", "ERR_400", [])
        self.assertEqual("Invalid request format", exception.response_body)

    def test_GettingResponseBody_DefaultScenario_ReturnNullResponseBody(self):
        exception = ApiException(400, None, "ERR_400", [])
        self.assertIsNone(exception.response_body)

    def test_GettingResponseBody_DefaultScenario_ReturnEmptyResponseBody(self):
        exception = ApiException(400, "", "ERR_400", [])
        self.assertEqual("", exception.response_body)

    def test_GettingErrorId_DefaultScenario_ReturnErrorId(self):
        exception = ApiException(402, "Payment required", "ERR_PAYMENT_FAILED", [])
        self.assertEqual("ERR_PAYMENT_FAILED", exception.error_id)

    def test_GettingErrorId_DefaultScenario_ReturnNullErrorId(self):
        exception = ApiException(400, "error", None, [])
        self.assertIsNone(exception.error_id)

    def test_GettingErrorId_DefaultScenario_ReturnEmptyErrorId(self):
        exception = ApiException(400, "error", "", [])
        self.assertEqual("", exception.error_id)

    def test_GettingErrors_DefaultScenario_ReturnErrorsList(self):
        errors = [_make_error("Error 1"), _make_error("Error 2")]
        exception = ApiException(400, "error", "ERR_400", errors)

        self.assertEqual(2, len(exception.errors))
        self.assertEqual("Error 1", exception.errors[0].message)
        self.assertEqual("Error 2", exception.errors[1].message)

    def test_GettingErrors_DefaultScenario_ConvertNullListToEmptyList(self):
        exception = ApiException(400, "error", "ERR_400", None)
        self.assertIsNotNone(exception.errors)
        self.assertEqual(0, len(exception.errors))

    def test_GettingErrors_DefaultScenario_ReturnEmptyListWhenNoErrors(self):
        exception = ApiException(400, "error", "ERR_400", [])
        self.assertIsNotNone(exception.errors)
        self.assertEqual(0, len(exception.errors))

    def test_GettingErrors_DefaultScenario_ReturnSingleError(self):
        errors = [_make_error("Single error")]
        exception = ApiException(400, "error", "ERR_400", errors)
        self.assertEqual(1, len(exception.errors))
        self.assertEqual("Single error", exception.errors[0].message)

    def test_ConvertingToString_DefaultScenario_IncludeStatusCodeWhenPositive(self):
        exception = ApiException(400, "Bad Request", "ERR_400", [])
        self.assertIn("status_code=400", str(exception))

    def test_ConvertingToString_DefaultScenario_ExcludeStatusCodeWhenZero(self):
        exception = ApiException(0, "response", "ERR_001", [])
        self.assertNotIn("status_code=", str(exception))

    def test_ConvertingToString_DefaultScenario_ExcludeStatusCodeWhenNegative(self):
        exception = ApiException(-1, "response", "ERR_001", [])
        self.assertNotIn("status_code=", str(exception))

    def test_ConvertingToString_DefaultScenario_IncludeResponseBodyWhenNonEmpty(self):
        exception = ApiException(400, "Invalid input data", "ERR_400", [])
        self.assertIn("response_body='Invalid input data'", str(exception))

    def test_ConvertingToString_DefaultScenario_ExcludeResponseBodyWhenNull(self):
        exception = ApiException(400, None, "ERR_400", [])
        self.assertNotIn("response_body=", str(exception))

    def test_ConvertingToString_DefaultScenario_ExcludeResponseBodyWhenEmpty(self):
        exception = ApiException(400, "", "ERR_400", [])
        self.assertNotIn("response_body=", str(exception))

    def test_ConvertingToString_DefaultScenario_IncludeDefaultMessageFromFirstConstructor(self):
        exception = ApiException(400, "error", "ERR_400", [])
        self.assertIn("the payment platform returned an error response", str(exception))

    def test_ConvertingToString_DefaultScenario_IncludeMessageFromConstructor(self):
        exception = ApiException(400, "error", "ERR_400", [], "Custom message")
        self.assertIn("Custom message", str(exception))

    def test_ConvertingToString_DefaultScenario_FormatWithStatusCodeAndResponseBody(self):
        exception = ApiException(401, "Unauthorized", "ERR_401", [])
        result = str(exception)
        self.assertIn("status_code=401", result)
        self.assertIn("response_body='Unauthorized'", result)

    def test_ConvertingToString_DefaultScenario_FormatWithStatusCodeOnlyWhenResponseBodyEmpty(self):
        exception = ApiException(403, "", "ERR_403", [])
        result = str(exception)
        self.assertIn("status_code=403", result)
        self.assertNotIn("response_body=", result)

    def test_ExtendingRuntimeException_DefaultScenario_BeInstanceOfRuntimeException(self):
        exception = ApiException(500, "error", "ERR_500", [])
        self.assertIsInstance(exception, RuntimeError)

    def test_ExtendingRuntimeException_DefaultScenario_BeThrowable(self):
        exception = ApiException(500, "error", "ERR_500", [])
        with self.assertRaises(ApiException):
            raise exception

    def test_ExtendingRuntimeException_DefaultScenario_BeCatchableAsRuntimeException(self):
        exception = ApiException(500, "error", "ERR_500", [])
        with self.assertRaises(RuntimeError):
            raise exception

if __name__ == '__main__':
    unittest.main()
