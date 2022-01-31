import unittest
import urllib.parse

from onlinepayments.sdk.defaultimpl.authorization_type import AuthorizationType
from onlinepayments.sdk.defaultimpl.default_authenticator import DefaultAuthenticator
from onlinepayments.sdk.request_header import RequestHeader


class DefaultAuthenticatorTest(unittest.TestCase):
    """Tests that the DefaultAuthenticator is capable of converting a set of request headers to a POST request
    and that it is capable of providing the correct signature"""

    def test_canonicalized_header_value(self):
        """Tests that the to_canonicalize_header function correctly removes control characters and excessive whitespace
        """
        authenticator = DefaultAuthenticator("apiKeyId", "secretApiKey", AuthorizationType.get_authorization("v1HMAC"))

        self.assertEqual("aap noot", authenticator.to_canonicalize_header_value("aap\nnoot  "))
        self.assertEqual("aap noot", authenticator.to_canonicalize_header_value(" aap\r\n  noot"))

    def test_create_authentication_signature_for_post(self):
        # TODO change meta info to something more sensible/python-like
        """Tests that the to_data_to_sign function correctly constructs a POST request for multiple headers"""
        authenticator = DefaultAuthenticator("apiKeyId", "secretApiKey", AuthorizationType.V1HMAC)
        http_headers = [RequestHeader("X-GCS-ServerMetaInfo",
                                      "{\"platformIdentifier\":\"Windows 10/10.0.18362 Python/3.8.5 (CPython; MSC v.1916 32 bit (Intel))\","
                                      "\"sdkIdentifier\":\"OnlinePaymentsPython3ServerSDK/v1.0.0\"}"),
                        RequestHeader("Content-Type", "application/json"),
                        RequestHeader("X-GCS-ClientMetaInfo", "{\"aap\",\"noot\"}"),
                        RequestHeader("User-Agent", "Apache-HttpClient/4.3.4 (java 1.5)"),
                        RequestHeader("Date", "Mon, 07 Jul 2014 12:12:40 GMT")]
        expected_start = "POST\n" \
                         "application/json\n"
        expected_end = "x-gcs-clientmetainfo:{\"aap\",\"noot\"}\n" \
                       "x-gcs-servermetainfo:{\"platformIdentifier\":\"Windows 10/10.0.18362 Python/3.8.5 (CPython; MSC v.1916 32 bit (Intel))\"," \
                       "\"sdkIdentifier\":\"OnlinePaymentsPython3ServerSDK/v1.0.0\"}\n" \
                       "/v2/1/products%20bla?aap=noot&mies=geen%20noot\n"

        url = urllib.parse.urlparse("http://localhost:8080/v2/1/products%20bla?aap=noot&mies=geen%20noot")
        data_to_sign = authenticator.to_data_to_sign("POST", url, http_headers)

        actual_start = data_to_sign[:22]
        actual_end = data_to_sign[52:]
        self.assertEqual(expected_start, actual_start)
        self.assertEqual(expected_end, actual_end)

    def test_create_authentication_signature_for_delete(self):
        """Tests if the default authenticator creates the correct signature"""
        authenticator = DefaultAuthenticator("apiKeyId", "secretApiKey")
        data_to_sign = "DELETE\n" \
                       "application/json\n" \
                       "Fri, 06 Jun 2014 13:39:43 GMT\n" \
                       "x-gcs-clientmetainfo:processed header value\n" \
                       "x-gcs-customerheader:processed header value\n" \
                       "x-gcs-servermetainfo:processed header value\n" \
                       "/v2/1/tokens/123456789\n"

        authentication_signature = authenticator.create_authentication_signature(data_to_sign)

        self.assertEqual("qi/6Uo1GVIfvKQYmKoq9amJC/UD1kQX2nZAQwYM+6jQ=", authentication_signature)

    def test_create_authentication_signature_for_get(self):
        """Tests if the default authenticator creates the correct signature"""
        authenticator = DefaultAuthenticator("apiKeyId", "6Kj5HT0MQKC6D8eb7W3lTg71kVKVDSt1")
        data_to_sign = "GET\n" \
                       "\n" \
                       "Fri, 06 Jun 2014 13:39:43 GMT\n" \
                       "/v2/1/tokens/123456789\n"

        authentication_signature = authenticator.create_authentication_signature(data_to_sign)
        self.assertEqual("miC7b0pEJ9Hx5yc4ouC54UoHwAhuPEdkwAN6NALo+Ow=", authentication_signature)

    def test_create_simple_authentication_signature(self):
        """Tests if the default authenticator creates the correct signature (with an authorization type with different casing)."""
        authenticator = DefaultAuthenticator("apiKeyId", "secretApiKey", "v1hmac")
        headers = [
            RequestHeader("Date", "Wed, 01 Jan 2020 11:00:00 GMT"),
            RequestHeader("X-GCS-ClientMetaInfo", "processed header value"),
            RequestHeader("X-GCS-CustomerHeader", "processed header value"),
            RequestHeader("X-GCS-ServerMetaInfo", "processed header value")
        ]
        url = urllib.parse.urlparse("http://localhost/v2/1/tokens")

        authentication_signature = authenticator.create_simple_authentication_signature("DELETE", url, headers)

        self.assertEqual("GCS v1HMAC:apiKeyId:zcDsJLRYsh99pqyCFdrVLyLVi+4A+QLis14rEtV8c98=", authentication_signature)

    def test_reject_unknown_authorization_type(self):
        """Tests if the default authenticator throws an exception if an invalid authorization type is provided."""
        self.assertRaises(RuntimeError, DefaultAuthenticator, "apiKeyId", "secretApiKey", "invalidAuthorizationType")


if __name__ == '__main__':
    unittest.main()
