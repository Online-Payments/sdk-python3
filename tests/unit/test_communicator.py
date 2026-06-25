import unittest
from datetime import datetime, timezone
from urllib.parse import urlparse
from unittest.mock import MagicMock, PropertyMock

from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.communicator import Communicator
from onlinepayments.sdk.authentication.authenticator import Authenticator
from onlinepayments.sdk.communication.communication_exception import CommunicationException
from onlinepayments.sdk.communication.connection import Connection
from onlinepayments.sdk.communication.i_metadata_provider import IMetadataProvider
from onlinepayments.sdk.communication.not_found_exception import NotFoundException
from onlinepayments.sdk.communication.request_header import RequestHeader
from onlinepayments.sdk.communication.request_param import RequestParam
from onlinepayments.sdk.communication.response_exception import ResponseException
from onlinepayments.sdk.json.marshaller import Marshaller


class CommunicatorTest(unittest.TestCase):

    BASE_URI = "https://payment.preprod.online-payments.com"
    RELATIVE_PATH = "v1/merchant/20000/convertamount"
    ABSOLUTE_URI = "https://payment.preprod.online-payments.com/v1/merchant/20000/convertamount"

    def setUp(self):
        self.connection = MagicMock(spec=Connection)
        self.authenticator = MagicMock(spec=Authenticator)
        self.metadata_provider = MagicMock(spec=IMetadataProvider)
        self.marshaller = MagicMock(spec=Marshaller)

        type(self.metadata_provider).metadata_headers = PropertyMock(
            return_value=[RequestHeader("X-GCS-ServerMetaInfo", "server-meta")]
        )
        self.authenticator.get_authorization.return_value = "dummy-authorization"

    def _create_communicator(self):
        return Communicator(
            api_endpoint=urlparse(self.BASE_URI),
            connection=self.connection,
            authenticator=self.authenticator,
            metadata_provider=self.metadata_provider,
            marshaller=self.marshaller,
        )

    @staticmethod
    def _json_headers():
        return {"Content-Type": "application/json"}

    @staticmethod
    def _html_headers():
        return {"Content-Type": "text/html"}

    @staticmethod
    def _json_body_chunks(body: str):
        return [body.encode("utf-8")]

    @staticmethod
    def _idempotence_response_headers(response_datetime: datetime):
        return {
            "Content-Type": "application/json",
            "X-GCS-Idempotence-Request-Timestamp": "123456789",
            "IdempotencyResponseDatetime": response_datetime.isoformat(),
        }

    def test_ConvertingToAbsoluteUri_outRequestParams_ReturnExpectedAbsoluteUri(self):
        communicator = self._create_communicator()
        first_uri = communicator._to_absolute_uri("v1/merchant/20000/convertamount", [])
        second_uri = communicator._to_absolute_uri("/v1/merchant/20000/convertamount", [])

        self.assertEqual("https://payment.preprod.online-payments.com/v1/merchant/20000/convertamount",
                         first_uri.geturl())
        self.assertEqual("https://payment.preprod.online-payments.com/v1/merchant/20000/convertamount",
                         second_uri.geturl())

    def test_ConvertingToAbsoluteUri_RequestParams_ReturnExpectedAbsoluteUriWithEncodedQuery(self):
        request_params = [RequestParam("amount", "123"), RequestParam("source", "USD"),
                         RequestParam("target", "EUR"), RequestParam("dummy", "é&%=")]
        communicator = self._create_communicator()
        first_uri = communicator._to_absolute_uri("v1/merchant/20000/convertamount", request_params)
        second_uri = communicator._to_absolute_uri("/v1/merchant/20000/convertamount", request_params)

        self.assertEqual("https://payment.preprod.online-payments.com/v1/merchant/20000/convertamount"
                         "?amount=123&source=USD&target=EUR&dummy=%C3%A9%26%25%3D", first_uri.geturl())
        self.assertEqual("https://payment.preprod.online-payments.com/v1/merchant/20000/convertamount"
                         "?amount=123&source=USD&target=EUR&dummy=%C3%A9%26%25%3D", second_uri.geturl())

    def test_ExecutingApiRequests_Getting_ReturnUnmarshalledResponseWhenJsonResponseIsValid(self):
        communicator = self._create_communicator()
        expected_response = object()

        self.connection.get.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        self.marshaller.unmarshal.return_value = expected_response

        response = communicator.get(self.RELATIVE_PATH, None, None, object, None)
        self.assertIs(expected_response, response)

        actual_uri = self.connection.get.call_args[0][0]
        self.assertEqual(self.ABSOLUTE_URI, actual_uri.geturl())

    def test_ExecutingApiRequests_Getting_ReturnHeadersAndChunksWhenUsingBinaryResponse(self):
        communicator = self._create_communicator()
        self.connection.get.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))

        result_headers, result_chunks = communicator.get_with_binary_response(self.RELATIVE_PATH, None,
                                                                              None, None)
        actual_uri = self.connection.get.call_args[0][0]
        self.assertEqual(self.ABSOLUTE_URI, actual_uri.geturl())

        body = b"".join(result_chunks).decode("utf-8")
        self.assertGreater(len(body), 0)

    def test_ExecutingApiRequests_Getting_ThrowNotFoundExceptionWithInvalidPathMessageWhenPathIsInvalid(self):
        communicator = self._create_communicator()
        self.connection.get.return_value = (404, self._html_headers(), self._json_body_chunks("Not found"))

        with self.assertRaises(NotFoundException) as ctx:
            communicator.get("does/not/exist", None, None, object, None)
        self.assertIn("invalid path: does/not/exist", str(ctx.exception))

        actual_uri = self.connection.get.call_args[0][0]
        self.assertEqual("https://payment.preprod.online-payments.com/does/not/exist", actual_uri.geturl())

    def test_ExecutingApiRequests_Getting_ThrowCommunicationExceptionWhenGetReturnsNonJsonErrorResponse(self):
        communicator = self._create_communicator()
        self.connection.get.return_value = (500, self._html_headers(), self._json_body_chunks("server error"))

        with self.assertRaises(CommunicationException):
            communicator.get("some/path", None, None, object, None)

    def test_ExecutingApiRequests_Posting_ReturnUnmarshalledResponseWhenJsonRequestAndResponseAreValid(self):
        communicator = self._create_communicator()
        request_body = object()
        expected_response = object()
        self.marshaller.marshal.return_value = '{"request":"body"}'
        self.connection.post.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        self.marshaller.unmarshal.return_value = expected_response
        response = communicator.post(self.RELATIVE_PATH, None, None, request_body,
                                     object, None)

        self.assertIs(expected_response, response)
        actual_uri = self.connection.post.call_args[0][0]
        self.assertEqual(self.ABSOLUTE_URI, actual_uri.geturl())
        actual_body = self.connection.post.call_args[0][2]
        self.assertEqual('{"request":"body"}', actual_body)

    def test_ExecutingApiRequests_Posting_ReturnHeadersAndChunksWhenUsingBinaryResponse(self):
        communicator = self._create_communicator()
        request_body = object()
        self.marshaller.marshal.return_value = '{"request":"body"}'
        self.connection.post.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        result_headers, result_chunks = communicator.post_with_binary_response(
            self.RELATIVE_PATH, None, None, request_body, None
        )

        actual_uri = self.connection.post.call_args[0][0]
        self.assertEqual(self.ABSOLUTE_URI, actual_uri.geturl())

        body = b"".join(result_chunks).decode("utf-8")
        self.assertGreater(len(body), 0)

    def test_ExecutingApiRequests_Posting_SendNullBodyWhenRequestBodyIsNull(self):
        communicator = self._create_communicator()
        expected_response = object()
        self.connection.post.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        self.marshaller.unmarshal.return_value = expected_response

        response = communicator.post(self.RELATIVE_PATH, None, None, None,
                                     object, None)
        self.assertIs(expected_response, response)
        self.marshaller.marshal.assert_not_called()

        actual_body = self.connection.post.call_args[0][2]
        self.assertIsNone(actual_body)

    def test_ExecutingApiRequests_Posting_ThrowResponseExceptionWhenPostReturnsJsonErrorResponse(self):
        communicator = self._create_communicator()
        request_body = object()
        self.marshaller.marshal.return_value = '{"request":"body"}'
        self.connection.post.return_value = (
            400,
            self._json_headers(),
            self._json_body_chunks('{"error":"bad request"}'),
        )

        with self.assertRaises(ResponseException) as ctx:
            communicator.post(self.RELATIVE_PATH, None, None, request_body,
                              object, None)
        self.assertEqual(400, ctx.exception.status_code)

    def test_ExecutingApiRequests_Posting_ThrowCommunicationExceptionWhenPostReturnsNonJsonErrorResponse(self):
        communicator = self._create_communicator()
        request_body = object()
        self.marshaller.marshal.return_value = '{"request":"body"}'
        self.connection.post.return_value = (500, self._html_headers(), self._json_body_chunks("server error"))

        with self.assertRaises(CommunicationException):
            communicator.post(self.RELATIVE_PATH, None, None, request_body,
                              object, None)

    def test_ExecutingApiRequests_Putting_ReturnUnmarshalledResponseWhenJsonRequestAndResponseAreValid(self):
        communicator = self._create_communicator()
        request_body = object()
        expected_response = object()
        self.marshaller.marshal.return_value = '{"request":"body"}'
        self.connection.put.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        self.marshaller.unmarshal.return_value = expected_response

        response = communicator.put(self.RELATIVE_PATH, None, None, request_body,
                                    object, None)
        self.assertIs(expected_response, response)

        actual_uri = self.connection.put.call_args[0][0]
        self.assertEqual(self.ABSOLUTE_URI, actual_uri.geturl())

        actual_body = self.connection.put.call_args[0][2]
        self.assertEqual('{"request":"body"}', actual_body)

    def test_ExecutingApiRequests_Putting_ReturnHeadersAndChunksWhenUsingBinaryResponse(self):
        communicator = self._create_communicator()
        request_body = object()
        self.marshaller.marshal.return_value = '{"request":"body"}'
        self.connection.put.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        result_headers, result_chunks = communicator.put_with_binary_response(
            self.RELATIVE_PATH, None, None, request_body, None
        )

        actual_uri = self.connection.put.call_args[0][0]
        self.assertEqual(self.ABSOLUTE_URI, actual_uri.geturl())

        body = b"".join(result_chunks).decode("utf-8")
        self.assertGreater(len(body), 0)

    def test_ExecutingApiRequests_Putting_SendNullBodyWhenRequestBodyIsNull(self):
        communicator = self._create_communicator()
        expected_response = object()
        self.connection.put.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        self.marshaller.unmarshal.return_value = expected_response
        response = communicator.put(self.RELATIVE_PATH, None, None,
                                    None, object, None)

        self.assertIs(expected_response, response)
        self.marshaller.marshal.assert_not_called()

        actual_body = self.connection.put.call_args[0][2]
        self.assertIsNone(actual_body)

    def test_ExecutingApiRequests_Putting_ThrowResponseExceptionWhenPutReturnsJsonErrorResponse(self):
        communicator = self._create_communicator()
        request_body = object()
        self.marshaller.marshal.return_value = '{"request":"body"}'
        self.connection.put.return_value = (
            400,
            self._json_headers(),
            self._json_body_chunks('{"error":"bad request"}'),
        )

        with self.assertRaises(ResponseException) as ctx:
            communicator.put(self.RELATIVE_PATH, None, None, request_body,
                             object, None)
        self.assertEqual(400, ctx.exception.status_code)

    def test_ExecutingApiRequests_Putting_ThrowCommunicationExceptionWhenPutReturnsNonJsonErrorResponse(self):
        communicator = self._create_communicator()
        request_body = object()
        self.marshaller.marshal.return_value = '{"request":"body"}'
        self.connection.put.return_value = (500, self._html_headers(), self._json_body_chunks("server error"))

        with self.assertRaises(CommunicationException):
            communicator.put(self.RELATIVE_PATH, None, None, request_body,
                             object, None)

    def test_ExecutingApiRequests_Deleting_ReturnUnmarshalledResponseWhenJsonResponseIsValid(self):
        communicator = self._create_communicator()
        expected_response = object()
        self.connection.delete.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        self.marshaller.unmarshal.return_value = expected_response

        response = communicator.delete(self.RELATIVE_PATH, None, None, object, None)
        self.assertIs(expected_response, response)

        actual_uri = self.connection.delete.call_args[0][0]
        self.assertEqual(self.ABSOLUTE_URI, actual_uri.geturl())

    def test_ExecutingApiRequests_Deleting_ReturnHeadersAndChunksWhenUsingBinaryResponse(self):
        communicator = self._create_communicator()
        self.connection.delete.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        result_headers, result_chunks = communicator.delete_with_binary_response(
            self.RELATIVE_PATH, None, None, None
        )

        actual_uri = self.connection.delete.call_args[0][0]
        self.assertEqual(self.ABSOLUTE_URI, actual_uri.geturl())

        body = b"".join(result_chunks).decode("utf-8")
        self.assertGreater(len(body), 0)

    def test_ExecutingApiRequests_Deleting_ThrowResponseExceptionWhenDeleteReturnsJsonErrorResponse(self):
        communicator = self._create_communicator()
        self.connection.delete.return_value = (
            400,
            self._json_headers(),
            self._json_body_chunks('{"error":"bad request"}'),
        )

        with self.assertRaises(ResponseException) as ctx:
            communicator.delete(self.RELATIVE_PATH, None, None, object, None)
        self.assertEqual(400, ctx.exception.status_code)

    def test_ExecutingApiRequests_Deleting_ThrowCommunicationExceptionWhenDeleteReturnsNonJsonErrorResponse(self):
        communicator = self._create_communicator()

        self.connection.delete.return_value = (500, self._html_headers(), self._json_body_chunks("server error"))

        with self.assertRaises(CommunicationException):
            communicator.delete(self.RELATIVE_PATH, None, None, object, None)

    def test_UsingIdempotence_Getting_AddIdempotenceHeaderAndOmitItWithoutContextWhenGettingWithIdempotenceKey(self):
        communicator = self._create_communicator()
        context_with_key = CallContext(idempotence_key="test-idempotence-key")
        self.connection.get.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        self.marshaller.unmarshal.return_value = object()
        communicator.get(self.RELATIVE_PATH, None, None, object, context_with_key)
        headers_with_key = self.connection.get.call_args[0][1]

        self.assertTrue(
            any(h.name == "X-GCS-Idempotence-Key" and h.value == "test-idempotence-key"
                for h in headers_with_key)
        )

        self.connection.get.reset_mock()
        self.connection.get.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        communicator.get(self.RELATIVE_PATH, None, None, object, None)
        headers_without_key = self.connection.get.call_args[0][1]

        self.assertFalse(
            any(h.name == "X-GCS-Idempotence-Key" for h in headers_without_key)
        )

    def test_UsingIdempotence_Getting_PopulateIdempotenceFieldsFromResponseHeadersWhenGettingWithCallContext(self):
        communicator = self._create_communicator()
        context = CallContext(idempotence_key="test-idempotence-key")
        response_datetime = datetime(2026, 4, 2, 10, 15, 30, tzinfo=timezone.utc)
        self.connection.get.return_value = (
            200,
            self._idempotence_response_headers(response_datetime),
            self._json_body_chunks('{"result":"OK"}'),
        )
        self.marshaller.unmarshal.return_value = object()
        response = communicator.get(self.RELATIVE_PATH, None, None, object, context)

        self.assertIsNotNone(response)
        self.assertEqual("test-idempotence-key", context.idempotence_key)
        self.assertEqual(123456789, context.idempotence_request_timestamp)
        self.assertEqual(response_datetime, context.idempotence_response_date_time)

    def test_UsingIdempotence_Posting_AddIdempotenceHeaderAndOmitItWithoutContextWhenPostingWithIdempotenceKey(self):
        communicator = self._create_communicator()
        request_body = object()
        context_with_key = CallContext(idempotence_key="test-idempotence-key")
        self.marshaller.marshal.return_value = '{"request":"body"}'
        self.connection.post.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        self.marshaller.unmarshal.return_value = object()
        communicator.post(self.RELATIVE_PATH, None, None, request_body,
                          object, context_with_key)
        headers_with_key = self.connection.post.call_args[0][1]

        self.assertTrue(
            any(h.name == "X-GCS-Idempotence-Key" and h.value == "test-idempotence-key"
                for h in headers_with_key)
        )

        self.connection.post.reset_mock()
        self.marshaller.marshal.return_value = '{"request":"body"}'
        self.connection.post.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        self.marshaller.unmarshal.return_value = object()

        communicator.post(self.RELATIVE_PATH, None, None, request_body, object, None)
        headers_without_key = self.connection.post.call_args[0][1]

        self.assertFalse(
            any(h.name == "X-GCS-Idempotence-Key" for h in headers_without_key)
        )

    def test_UsingIdempotence_Posting_PopulateIdempotenceFieldsFromResponseHeadersWhenPostingWithCallContext(self):
        communicator = self._create_communicator()
        request_body = object()
        context = CallContext(idempotence_key="test-idempotence-key")
        response_datetime = datetime(2026, 4, 2, 10, 15, 30, tzinfo=timezone.utc)
        self.marshaller.marshal.return_value = '{"request":"body"}'
        self.connection.post.return_value = (
            200,
            self._idempotence_response_headers(response_datetime),
            self._json_body_chunks('{"result":"OK"}'),
        )
        self.marshaller.unmarshal.return_value = object()
        response = communicator.post(self.RELATIVE_PATH, None, None, request_body,
                                     object, context)

        self.assertIsNotNone(response)
        self.assertEqual("test-idempotence-key", context.idempotence_key)
        self.assertEqual(123456789, context.idempotence_request_timestamp)
        self.assertEqual(response_datetime, context.idempotence_response_date_time)

    def test_UsingIdempotence_Putting_AddIdempotenceHeaderAndOmitItWithoutContextWhenPuttingWithIdempotenceKey(self):
        communicator = self._create_communicator()
        request_body = object()
        context_with_key = CallContext(idempotence_key="test-idempotence-key")

        self.marshaller.marshal.return_value = '{"request":"body"}'
        self.connection.put.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        self.marshaller.unmarshal.return_value = object()
        communicator.put(self.RELATIVE_PATH, None, None, request_body,
                         object, context_with_key)
        headers_with_key = self.connection.put.call_args[0][1]

        self.assertTrue(
            any(h.name == "X-GCS-Idempotence-Key" and h.value == "test-idempotence-key"
                for h in headers_with_key)
        )

        self.connection.put.reset_mock()
        self.marshaller.marshal.return_value = '{"request":"body"}'
        self.connection.put.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        self.marshaller.unmarshal.return_value = object()
        communicator.put(self.RELATIVE_PATH, None, None, request_body, object, None)
        headers_without_key = self.connection.put.call_args[0][1]

        self.assertFalse(
            any(h.name == "X-GCS-Idempotence-Key" for h in headers_without_key)
        )

    def test_UsingIdempotence_Putting_PopulateIdempotenceFieldsFromResponseHeadersWhenPuttingWithCallContext(self):
        communicator = self._create_communicator()
        request_body = object()
        context = CallContext(idempotence_key="test-idempotence-key")
        response_datetime = datetime(2026, 4, 2, 10, 15, 30, tzinfo=timezone.utc)
        self.marshaller.marshal.return_value = '{"request":"body"}'
        self.connection.put.return_value = (
            200,
            self._idempotence_response_headers(response_datetime),
            self._json_body_chunks('{"result":"OK"}'),
        )
        self.marshaller.unmarshal.return_value = object()
        response = communicator.put(self.RELATIVE_PATH, None, None, request_body,
                                    object, context)

        self.assertIsNotNone(response)
        self.assertEqual("test-idempotence-key", context.idempotence_key)
        self.assertEqual(123456789, context.idempotence_request_timestamp)
        self.assertEqual(response_datetime, context.idempotence_response_date_time)

    def test_UsingIdempotence_Deleting_AddIdempotenceHeaderAndOmitItWithoutContextWhenDeletingWithIdempotenceKey(self):
        communicator = self._create_communicator()
        context_with_key = CallContext(idempotence_key="test-idempotence-key")
        self.connection.delete.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        self.marshaller.unmarshal.return_value = object()
        communicator.delete(self.RELATIVE_PATH, None, None, object, context_with_key)
        headers_with_key = self.connection.delete.call_args[0][1]

        self.assertTrue(
            any(h.name == "X-GCS-Idempotence-Key" and h.value == "test-idempotence-key"
                for h in headers_with_key)
        )

        self.connection.delete.reset_mock()
        self.connection.delete.return_value = (200, self._json_headers(), self._json_body_chunks('{"result":"OK"}'))
        communicator.delete(self.RELATIVE_PATH, None, None, object, None)
        headers_without_key = self.connection.delete.call_args[0][1]

        self.assertFalse(
            any(h.name == "X-GCS-Idempotence-Key" for h in headers_without_key)
        )

    def test_UsingIdempotence_Deleting_PopulateIdempotenceFieldsFromResponseHeadersWhenDeletingWithCallContext(self):
        communicator = self._create_communicator()
        context = CallContext(idempotence_key="test-idempotence-key")
        response_datetime = datetime(2026, 4, 2, 10, 15, 30, tzinfo=timezone.utc)
        self.connection.delete.return_value = (
            200,
            self._idempotence_response_headers(response_datetime),
            self._json_body_chunks('{"result":"OK"}'),
        )
        self.marshaller.unmarshal.return_value = object()
        response = communicator.delete(self.RELATIVE_PATH, None, None, object, context)

        self.assertIsNotNone(response)
        self.assertEqual("test-idempotence-key", context.idempotence_key)
        self.assertEqual(123456789, context.idempotence_request_timestamp)
        self.assertEqual(response_datetime, context.idempotence_response_date_time)

    def test_ConstructingCommunicator_DefaultScenario_CreateInstanceWithValidParameters(self):
        communicator = self._create_communicator()
        self.assertIsNotNone(communicator)

    def test_ConstructingCommunicator_DefaultScenario_ThrowExceptionWhenApiEndpointIsNull(self):
        with self.assertRaises(ValueError):
            Communicator(
                api_endpoint=None,
                connection=self.connection,
                authenticator=self.authenticator,
                metadata_provider=self.metadata_provider,
                marshaller=self.marshaller,
            )

    def test_ConstructingCommunicator_DefaultScenario_ThrowExceptionWhenApiEndpointHasPath(self):
        invalid_endpoint = urlparse("https://payment.preprod.online-payments.com/v1")
        with self.assertRaises(ValueError):
            Communicator(
                api_endpoint=invalid_endpoint,
                connection=self.connection,
                authenticator=self.authenticator,
                metadata_provider=self.metadata_provider,
                marshaller=self.marshaller,
            )

    def test_ConstructingCommunicator_DefaultScenario_ThrowExceptionWhenApiEndpointHasUserInfo(self):
        invalid_endpoint = urlparse("https://user:pass@payment.preprod.online-payments.com")
        with self.assertRaises(ValueError):
            Communicator(
                api_endpoint=invalid_endpoint,
                connection=self.connection,
                authenticator=self.authenticator,
                metadata_provider=self.metadata_provider,
                marshaller=self.marshaller,
            )

    def test_ConstructingCommunicator_DefaultScenario_ThrowExceptionWhenApiEndpointHasQuery(self):
        invalid_endpoint = urlparse("https://payment.preprod.online-payments.com?key=value")
        with self.assertRaises(ValueError):
            Communicator(
                api_endpoint=invalid_endpoint,
                connection=self.connection,
                authenticator=self.authenticator,
                metadata_provider=self.metadata_provider,
                marshaller=self.marshaller,
            )

    def test_ConstructingCommunicator_DefaultScenario_ThrowExceptionWhenApiEndpointHasFragment(self):
        invalid_endpoint = urlparse("https://payment.preprod.online-payments.com#section")
        with self.assertRaises(ValueError):
            Communicator(
                api_endpoint=invalid_endpoint,
                connection=self.connection,
                authenticator=self.authenticator,
                metadata_provider=self.metadata_provider,
                marshaller=self.marshaller,
            )

    def test_ConstructingCommunicator_DefaultScenario_ThrowExceptionWhenConnectionIsNull(self):
        with self.assertRaises(ValueError):
            Communicator(
                api_endpoint=urlparse(self.BASE_URI),
                connection=None,
                authenticator=self.authenticator,
                metadata_provider=self.metadata_provider,
                marshaller=self.marshaller,
            )

    def test_ConstructingCommunicator_DefaultScenario_ThrowExceptionWhenAuthenticatorIsNull(self):
        with self.assertRaises(ValueError):
            Communicator(
                api_endpoint=urlparse(self.BASE_URI),
                connection=self.connection,
                authenticator=None,
                metadata_provider=self.metadata_provider,
                marshaller=self.marshaller,
            )

    def test_ConstructingCommunicator_DefaultScenario_ThrowExceptionWhenMetadataProviderIsNull(self):
        with self.assertRaises(ValueError):
            Communicator(
                api_endpoint=urlparse(self.BASE_URI),
                connection=self.connection,
                authenticator=self.authenticator,
                metadata_provider=None,
                marshaller=self.marshaller,
            )

    def test_ConstructingCommunicator_DefaultScenario_ThrowExceptionWhenMarshallerIsNull(self):
        with self.assertRaises(ValueError):
            Communicator(
                api_endpoint=urlparse(self.BASE_URI),
                connection=self.connection,
                authenticator=self.authenticator,
                metadata_provider=self.metadata_provider,
                marshaller=None,
            )

    def test_GettingMarshaller_DefaultScenario_ReturnNonNullMarshaller(self):
        communicator = self._create_communicator()
        self.assertIsNotNone(communicator.marshaller)

    def test_GettingMarshaller_DefaultScenario_ReturnSameMarshallerInstance(self):
        communicator = self._create_communicator()
        first_result = communicator.marshaller
        second_result = communicator.marshaller
        self.assertIs(first_result, second_result)

    def test_GettingMarshaller_DefaultScenario_ReturnConfiguredMarshaller(self):
        communicator = self._create_communicator()
        self.assertIs(self.marshaller, communicator.marshaller)

    def test_ClosingCommunicator_DefaultScenario_DelegateToConnection(self):
        communicator = self._create_communicator()
        communicator.close()
        self.connection.close.assert_called_once()

    def test_ClosingCommunicator_DefaultScenario_ThrowIOExceptionWhenConnectionThrows(self):
        communicator = self._create_communicator()
        self.connection.close.side_effect = IOError("Connection error")
        with self.assertRaises(IOError):
            communicator.close()

    def test_ClosingCommunicator_DefaultScenario_BeCloseable(self):
        with self._create_communicator() as communicator:
            self.assertIsNotNone(communicator)


if __name__ == '__main__':
    unittest.main()
