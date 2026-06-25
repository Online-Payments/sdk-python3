import unittest

from onlinepayments.sdk.log.body_obfuscator import BodyObfuscator
from onlinepayments.sdk.log.header_obfuscator import HeaderObfuscator
from onlinepayments.sdk.log.request_log_message import RequestLogMessage


class LogMessageBuilderTest(unittest.TestCase):

    @staticmethod
    def _builder():
        return RequestLogMessage(
            "test-id",
            "GET",
            "/api/endpoint",
            BodyObfuscator.default_body_obfuscator(),
            HeaderObfuscator.default_header_obfuscator(),
        )

    def test_EmptyingIfNull_DefaultScenario_ReturnEmptyStringForNull(self):
        builder = self._builder()
        self.assertEqual("", builder.empty_if_none(None))

    def test_EmptyingIfNull_DefaultScenario_ReturnValueForNonNull(self):
        builder = self._builder()
        self.assertEqual("test-value", builder.empty_if_none("test-value"))

    def test_SettingBinaryContent_DefaultScenario_AcceptValidBinaryContentType(self):
        builder = self._builder()
        builder.set_binary_body("application/octet-stream")
        self.assertEqual("<binary content>", builder.body)
        self.assertEqual("application/octet-stream", builder.content_type)

    def test_SettingBinaryContent_DefaultScenario_AcceptOtherBinaryContentTypes(self):
        builder = self._builder()
        builder.set_binary_body("image/png")
        self.assertEqual("<binary content>", builder.body)
        self.assertEqual("image/png", builder.content_type)

    def test_SettingBinaryContent_DefaultScenario_RejectTextContentType(self):
        builder = self._builder()
        with self.assertRaises(ValueError):
            builder.set_binary_body("text/plain")

    def test_SettingBinaryContent_DefaultScenario_RejectJsonContentType(self):
        builder = self._builder()
        with self.assertRaises(ValueError):
            builder.set_binary_body("application/json")

    def test_SettingBinaryContent_DefaultScenario_RejectXmlContentType(self):
        builder = self._builder()
        with self.assertRaises(ValueError):
            builder.set_binary_body("application/xml")

    def test_Constructing_DefaultScenario_ThrowExceptionWhenRequestIdIsNull(self):
        with self.assertRaises(ValueError):
            RequestLogMessage(None, "GET", "/api/endpoint",
                              BodyObfuscator.default_body_obfuscator(),
                              HeaderObfuscator.default_header_obfuscator())

    def test_Constructing_DefaultScenario_ThrowExceptionWhenRequestIdIsEmpty(self):
        with self.assertRaises(ValueError):
            RequestLogMessage("", "GET", "/api/endpoint",
                              BodyObfuscator.default_body_obfuscator(),
                              HeaderObfuscator.default_header_obfuscator())

    def test_Constructing_DefaultScenario_ThrowExceptionWhenBodyObfuscatorIsNull(self):
        with self.assertRaises(ValueError):
            RequestLogMessage("test-id", "GET", "/api/endpoint",
                              None,
                              HeaderObfuscator.default_header_obfuscator())

    def test_Constructing_DefaultScenario_ThrowExceptionWhenHeaderObfuscatorIsNull(self):
        with self.assertRaises(ValueError):
            RequestLogMessage("test-id", "GET", "/api/endpoint",
                              BodyObfuscator.default_body_obfuscator(),
                              None)

    def test_Constructing_DefaultScenario_CreateInstanceWithValidParameters(self):
        builder = self._builder()
        self.assertIsNotNone(builder)
        self.assertEqual("test-id", builder.request_id)

    def test_AddingHeaders_DefaultScenario_AddMultipleHeaders(self):
        builder = self._builder()
        builder.add_header("Content-Type", "application/json")
        builder.add_header("Authorization", "Bearer token")

        headers = builder.headers
        self.assertIn("Content-Type", headers)
        self.assertIn("Authorization", headers)
        self.assertIn(", ", headers)

    def test_AddingHeaders_DefaultScenario_HandleNullHeaderValue(self):
        builder = self._builder()
        builder.add_header("X-Custom", None)
        self.assertIn("X-Custom", builder.headers)

    def test_SettingBody_DefaultScenario_SetBodyWithString(self):
        builder = self._builder()
        builder.set_body("test body", "text/plain")
        self.assertEqual("test body", builder.body)
        self.assertEqual("text/plain", builder.content_type)

    def test_SettingBody_DefaultScenario_SetBodyWithInputStream(self):
        builder = self._builder()
        builder.set_body("test input stream body".encode("utf-8"), "text/plain", "utf-8")
        self.assertEqual("test input stream body", builder.body)
        self.assertEqual("text/plain", builder.content_type)

    def test_SettingBody_DefaultScenario_SetBinaryBodyWithInputStream(self):
        builder = self._builder()
        builder.set_body(bytes([1, 2, 3, 4, 5]), "application/octet-stream")
        self.assertEqual("<binary content>", builder.body)
        self.assertEqual("application/octet-stream", builder.content_type)

    def test_SettingBody_DefaultScenario_SetBodyWithReader(self):
        builder = self._builder()
        builder.set_body("test reader body", "text/plain")
        self.assertEqual("test reader body", builder.body)
        self.assertEqual("text/plain", builder.content_type)


if __name__ == '__main__':
    unittest.main()
