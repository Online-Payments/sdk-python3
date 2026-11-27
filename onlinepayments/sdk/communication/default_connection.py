import functools
import math
import gzip
import uuid
from datetime import datetime, timedelta
from collections.abc import Iterator, Mapping, Sequence
from typing import Any
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from requests.models import PreparedRequest
from requests.structures import CaseInsensitiveDict
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
                 proxy_configuration: ProxyConfiguration | None = None):
        if connect_timeout is None:
            raise ValueError("connect_timeout is required")
        if socket_timeout is None:
            raise ValueError("socket_timeout is required")
        self.logger: CommunicatorLogger | None = None
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
                "http": proxy_configuration.to_url(),
                "https": proxy_configuration.to_url()
            }
            self.__requests_session.proxies = proxy

        self.__body_obfuscator = BodyObfuscator.default_body_obfuscator()
        self.__header_obfuscator = HeaderObfuscator.default_header_obfuscator()

    @property
    def connect_timeout(self) -> int | None:
        """Connection timeout in seconds"""
        return self.__connect_timeout

    @property
    def socket_timeout(self) -> int | None:
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
        data: str | bytes | None
        if isinstance(body, MultipartFormDataObject):
            data = self.__to_multipart_encoder(body).to_string()
        else:
            data = body

        headers_dict = {h.name: h.value for h in (request_headers or [])}
        content_encoding = headers_dict.get('Content-Encoding') or headers_dict.get('content-encoding')

        if data is not None and content_encoding and 'gzip' in content_encoding.lower():
            if isinstance(data, str):
                data = data.encode("utf-8")
            data = gzip.compress(data)

        return self._request('post', url, request_headers, data)

    def put(self, url: URI, request_headers: Sequence[RequestHeader], body: RequestBody) -> Response:
        """Perform a request to the server given by url

        :param url: the url to the server, given as a parsed url
        :param request_headers: a sequence containing RequestHeader objects representing the request headers
        :param body: the request body
        """
        data: str | bytes | None
        if isinstance(body, MultipartFormDataObject):
            data = self.__to_multipart_encoder(body).to_string()
        else:
            data = body
        return self._request('put', url, request_headers, data)

    @staticmethod
    def __to_multipart_encoder(multipart: MultipartFormDataObject) -> MultipartEncoder:
        fields: dict[str, Any] = {}
        for name, value in multipart.values.items():
            fields[name] = value
        for name, uploadable_file in multipart.files.items():
            fields[name] = (uploadable_file.file_name, uploadable_file.content, uploadable_file.content_type)
        encoder = MultipartEncoder(fields=fields,
                                   boundary=multipart.boundary)
        if encoder.content_type != multipart.content_type:
            raise ValueError("MultipartEncoder did not create the expected content type")
        return encoder

    class _ToResult:
        def __call__(self, func):
            def _wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                header = next(result)
                return header + (result,)
            return _wrapper

    @_ToResult()
    def _request(self, method: str, url: URI, headers: Sequence[RequestHeader],
                 body: str | bytes | None = None) -> Iterator[tuple[int, CaseInsensitiveDict[str]] | bytes]:
        """
        Perform a request to the server given by url

        :param url: the url to the server, given as a parsed url
        :param headers: a sequence containing RequestHeader objects representing the request headers
        :param body: the request body
        """
        if not isinstance(url, str):
            url = url.geturl()

        headers_dict = {h.name: h.value for h in headers if h.value is not None} if headers else {}

        _id = str(uuid.uuid4())
        start_time = datetime.now()
        try:
            # send request with all parameters not declared in session and with callback for logging response
            request = requests.Request(method, url,
                                       headers=headers_dict,
                                       data=body,
                                       hooks={'response': functools.partial(self._cb_log_response,
                                                                            request_id=_id, start_time=start_time)})
            prepped_request = self.__requests_session.prepare_request(request)
            self._log_request(prepped_request, _id)
            timeout_ = (self.__connect_timeout, self.__socket_timeout)
            requests_response = self.__requests_session.send(prepped_request,
                                                             timeout=timeout_,
                                                             stream=True)
            try:
                iterable = requests_response.iter_content(chunk_size=1024)
                yield requests_response.status_code, requests_response.headers
                yield from iterable
            finally:
                requests_response.close()

        except Exception as exception:
            self._log_error(_id, exception, start_time)
            raise CommunicationException(exception) from exception

    def _log_request(self, request: PreparedRequest, request_id: str) -> None:
        """
        Log parameter request if logging is enabled at the moment of logging.
        """
        logger = self.logger
        if logger is None:
            return
        method = str(request.method)
        url = urlparse(str(request.url))
        if url.query:
            local_path = url.path + "?" + url.query
        else:
            local_path = url.path
        try:
            message = RequestLogMessage(request_id=request_id,
                                        method=method,
                                        uri=local_path,
                                        body_obfuscator=self.__body_obfuscator,
                                        header_obfuscator=self.__header_obfuscator)
            for name, value in request.headers.items():
                message.add_header(name, self.__to_str(value))
            body = request.body if isinstance(request.body, (str, bytes)) else None
            if isinstance(body, bytes) and 'gzip' in self.__to_str(request.headers.get('Content-Encoding', '')).lower():
                body = gzip.decompress(body).decode(CHARSET)
            if body:
                content = self.__to_str(request.headers['Content-Type'])
                if content != "application/json":
                    message.set_body(body, content, CHARSET)
                else:
                    message.set_body(body, content)
            logger.log_request(message)
        except Exception as exception:
            logger.log(f"An error occurred trying to log request '{request_id}'", exception)

    def _cb_log_response(self, response: requests.models.Response, request_id: str, start_time: datetime, **kwargs) -> None:
        """Log parameter response if logging is enabled at the moment of logging"""
        logger = self.logger
        if logger is None:
            return
        duration = math.ceil((datetime.now() - start_time).total_seconds() * 1000)
        status_code = response.status_code
        try:
            message = ResponseLogMessage(request_id=request_id,
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
            logger.log(f"An error occurred trying to log response '{request_id}'", exception)

    def _log_error(self, request_id: str, error: Exception, start_time: datetime) -> None:
        """Log communication errors when logging is enabled"""
        logger = self.logger
        if logger:
            duration = math.ceil((datetime.now() - start_time).total_seconds() * 1000)
            logger.log(f"Error occurred for outgoing request (requestId='{request_id}', {duration} ms)", error)

    @staticmethod
    def __to_str(value: str | bytes) -> str:
        return value.decode(CHARSET) if isinstance(value, bytes) else value

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
