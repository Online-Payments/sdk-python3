import io
import os
import re
import time
import unittest
from datetime import timedelta
from typing import List
from unittest.mock import MagicMock
from urllib.parse import urlparse

import tests.file_utils as file_utils
from tests.unit.server_mock_utils import create_server_listening, create_communicator

from onlinepayments.sdk.proxy_configuration import ProxyConfiguration
from onlinepayments.sdk.communication.default_connection import DefaultConnection
from onlinepayments.sdk.communication.multipart_form_data_object import MultipartFormDataObject
from onlinepayments.sdk.communicator_configuration import CommunicatorConfiguration
from onlinepayments.sdk.domain.uploadable_file import UploadableFile
from onlinepayments.sdk.log.communicator_logger import CommunicatorLogger

from onlinepayments.sdk.communication.communication_exception import CommunicationException
from onlinepayments.sdk.communication.not_found_exception import NotFoundException
from onlinepayments.sdk.communication.param_request import ParamRequest
from onlinepayments.sdk.communication.request_param import RequestParam
from onlinepayments.sdk.communication.response_exception import ResponseException
from onlinepayments.sdk.domain.data_object import DataObject
from requests.exceptions import Timeout

CONNECT_TIMEOUT = 10
SOCKET_TIMEOUT = 20
MAX_CONNECTIONS = 100


class DefaultConnectionTest(unittest.TestCase):

    def setUp(self):
        self.request_path = None
        self.communicator = None

    def test_ConstructingDefaultConnection_BuiltWithProxy_UseConfiguredProxy(self):
        proxy_config = ProxyConfiguration.from_uri("http://test-proxy")

        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT, proxy_configuration=proxy_config)

        self.assertTimeouts(connection, CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        self.assertMaxConnections(connection, CommunicatorConfiguration.DEFAULT_MAX_CONNECTIONS)
        self.assertProxy(connection, proxy_config)

    def test_ConstructingDefaultConnection_BuiltWithProxy_UseConfiguredAuthenticatedProxy(self):
        proxy_config = ProxyConfiguration.from_uri("http://test-proxy", "test-username", "test-password")

        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT, proxy_configuration=proxy_config)

        self.assertTimeouts(connection, CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        self.assertMaxConnections(connection, CommunicatorConfiguration.DEFAULT_MAX_CONNECTIONS)
        self.assertProxy(connection, proxy_config)

    def test_ConstructingDefaultConnection_BuiltWithMaxConnections_UseConfiguredMaxConnections(self):
        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT, MAX_CONNECTIONS)

        self.assertTimeouts(connection, CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        self.assertMaxConnections(connection, MAX_CONNECTIONS)
        self.assertNoProxy(connection)

    def test_ConstructingDefaultConnection_BuiltWithMaxConnections_UseConfiguredMaxConnectionsPerProxyRoute(self):
        proxy_config = ProxyConfiguration.from_uri("http://test-proxy")

        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT,
                                       MAX_CONNECTIONS, proxy_configuration=proxy_config)

        self.assertTimeouts(connection, CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        self.assertMaxConnections(connection, MAX_CONNECTIONS)
        self.assertProxy(connection, proxy_config)

    def test_ConstructingDefaultConnection_BuiltWithDefaultOptions_UseDefaultConfiguration(self):
        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT)

        self.assertTimeouts(connection, CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        self.assertMaxConnections(connection, CommunicatorConfiguration.DEFAULT_MAX_CONNECTIONS)
        self.assertNoProxy(connection)

    def test_EnablingAndDisablingLogging_DefaultScenario_EnableLogging(self):
        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        logger = MagicMock(spec=CommunicatorLogger)
        connection.enable_logging(logger)

    def test_EnablingAndDisablingLogging_DefaultScenario_DisableLogging(self):
        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        connection.disable_logging()

    def test_EnablingAndDisablingLogging_DefaultScenario_AcceptNullLogger(self):
        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        connection.enable_logging(None)

    def test_SettingObfuscators_DefaultScenario_AcceptNullBodyObfuscator(self):
        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        connection.set_body_obfuscator(None)

    def test_SettingObfuscators_DefaultScenario_AcceptNullHeaderObfuscator(self):
        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        connection.set_header_obfuscator(None)

    def test_ClosingIdleConnections_DefaultScenario_NotThrow(self):
        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        connection.close_idle_connections(timedelta(seconds=5))

    def test_ClosingExpiredConnections_DefaultScenario_NotThrow(self):
        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        connection.close_expired_connections()

    def test_ClosingConnection_DefaultScenario_CloseHttpClient(self):
        connection = DefaultConnection(CONNECT_TIMEOUT, SOCKET_TIMEOUT)
        connection.close()

    def test_LoggingIsEnabled_Getting_LogExpectedRequestAndResponseWithoutQueryParams(self):
        test_path = "/v1/get"
        logger = TestLogger()

        response_body = read_resource("getWithoutQueryParams.json")
        handler = self.create_handler(body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:
            with create_communicator(address) as communicator:
                communicator.enable_logging(logger)
                response = communicator.get('/v1/get', None, None, GenericObject, None)

        self.assertIsNotNone(response)
        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertEqual('OK', response.content['result'])
        self.assertEqual(2, len(logger.entries))
        request_entry = logger.entries[0]
        self.assertIsNotNone(request_entry[0])
        self.assertIsNone(request_entry[1])
        response_entry = logger.entries[1]
        self.assertIsNotNone(response_entry[0])
        self.assertIsNone(response_entry[1])
        self.assertRequestAndResponse(request_entry[0], response_entry[0], "getWithoutQueryParams")

    def test_LoggingIsEnabled_Getting_LogExpectedRequestAndResponseWithQueryParams(self):
        test_path = "/v1/get"
        logger = TestLogger()

        query_params = TestParamRequest([
            RequestParam("source", "EUR"),
            RequestParam("target", "USD"),
            RequestParam("amount", "1000"),
        ])

        response_body = read_resource("getWithQueryParams.json")
        handler = self.create_handler(body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:
            with create_communicator(address) as communicator:
                communicator.enable_logging(logger)
                response = communicator.get('/v1/get', None, query_params, GenericObject, None)

        self.assertIsNotNone(response)
        self.assertEqual(4547504, response.content['convertedAmount'])
        self.assertEqual(test_path, self.request_path.split("?")[0],
                         'Request has arrived at {} instead of {}'.format(self.request_path.split("?")[0], test_path))
        self.assertLogsRequestAndResponse(logger, "getWithQueryParams")

    def test_LoggingIsEnabled_Getting_LogExpectedRequestAndResponseWithUtf8Response(self):
        test_path = "/v1/get-utf8"
        logger = TestLogger()

        response_body = read_resource("getWithUtf8Response.json")
        handler = self.create_handler(body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:
            with create_communicator(address) as communicator:
                communicator.enable_logging(logger)
                response = communicator.get('/v1/get-utf8', None, None, GenericObject, None)

        self.assertIsNotNone(response)
        self.assertEqual('café über €', response.content['message'])
        self.assertEqual(test_path, self.request_path)
        self.assertLogsRequestAndResponse(logger, "getWithUtf8Response")

    def test_LoggingIsEnabled_Posting_LogExpectedRequestAndResponseWithSuccessResponse(self):
        test_path = "/v1/created"
        logger = TestLogger()

        request = create_post_request()
        response_body = read_resource("postWithCreatedResponse.json")
        additional_headers = (("content-Type", "application/json"),
                               ("Location", "http://localhost/v1/created/000000123410000595980000100001"))
        handler = self.create_handler(response_code=201, body=response_body,
                                      additional_headers=additional_headers)
        with create_server_listening(handler) as address:
            with create_communicator(address) as communicator:
                communicator.enable_logging(logger)
                response = communicator.post('/v1/created', None, None, request, GenericObject, None)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.content['payment'])
        self.assertEqual('000000123410000595980000100001', response.content['payment']['id'])
        self.assertEqual('PENDING_APPROVAL', response.content['payment']['status'])
        self.assertEqual(test_path, self.request_path,
                         'Request has arrived at "{1}" while it should have been delivered to "{0}"'.format(
                             test_path, self.request_path))
        self.assertLogsRequestAndResponse(logger, "postWithCreatedResponse")

    def test_LoggingIsEnabled_Posting_LogExpectedRequestAndResponseBeforeThrowingWithClientErrorResponse(self):
        test_path = "/v1/bad-request"
        logger = TestLogger()

        request = create_post_request()
        response_body = read_resource("postWithBadRequestResponse.json")
        handler = self.create_handler(response_code=400, body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:
            with create_communicator(address) as communicator:
                communicator.enable_logging(logger)
                with self.assertRaises(ResponseException):
                    communicator.post('/v1/bad-request', None, None, request, GenericObject, None)

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertLogsRequestAndResponse(logger, "postWithBadRequestResponse")

    def test_LoggingIsEnabled_Putting_LogExpectedRequestAndResponseWithSuccessResponse(self):
        test_path = "/v1/put"
        logger = TestLogger()

        request = {'key': 'value'}
        response_body = read_resource("putWithSuccessResponse.json")
        handler = self.create_handler(body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:
            with create_communicator(address) as communicator:
                communicator.enable_logging(logger)
                response = communicator.put('/v1/put', None, None, request, GenericObject, None)

        self.assertIsNotNone(response)
        self.assertEqual('OK', response.content['result'])
        self.assertEqual(test_path, self.request_path)
        self.assertLogsRequestAndResponse(logger, "putWithSuccessResponse")

    def test_LoggingIsEnabled_Putting_LogExpectedRequestAndResponseBeforeThrowingWithBadRequestResponse(self):
        test_path = "/v1/put-bad-request"
        logger = TestLogger()

        request = {'key': 'value'}
        response_body = read_resource("putWithBadRequestResponse.json")
        handler = self.create_handler(response_code=400, body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:
            with create_communicator(address) as communicator:
                communicator.enable_logging(logger)
                with self.assertRaises(ResponseException):
                    communicator.put('/v1/put-bad-request', None, None, request, GenericObject, None)

        self.assertEqual(test_path, self.request_path)
        self.assertLogsRequestAndResponse(logger, "putWithBadRequestResponse")

    def test_LoggingIsEnabled_Deleting_LogExpectedRequestAndResponseWithVoidResponse(self):
        test_path = "/v1/void"
        logger = TestLogger()

        handler = self.create_handler(response_code=204)
        with create_server_listening(handler) as address:
            with create_communicator(address) as communicator:
                communicator.enable_logging(logger)
                communicator.delete('/v1/void', None, None, None, None)

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertLogsRequestAndResponse(logger, "deleteWithVoidResponse")

    def test_LoggingIsEnabled_Deleting_LogExpectedRequestAndResponseAndPassEmptyBodyToHandlerVoidContent(self):
        test_path = "/v1/void"
        logger = TestLogger()

        handler = self.create_handler(response_code=204)
        with create_server_listening(handler) as address:
            with create_communicator(address) as communicator:
                communicator.enable_logging(logger)
                # binary-response variant: the void response body is returned to the caller as chunks
                response_headers, response_chunks = communicator.delete_with_binary_response(
                    '/v1/void', None, None, None)
                body = b"".join(response_chunks)

        self.assertEqual(b"", body, 'Void response body passed to the handler should be empty')
        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertLogsRequestAndResponse(logger, "deleteWithVoidResponse")

    def test_LoggingIsEnabled_HandlingBinaryRequests_LogContentLengthWithoutChunkedTransferEncodingWithKnownLength(self):
        logger = TestLogger()
        data = os.urandom(1024)

        handler = self.create_handler(response_code=204)

        with create_server_listening(handler) as address:
            with create_communicator(address) as communicator:
                communicator.enable_logging(logger)

                uploadable_file = UploadableFile("dummyFile", io.BytesIO(data),
                                                 "application/octet-stream", len(data))
                multipart = MultipartFormDataObject()
                multipart.add_file("file", uploadable_file)
                communicator.post('/binaryRequest', None, None, multipart, None, None)

        self.assertEqual(2, len(logger.entries))
        request_entry = logger.entries[0]
        self.assertIsNotNone(request_entry[0])
        self.assertIsNone(request_entry[1])
        response_entry = logger.entries[1]
        self.assertIsNotNone(response_entry[0])
        self.assertIsNone(response_entry[1])
        self.assertRequestAndResponse(request_entry[0], response_entry[0], "binaryRequest")
        headers = request_entry[0].get_header_list()
        self.assertTrue(any(h[0].lower() == 'content-length' for h in headers),
                        "Content-Length must be present for known-length file upload")
        self.assertFalse(any(h[0].lower() == 'transfer-encoding' and 'chunked' in h[1].lower()
                             for h in headers),
                         "Transfer-Encoding: chunked must not be present for known-length file upload")

    def test_LoggingIsEnabled_HandlingBinaryRequests_LogContentLengthEvenWithUnknownLength(self):
        logger = TestLogger()
        data = os.urandom(1024)

        handler = self.create_handler(response_code=204)

        with create_server_listening(handler) as address:
            with create_communicator(address) as communicator:
                communicator.enable_logging(logger)

                uploadable_file = UploadableFile("dummyFile", io.BytesIO(data), "application/octet-stream")
                multipart = MultipartFormDataObject()
                multipart.add_file("file", uploadable_file)
                communicator.post('/binaryRequest', None, None, multipart, None, None)

        self.assertEqual(2, len(logger.entries))
        request_entry = logger.entries[0]
        self.assertIsNotNone(request_entry[0])
        self.assertIsNone(request_entry[1])
        response_entry = logger.entries[1]
        self.assertIsNotNone(response_entry[0])
        self.assertIsNone(response_entry[1])
        self.assertRequestAndResponse(request_entry[0], response_entry[0], "binaryRequest")
        headers = request_entry[0].get_header_list()
        self.assertTrue(any(h[0].lower() == 'content-length' for h in headers),
                        "Content-Length must be present: Python SDK uses to_string() for multipart regardless of content_length")
        self.assertFalse(any(h[0].lower() == 'transfer-encoding' and 'chunked' in h[1].lower()
                             for h in headers),
                         "Transfer-Encoding: chunked must not be present: Python SDK always uses Content-Length for multipart")

    def test_LoggingIsEnabled_HandlingBinaryResponses_LogExpectedRequestAndResponseAndPassBodyToResponseHandler(self):
        logger = TestLogger()
        data = os.urandom(1024)

        def binary_handler(handler):
            self.request_path = handler.path
            handler.protocol_version = 'HTTP/1.1'
            try:
                handler.send_response(200)
                handler.send_header('Content-Type', 'application/octet-stream')
                handler.send_header('Dummy', None)
                handler.send_header('Content-Length', len(data))
                handler.end_headers()
                handler.wfile.write(data)
            except ConnectionAbortedError:
                pass

        connect_timeout = 0.500
        socket_timeout = 0.500
        with create_server_listening(binary_handler) as address:
            url = urlparse(address + '/binaryContent')
            connection = DefaultConnection(connect_timeout, socket_timeout)
            connection.enable_logging(logger)
            try:
                status, headers, chunks = connection.get(url, [])
                received_data = b"".join(chunks)
            finally:
                connection.close()

        self.assertEqual(200, status)
        self.assertEqual(data, received_data)
        self.assertEqual(2, len(logger.entries))
        request_entry = logger.entries[0]
        self.assertIsNotNone(request_entry[0])
        self.assertIsNone(request_entry[1])
        response_entry = logger.entries[1]
        self.assertIsNotNone(response_entry[0])
        self.assertIsNone(response_entry[1])
        self.assertRequestAndResponse(request_entry[0], response_entry[0], "binaryResponse")

    def test_LoggingIsEnabled_HandlingErrors_LogExpectedRequestAndErrorResponseWithUnknownServerError(self):
        test_path = "/v1/get"
        logger = TestLogger()

        response_body = read_resource("unknownServerError.json")
        handler = self.create_handler(response_code=500, body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:
            with create_communicator(address) as communicator:
                communicator.enable_logging(logger)
                with self.assertRaises(ResponseException):
                    communicator.get('/v1/get', None, None, GenericObject, None)

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertLogsRequestAndResponse(logger, "getWithoutQueryParams", "unknownServerError")

    def test_LoggingIsEnabled_HandlingErrors_LogExpectedRequestAndResponseBeforeThrowingWithInvalidHtmlResponse(self):
        test_path = "/v1/get"
        logger = TestLogger()

        response_body = read_resource("notFound.html")
        handler = self.create_handler(response_code=404, body=response_body,
                                      additional_headers=(("Content-Type", "text/html"),))
        with create_server_listening(handler) as address:
            with create_communicator(address, connect_timeout=0.500, socket_timeout=0.050) as communicator:
                communicator.enable_logging(logger)
                with self.assertRaises(NotFoundException):
                    communicator.get('/v1/get', None, None, GenericObject, None)

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertLogsRequestAndResponse(logger, "getWithoutQueryParams", "notFound")

    def test_LoggingIsEnabled_HandlingErrors_LogRequestAndErrorWithCommunicationException(self):
        test_path = "/v1/get"
        logger = TestLogger()

        response_body = read_resource("notFound.html")
        handler = self.create_handler(response_code=404, body=response_body,
                                      additional_headers=(("Content-Type", "text/html"),))

        def delayed_response(*args, **kwargs):
            time.sleep(0.100)
            handler(*args, **kwargs)

        with create_server_listening(delayed_response) as address:
            with create_communicator(address, socket_timeout=0.05) as communicator:
                communicator.enable_logging(logger)
                with self.assertRaises(CommunicationException):
                    communicator.get('/v1/get', None, None, GenericObject, None)

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertEqual(2, len(logger.entries))
        request_entry = logger.entries[0]
        self.assertIsNotNone(request_entry[0])
        self.assertIsNone(request_entry[1])
        response_entry = logger.entries[1]
        self.assertIsNotNone(response_entry[0])
        self.assertIsNotNone(response_entry[1])
        self.assertRequestAndError(request_entry[0], response_entry[0], "getWithoutQueryParams")
        self.assertIsInstance(response_entry[1], Timeout, "logger should have logged a timeout error")

    def test_LoggingIsEnabled_DisablingLogging_NotLogSubsequentRequestsAfterLoggingIsDisabled(self):
        logger = TestLogger()

        response_body = read_resource("getWithoutQueryParams.json")
        handler = self.create_handler(body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:
            with create_communicator(address) as communicator:
                communicator.enable_logging(logger)
                communicator.disable_logging()
                response = communicator.get('/v1/get', None, None, GenericObject, None)

        self.assertIsNotNone(response)
        self.assertEqual('OK', response.content['result'])
        self.assertEqual(0, len(logger.entries))

    def test_LoggingIsEnabled_LoggingStateChangesDuringRequestLifecycle_LogRequestOnlyWhenLoggingIsDisabledBeforeResponse(self):
        test_path = "/v1/get"
        logger = TestLogger()

        response_body = read_resource("getWithoutQueryParams.json")
        handler = self.create_handler(response_code=200, body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))

        def disable_logging_response(*args, **kwargs):
            self.communicator.disable_logging()
            handler(*args, **kwargs)

        with create_server_listening(disable_logging_response) as address:
            with create_communicator(address) as communicator:
                self.communicator = communicator
                communicator.enable_logging(logger)
                response = communicator.get('/v1/get', None, None, GenericObject, None)

        self.assertEqual("OK", response.content['result'])
        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertEqual(1, len(logger.entries))
        request_entry = logger.entries[0]
        self.assertIsNotNone(request_entry[0])
        self.assertIsNone(request_entry[1],
                          "Error '{}' logged that should not have been thrown".format(request_entry[1]))
        self.assertRequest(request_entry[0], "getWithoutQueryParams")

    def test_LoggingIsEnabled_LoggingStateChangesDuringRequestLifecycle_LogResponseOnlyWhenLoggingIsEnabledAfterRequest(self):
        test_path = "/v1/get"
        logger = TestLogger()

        response_body = read_resource("getWithoutQueryParams.json")
        handler = self.create_handler(response_code=200, body=response_body,
                                      additional_headers=(("Content-Type", "application/json"),))

        def enable_logging_response(*args, **kwargs):
            self.communicator.enable_logging(logger)
            handler(*args, **kwargs)

        with create_server_listening(enable_logging_response) as address:
            with create_communicator(address) as communicator:
                self.communicator = communicator
                response = communicator.get('/v1/get', None, None, GenericObject, None)

        self.assertEqual("OK", response.content['result'])
        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertEqual(1, len(logger.entries))
        response_entry = logger.entries[0]
        self.assertIsNotNone(response_entry[0])
        self.assertIsNone(response_entry[1],
                          "Error '{}' logged that should not have been thrown".format(response_entry[1]))
        self.assertResponse(response_entry[0], "getWithoutQueryParams")

    def test_LoggingIsEnabled_LoggingStateChangesDuringRequestLifecycle_LogErrorOnlyWhenLoggingIsEnabledAfterRequestFailure(self):
        test_path = "/v1/get"
        logger = TestLogger()

        response_body = read_resource("notFound.html")
        handler = self.create_handler(response_code=404, body=response_body,
                                      additional_headers=(("Content-Type", "text/html"),))

        def enable_logging_late_response(*args, **kwargs):
            self.communicator.enable_logging(logger)
            time.sleep(0.1)
            handler(*args, **kwargs)

        with create_server_listening(enable_logging_late_response) as address:
            with create_communicator(address, connect_timeout=0.500, socket_timeout=0.050) as communicator:
                self.communicator = communicator
                with self.assertRaises(CommunicationException):
                    communicator.get('/v1/get', None, None, GenericObject, None)

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertEqual(1, len(logger.entries))
        error_entry = logger.entries[0]
        self.assertIsNotNone(error_entry[0])
        self.assertIsNotNone(error_entry[1])
        self.assertError(error_entry[0])
        self.assertIsInstance(error_entry[1], Timeout,
                              "logger should have logged a timeout error, logged {} instead".format(error_entry[1]))

    def assertLogsRequestAndResponse(self, logger, request_resource_prefix, response_resource_prefix=None):
        if response_resource_prefix is None:
            response_resource_prefix = request_resource_prefix
        self.assertEqual(2, len(logger.entries))
        request_entry = logger.entries[0]
        self.assertIsNotNone(request_entry[0])
        self.assertIsNone(request_entry[1],
                          "Error '{}' logged that should not have been thrown".format(request_entry[1]))
        response_entry = logger.entries[1]
        self.assertIsNotNone(response_entry[0])
        self.assertIsNone(response_entry[1],
                          "Error '{}' logged that should not have been thrown".format(response_entry[1]))
        self.assertRequestAndResponse(request_entry[0], response_entry[0],
                                      request_resource_prefix, response_resource_prefix)

    def assertRequestAndResponse(self, request_message, response_message,
                                 request_resource_prefix, response_resource_prefix=None):
        if response_resource_prefix is None:
            response_resource_prefix = request_resource_prefix
        request_id = self.assertRequest(request_message, request_resource_prefix)
        self.assertResponse(response_message, response_resource_prefix, request_id)

    def assertRequestAndError(self, request_message, error_message, resource_prefix):
        request_id = self.assertRequest(request_message, resource_prefix)
        self.assertError(error_message, request_id)

    def assertRequest(self, request_message, request_resource_prefix):
        request_resource = request_resource_prefix + "_request"
        regex = globals()[request_resource](request_message, self)
        if isinstance(regex, str):
            request_pattern = re.compile(regex, re.DOTALL)
            match = request_pattern.match(request_message.get_message())
            if match is None:
                raise AssertionError("request message '" + request_message.get_message() +
                                     "' does not match pattern " + str(request_pattern))
            return match.group(1)
        return regex[0]

    def assertResponse(self, response_message, response_resource_prefix, request_id=None):
        response_resource = response_resource_prefix + "_response"
        regex = globals()[response_resource](response_message, self)
        if isinstance(regex, str):
            response_pattern = re.compile(regex, re.DOTALL)
            match = response_pattern.match(response_message.get_message())
            if match is None:
                raise AssertionError("response message '" + response_message.get_message() +
                                     "' does not match pattern " + str(response_pattern))
            if request_id is not None:
                self.assertEqual(request_id, match.group(1),
                                 "request_id '{0}' does not match response_id '{1}'".format(
                                     request_id, match.group(1)))

    def assertError(self, error_message, request_id=None):
        error_pattern_string = generic_error()
        error_pattern = re.compile(error_pattern_string, re.DOTALL)
        match = error_pattern.match(error_message)
        if match is None:
            raise AssertionError("error message '" + error_message +
                                 "' does not match pattern " + str(error_pattern_string))
        if request_id is not None:
            self.assertEqual(request_id, match.group(1),
                             "request_id '{0}' does not match error_id '{1}'".format(request_id, match.group(1)))

    def assertHeaderIn(self, _tuple, _list):
        self.assertIn((_tuple[0].lower(), _tuple[1]),
                      list(map(lambda el: (el[0].lower(), el[1]), _list)))

    def create_handler(self, response_code=200, body='', additional_headers=()):
        def handler_func(handler):
            self.request_path = handler.path
            handler.protocol_version = 'HTTP/1.1'
            try:
                handler.send_response(response_code)
                for header in additional_headers:
                    handler.send_header(*header)
                handler.send_header('Dummy', None)
                handler.send_header('Content-Length', len(bytes(body, "utf-8")))
                handler.end_headers()
                handler.wfile.write(bytes(body, "utf-8"))
            except ConnectionAbortedError:
                pass
        return handler_func

    def assertNoProxy(self, default_connection):
        self.assertFalse(default_connection._DefaultConnection__requests_session.proxies)

    def assertProxy(self, connection, proxy_configuration):
        self.assertIn(str(proxy_configuration),
                      list(connection._DefaultConnection__requests_session.proxies.values()))

    def assertTimeouts(self, connection, connection_timeout, socket_timeout):
        self.assertEqual(connection_timeout, connection.connect_timeout)
        self.assertEqual(socket_timeout, connection.socket_timeout)

    def assertMaxConnections(self, connection, expected_max_connections):
        requests_session = connection._DefaultConnection__requests_session
        http_poolsize = requests_session.get_adapter("http://")._pool_maxsize
        https_poolsize = requests_session.get_adapter("https://")._pool_maxsize
        self.assertEqual(expected_max_connections, http_poolsize)
        self.assertEqual(expected_max_connections, https_poolsize)

class TestLogger(CommunicatorLogger):
    def __init__(self):
        CommunicatorLogger.__init__(self)
        self.entries = []

    def log_request(self, request_log_message):
        self.entries.append((request_log_message, None))

    def log_response(self, response_log_message):
        self.entries.append((response_log_message, None))

    def log(self, message, thrown=None):
        self.entries.append((message, thrown))


class GenericObject(DataObject):
    content: dict = {}

    def to_dictionary(self) -> dict:
        return self.content

    def from_dictionary(self, dictionary: dict) -> 'DataObject':
        self.content = dictionary
        return self


class TestParamRequest(ParamRequest):

    def __init__(self, params: List[RequestParam]):
        self.params = params

    def to_request_parameters(self) -> List[RequestParam]:
        return self.params

def create_post_request():
    return {'card': {'cvv': '123', 'cardNumber': '1234567890123456', 'expiryDate': '1220'}}

def read_resource(file_name):
    return file_utils.read_file(os.path.join("communication", file_name), encoding='utf-8')

def getWithoutQueryParams_request(request, test):
    test.assertEqual(request.method, "GET")
    test.assertEqual(request.uri, '/v1/get')
    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertTrue(len(list(filter(lambda h: h[0] == 'X-GCS-ServerMetaInfo', headers))))
    test.assertIsNone(request.body)
    return request.request_id, False

def getWithoutQueryParams_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 200)
    test.assertEqual(response.content_type, 'application/json')
    headers = response.get_header_list()
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False

def getWithQueryParams_request(request, test):
    test.assertEqual(request.method, "GET")
    test.assertEqual(request.uri, '/v1/get?source=EUR&target=USD&amount=1000')
    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertTrue(len(list(filter(lambda h: h[0] == 'X-GCS-ServerMetaInfo', headers))))
    test.assertIsNone(request.body)
    return request.request_id, False

def getWithQueryParams_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 200)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertEqual(response.content_type, 'application/json')
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False


def getWithUtf8Response_request(request, test):
    test.assertEqual(request.method, "GET")
    test.assertEqual(request.uri, '/v1/get-utf8')
    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertTrue(len(list(filter(lambda h: h[0] == 'X-GCS-ServerMetaInfo', headers))))
    test.assertIsNone(request.body)
    return request.request_id, False

def getWithUtf8Response_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 200)
    test.assertEqual(response.content_type, 'application/json')
    headers = response.get_header_list()
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False


def postWithCreatedResponse_request(request, test):
    test.assertEqual(request.method, "POST")
    test.assertEqual(request.uri, '/v1/created')
    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertTrue(len(list(filter(lambda h: h[0] == 'X-GCS-ServerMetaInfo', headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertEqual(request.content_type, 'application/json')
    test.assertIsNotNone(request.body)
    test.assertTrue(len(request.body))
    return request.request_id, False


def postWithCreatedResponse_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 201)
    test.assertEqual(response.content_type, 'application/json')
    headers = response.get_header_list()
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertHeaderIn(('Location', '"http://localhost/v1/created/000000123410000595980000100001"'), headers)
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False


def postWithBadRequestResponse_request(request, test):
    test.assertEqual(request.method, "POST")
    test.assertEqual(request.uri, '/v1/bad-request')
    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertTrue(len(list(filter(lambda h: h[0] == 'X-GCS-ServerMetaInfo', headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertEqual(request.content_type, 'application/json')
    test.assertIsNotNone(request.body)
    test.assertTrue(len(request.body))
    return request.request_id, False


def postWithBadRequestResponse_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 400)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertEqual(response.content_type, 'application/json')
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False


def putWithSuccessResponse_request(request, test):
    test.assertEqual(request.method, "PUT")
    test.assertEqual(request.uri, '/v1/put')
    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertTrue(len(list(filter(lambda h: h[0] == 'X-GCS-ServerMetaInfo', headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertEqual(request.content_type, 'application/json')
    test.assertIsNotNone(request.body)
    test.assertTrue(len(request.body))
    return request.request_id, False


def putWithSuccessResponse_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 200)
    test.assertEqual(response.content_type, 'application/json')
    headers = response.get_header_list()
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False


def putWithBadRequestResponse_request(request, test):
    test.assertEqual(request.method, "PUT")
    test.assertEqual(request.uri, '/v1/put-bad-request')
    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertTrue(len(list(filter(lambda h: h[0] == 'X-GCS-ServerMetaInfo', headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertEqual(request.content_type, 'application/json')
    test.assertIsNotNone(request.body)
    test.assertTrue(len(request.body))
    return request.request_id, False


def putWithBadRequestResponse_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 400)
    test.assertEqual(response.content_type, 'application/json')
    headers = response.get_header_list()
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False


def deleteWithVoidResponse_request(request, test):
    test.assertEqual(request.method, "DELETE")
    test.assertEqual(request.uri, '/v1/void')
    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertTrue(len(list(filter(lambda h: h[0] == 'X-GCS-ServerMetaInfo', headers))))
    test.assertIsNone(request.body)
    return request.request_id, False


def deleteWithVoidResponse_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 204)
    test.assertIsNone(response.content_type)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertIsNone(response.body)
    return response.request_id, False


def unknownServerError_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 500)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertEqual(response.content_type, 'application/json')
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False


def notFound_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 404)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertHeaderIn(('Content-Type', '"text/html"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertEqual(response.content_type, 'text/html')
    test.assertIsNotNone(response.body)
    test.assertEqual(response.body, "Not Found")
    return response.request_id, False


def binaryResponse_request(request, test):
    test.assertEqual(request.method, "GET")
    test.assertEqual(request.uri, '/binaryContent')
    test.assertIsNone(request.body)
    return request.request_id, False


def binaryResponse_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 200)
    test.assertEqual(response.content_type, 'application/octet-stream')
    test.assertEqual(response.body, "<binary content>")
    headers = response.get_header_list()
    test.assertHeaderIn(('Content-Type', '"application/octet-stream"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    return response.request_id, False


def binaryRequest_request(request, test):
    test.assertEqual(request.method, "POST")
    test.assertEqual(request.uri, '/binaryRequest')
    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertTrue(len(list(filter(lambda h: h[0] == 'X-GCS-ServerMetaInfo', headers))))
    content_type_headers = [h for h in headers if h[0].lower() == 'content-type']
    test.assertTrue(len(content_type_headers) > 0, "Content-Type header missing from binary request log")
    test.assertIn('multipart/form-data', content_type_headers[0][1])
    test.assertEqual(request.body, '<binary content>')
    return request.request_id, False


def binaryRequest_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 204)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter(lambda h: h[0] == 'Date', headers))))
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertIsNone(response.body)
    return response.request_id, False


def generic_error():
    return r"Error occurred for outgoing request \(requestId='([-a-zA-Z0-9]+)', \d+ s\)"


if __name__ == '__main__':
    unittest.main()
