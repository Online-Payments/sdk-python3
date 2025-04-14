import os
import re
import time
import unittest
from typing import List

from requests.exceptions import Timeout

import tests.file_utils as file_utils
from tests.unit.server_mock_utils import create_server_listening, create_communicator

from onlinepayments.sdk.communication.communication_exception import CommunicationException
from onlinepayments.sdk.communication.not_found_exception import NotFoundException
from onlinepayments.sdk.communication.param_request import ParamRequest
from onlinepayments.sdk.communication.request_param import RequestParam
from onlinepayments.sdk.communication.response_exception import ResponseException
from onlinepayments.sdk.domain.data_object import DataObject
from onlinepayments.sdk.log.communicator_logger import CommunicatorLogger


class DefaultConnectionLoggerTest(unittest.TestCase):
    """Tests that services can operate through DefaultConnection and that their network traffic is appropriately logged
    """

    def setUp(self):
        self.request_path = None  # Indicating whether or not a request has arrived at the correct server path
        self.communicator = None  # Stores the communicator used in testing so callbacks can reach it

    def test_get_without_query_params(self):
        """Test that a GET service without parameters can connect to a server and is logged appropriately"""
        test_path = "/v1/get"  # relative url through which the request should be sent
        logger = TestLogger()

        response_body = read_resource("getWithoutQueryParams.json")
        handler = self.create_handler(body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:  # start server to listen to request
            with create_communicator(address) as communicator:  # create communicator under test
                communicator.enable_logging(logger)
                response = communicator.get('/v1/get', None, None, GenericObject, None)

        self.assertIsNotNone(response)
        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertEqual('OK', response.content['result'])
        self.assertEqual(2, len(logger.entries))
        # for request and response, check that the message exists in the logs and there are no errors
        request_entry = logger.entries[0]
        self.assertIsNotNone(request_entry[0])
        self.assertIsNone(request_entry[1])
        response_entry = logger.entries[1]
        self.assertIsNotNone(response_entry[0])
        self.assertIsNone(response_entry[1])
        # for request and response, check that their output is as predicted and that they match each other
        self.assertRequestAndResponse(request_entry[0], response_entry[0], "getWithoutQueryParams")

    def test_get_with_query_params(self):
        """Test that a GET service with parameters can connect to a server and is logged appropriately"""
        test_path = "/v1/get"  # relative url through which the request should be sent
        logger = TestLogger()

        query_params = TestParamRequest([
            RequestParam("source", "EUR"),
            RequestParam("target", "USD"),
            RequestParam("amount", "1000"),
        ])

        response_body = read_resource("getWithQueryParams.json")
        handler = self.create_handler(body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:  # start server to listen to request
            with create_communicator(address) as communicator:  # create communicator under test
                communicator.enable_logging(logger)
                response = communicator.get('/v1/get', None, query_params, GenericObject, None)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.content['convertedAmount'])
        self.assertEqual(test_path, self.request_path.split("?")[0],
                         'Request has arrived at {} instead of {}'.format(self.request_path.split("?")[0], test_path))
        self.assertLogsRequestAndResponse(logger, "getWithQueryParams")

    def test_delete_with_void_response(self):
        """Test that a POST service without body and a void response can connect to a server and is logged appropriately
        """
        test_path = "/v1/void"  # relative url through which the request should be sent
        logger = TestLogger()

        handler = self.create_handler(response_code=204)
        with create_server_listening(handler) as address:  # start server to listen to request
            with create_communicator(address) as communicator:  # create communicator under test
                communicator.enable_logging(logger)
                communicator.delete('/v1/void', None, None, None, None)

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertLogsRequestAndResponse(logger, "deleteWithVoidResponse")

    def test_post_with_created_response(self):
        """Test that a POST service with 201 response can connect to a server and is logged appropriately"""
        test_path = "/v1/created"  # relative url through which the request should be sent
        logger = TestLogger()

        request = create_post_request()

        response_body = read_resource("postWithCreatedResponse.json")
        additional_headers = (("content-Type", "application/json"),
                              ("Location", "http://localhost/v1/created/000000123410000595980000100001"))
        handler = self.create_handler(response_code=201, body=response_body,
                                      additional_headers=additional_headers)
        with create_server_listening(handler) as address:  # start server to listen to request
            with create_communicator(address) as communicator:  # create communicator under test
                communicator.enable_logging(logger)
                response = communicator.post('/v1/created', None, None, request, GenericObject, None)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.content['payment'])
        self.assertIsNotNone(response.content['payment']['id'])
        self.assertEqual(test_path, self.request_path,
                         'Request has arrived at "{1}" while it should have been delivered to "{0}"'.format(
                             test_path, self.request_path))
        self.assertLogsRequestAndResponse(logger, "postWithCreatedResponse")

    def test_post_with_bad_request_response(self):
        """Test that a POST service that is invalid results in an error, which is logged appropriately"""
        test_path = "/v1/bad-request"  # relative url through which the request should be sent
        logger = TestLogger()

        request = create_post_request()

        response_body = read_resource("postWithBadRequestResponse.json")
        handler = self.create_handler(response_code=400, body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:  # start server to listen to request
            with create_communicator(address) as communicator:  # create communicator under test
                communicator.enable_logging(logger)
                with self.assertRaises(ResponseException):
                    communicator.post('/v1/bad-request', None, None, request, GenericObject, None)

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertLogsRequestAndResponse(logger, "postWithBadRequestResponse")

    def test_logging_unknown_server_error(self):
        """Test that a GET service that results in an error is logged appropriately"""
        # reuse the request from getWithoutQueryParams
        test_path = "/v1/get"  # relative url through which the request should be sent
        logger = TestLogger()

        response_body = read_resource("unknownServerError.json")
        handler = self.create_handler(response_code=500, body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:  # start server to listen to request
            with create_communicator(address) as communicator:  # create communicator under test
                communicator.enable_logging(logger)
                with self.assertRaises(ResponseException):
                    communicator.get('/v1/get', None, None, GenericObject, None)

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertLogsRequestAndResponse(logger, "getWithoutQueryParams", "unknownServerError")

    def test_non_json(self):
        """Test that a GET service that results in a not found error is logged appropriately"""
        # reuse the request from getWithoutQueryParams
        test_path = "/v1/get"  # relative url through which the request should be sent
        logger = TestLogger()

        response_body = read_resource("notFound.html")
        handler = self.create_handler(response_code=404, body=response_body,
                                      additional_headers=(("Content-Type", "text/html"),))
        with create_server_listening(handler) as address:  # start server to listen to request
            with create_communicator(address, connect_timeout=0.500, socket_timeout=0.050) as communicator:
                communicator.enable_logging(logger)
                with self.assertRaises(NotFoundException):
                    communicator.get('/v1/get', None, None, GenericObject, None)

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertLogsRequestAndResponse(logger, "getWithoutQueryParams", "notFound")

    def test_read_timeout(self):
        """Test that if an exception is thrown before log due to a timeout, it is logged"""
        # reuse the request from getWithoutQueryParams
        test_path = "/v1/get"  # relative url through which the request should be sent
        logger = TestLogger()

        response_body = read_resource("notFound.html")
        handler = self.create_handler(response_code=404, body=response_body,
                                      additional_headers=(("Content-Type", "text/html"),))

        def delayed_response(*args, **kwargs):
            time.sleep(0.100)
            handler(*args, **kwargs)

        with create_server_listening(delayed_response) as address:  # start server to listen to request
            with create_communicator(address, socket_timeout=0.05) as communicator:  # create communicator under test
                communicator.enable_logging(logger)
                with self.assertRaises(CommunicationException):
                    communicator.get('/v1/get', None, None, GenericObject, None)

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertEqual(2, len(logger.entries))
        # for request and response, check that the message exists in the logs and there is an error in the response
        request_entry = logger.entries[0]
        self.assertIsNotNone(request_entry[0])
        self.assertIsNone(request_entry[1])
        response_entry = logger.entries[1]
        self.assertIsNotNone(response_entry[0])
        self.assertIsNotNone(response_entry[1])
        # for request and error, check that their output is as predicted and that they match each other
        self.assertRequestAndError(request_entry[0], response_entry[0], "getWithoutQueryParams")
        self.assertIsInstance(response_entry[1], Timeout, "logger should have logged a timeout error")

    def test_log_request_only(self):
        """Test that a request can be logged separately by disabling log between request and response"""
        # reuse the request and response from getWithoutQueryParams
        test_path = "/v1/get"  # relative url through which the request should be sent
        logger = TestLogger()

        response_body = read_resource("getWithoutQueryParams.json")
        handler = self.create_handler(response_code=200, body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))

        def disable_logging_response(*args, **kwargs):  # handler that disables the log of the communicator
            self.communicator.disable_logging()  # before responding
            handler(*args, **kwargs)

        with create_server_listening(disable_logging_response) as address:  # start server to listen to request
            with create_communicator(address) as communicator:  # create communicator under test
                self.communicator = communicator
                communicator.enable_logging(logger)
                response = communicator.get('/v1/get', None, None, GenericObject, None)

        self.assertEqual("OK", response.content['result'])
        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertEqual(1, len(logger.entries))
        # check that the request message exists in the logs and there are no errors
        request_entry = logger.entries[0]
        self.assertIsNotNone(request_entry[0])
        self.assertIsNone(request_entry[1],
                          "Error '{}' logged that should not have been thrown".format(request_entry[1]))
        # check that the request is formatted correctly
        self.assertRequest(request_entry[0], "getWithoutQueryParams")

    def test_log_response_only(self):
        """Test that a response can be logged separately by enabling log between request and response"""
        # reuse the request and response from getWithoutQueryParams
        test_path = "/v1/get"  # relative url through which the request should be sent
        logger = TestLogger()

        response_body = read_resource("getWithoutQueryParams.json")
        handler = self.create_handler(response_code=200, body=response_body,
                                      additional_headers=(("Content-Type", "application/json"),))

        def enable_logging_response(*args, **kwargs):  # handler that enables the log of the communicator
            self.communicator.enable_logging(logger)  # before responding
            handler(*args, **kwargs)

        with create_server_listening(enable_logging_response) as address:  # start server to listen to request
            with create_communicator(address) as communicator:  # create communicator under test
                self.communicator = communicator
                response = communicator.get('/v1/get', None, None, GenericObject, None)

        self.assertEqual("OK", response.content['result'])
        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertEqual(1, len(logger.entries))
        # check that the response message exists in the logs and there are no errors
        response_entry = logger.entries[0]
        self.assertIsNotNone(response_entry[0])
        self.assertIsNone(response_entry[1],
                          "Error '{}' logged that should not have been thrown".format(response_entry[1]))
        # check that the response is formatted correctly
        self.assertResponse(response_entry[0], "getWithoutQueryParams")

    def test_log_error_only(self):
        """Test that an error can be logged separately by enabling log between request and response"""
        # reuse the request from getWithoutQueryParams
        test_path = "/v1/get"  # relative url through which the request should be sent
        logger = TestLogger()

        response_body = read_resource("notFound.html")
        handler = self.create_handler(response_code=404, body=response_body,
                                      additional_headers=(("Content-Type", "text/html"),))

        def enable_logging_late_response(*args, **kwargs):  # handler that enables the log of the communicator
            self.communicator.enable_logging(logger)  # and waits for a timeout before responding
            time.sleep(0.1)
            handler(*args, **kwargs)

        with create_server_listening(enable_logging_late_response) as address:  # start server to listen to request
            with create_communicator(address, connect_timeout=0.500, socket_timeout=0.050) as communicator:
                self.communicator = communicator
                with self.assertRaises(CommunicationException):
                    communicator.get('/v1/get', None, None, GenericObject, None)

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertEqual(1, len(logger.entries))
        # check that the response message exists in the logs and there are no errors
        error_entry = logger.entries[0]
        self.assertIsNotNone(error_entry[0])
        self.assertIsNotNone(error_entry[1])
        # check that the error is formatted correctly
        self.assertError(error_entry[0])
        self.assertIsInstance(error_entry[1], Timeout,
                              "logger should have logged a timeout error, logged {} instead".format(error_entry[1]))

    def assertLogsRequestAndResponse(self, logger, request_resource_prefix, response_resource_prefix=None):
        """Assert that the logs of the logger contain both request and response and no errors,
        then check that the request and response match using "assertRequestAndResponse"
        """
        if response_resource_prefix is None:
            response_resource_prefix = request_resource_prefix
        self.assertEqual(2, len(logger.entries))
        # for request and response, check that the message exists in the logs and there are no errors
        request_entry = logger.entries[0]
        self.assertIsNotNone(request_entry[0])
        self.assertIsNone(request_entry[1],
                          "Error '{}' logged that should not have been thrown".format(request_entry[1]))
        response_entry = logger.entries[1]
        self.assertIsNotNone(response_entry[0])
        self.assertIsNone(response_entry[1],
                          "Error '{}' logged that should not have been thrown".format(response_entry[1]))
        # for request and response, check that their output is as predicted and that they match each other
        self.assertRequestAndResponse(request_entry[0], response_entry[0],
                                      request_resource_prefix, response_resource_prefix)

    def assertRequestAndResponse(self, request_message, response_message,
                                 request_resource_prefix, response_resource_prefix=None):
        """Assert that the request and response messages match the request and response regular expressions stored in
        'request_resource_prefix'.request and 'response_resource_prefix'.response respectively.

        If response_resource_prefix is not given it is assumed to be equal to request_resource_prefix"""
        if response_resource_prefix is None:
            response_resource_prefix = request_resource_prefix
        request_id = self.assertRequest(request_message, request_resource_prefix)
        self.assertResponse(response_message, response_resource_prefix, request_id)

    def assertRequestAndError(self, request_message, error_message, resource_prefix):
        """Assert that the request message matches the request regular expression stored in 'resource_prefix.request'
        and the error is a valid error message and refers to the request"""
        request_id = self.assertRequest(request_message, resource_prefix)
        self.assertError(error_message, request_id)

    def assertRequest(self, request_message, request_resource_prefix):
        """Assert that the request message matches the regex stored in 'request_resource_prefix'.request

        :param request_message: the request message to match
        :param request_resource_prefix: prefix of the regex file location,
        it will be appended with '.request' to obtain the file location
        :return: the request_id for use in matching the corresponding response or error
        """
        request_resource = request_resource_prefix + "_request"
        regex = globals()[request_resource](request_message, self)
        if type(regex) == type(""):
            request_pattern = re.compile(regex, re.DOTALL)
            match = request_pattern.match(request_message.get_message())
            print(globals()[request_resource])
            if match is None:
                raise AssertionError("request message '" + request_message.get_message() +
                                     "' does not match pattern " + str(request_pattern))
            self.assertRegex(request_message, request_pattern)
            return match.group(1)
        return regex[0]

    def assertResponse(self, response_message, response_resource_prefix, request_id=None):
        """Assert that the response message matches the regex stored in 'response_resource_prefix'.response

        :param response_message: the response message to match
        :param response_resource_prefix: prefix of the regex file location,
        it will be appended with '.response' to obtain the file location
        :param request_id: if a request_id is provided, it is matched against the response_id found in the response,
        failing the assert if not equal
        """
        response_resource = response_resource_prefix + "_response"
        # for each response call the corresponding asserting function
        regex = globals()[response_resource](response_message, self)
        if type(regex) == type(""):
            response_pattern = re.compile(regex, re.DOTALL)
            match = response_pattern.match(response_message.get_message())
            if match is None:
                raise AssertionError("response message '" + response_message.get_message() +
                                     "' does not match pattern " + str(response_pattern))
            if request_id is not None:
                self.assertEqual(request_id, match.group(1),
                                 "request_id '{0}' does not match response_id '{1}'".format(request_id, match.group(1)))

    def assertError(self, error_message, request_id=None):
        """Assert that the error message matches the regex stored in 'generic.error'

        :param error_message: the error message to match
        :param request_id: if a request_id is provided, it is matched against the error_id found in the error,
        failing the assert if not equal
        """
        error_resource = "generic_error"
        error_pattern_string = globals()[error_resource]()
        error_pattern = re.compile(error_pattern_string, re.DOTALL)
        match = error_pattern.match(error_message)
        if match is None:
            raise AssertionError("response message '" + error_message +
                                 "' does not match pattern " + str(error_pattern_string))
        if request_id is not None:
            self.assertEqual(request_id, match.group(1),
                             "request_id '{0}' does not match error_id '{1}'".format(request_id, match.group(1)))

    def assertHeaderIn(self, _tuple, _list):
        # If tuple has incorrect number of elements, assume it is not in the list
        self.assertIn((_tuple[0].lower(), _tuple[1]),
                      list(map((lambda el: (el[0].lower(), el[1])), _list)))

    def create_handler(self, response_code=200, body='',  # path='',
                       additional_headers=()):
        """Creates a request handler that receives the request on the server side

        :param response_code: status code of the desired response
        :param body: the body of the response message to return, it should be in json format
        :param additional_headers: additional headers that are added to the handler's response
        If the request is sent through the proper path, self.request_successful will be set to true, false otherwise
        """

        def handler_func(handler):
            self.request_path = handler.path  # record if the request was sent through the expected path
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


def create_post_request():
    """Creates a commonly used request for testing"""
    return {'card': {'cvv': '123', 'cardNumber': '1234567890123456', 'expiryDate': '1220'}}


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


# reads a file names file_name stored under resources/communication
def read_resource(file_name): return file_utils.read_file(os.path.join("communication", file_name))


# ------------------------ REGEX SOURCES ------------------


def getWithQueryParams_request(request, test):
    test.assertEqual(request.method, "GET")
    test.assertEqual(request.uri, '/v1/get?source=EUR&target=USD&amount=1000')

    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertTrue(len(list(filter((lambda header: header[0] == 'X-GCS-ServerMetaInfo'), headers))))

    test.assertIsNone(request.body)

    return request.request_id, False


def getWithQueryParams_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 200)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertEqual(response.content_type, 'application/json')
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False


def postWithBadRequestResponse_request(request, test):
    test.assertEqual(request.method, "POST")
    test.assertEqual(request.uri, '/v1/bad-request')

    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertTrue(len(list(filter((lambda header: header[0] == 'X-GCS-ServerMetaInfo'), headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)

    test.assertEqual(request.content_type, 'application/json')

    test.assertIsNotNone(request.body)
    test.assertTrue(len(request.body))

    return request.request_id, False


def postWithBadRequestResponse_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 400)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertEqual(response.content_type, 'application/json')
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False


def postWithCreatedResponse_request(request, test):
    test.assertEqual(request.method, "POST")
    test.assertEqual(request.uri, '/v1/created')

    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertTrue(len(list(filter((lambda header: header[0] == 'X-GCS-ServerMetaInfo'), headers))))
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
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertHeaderIn(('Location', '"http://localhost/v1/created/000000123410000595980000100001"'), headers)
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False


def deleteWithVoidResponse_request(request, test):
    test.assertEqual(request.method, "DELETE")
    test.assertEqual(request.uri, '/v1/void')

    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertTrue(len(list(filter((lambda header: header[0] == 'X-GCS-ServerMetaInfo'), headers))))

    return request.request_id, False


def deleteWithVoidResponse_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 204)
    test.assertIsNone(response.content_type)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertIsNone(response.body)
    return response.request_id, False


def generic_error():
    return r"""Error\ occurred\ for\ outgoing\ request\ \(requestId\=\'([-a-zA-Z0-9]+)\'\,\ \d+\ s\)"""


def notFound_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 404)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertHeaderIn(('Content-Type', '"text/html"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertEqual(response.content_type, 'text/html')
    test.assertIsNotNone(response.body)
    test.assertEqual(response.body, "Not Found")
    return response.request_id, False


def getWithoutQueryParams_request(request, test):
    test.assertEqual(request.method, "GET")
    test.assertEqual(request.uri, '/v1/get')

    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertTrue(len(list(filter((lambda header: header[0] == 'X-GCS-ServerMetaInfo'), headers))))

    return request.request_id, False


def getWithoutQueryParams_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 200)
    test.assertEqual(response.content_type, 'application/json')
    headers = response.get_header_list()
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False


def unknownServerError_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 500)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertEqual(response.content_type, 'application/json')
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False


if __name__ == '__main__':
    unittest.main()
