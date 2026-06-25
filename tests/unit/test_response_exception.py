import unittest

from onlinepayments.sdk.communication.response_exception import ResponseException


class ResponseExceptionTest(unittest.TestCase):

    def test_ResponseExceptionIsCreatedWithoutHeaders_DefaultScenario_ReturnEmptyHeadersAndNullHeaderValues(self):
        exception = ResponseException(400, None, None)

        self.assertEqual(400, exception.status_code)
        self.assertIsNone(exception.body)
        self.assertIsNotNone(exception.headers)
        self.assertEqual(0, len(exception.headers))
        self.assertIsNone(exception.get_header("Content-Type"))
        self.assertIsNone(exception.get_header_value("Content-Type"))

    def test_ResponseExceptionIsCreatedWithHeaders_DefaultScenario_ReturnExpectedHeadersAndHeaderValues(self):
        headers = {"Content-Type": "application/json", "X-Request-Id": "request-id"}
        exception = ResponseException(400, '{"error":"bad request"}', headers)

        self.assertEqual(400, exception.status_code)
        self.assertEqual('{"error":"bad request"}', exception.body)
        self.assertEqual(headers, exception.headers)
        self.assertIsNotNone(exception.get_header("Content-Type"))
        self.assertEqual("application/json", exception.get_header_value("Content-Type"))
        self.assertIsNotNone(exception.get_header("X-Request-Id"))
        self.assertEqual("request-id", exception.get_header_value("X-Request-Id"))

    def test_ResponseExceptionIsCreatedWithHeaders_DefaultScenario_ReturnHeaderValueWithCaseInsensitiveMatch(self):
        exception = ResponseException(400, "body", {"Content-Type": "application/json"})
        self.assertEqual("application/json", exception.get_header_value("content-type"))
        self.assertEqual("application/json", exception.get_header_value("CONTENT-TYPE"))

    def test_ResponseExceptionIsConvertedToString_DefaultScenario_ContainStatusCodeAndResponseBody(self):
        exception = ResponseException(404, '{"error":"not found"}', {"Content-Type": "application/json"})
        result = str(exception)
        self.assertIn("status_code=404", result)
        self.assertIn('response_body=\'{"error":"not found"}\'', result)

    def test_ResponseExceptionIsConvertedToString_DefaultScenario_ExcludeStatusCodeWhenZero(self):
        self.assertNotIn("status_code=", str(ResponseException(0, "body", None)))

    def test_ResponseExceptionIsConvertedToString_DefaultScenario_ExcludeResponseBodyWhenNone(self):
        self.assertNotIn("response_body=", str(ResponseException(400, None, None)))

    def test_ResponseExceptionIsConvertedToString_DefaultScenario_ExcludeResponseBodyWhenEmpty(self):
        self.assertNotIn("response_body=", str(ResponseException(400, "", None)))


if __name__ == '__main__':
    unittest.main()
