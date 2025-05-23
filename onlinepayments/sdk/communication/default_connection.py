import math
import uuid
from datetime import datetime, timedelta
from typing import Mapping, Optional, Sequence
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from requests.models import PreparedRequest
from requests.exceptions import RequestException, Timeout
from requests_toolbelt import MultipartEncoder

from .communication_exception import CommunicationException
from .connection import RequestBody, Response, URI
from .multipart_form_data_object import MultipartFormDataObject
from .pooled_connection import PooledConnection
from .request_header import RequestHeader
from .response_header import get_header_value

from onlinepayments.sdk.communicator_configuration import CommunicatorConfiguration
from onlinepayments.sdk.proxy_configuration import ProxyConfiguration
from onlinepayments.sdk.log.body_obfuscator import BodyObfuscator
from onlinepayments.sdk.log.communicator_logger import CommunicatorLogger
from onlinepayments.sdk.log.header_obfuscator import HeaderObfuscator
from onlinepayments.sdk.log.request_log_message import RequestLogMessage
from onlinepayments.sdk.log.response_log_message import ResponseLogMessage

CHARSET = "UTF-8"


class DefaultConnection(PooledConnection):
    """
    Provides an HTTP request interface, thread-safe

    :param connect_timeout: timeout in seconds before a pending connection is dropped
    :param socket_timeout: timeout in seconds before dropping an established connection.
     This is the time the server is allowed for a response
    :param max_connections: the maximum number of connections in the connection pool
    :param proxy_configuration: ProxyConfiguration object that contains data about proxy settings if present.
     It should be writeable as string and have a scheme attribute.

    Use the methods get, delete, post and put to perform the corresponding HTTP request.
    Alternatively you can use request with the request method as the first parameter.

    URI, headers and body should be given on a per-request basis.
    """

    def __init__(self, connect_timeout: int, socket_timeout: int,
                 max_connections: int = CommunicatorConfiguration.DEFAULT_MAX_CONNECTIONS,
                 proxy_configuration: Optional[ProxyConfiguration] = None):
        self.logger = None
        self.__requests_session = requests.session()
        self.__requests_session.mount("http://", HTTPAdapter(pool_maxsize=max_connections,
                                                             pool_connections=1))
        self.__requests_session.mount("https://", HTTPAdapter(pool_maxsize=max_connections,
                                                              pool_connections=1))
        # request timeouts are in seconds
        self.__connect_timeout = connect_timeout if connect_timeout >= 0 else None
        self.__socket_timeout = socket_timeout if socket_timeout >= 0 else None
        if proxy_configuration:
            proxy = {
                "http": str(proxy_configuration),
                "https": str(proxy_configuration)
            }
            self.__requests_session.proxies = proxy

        self.__body_obfuscator = BodyObfuscator.default_body_obfuscator()
        self.__header_obfuscator = HeaderObfuscator.default_header_obfuscator()

    @property
    def connect_timeout(self) -> Optional[int]:
        """Connection timeout in seconds"""
        return self.__connect_timeout

    @property
    def socket_timeout(self) -> Optional[int]:
        """Socket timeout in seconds"""
        return self.__socket_timeout

    def get(self, url: URI, request_headers: Sequence[RequestHeader]) -> Response:
        """Perform a request to the server given by url

        :param url: the url to the server, given as a parsed url
        :param request_headers: a sequence containing RequestHeader objects representing the request headers
        """
        return self._request('get', url, request_headers)

    def delete(self, url: URI, request_headers: Sequence[RequestHeader]) -> Response:
        """Perform a request to the server given by url

        :param url: the url to the server, given as a parsed url
        :param request_headers: a sequence containing RequestHeader objects representing the request headers
        """
        return self._request('delete', url, request_headers)

    def post(self, url: URI, request_headers: Sequence[RequestHeader], body: RequestBody) -> Response:
        """Perform a request to the server given by url

        :param url: the url to the server, given as a parsed url
        :param request_headers: a sequence containing RequestHeader objects representing the request headers
        :param body: the request body
        """
        if isinstance(body, MultipartFormDataObject):
            body = self.__to_multipart_encoder(body)
        return self._request('post', url, request_headers, body)

    def put(self, url: URI, request_headers: Sequence[RequestHeader], body: RequestBody) -> Response:
        """Perform a request to the server given by url

        :param url: the url to the server, given as a parsed url
        :param request_headers: a sequence containing RequestHeader objects representing the request headers
        :param body: the request body
        """
        if isinstance(body, MultipartFormDataObject):
            body = self.__to_multipart_encoder(body)
        return self._request('put', url, request_headers, body)

    @staticmethod
    def __to_multipart_encoder(multipart: MultipartFormDataObject) -> MultipartEncoder:
        fields = {}
        for name, value in multipart.values.items():
            fields[name] = value
        for name, uploadable_file in multipart.files.items():
            fields[name] = (uploadable_file.file_name, uploadable_file.content, uploadable_file.content_type)
        encoder = MultipartEncoder(fields=fields,
                                   boundary=multipart.boundary)
        if encoder.content_type != multipart.content_type:
            raise ValueError("MultipartEncoder did not create the expected content type")
        return encoder

    class _ToResult(object):
        def __call__(self, func):
            def _wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                header = next(result)
                return header + (result,)
            return _wrapper

    @_ToResult()
    def _request(self, method: str, url: URI, headers: Sequence[RequestHeader], body: RequestBody = None) -> Response:
        """
        Perform a request to the server given by url

        :param url: the url to the server, given as a parsed url
        :param headers: a sequence containing RequestHeader objects representing the request headers
        :param body: the request body
        """
        headers = {} if not headers else headers
        if not isinstance(url, str):
            url = url.geturl()

        # convert the sequence of RequestParam objects to a dictionary of key:value pairs if necessary
        if headers and not isinstance(headers, dict):
            headers = {param.name: param.value for param in headers}

        # send request with all parameters not declared in session and with callback for logging response
        request = requests.Request(method, url,
                                   headers=headers,
                                   data=body,
                                   hooks={'response': self._cb_log_response})
        prepped_request = self.__requests_session.prepare_request(request)
        # add timestamp to request for later reference
        prepped_request.timestamp = datetime.now()
        _id = str(uuid.uuid4())
        # store random id in request so it can be matched with its response in logging
        prepped_request.id = _id
        self._log_request(prepped_request)
        try:
            timeout_ = (self.__connect_timeout, self.__socket_timeout)
            requests_response = self.__requests_session.send(prepped_request,
                                                             timeout=timeout_,
                                                             stream=True)
            try:
                iterable = requests_response.iter_content(chunk_size=1024)
                yield requests_response.status_code, requests_response.headers
                for chunk in iterable:
                    yield chunk
            finally:
                requests_response.close()

        except Timeout as timeout:
            self._log_error(prepped_request.id, timeout, prepped_request.timestamp)
            raise CommunicationException(timeout)
        except RequestException as exception:
            self._log_error(prepped_request.id, exception, prepped_request.timestamp)
            raise CommunicationException(exception)
        except Exception as exception:
            self._log_error(prepped_request.id, exception, prepped_request.timestamp)
            raise

    def _log_request(self, request: PreparedRequest) -> None:
        """
        Log parameter request if logging is enabled at the moment of logging.
        Also adds a timestamp to the request for response logging
        """
        logger = self.logger
        if logger is None:
            return
        method = request.method
        url = urlparse(request.url)
        if url.query:
            local_path = url.path + "?" + url.query
        else:
            local_path = url.path
        try:
            message = RequestLogMessage(request_id=request.id,
                                        method=method,
                                        uri=local_path,
                                        body_obfuscator=self.__body_obfuscator,
                                        header_obfuscator=self.__header_obfuscator)
            for name in request.headers:
                message.add_header(name, request.headers[name])
            body = request.body
            if body:
                content = request.headers['Content-Type']
                if content != "application/json":
                    message.set_body(body, content, CHARSET)
                else:
                    message.set_body(body, content)
            logger.log_request(message)
        except Exception as exception:
            logger.log("An error occurred trying to log request '{}'".format(request.id), exception)

    def _cb_log_response(self, response: requests.models.Response, **kwargs) -> None:
        """Log parameter response if logging is enabled at the moment of logging"""
        logger = self.logger
        if logger is None:
            return
        request = response.request
        _id = request.id
        duration = math.ceil((datetime.now() - request.timestamp).total_seconds() * 1000)
        status_code = response.status_code
        try:
            message = ResponseLogMessage(request_id=_id,
                                         status_code=status_code,
                                         duration=duration,
                                         body_obfuscator=self.__body_obfuscator,
                                         header_obfuscator=self.__header_obfuscator)
            for name in response.headers:
                message.add_header(name, response.headers[name])
            if self.__is_binary(response.headers):
                body = "<binary content>"
            else:
                # The response is always encoded UTF8
                # When this is not specified anywhere, the response body will be encoded in the wrong way
                response.encoding = 'utf8'
                body = response.text
            if body:
                content = response.headers['Content-Type']
                message.set_body(body, content)
            logger.log_response(message)
        except Exception as exception:
            logger.log("An error occurred trying to log response '{}'".format(_id), exception)

    def _log_error(self, request_id: str, error: Exception, start_time: datetime) -> None:
        """Log communication errors when logging is enabled"""
        logger = self.logger
        if logger:
            duration = math.ceil((datetime.now() - start_time).total_seconds() * 1000)
            logger.log("Error occurred for outgoing request (requestId='{}', {} s)".format(request_id, duration), error)

    @staticmethod
    def __is_binary(headers: Mapping[str, str]) -> bool:
        content_type = get_header_value(headers, "Content-Type")
        if content_type is None:
            return False
        content_type = content_type.lower()
        return not (content_type.startswith("text/") or "json" in content_type or "xml" in content_type)

    def set_body_obfuscator(self, body_obfuscator: BodyObfuscator) -> None:
        self.__body_obfuscator = body_obfuscator

    def set_header_obfuscator(self, header_obfuscator: HeaderObfuscator) -> None:
        self.__header_obfuscator = header_obfuscator

    def enable_logging(self, communicator_logger: CommunicatorLogger) -> None:
        self.logger = communicator_logger

    def disable_logging(self) -> None:
        self.logger = None

    def close_idle_connections(self, idle_time: timedelta) -> None:
        """
        :param idle_time: a datetime.timedelta object indicating the idle time
        """
        pass

    def close_expired_connections(self) -> None:
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self) -> None:
        """
        Explicitly closes the connection
        """
        self.__requests_session.close()
