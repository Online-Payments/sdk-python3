import unittest

from onlinepayments.sdk.log.body_obfuscator import BodyObfuscator
from onlinepayments.sdk.log.header_obfuscator import HeaderObfuscator
from onlinepayments.sdk.log.response_log_message import ResponseLogMessage


class ResponseLogMessageBuilderTest(unittest.TestCase):

    @staticmethod
    def _message(request_id="test-request-id", status_code=200, duration=None):
        if duration is None:
            return ResponseLogMessage(
                request_id, status_code,
                body_obfuscator=BodyObfuscator.default_body_obfuscator(),
                header_obfuscator=HeaderObfuscator.default_header_obfuscator())
        return ResponseLogMessage(
            request_id, status_code, duration,
            BodyObfuscator.default_body_obfuscator(),
            HeaderObfuscator.default_header_obfuscator())

    def test_ConstructingWithoutDuration_DefaultScenario_CreateInstanceWithFourParameters(self):
        msg = self._message("test-request-id", 200)
        self.assertIsNotNone(msg)
        self.assertEqual(200, msg.get_status_code())
        self.assertLess(msg.get_duration(), 0)

    def test_ConstructingWithoutDuration_DefaultScenario_DelegateToFiveParameterConstructor(self):
        msg = self._message("test-request-id", 404)
        msg.set_body("Not found", "text/plain")
        message = msg.get_message()
        self.assertNotIn("ms)", message)

    def test_ConstructingWithDuration_DefaultScenario_CreateInstanceWithFiveParametersAndZeroDuration(self):
        msg = self._message("test-request-id", 200, 0)
        self.assertIsNotNone(msg)
        self.assertEqual(0, msg.get_duration())

    def test_ConstructingWithDuration_DefaultScenario_CreateInstanceWithFiveParametersAndPositiveDuration(self):
        msg = self._message("test-request-id", 200, 150)
        self.assertIsNotNone(msg)
        self.assertEqual(150, msg.get_duration())

    def test_ConstructingWithDuration_DefaultScenario_CreateInstanceWithFiveParametersAndLargeDuration(self):
        msg = self._message("test-request-id", 200, 5000)
        self.assertIsNotNone(msg)
        self.assertEqual(5000, msg.get_duration())

    def test_BuildingMessageWithoutDuration_DefaultScenario_ExcludeDurationWhenNegative(self):
        msg = self._message("test-request-id", 200)
        msg.set_body("Response body", "application/json")
        message = msg.get_message()
        self.assertIn("Incoming response (requestId='test-request-id')", message)
        self.assertNotIn("ms)", message)

    def test_BuildingMessageWithoutDuration_DefaultScenario_IncludeStatusCodeAndHeaders(self):
        msg = self._message("test-id", 404)
        msg.add_header("Content-Type", "application/json")
        msg.set_body("Not found", "application/json")
        message = msg.get_message()
        self.assertIn("404", message)
        self.assertIn("Content-Type", message)

    def test_BuildingMessageWithoutDuration_DefaultScenario_HandleNullBodyAndContentType(self):
        msg = self._message("test-request-id", 204)
        message = msg.get_message()
        self.assertIn("204", message)
        self.assertIn("content-type:", message)
        self.assertIn("body:", message)

    def test_BuildingMessageWithDuration_DefaultScenario_IncludeDurationWhenPositive(self):
        msg = self._message("test-request-id", 200, 100)
        msg.set_body("Success", "text/plain")
        message = msg.get_message()
        self.assertIn("Incoming response (requestId='test-request-id', 100 ms)", message)

    def test_BuildingMessageWithDuration_DefaultScenario_IncludeDurationWhenZero(self):
        msg = self._message("test-request-id", 200, 0)
        msg.set_body("Success", "text/plain")
        message = msg.get_message()
        self.assertIn("Incoming response (requestId='test-request-id', 0 ms)", message)

    def test_BuildingMessageWithDuration_DefaultScenario_IncludeDurationWithLargeValues(self):
        msg = self._message("test-request-id", 200, 5000)
        msg.set_body("Success", "text/plain")
        message = msg.get_message()
        self.assertIn("5000 ms", message)

    def test_BuildingMessageWithDuration_DefaultScenario_IncludeStatusCodeWithDuration(self):
        msg = self._message("test-id", 500, 250)
        msg.set_body("Server error", "text/plain")
        message = msg.get_message()
        self.assertIn("500", message)
        self.assertIn("250 ms", message)

    def test_FormattingMessage_DefaultScenario_IncludeAllHeadersInMessage(self):
        msg = self._message("test-id", 200)
        msg.add_header("Content-Type", "application/json")
        msg.add_header("X-Custom-Header", "custom-value")
        msg.add_header("Cache-Control", "no-cache")
        msg.set_body("Response", "application/json")
        message = msg.get_message()
        self.assertIn("Content-Type", message)
        self.assertIn("X-Custom-Header", message)
        self.assertIn("Cache-Control", message)

    def test_FormattingMessage_DefaultScenario_ObfuscateSensitiveHeaders(self):
        msg = self._message("test-id", 200)
        msg.add_header("Authorization", "Bearer secret-token-12345")
        msg.set_body("Response", "application/json")
        message = msg.get_message()
        self.assertIn("Authorization", message)
        self.assertIn("*", message)
        self.assertNotIn("secret-token-12345", message)

    def test_FormattingMessage_DefaultScenario_IncludeContentTypeInMessage(self):
        msg = self._message("test-id", 200)
        msg.set_body("Response body", "application/xml")
        message = msg.get_message()
        self.assertIn("content-type: application/xml", message)

    def test_FormattingMessage_DefaultScenario_IncludeBodyInMessage(self):
        msg = self._message("test-id", 200)
        msg.set_body("Response body content", "text/plain")
        message = msg.get_message()
        self.assertIn("Response body content", message)

    def test_FormattingMessage_DefaultScenario_FormatWithMultilineStructure(self):
        msg = self._message("test-id", 200)
        msg.add_header("Content-Type", "application/json")
        msg.set_body('{ "key": "value" }', "application/json")
        message = msg.get_message()
        self.assertIn("\n", message)
        self.assertTrue(message.startswith("Incoming response"))
        self.assertIn("status_code", message)
        self.assertIn("headers", message)
        self.assertIn("content-type", message)
        self.assertIn("body", message)

    def test_HandlingDifferentStatusCodes_DefaultScenario_HandleSuccessStatusCode(self):
        msg = self._message("test-id", 200)
        msg.set_body("OK", "text/plain")
        message = msg.get_message()
        self.assertIn("200", message)

    def test_HandlingDifferentStatusCodes_DefaultScenario_HandleRedirectStatusCode(self):
        msg = self._message("test-id", 301)
        msg.set_body("Moved", "text/plain")
        message = msg.get_message()
        self.assertIn("301", message)

    def test_HandlingDifferentStatusCodes_DefaultScenario_HandleClientErrorStatusCode(self):
        msg = self._message("test-id", 400)
        msg.set_body("Bad request", "application/json")
        message = msg.get_message()
        self.assertIn("400", message)

    def test_HandlingDifferentStatusCodes_DefaultScenario_HandleServerErrorStatusCode(self):
        msg = self._message("test-id", 500)
        msg.set_body("Internal error", "text/plain")
        message = msg.get_message()
        self.assertIn("500", message)


if __name__ == '__main__':
    unittest.main()
