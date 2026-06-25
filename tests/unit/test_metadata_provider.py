import base64
import unittest

from onlinepayments.sdk.communication.metadata_provider import MetadataProvider
from onlinepayments.sdk.communication.request_header import RequestHeader
from onlinepayments.sdk.domain.shopping_cart_extension import ShoppingCartExtension
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller


class MetadataProviderTest(unittest.TestCase):

    def test_GettingServerMetadataHeaders_ShoppingCartExtensionIncludingId_ReturnServerMetaInfoHeader(self):
        shopping_cart_extension = ShoppingCartExtension("OnlinePayments.creator", "Extension", "1.0", "ExtensionId")
        metadata_provider = MetadataProvider("OnlinePayments", shopping_cart_extension)

        request_headers = metadata_provider.metadata_headers
        self.assertEqual(1, len(request_headers))
        self.assertServerMetaInfo(metadata_provider, "OnlinePayments", shopping_cart_extension, request_headers[0])

    def test_GettingServerMetadataHeaders_ShoppingCartExtensionWithoutId_ReturnServerMetaInfoHeader(self):
        shopping_cart_extension = ShoppingCartExtension("OnlinePayments.creator", "Extension", "1.0")
        metadata_provider = MetadataProvider("OnlinePayments", shopping_cart_extension)
        request_headers = metadata_provider.metadata_headers

        self.assertEqual(1, len(request_headers))
        self.assertServerMetaInfo(metadata_provider, "OnlinePayments", shopping_cart_extension, request_headers[0])

    def test_GettingServerMetadataHeaders_WithoutShoppingCartExtension_ReturnServerMetaInfoHeader(self):
        metadata_provider = MetadataProvider("OnlinePayments")
        request_headers = metadata_provider.metadata_headers

        self.assertEqual(1, len(request_headers))
        self.assertServerMetaInfo(metadata_provider, "OnlinePayments", None, request_headers[0])

    def test_GettingServerMetadataHeaders_AdditionalHeaders_ReturnServerMetaInfoAndAdditionalHeaders(self):
        additional_headers = [RequestHeader("Header1", "&=$%"), RequestHeader("Header2", "blah blah"),
                              RequestHeader("Header3", "foo")]
        metadata_provider = MetadataProvider("OnlinePayments", None, additional_headers)
        request_headers = metadata_provider.metadata_headers

        self.assertEqual(len(additional_headers) + 1, len(request_headers))
        self.assertServerMetaInfo(metadata_provider, "OnlinePayments", None, request_headers[0])
        for expected_header, actual_header in zip(additional_headers, request_headers[1:]):
            self.assertEqual(expected_header.name, actual_header.name)
            self.assertEqual(expected_header.value, actual_header.value)

    def test_ConstructedWithAdditionalHeaders_DefaultScenario_RaiseValueErrorWithProhibitedHeader(self):
        for name in MetadataProvider.prohibited_headers:
            additional_headers = [RequestHeader("Header1", "Value1"),
                                  RequestHeader(name, "should be slashed and burnt"),
                                  RequestHeader("Header3", "Value3")]
            with self.assertRaises(ValueError) as error:
                MetadataProvider("OnlinePayments", None, additional_headers)
            self.assertIn(name, str(error.exception))

    def test_Constructed_DefaultScenario_RaiseValueErrorWhenIntegratorIsNone(self):
        with self.assertRaises(ValueError):
            MetadataProvider(None)

    def test_Constructed_DefaultScenario_RaiseValueErrorWhenIntegratorIsEmpty(self):
        with self.assertRaises(ValueError):
            MetadataProvider("")

    def test_Constructed_DefaultScenario_RaiseValueErrorWhenIntegratorIsWhitespace(self):
        with self.assertRaises(ValueError):
            MetadataProvider("   ")

    def assertServerMetaInfo(self, metadata_provider, integrator, shopping_cart_extension=None, request_header=None):
        self.assertEqual("X-GCS-ServerMetaInfo", request_header.name)
        self.assertIsNotNone(request_header.value)

        server_meta_info_json = base64.b64decode(request_header.value).decode('utf-8')
        server_meta_info = DefaultMarshaller.instance().unmarshal(server_meta_info_json, MetadataProvider.ServerMetaInfo)
        self.assertEqual(metadata_provider._platform_identifier, server_meta_info.platform_identifier)
        self.assertEqual(metadata_provider._sdk_identifier, server_meta_info.sdk_identifier)
        self.assertEqual("OnlinePayments", server_meta_info.sdk_creator)
        self.assertEqual(integrator, server_meta_info.integrator)
        if shopping_cart_extension is None:
            self.assertIsNone(server_meta_info.shopping_cart_extension)
        else:
            self.assertEqual(shopping_cart_extension.creator, server_meta_info.shopping_cart_extension.creator)
            self.assertEqual(shopping_cart_extension.name, server_meta_info.shopping_cart_extension.name)
            self.assertEqual(shopping_cart_extension.version, server_meta_info.shopping_cart_extension.version)
            self.assertEqual(shopping_cart_extension.extension_id, server_meta_info.shopping_cart_extension.extension_id)


if __name__ == '__main__':
    unittest.main()
