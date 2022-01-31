import unittest

from onlinepayments.sdk.response_header import get_header, get_header_value


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


if __name__ == '__main__':
    unittest.main()
