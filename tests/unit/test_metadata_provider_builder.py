import unittest

from onlinepayments.sdk.communication.metadata_provider import MetadataProvider
from onlinepayments.sdk.communication.request_header import RequestHeader

SERVER_META_INFO_HEADER = "X-GCS-ServerMetaInfo"
NON_PROHIBITED_HEADERS = ["Dummy", "Accept", "If-None-Match", "If-Modified-Since"]


class MetadataProviderBuilderTest(unittest.TestCase):

    def test_WithAdditionalRequestHeaderIsCalled_DefaultScenario_ThrowIllegalArgumentExceptionWithProhibitedHeader(self):
        for name in MetadataProvider.prohibited_headers:
            with self.subTest(header=name):
                with self.assertRaises(ValueError) as context:
                    MetadataProvider("OnlinePayments", additional_request_headers=[
                        RequestHeader(name, "some-value")
                    ])
                self.assertIn(name, str(context.exception))

    def test_WithAdditionalRequestHeaderIsCalled_DefaultScenario_AddHeaderToMetadataProviderWithNonProhibitedHeader(self):
        for name in NON_PROHIBITED_HEADERS:
            with self.subTest(header=name):
                additional_header = RequestHeader(name, "value-" + name)

                provider = MetadataProvider("OnlinePayments", additional_request_headers=[additional_header])

                headers = provider.metadata_headers
                self.assertEqual(2, len(headers))
                self.assertEqual(SERVER_META_INFO_HEADER, headers[0].name)
                self.assertEqual(additional_header.name, headers[1].name)
                self.assertEqual(additional_header.value, headers[1].value)

    def test_WithAdditionalRequestHeaderIsCalled_DefaultScenario_AddMultipleNonProhibitedHeaders(self):
        first_header = RequestHeader("Dummy", "first-value")
        second_header = RequestHeader("Accept", "second-value")

        provider = MetadataProvider("OnlinePayments", additional_request_headers=[first_header, second_header])

        headers = provider.metadata_headers
        self.assertEqual(3, len(headers))
        self.assertEqual(SERVER_META_INFO_HEADER, headers[0].name)
        self.assertEqual(first_header.name, headers[1].name)
        self.assertEqual(first_header.value, headers[1].value)
        self.assertEqual(second_header.name, headers[2].name)
        self.assertEqual(second_header.value, headers[2].value)

    def test_WithAdditionalRequestHeaderIsCalledWithNull_DefaultScenario_ThrowAttributeError(self):
        with self.assertRaises(AttributeError):
            MetadataProvider("OnlinePayments", additional_request_headers=[None])

    def test_WithAdditionalRequestHeaderIsCalled_DefaultScenario_NormalizeWhitespaceInHeaderValue(self):
        additional_header = RequestHeader("X-Custom", "value\n  with\n  newline")
        provider = MetadataProvider("OnlinePayments", additional_request_headers=[additional_header])

        values = {h.name: h.value for h in provider.metadata_headers}
        self.assertEqual("value with newline", values["X-Custom"])


if __name__ == '__main__':
    unittest.main()
