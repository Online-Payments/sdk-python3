import unittest

from onlinepayments.sdk.communication.request_param import RequestParam


class RequestParamTest(unittest.TestCase):

    def test_ConstructedWithInvalidName_DefaultScenario_ThrowExceptionWhenNameIsNull(self):
        with self.assertRaises(ValueError) as ctx:
            RequestParam(None, "value")
        self.assertEqual("name is required", str(ctx.exception))

    def test_ConstructedWithInvalidName_DefaultScenario_ThrowExceptionWhenNameIsEmpty(self):
        with self.assertRaises(ValueError) as ctx:
            RequestParam("", "value")
        self.assertEqual("name is required", str(ctx.exception))

    def test_ConstructedWithInvalidName_DefaultScenario_ThrowExceptionWhenNameIsWhitespace(self):
        with self.assertRaises(ValueError) as ctx:
            RequestParam("   ", "value")
        self.assertEqual("name is required", str(ctx.exception))

    def test_ConstructedWithValidParameters_DefaultScenario_CreateParamWithValidNameAndValue(self):
        param = RequestParam("userId", "12345")
        self.assertEqual("userId", param.name)
        self.assertEqual("12345", param.value)

    def test_ConstructedWithValidParameters_DefaultScenario_CreateParamWithValidNameAndNullValue(self):
        param = RequestParam("pageSize", None)
        self.assertEqual("pageSize", param.name)
        self.assertIsNone(param.value)

    def test_ConstructedWithValidParameters_DefaultScenario_CreateParamWithValidNameAndEmptyValue(self):
        param = RequestParam("filter", "")
        self.assertEqual("filter", param.name)
        self.assertEqual("", param.value)

    def test_GettingName_DefaultScenario_ReturnConfiguredName(self):
        param = RequestParam("sortOrder", "DESC")
        self.assertEqual("sortOrder", param.name)

    def test_GettingValue_DefaultScenario_ReturnConfiguredValue(self):
        param = RequestParam("limit", "100")
        self.assertEqual("100", param.value)

    def test_GettingValue_DefaultScenario_ReturnNullValue(self):
        param = RequestParam("offset", None)
        self.assertIsNone(param.value)

    def test_GettingValue_DefaultScenario_ReturnEmptyValue(self):
        param = RequestParam("search", "")
        self.assertEqual("", param.value)

    def test_ConvertingToString_DefaultScenario_ReturnFormattedNameAndValue(self):
        param = RequestParam("key", "value")
        self.assertEqual("key:value", str(param))

    def test_ConvertingToString_DefaultScenario_ReturnFormattedStringWithNullValue(self):
        param = RequestParam("param", None)
        self.assertEqual("param:None", str(param))

    def test_ConvertingToString_DefaultScenario_ReturnFormattedStringWithEmptyValue(self):
        param = RequestParam("param", "")
        self.assertEqual("param:", str(param))


if __name__ == '__main__':
    unittest.main()
