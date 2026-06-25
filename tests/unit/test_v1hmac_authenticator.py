import unittest
import urllib.parse
import uuid

from tests.unit.test_factory import PROPERTIES_URI

from onlinepayments.sdk.factory import Factory
from onlinepayments.sdk.authentication.authorization_type import AuthorizationType
from onlinepayments.sdk.authentication.v1hmac_authenticator import V1HmacAuthenticator
from onlinepayments.sdk.communication.request_header import RequestHeader


DATE_HEADER = RequestHeader("Date", "Mon, 07 Jul 2014 12:12:40 GMT")


def _make_configuration(api_key_id="apiKeyId", secret_api_key="secretApiKey"):
    config = Factory.create_configuration(PROPERTIES_URI, str(uuid.uuid4()), str(uuid.uuid4()))
    config.connect_timeout = 1000
    config.socket_timeout = 1000
    config.api_key_id = api_key_id
    config.secret_api_key = secret_api_key
    return config


class V1HmacAuthenticatorTest(unittest.TestCase):

    def setUp(self):
        self.authenticator = V1HmacAuthenticator(_make_configuration())

    def test_ConstructorTests_CommunicatorConfiguration_RaiseValueErrorWhenSecretApiKeyIsNull(self):
        config = _make_configuration()
        config.secret_api_key = None
        with self.assertRaises(ValueError):
            V1HmacAuthenticator(config)

    def test_ConstructorTests_CommunicatorConfiguration_RaiseValueErrorWhenSecretApiKeyIsEmpty(self):
        config = _make_configuration()
        config.secret_api_key = ""
        with self.assertRaises(ValueError):
            V1HmacAuthenticator(config)

    def test_ConstructorTests_CommunicatorConfiguration_RaiseValueErrorWhenApiKeyIdIsNull(self):
        config = _make_configuration()
        config.api_key_id = None
        with self.assertRaises(ValueError):
            V1HmacAuthenticator(config)

    def test_ConstructorTests_CommunicatorConfiguration_RaiseValueErrorWhenApiKeyIdIsEmpty(self):
        config = _make_configuration()
        config.api_key_id = ""
        with self.assertRaises(ValueError):
            V1HmacAuthenticator(config)

    def test_ConstructorTests_CommunicatorConfiguration_RaiseValueErrorWhenAuthorizationTypeIsNull(self):
        config = _make_configuration()
        config.authorization_type = None
        with self.assertRaises(ValueError):
            V1HmacAuthenticator(config)

    def test_ConstructorTests_CommunicatorConfiguration_RaiseValueErrorWhenConnectTimeoutNotPositive(self):
        config = _make_configuration()
        config.connect_timeout = 0
        with self.assertRaises(ValueError):
            V1HmacAuthenticator(config)

    def test_ConstructorTests_CommunicatorConfiguration_RaiseValueErrorWhenSocketTimeoutNotPositive(self):
        config = _make_configuration()
        config.socket_timeout = 0
        with self.assertRaises(ValueError):
            V1HmacAuthenticator(config)

    def test_ConstructorTests_CommunicatorConfiguration_CreateAuthenticatorFromConfiguration(self):
        self.assertIsNotNone(V1HmacAuthenticator(_make_configuration()))

    def test_GettingAuthorization_ValidInput_ContainV1HmacAuthorizationType(self):
        url = urllib.parse.urlparse(
            "http://localhost:8080/v2/1/services%20bla/testconnection?aap=noot&mies=geen%20noot")
        authorization = self.authenticator.get_authorization("POST", url, [DATE_HEADER])
        self.assertIn("v1HMAC", authorization)

    def test_GettingAuthorization_ValidInput_ReturnExpectedAuthorizationHeader_MinimalExample(self):
        authenticator = V1HmacAuthenticator(
            _make_configuration("EC36A74A98D21", "6Kj5HT0MQKC6D8eb7W3lTg71kVKVDSt1"))
        url = urllib.parse.urlparse("http://localhost:8080/v2/1/tokens/2")
        headers = [RequestHeader("Date", "Fri, 06 Jun 2014 13:39:43 GMT")]

        authorization = authenticator.get_authorization("GET", url, headers)

        self.assertEqual(
            "GCS v1HMAC:EC36A74A98D21:vCos01y77soPNJOW6kDCm4Bu5b2darAZ09PP7Wa+jRA=", authorization)

    def test_GettingAuthorization_ValidInput_ReturnExpectedAuthorizationHeader_FullExample(self):
        headers = [
            RequestHeader("Date", "Wed, 01 Jan 2020 11:00:00 GMT"),
            RequestHeader("X-GCS-ClientMetaInfo", "processed header value"),
            RequestHeader("X-GCS-CustomerHeader", "processed header value"),
            RequestHeader("X-GCS-ServerMetaInfo", "processed header value"),
        ]
        url = urllib.parse.urlparse("http://localhost/v2/1/tokens")

        authorization = self.authenticator.get_authorization("DELETE", url, headers)

        self.assertEqual(
            "GCS v1HMAC:apiKeyId:zcDsJLRYsh99pqyCFdrVLyLVi+4A+QLis14rEtV8c98=", authorization)

    def test_GettingAuthorization_InvalidInput_RaiseValueErrorWhenHttpMethodIsNull(self):
        url = urllib.parse.urlparse("http://localhost:8080/v2/1/tokens/2")
        with self.assertRaises(ValueError):
            self.authenticator.get_authorization(None, url, [])

    def test_GettingAuthorization_InvalidInput_RaiseValueErrorWhenHttpMethodIsEmpty(self):
        url = urllib.parse.urlparse("http://localhost:8080/v2/1/tokens/2")
        with self.assertRaises(ValueError):
            self.authenticator.get_authorization("", url, [])

    def test_GettingAuthorization_InvalidInput_RaiseValueErrorWhenHttpMethodIsWhitespace(self):
        url = urllib.parse.urlparse("http://localhost:8080/v2/1/tokens/2")
        with self.assertRaises(ValueError):
            self.authenticator.get_authorization("   ", url, [])

    def test_GettingAuthorization_InvalidInput_RaiseValueErrorWhenResourceUriIsNull(self):
        with self.assertRaises(ValueError):
            self.authenticator.get_authorization("GET", None, [])

    def test_GettingAuthorization_InvalidInput_RaiseValueErrorWhenResourceUriIsNullWithNullHeaders(self):
        with self.assertRaises(ValueError):
            self.authenticator.get_authorization("POST", None, None)

    def test_CanonicalizingHeaderValue_WhitespaceAndNewLines_ReturnNormalizedValue(self):
        self.assertEqual("aap noot", self.authenticator.to_canonicalize_header_value("aap\nnoot  "))
        self.assertEqual("aap noot", self.authenticator.to_canonicalize_header_value(" aap\r\n  noot"))

    def test_CanonicalizingHeaderValue_NullAndEmptyValues_ReturnEmptyStringForNullValue(self):
        self.assertEqual("", self.authenticator.to_canonicalize_header_value(None))

    def test_CanonicalizingHeaderValue_NullAndEmptyValues_ReturnEmptyStringForEmptyValue(self):
        self.assertEqual("", self.authenticator.to_canonicalize_header_value(""))

    def test_CanonicalizingHeaderValue_NullAndEmptyValues_ReturnTrimmedValueForWhitespaceOnly(self):
        self.assertEqual("", self.authenticator.to_canonicalize_header_value("   "))

    def test_CanonicalizingHeaderValue_NullAndEmptyValues_ReturnNormalizedValueWithCarriageReturn(self):
        self.assertEqual("a b c", self.authenticator.to_canonicalize_header_value("a\r\nb\r\nc"))

    def test_CanonicalizingHeaderNamesThroughDataToSign_DefaultScenario_CanonicalizeXGcsHeaderNamesToLowercase(self):
        headers = [
            RequestHeader("X-GCS-ServerMetaInfo", "server-value"),
            RequestHeader("X-GCS-CLIENTMETAINFO", "client-value"),
            RequestHeader("X-GCS-CustomerHeader", "customer-value"),
            DATE_HEADER,
        ]
        url = urllib.parse.urlparse("http://localhost:8080/v2/1/tokens/2")
        data_to_sign = self.authenticator.to_data_to_sign("GET", url, headers)

        self.assertIn("x-gcs-clientmetainfo:client-value\n", data_to_sign)
        self.assertIn("x-gcs-customerheader:customer-value\n", data_to_sign)
        self.assertIn("x-gcs-servermetainfo:server-value\n", data_to_sign)

    def test_CanonicalizingHeaderNamesThroughDataToSign_DefaultScenario_SortCanonicalizedXGcsHeaderNamesAlphabetically(self):
        headers = [
            RequestHeader("X-GCS-ServerMetaInfo", "server-value"),
            RequestHeader("X-GCS-CustomerHeader", "customer-value"),
            RequestHeader("X-GCS-ClientMetaInfo", "client-value"),
            DATE_HEADER,
        ]
        url = urllib.parse.urlparse("http://localhost:8080/v2/1/tokens/2")
        data_to_sign = self.authenticator.to_data_to_sign("GET", url, headers)

        client_index = data_to_sign.index("x-gcs-clientmetainfo:client-value\n")
        customer_index = data_to_sign.index("x-gcs-customerheader:customer-value\n")
        server_index = data_to_sign.index("x-gcs-servermetainfo:server-value\n")
        self.assertTrue(client_index < customer_index)
        self.assertTrue(customer_index < server_index)

    def test_CanonicalizingHeaderNamesThroughDataToSign_DefaultScenario_IgnoreNonXGcsHeadersWhenCreatingCanonicalHeaderBlock(self):
        headers = [
            RequestHeader("User-Agent", "test-agent"),
            RequestHeader("Accept", "application/json"),
            DATE_HEADER,
        ]
        url = urllib.parse.urlparse("http://localhost:8080/v2/1/tokens/2")
        data_to_sign = self.authenticator.to_data_to_sign("GET", url, headers)

        self.assertNotIn("user-agent", data_to_sign)
        self.assertNotIn("accept:application/json", data_to_sign)

    def test_CreatingDataToSign_ValidHeaders_ReturnExpectedCanonicalString(self):
        http_headers = [
            RequestHeader("X-GCS-ServerMetaInfo",
                          "{\"platformIdentifier\":\"Windows 10/10.0.18362 Python/3.8.5 (CPython; MSC v.1916 32 bit (Intel))\","
                          "\"sdkIdentifier\":\"OnlinePaymentsPython3ServerSDK/v1.0.0\"}"),
            RequestHeader("Content-Type", "application/json"),
            RequestHeader("X-GCS-ClientMetaInfo", "{\"aap\",\"noot\"}"),
            RequestHeader("User-Agent", "Apache-HttpClient/4.3.4 (java 1.5)"),
            RequestHeader("Date", "Mon, 07 Jul 2014 12:12:40 GMT"),
        ]
        expected_start = "POST\napplication/json\n"
        expected_end = "x-gcs-clientmetainfo:{\"aap\",\"noot\"}\n" \
                       "x-gcs-servermetainfo:{\"platformIdentifier\":\"Windows 10/10.0.18362 Python/3.8.5 (CPython; MSC v.1916 32 bit (Intel))\"," \
                       "\"sdkIdentifier\":\"OnlinePaymentsPython3ServerSDK/v1.0.0\"}\n" \
                       "/v2/1/products%20bla?aap=noot&mies=geen%20noot\n"

        url = urllib.parse.urlparse("http://localhost:8080/v2/1/products%20bla?aap=noot&mies=geen%20noot")
        data_to_sign = self.authenticator.to_data_to_sign("POST", url, http_headers)

        self.assertEqual(expected_start, data_to_sign[:22])
        self.assertEqual(expected_end, data_to_sign[52:])

    def test_CreatingDataToSign_SpecialCharactersInMerchantId_ReturnCorrectCanonicalPath(self):
        headers = [
            RequestHeader("Content-Type", "application/json"),
            DATE_HEADER,
        ]
        url = urllib.parse.urlparse(
            "http://localhost:8080/v2/spécificCharacterMerchant/testconnection?aap=noot&mies=geen%20noot")
        data_to_sign = self.authenticator.to_data_to_sign("POST", url, headers)

        self.assertIn("/v2/spécificCharacterMerchant/testconnection?aap=noot&mies=geen%20noot\n", data_to_sign)

    def test_CreatingDataToSign_NoXgcsHeaders_ExcludeNonXgcsHeaders(self):
        headers = [
            RequestHeader("Content-Type", "application/json"),
            RequestHeader("User-Agent", "test-agent"),
            DATE_HEADER,
        ]
        url = urllib.parse.urlparse("http://localhost:8080/v2/1/tokens/2")
        data_to_sign = self.authenticator.to_data_to_sign("GET", url, headers)

        self.assertIn("GET\n", data_to_sign)
        self.assertIn("application/json\n", data_to_sign)
        self.assertIn("Mon, 07 Jul 2014 12:12:40 GMT\n", data_to_sign)
        self.assertIn("/v2/1/tokens/2\n", data_to_sign)

    def test_CreatingDataToSign_outContentTypeHeader_AppendEmptyLineForMissingContentType(self):
        headers = [DATE_HEADER]
        url = urllib.parse.urlparse("http://localhost:8080/v2/1/tokens/2")
        data_to_sign = self.authenticator.to_data_to_sign("DELETE", url, headers)

        self.assertTrue(data_to_sign.startswith("DELETE\n\n"))

    def test_CreatingDataToSign_UriWithoutQuery_NotIncludeQueryParamSeparator(self):
        headers = [DATE_HEADER]
        url = urllib.parse.urlparse("http://localhost:8080/v2/1/tokens/2")
        data_to_sign = self.authenticator.to_data_to_sign("GET", url, headers)

        self.assertTrue(data_to_sign.endswith("/v2/1/tokens/2\n"))

    def test_CreatingAuthenticationSignature_ForDeleteRequest_ReturnExpectedSignature(self):
        data_to_sign = "DELETE\n" \
                       "application/json\n" \
                       "Fri, 06 Jun 2014 13:39:43 GMT\n" \
                       "x-gcs-clientmetainfo:processed header value\n" \
                       "x-gcs-customerheader:processed header value\n" \
                       "x-gcs-servermetainfo:processed header value\n" \
                       "/v2/1/tokens/123456789\n"

        signature = self.authenticator.create_authentication_signature(data_to_sign)

        self.assertEqual("qi/6Uo1GVIfvKQYmKoq9amJC/UD1kQX2nZAQwYM+6jQ=", signature)

    def test_CreatingAuthenticationSignature_ForGetRequest_ReturnExpectedSignature(self):
        authenticator = V1HmacAuthenticator(
            _make_configuration(secret_api_key="6Kj5HT0MQKC6D8eb7W3lTg71kVKVDSt1"))
        data_to_sign = "GET\n" \
                       "\n" \
                       "Fri, 06 Jun 2014 13:39:43 GMT\n" \
                       "/v2/1/tokens/123456789\n"

        signature = authenticator.create_authentication_signature(data_to_sign)

        self.assertEqual("miC7b0pEJ9Hx5yc4ouC54UoHwAhuPEdkwAN6NALo+Ow=", signature)

    def test_WorkingWithAuthorizationType_GettingSignatureString_ReturnV1HmacSignatureString(self):
        self.assertEqual("v1HMAC", AuthorizationType.V1HMAC)

    def test_WorkingWithAuthorizationType_ConvertingFromString_ReturnV1HmacForExactMatch(self):
        self.assertEqual("v1HMAC", AuthorizationType.get_authorization("v1HMAC"))

    def test_WorkingWithAuthorizationType_ConvertingFromString_RaiseValueErrorForNullInput(self):
        with self.assertRaises(ValueError):
            AuthorizationType.get_authorization(None)

    def test_WorkingWithAuthorizationType_ConvertingFromString_RaiseValueErrorForInvalidInput(self):
        with self.assertRaises(ValueError):
            AuthorizationType.get_authorization("invalid")

    def test_WorkingWithAuthorizationType_ConvertingFromString_RaiseValueErrorForEmptyString(self):
        with self.assertRaises(ValueError):
            AuthorizationType.get_authorization("")

    def test_WorkingWithAuthorizationType_ConvertingFromString_RaiseValueErrorForUnknownType(self):
        with self.assertRaises(ValueError):
            AuthorizationType.get_authorization("V2HMAC")


if __name__ == '__main__':
    unittest.main()
