from datetime import datetime, timedelta, timezone
from typing import Any, Iterable, List, Mapping, Optional, Type, Union
from urllib.parse import quote, urlparse, ParseResult

from .call_context import CallContext
from .i_communicator import ICommunicator, BinaryResponse

from onlinepayments.sdk.authentication.authenticator import Authenticator
from onlinepayments.sdk.communication.communication_exception import CommunicationException
from onlinepayments.sdk.communication.connection import Connection, Response
from onlinepayments.sdk.communication.not_found_exception import NotFoundException
from onlinepayments.sdk.communication.pooled_connection import PooledConnection
from onlinepayments.sdk.communication.i_metadata_provider import IMetadataProvider
from onlinepayments.sdk.communication.multipart_form_data_object import MultipartFormDataObject
from onlinepayments.sdk.communication.multipart_form_data_request import MultipartFormDataRequest
from onlinepayments.sdk.communication.param_request import ParamRequest
from onlinepayments.sdk.communication.request_header import RequestHeader
from onlinepayments.sdk.communication.request_param import RequestParam
from onlinepayments.sdk.communication.response_exception import ResponseException
from onlinepayments.sdk.communication.response_header import get_header_value
from onlinepayments.sdk.domain.data_object import DataObject
from onlinepayments.sdk.json.marshaller import Marshaller, T
from onlinepayments.sdk.log.body_obfuscator import BodyObfuscator
from onlinepayments.sdk.log.communicator_logger import CommunicatorLogger
from onlinepayments.sdk.log.header_obfuscator import HeaderObfuscator


class Communicator(ICommunicator):
    """
    Used to communicate with the Online Payments platform web services.

    It contains all the logic to transform a request object to an HTTP request and an HTTP response to a response object.
    """

    def __init__(self, api_endpoint: Union[str, ParseResult], connection: Connection, authenticator: Authenticator,
                 metadata_provider: IMetadataProvider, marshaller: Marshaller):
        if api_endpoint is None:
            raise ValueError("api_endpoint is required")
        if isinstance(api_endpoint, str):
            api_endpoint = urlparse(api_endpoint)
        if api_endpoint.scheme.lower() not in ["http", "https"] or not api_endpoint.netloc:
            raise ValueError("invalid api_endpoint: " + str(api_endpoint))
        if api_endpoint.path:
            raise ValueError("api_endpoint should not contain a path")
        if api_endpoint.username is not None or api_endpoint.query or api_endpoint.fragment:
            raise ValueError("api_endpoint should not contain user info, query or fragment")
        if connection is None:
            raise ValueError("connection is required")
        if authenticator is None:
            raise ValueError("authenticator is required")
        if metadata_provider is None:
            raise ValueError("metadata_provider is required")
        if marshaller is None:
            raise ValueError("marshaller is required")
        self.__api_endpoint = api_endpoint
        self.__connection = connection
        self.__authenticator = authenticator
        self.__metadata_provider = metadata_provider
        self.__marshaller = marshaller

    def close(self) -> None:
        """
        Releases any system resources associated with this object.
        """
        self.__connection.close()

    def _get_with_binary_response(self, relative_path: str, request_headers: Optional[List[RequestHeader]],
                                  request_parameters: Optional[ParamRequest],
                                  context: Optional[CallContext]) -> Response:
        if request_parameters is None:
            request_parameter_list = None
        else:
            request_parameter_list = request_parameters.to_request_parameters()
        uri = self._to_absolute_uri(relative_path, request_parameter_list)
        if request_headers is None:
            request_headers = []
        self._add_generic_headers("GET", uri, request_headers, context)

        return self.__connection.get(uri, request_headers)

    def get_with_binary_response(self, relative_path: str, request_headers: Optional[List[RequestHeader]],
                                 request_parameters: Optional[ParamRequest],
                                 context: Optional[CallContext]) -> BinaryResponse:
        """
        Corresponds to the HTTP GET method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param context: The optional call context to use.
        :raise CommunicationException: when an exception occurred communicating with the Online Payments platform
        :raise ResponseException: when an error response was received from the Online Payments platform
        """
        (status, headers, chunks) = self._get_with_binary_response(relative_path, request_headers, request_parameters, context)
        return self._process_binary_response(status, chunks, headers, relative_path, context)

    def get(self, relative_path: str, request_headers: Optional[List[RequestHeader]],
            request_parameters: Optional[ParamRequest],
            response_type: Type[T],
            context: Optional[CallContext]) -> T:
        """
        Corresponds to the HTTP GET method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param response_type: The type of response to return.
        :param context: The optional call context to use.
        :raise CommunicationException: when an exception occurred communicating with the Online Payments platform
        :raise ResponseException: when an error response was received from the Online Payments platform
        """
        (status, headers, chunks) = self._get_with_binary_response(relative_path, request_headers, request_parameters, context)
        return self._process_response(status, chunks, headers, relative_path, response_type, context)

    def _delete_with_binary_response(self, relative_path: str, request_headers: Optional[List[RequestHeader]],
                                     request_parameters: Optional[ParamRequest],
                                     context: Optional[CallContext]) -> Response:
        if request_parameters is None:
            request_parameter_list = None
        else:
            request_parameter_list = request_parameters.to_request_parameters()
        uri = self._to_absolute_uri(relative_path, request_parameter_list)
        if request_headers is None:
            request_headers = []
        self._add_generic_headers("DELETE", uri, request_headers, context)

        return self.__connection.delete(uri, request_headers)

    def delete_with_binary_response(self, relative_path: str, request_headers: Optional[List[RequestHeader]],
                                    request_parameters: Optional[ParamRequest],
                                    context: Optional[CallContext]) -> BinaryResponse:
        """
        Corresponds to the HTTP DELETE method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param context: The optional call context to use.
        :raise CommunicationException: when an exception occurred communicating with the Online Payments platform
        :raise ResponseException: when an error response was received from the Online Payments platform
        """
        (status, headers, chunks) = self._delete_with_binary_response(relative_path, request_headers, request_parameters, context)
        return self._process_binary_response(status, chunks, headers, relative_path, context)

    def delete(self, relative_path: str, request_headers: Optional[List[RequestHeader]],
               request_parameters: Optional[ParamRequest],
               response_type: Type[T],
               context: Optional[CallContext]) -> T:
        """
        Corresponds to the HTTP DELETE method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param response_type: The type of response to return.
        :param context: The optional call context to use.
        :raise CommunicationException: when an exception occurred communicating with the Online Payments platform
        :raise ResponseException: when an error response was received from the Online Payments platform
        """
        (status, headers, chunks) = self._delete_with_binary_response(relative_path, request_headers, request_parameters, context)
        return self._process_response(status, chunks, headers, relative_path, response_type, context)

    def _post_with_binary_response(self, relative_path: str, request_headers: Optional[List[RequestHeader]],
                                   request_parameters: Optional[ParamRequest],
                                   request_body: Any,
                                   context: Optional[CallContext]) -> Response:
        if request_parameters is None:
            request_parameter_list = None
        else:
            request_parameter_list = request_parameters.to_request_parameters()
        uri = self._to_absolute_uri(relative_path, request_parameter_list)
        if request_headers is None:
            request_headers = []

        body = None
        if isinstance(request_body, MultipartFormDataObject):
            request_headers.append(RequestHeader("Content-Type", request_body.content_type))
            body = request_body
        elif isinstance(request_body, MultipartFormDataRequest):
            multipart = request_body.to_multipart_form_data_object()
            request_headers.append(RequestHeader("Content-Type", multipart.content_type))
            body = multipart
        elif request_body is not None:
            request_headers.append(RequestHeader("Content-Type", "application/json"))
            body = self.__marshaller.marshal(request_body)

        self._add_generic_headers("POST", uri, request_headers, context)
        return self.__connection.post(uri, request_headers, body)

    def post_with_binary_response(self, relative_path: str, request_headers: Optional[List[RequestHeader]],
                                  request_parameters: Optional[ParamRequest], request_body: Any,
                                  context: Optional[CallContext]) -> BinaryResponse:
        """
        Corresponds to the HTTP POST method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param request_body: The optional request body to send.
        :param context: The optional call context to use.
        :raise CommunicationException: when an exception occurred communicating with the Online Payments platform
        :raise ResponseException: when an error response was received from the Online Payments platform
        """
        (status, headers, chunks) = self._post_with_binary_response(relative_path, request_headers, request_parameters, request_body, context)
        return self._process_binary_response(status, chunks, headers, relative_path, context)

    def post(self, relative_path: str, request_headers: Optional[List[RequestHeader]],
             request_parameters: Optional[ParamRequest], request_body: Any,
             response_type: Type[T],
             context: Optional[CallContext]) -> T:
        """
        Corresponds to the HTTP POST method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param request_body: The optional request body to send.
        :param response_type: The type of response to return.
        :param context: The optional call context to use.
        :raise CommunicationException: when an exception occurred communicating with the Online Payments platform
        :raise ResponseException: when an error response was received from the Online Payments platform
        """
        (status, headers, chunks) = self._post_with_binary_response(relative_path, request_headers, request_parameters, request_body, context)
        return self._process_response(status, chunks, headers, relative_path, response_type, context)

    def _put_with_binary_response(self, relative_path: str, request_headers: Optional[List[RequestHeader]],
                                  request_parameters: Optional[ParamRequest], request_body: Any,
                                  context: Optional[CallContext]) -> Response:
        if request_parameters is None:
            request_parameter_list = None
        else:
            request_parameter_list = request_parameters.to_request_parameters()
        uri = self._to_absolute_uri(relative_path, request_parameter_list)
        if request_headers is None:
            request_headers = []

        body = None
        if isinstance(request_body, MultipartFormDataObject):
            request_headers.append(RequestHeader("Content-Type", request_body.content_type))
            body = request_body
        elif isinstance(request_body, MultipartFormDataRequest):
            multipart = request_body.to_multipart_form_data_object()
            request_headers.append(RequestHeader("Content-Type", multipart.content_type))
            body = multipart
        elif request_body is not None:
            request_headers.append(RequestHeader("Content-Type", "application/json"))
            body = self.__marshaller.marshal(request_body)

        self._add_generic_headers("PUT", uri, request_headers, context)
        return self.__connection.put(uri, request_headers, body)

    def put_with_binary_response(self, relative_path: str, request_headers: Optional[List[RequestHeader]],
                                 request_parameters: Optional[ParamRequest], request_body: Any,
                                 context: Optional[CallContext]) -> BinaryResponse:
        """
        Corresponds to the HTTP PUT method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param request_body: The optional request body to send.
        :param context: The optional call context to use.
        :raise CommunicationException: when an exception occurred communicating with the Online Payments platform
        :raise ResponseException: when an error response was received from the Online Payments platform
        """
        (status, headers, chunks) = self._put_with_binary_response(relative_path, request_headers, request_parameters, request_body, context)
        return self._process_binary_response(status, chunks, headers, relative_path, context)

    def put(self, relative_path: str, request_headers: Optional[List[RequestHeader]],
            request_parameters: Optional[ParamRequest], request_body: Any,
            response_type: Type[T],
            context: Optional[CallContext]) -> T:
        """
        Corresponds to the HTTP PUT method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param request_body: The optional request body to send.
        :param response_type: The type of response to return.
        :param context: The optional call context to use.
        :raise CommunicationException: when an exception occurred communicating with the Online Payments platform
        :raise ResponseException: when an error response was received from the Online Payments platform
        """
        (status, headers, chunks) = self._put_with_binary_response(relative_path, request_headers, request_parameters, request_body, context)
        return self._process_response(status, chunks, headers, relative_path, response_type, context)

    @property
    def marshaller(self) -> Marshaller:
        """
        :return: The Marshaller object associated with this communicator. Never None.
        """
        return self.__marshaller

    def _to_absolute_uri(self, relative_path: str, request_parameters: List[RequestParam]) -> ParseResult:
        if relative_path.startswith("/"):
            absolute_path = relative_path
        else:
            absolute_path = "/" + relative_path
        uri = self.__api_endpoint.geturl() + absolute_path
        separator = "?"
        if request_parameters is not None:
            for nvp in request_parameters:
                uri += separator
                uri += quote(nvp.name) + "=" + quote(nvp.value)
                separator = "&"
        # no need to revalidate that uri has a valid scheme and netloc
        return urlparse(uri)

    def _add_generic_headers(self, http_method: str, uri: ParseResult, request_headers: List[RequestHeader],
                             context: Optional[CallContext]) -> None:
        """
        Adds the necessary headers to the given list of headers. This includes
        the authorization header, which uses other headers, so when you need to
        override this method, make sure to call super.addGenericHeaders at the
        end of your overridden method.
        """
        # add server meta info header
        request_headers.extend(self.__metadata_provider.metadata_headers)
        # add date header
        request_headers.append(RequestHeader("Date", self._get_header_date_string()))
        if context is not None and context.idempotence_key is not None:
            # add context specific headers
            request_headers.append(RequestHeader("X-GCS-Idempotence-Key", context.idempotence_key))
        # add authorization
        authenticator = self.__authenticator
        authorization = authenticator.get_authorization(http_method, uri, request_headers)
        request_headers.append(RequestHeader("Authorization", authorization))

    @staticmethod
    def _get_header_date_string() -> str:
        """
        Returns the date in the preferred format for the HTTP date header.
        """
        date_format_utc = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
        return date_format_utc

    @staticmethod
    def __collect_chunks(chunks: Iterable[bytes]) -> str:
        collected_body = b""
        for chunk in chunks:
            collected_body += chunk
        return collected_body.decode('utf-8')

    def _process_binary_response(self, status: int, chunks: Iterable[bytes], headers: Mapping[str, str], request_path: str,
                                 context: Optional[CallContext]) -> BinaryResponse:
        if context is not None:
            self._update_context(headers, context)
        self._throw_exception_if_necessary_binary(status, chunks, headers, request_path)
        return headers, chunks

    def _process_response(self, status: int, chunks: Iterable[bytes], headers: Mapping[str, str], request_path: str,
                          response_type: Type[T],
                          context: Optional[CallContext]) -> T:
        if context is not None:
            self._update_context(headers, context)
        body = self.__collect_chunks(chunks)
        self._throw_exception_if_necessary(status, body, headers, request_path)
        return self.__marshaller.unmarshal(body, response_type)

    @staticmethod
    def _update_context(headers: Mapping[str, str], context: Optional[CallContext]) -> None:
        """
        Updates the given call context based on the contents of the given response.
        """
        idempotence_request_timestamp_value = get_header_value(headers, "X-GCS-Idempotence-Request-Timestamp")
        if idempotence_request_timestamp_value is not None:
            idempotence_request_timestamp = int(idempotence_request_timestamp_value)
            context.idempotence_request_timestamp = idempotence_request_timestamp
        else:
            context.idempotence_request_timestamp = None
        idempotence_response_date_time_value = get_header_value(headers, "IdempotencyResponseDatetime")
        if idempotence_response_date_time_value is not None:
            idempotence_response_date_time = DataObject.parse_datetime(idempotence_response_date_time_value)
            context.idempotence_response_date_time = idempotence_response_date_time
        else:
            context.idempotence_response_date_time = None

    def _throw_exception_if_necessary_binary(self, status: int, chunks: Iterable[bytes], headers: Mapping[str, str], request_path: str) -> None:
        """
        Checks the Response for errors and throws an exception if necessary.
        """
        # status codes in the 100 or 300 range are not expected
        if status < 200 or status >= 300:
            body = self.__collect_chunks(chunks)
            self.__throw_exception(status, body, headers, request_path)

    def _throw_exception_if_necessary(self, status: int, body: str, headers: Mapping[str, str], request_path: str) -> None:
        """
        Checks the Response for errors and throws an exception if necessary.
        """
        # status codes in the 100 or 300 range are not expected
        if status < 200 or status >= 300:
            self.__throw_exception(status, body, headers, request_path)

    def __throw_exception(self, status: int, body: str, headers: Mapping[str, str], request_path: str) -> None:
        if body is not None and not self.__is_json(headers):
            cause = ResponseException(status, body, headers)
            if status == 404:
                raise NotFoundException(cause, "The requested resource was not found; invalid path: " + request_path)
            else:
                raise CommunicationException(cause)
        else:
            raise ResponseException(status, body, headers)

    @staticmethod
    def __is_json(headers: Mapping[str, str]) -> bool:
        content_type = get_header_value(headers, "Content-Type")
        if content_type is None:
            return True
        content_type = content_type.lower()
        return ("application/json" == content_type) or \
               ("application/problem+json" == content_type) or \
               (content_type.startswith("application/json")) or \
               (content_type.startswith("application/problem+json"))

    def close_idle_connections(self, idle_time: timedelta) -> None:
        """
        Utility method that delegates the call to this communicator's connection
        if that's an instance of PooledConnection. If not this method does nothing.

        :param idle_time: a datetime.timedelta object indicating the idle time
        """
        if isinstance(self.__connection, PooledConnection):
            self.__connection.close_idle_connections(idle_time)

    def close_expired_connections(self) -> None:
        """
        Utility method that delegates the call to this communicator's connection
        if that's an instance of PooledConnection. If not this method does nothing.
        """
        if isinstance(self.__connection, PooledConnection):
            self.__connection.close_expired_connections()

    def set_body_obfuscator(self, body_obfuscator: BodyObfuscator) -> None:
        # delegate to the connection
        self.__connection.set_body_obfuscator(body_obfuscator)

    def set_header_obfuscator(self, header_obfuscator: HeaderObfuscator) -> None:
        # delegate to the connection
        self.__connection.set_header_obfuscator(header_obfuscator)

    def enable_logging(self, communicator_logger: CommunicatorLogger) -> None:
        # delegate to the connection
        self.__connection.enable_logging(communicator_logger)

    def disable_logging(self) -> None:
        # delegate to the connection
        self.__connection.disable_logging()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
