import unittest

from onlinepayments.sdk.communication.request_header import RequestHeader, get_header, get_header_value


class RequestHeaderTest(unittest.TestCase):

    def test_ConstructedWithNullName_DefaultScenario_RaiseValueError(self):
        with self.assertRaises(ValueError):
            RequestHeader(None, "value")

    def test_ConstructedWithEmptyName_DefaultScenario_RaiseValueError(self):
        with self.assertRaises(ValueError):
            RequestHeader("", "value")

    def test_ConstructedWithEmptyName_DefaultScenario_RaiseValueErrorWhenNameContainsOnlyWhitespace(self):
        with self.assertRaises(ValueError):
            RequestHeader("   ", "value")

    def test_GettingName_DefaultScenario_ReturnConfiguredName(self):
        header = RequestHeader("Content-Type", "application/json")
        self.assertEqual("Content-Type", header.name)

    def test_GettingValue_DefaultScenario_ReturnConfiguredValue(self):
        header = RequestHeader("Content-Type", "application/json")
        self.assertEqual("application/json", header.value)

    def test_GettingValue_DefaultScenario_ReturnValueWithoutNormalization(self):
        header = RequestHeader("Authorization", "Bearer\ntoken  ")
        self.assertEqual("Bearer\ntoken  ", header.value)

    def test_GettingValue_DefaultScenario_DecodeBytesValueToString(self):
        header = RequestHeader("X-Binary", b"byte-value")
        self.assertEqual("byte-value", header.value)

    def test_ConstructedWithValidParameters_DefaultScenario_CreateHeaderWithValidNameAndValue(self):
        header = RequestHeader("Authorization", "Bearer token123")
        self.assertEqual("Authorization", header.name)
        self.assertEqual("Bearer token123", header.value)

    def test_ConstructedWithValidParameters_DefaultScenario_CreateHeaderWithValidNameAndNullValue(self):
        header = RequestHeader("X-Custom-Header", None)
        self.assertEqual("X-Custom-Header", header.name)
        self.assertIsNone(header.value)

    def test_ConstructedWithValidParameters_DefaultScenario_CreateHeaderWithValidNameAndEmptyValue(self):
        header = RequestHeader("X-Custom-Header", "")
        self.assertEqual("X-Custom-Header", header.name)
        self.assertEqual("", header.value)

    def test_ConvertingToString_DefaultScenario_ReturnFormattedNameAndValue(self):
        header = RequestHeader("Content-Type", "application/json")
        self.assertEqual("Content-Type:application/json", str(header))

    def test_ConvertingToString_DefaultScenario_ReturnFormattedStringWithNullValue(self):
        header = RequestHeader("X-Custom-Header", None)
        self.assertEqual("X-Custom-Header:None", str(header))

    def test_ConvertingToString_DefaultScenario_ReturnFormattedStringWithEmptyValue(self):
        header = RequestHeader("X-Custom-Header", "")
        self.assertEqual("X-Custom-Header:", str(header))

    def test_GettingHeaderFromList_DefaultScenario_ReturnHeaderWithExactCaseMatch(self):
        headers = [
            RequestHeader("Content-Type", "application/json"),
            RequestHeader("Authorization", "Bearer token"),
            RequestHeader("X-Custom-Header", "custom-value"),
        ]
        result = get_header(headers, "Content-Type")
        self.assertEqual("Content-Type", result.name)
        self.assertEqual("application/json", result.value)

    def test_GettingHeaderFromList_DefaultScenario_ReturnHeaderWithCaseInsensitiveMatch(self):
        headers = [
            RequestHeader("Content-Type", "application/json"),
            RequestHeader("Authorization", "Bearer token"),
        ]
        self.assertEqual("Content-Type", get_header(headers, "content-type").name)
        self.assertEqual("Content-Type", get_header(headers, "CONTENT-TYPE").name)
        self.assertEqual("Content-Type", get_header(headers, "CoNtEnT-tYpE").name)

    def test_GettingHeaderFromList_DefaultScenario_ReturnNullWhenHeaderNotFound(self):
        headers = [RequestHeader("Content-Type", "application/json")]
        self.assertIsNone(get_header(headers, "X-Non-Existent"))

    def test_GettingHeaderFromList_DefaultScenario_ReturnFirstMatchWhenMultipleHeadersSameName(self):
        headers = [
            RequestHeader("Set-Cookie", "cookie1=value1"),
            RequestHeader("Set-Cookie", "cookie2=value2"),
        ]
        result = get_header(headers, "Set-Cookie")
        self.assertEqual("Set-Cookie", result.name)
        self.assertEqual("cookie1=value1", result.value)

    def test_GettingHeaderValueFromList_DefaultScenario_ReturnValueForExistingHeader(self):
        headers = [
            RequestHeader("Content-Type", "application/json"),
            RequestHeader("Authorization", "Bearer token"),
        ]
        self.assertEqual("Bearer token", get_header_value(headers, "Authorization"))

    def test_GettingHeaderValueFromList_DefaultScenario_ReturnValueWithCaseInsensitiveMatch(self):
        headers = [RequestHeader("Authorization", "Bearer token")]
        self.assertEqual("Bearer token", get_header_value(headers, "authorization"))
        self.assertEqual("Bearer token", get_header_value(headers, "AUTHORIZATION"))

    def test_GettingHeaderValueFromList_DefaultScenario_ReturnNullWhenHeaderNotFound(self):
        headers = [RequestHeader("Content-Type", "application/json")]
        self.assertIsNone(get_header_value(headers, "X-Non-Existent"))

    def test_GettingHeaderValueFromList_DefaultScenario_ReturnNullValueWhenHeaderValueIsNull(self):
        headers = [RequestHeader("Content-Type", None)]
        self.assertIsNone(get_header_value(headers, "Content-Type"))

    def test_GettingHeaderValueFromList_DefaultScenario_ReturnEmptyStringWhenHeaderValueIsEmpty(self):
        headers = [RequestHeader("Content-Type", "")]
        self.assertEqual("", get_header_value(headers, "Content-Type"))

    def test_GettingHeaderFromList_DefaultScenario_AcceptDictAndNoneHeaders(self):
        headers = {"Content-Type": "application/json"}
        self.assertEqual("Content-Type:application/json", str(get_header(headers, "Content-Type")))
        self.assertEqual("Content-Type:application/json", str(get_header(headers, "content-type")))
        self.assertIsNone(get_header(headers, "X-Non-Existent"))
        self.assertIsNone(get_header(None, "Content-Type"))

    def test_GettingHeaderValueFromList_DefaultScenario_AcceptDictAndNoneHeaders(self):
        headers = {"Content-Type": "application/json"}
        self.assertEqual("application/json", get_header_value(headers, "Content-Type"))
        self.assertEqual("application/json", get_header_value(headers, "content-type"))
        self.assertIsNone(get_header_value(headers, "X-Non-Existent"))
        self.assertIsNone(get_header_value(None, "Content-Type"))


if __name__ == '__main__':
    unittest.main()
