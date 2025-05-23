import unittest

from onlinepayments.sdk.communication.response_header import get_header, get_header_value, get_disposition_filename


class ResponseHeaderTest(unittest.TestCase):

    def test_get_header_value(self):
        """Tests get_header_value"""
        headers = {"Content-Type": "application/json"}
        self.assertEqual("application/json", get_header_value(headers, "Content-Type"))
        self.assertEqual("application/json", get_header_value(headers, "content-type"))
        self.assertIsNone(get_header_value(headers, "Content-Length"))

    def test_get_header(self):
        """Tests get_header_value"""
        headers = {"Content-Type": "application/json"}
        self.assertEqual(("Content-Type", "application/json"), get_header(headers, "Content-Type"))
        self.assertEqual(("Content-Type", "application/json"), get_header(headers, "content-type"))
        self.assertIsNone(get_header(headers, "Content-Length"))

    def test_get_disposition_filename(self):
        """Tests that get_disposition_filename works as expected"""
        test_data = {"attachment; filename=testfile": "testfile",
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
                     "filename='": "'"}

        for value, expected in test_data.items():
            headers = {"Content-Disposition": value}
            self.assertEqual(expected, get_disposition_filename(headers))


if __name__ == '__main__':
    unittest.main()
