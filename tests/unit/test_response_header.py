import unittest

from onlinepayments.sdk.communication.response_header import get_header, get_header_value, get_disposition_filename


class ResponseHeaderTest(unittest.TestCase):

    def test_GettingHeaderFromList_DefaultScenario_ReturnHeaderWithExactCaseMatch(self):
        headers = {"Content-Type": "application/json", "Authorization": "Bearer token"}
        self.assertEqual(("Content-Type", "application/json"), get_header(headers, "Content-Type"))

    def test_GettingHeaderFromList_DefaultScenario_ReturnHeaderWithCaseInsensitiveMatch(self):
        headers = {"Content-Type": "application/json"}
        self.assertEqual(("Content-Type", "application/json"), get_header(headers, "content-type"))
        self.assertEqual(("Content-Type", "application/json"), get_header(headers, "CONTENT-TYPE"))
        self.assertEqual(("Content-Type", "application/json"), get_header(headers, "CoNtEnT-tYpE"))

    def test_GettingHeaderFromList_DefaultScenario_ReturnNullWhenHeaderNotFound(self):
        headers = {"Content-Type": "application/json"}
        self.assertIsNone(get_header(headers, "X-Non-Existent"))

    def test_GettingHeaderFromList_DefaultScenario_ReturnNullWhenHeadersIsNone(self):
        self.assertIsNone(get_header(None, "Content-Type"))

    def test_GettingHeaderValueFromList_DefaultScenario_ReturnValueForExistingHeader(self):
        headers = {"Content-Type": "application/json", "Authorization": "Bearer token"}
        self.assertEqual("Bearer token", get_header_value(headers, "Authorization"))

    def test_GettingHeaderValueFromList_DefaultScenario_ReturnValueWithCaseInsensitiveMatch(self):
        headers = {"Authorization": "Bearer token"}
        self.assertEqual("Bearer token", get_header_value(headers, "authorization"))
        self.assertEqual("Bearer token", get_header_value(headers, "AUTHORIZATION"))

    def test_GettingHeaderValueFromList_DefaultScenario_ReturnNullWhenHeaderNotFound(self):
        headers = {"Content-Type": "application/json"}
        self.assertIsNone(get_header_value(headers, "X-Non-Existent"))

    def test_GettingHeaderValueFromList_DefaultScenario_ReturnNullWhenHeadersIsNone(self):
        self.assertIsNone(get_header_value(None, "Content-Type"))

    def test_GettingDispositionFilenameFromVariousContentDispositionValues_DefaultScenario_ReturnExpectedFilename(self):
        test_data = {
            "attachment; filename=testfile": "testfile",
            "attachment; filename=\"testfile\"": "testfile",
            "attachment; filename=\"testfile": "\"testfile",
            "attachment; filename=testfile\"": "testfile\"",
            "attachment; filename='testfile'": "testfile",
            "attachment; filename='testfile": "'testfile",
            "attachment; filename=testfile'": "testfile'",
            "filename=testfile": "testfile",
            "filename=\"testfile\"": "testfile",
            "filename=\"testfile": "\"testfile",
            "filename=testfile\"": "testfile\"",
            "filename='testfile'": "testfile",
            "filename='testfile": "'testfile",
            "filename=testfile'": "testfile'",
            "attachment; filename=testfile; x=y": "testfile",
            "attachment; filename=\"testfile\"; x=y": "testfile",
            "attachment; filename=\"testfile; x=y": "\"testfile",
            "attachment; filename=testfile\"; x=y": "testfile\"",
            "attachment; filename='testfile'; x=y": "testfile",
            "attachment; filename='testfile; x=y": "'testfile",
            "attachment; filename=testfile'; x=y": "testfile'",
            "attachment": None,
            "filename=\"": "\"",
            "filename='": "'",
        }
        for value, expected in test_data.items():
            self.assertEqual(expected, get_disposition_filename({"Content-Disposition": value}))

    def test_GettingDispositionFilename_DefaultScenario_ReturnNullWhenHeaderAbsent(self):
        self.assertIsNone(get_disposition_filename({"Content-Type": "application/json"}))
        self.assertIsNone(get_disposition_filename(None))


if __name__ == '__main__':
    unittest.main()
