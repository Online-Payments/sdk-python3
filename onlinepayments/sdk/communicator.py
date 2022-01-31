from datetime import datetime
from typing import Union, cast
from urllib.parse import ParseResult, ParseResultBytes, quote, urlparse

from onlinepayments.sdk.authenticator import Authenticator
from onlinepayments.sdk.communication_exception import CommunicationException
from onlinepayments.sdk.connection import Connection
from onlinepayments.sdk.defaultimpl.default_connection import DefaultConnection
from onlinepayments.sdk.defaultimpl.default_marshaller import DefaultMarshaller
from onlinepayments.sdk.log.logging_capable import LoggingCapable
from onlinepayments.sdk.marshaller import Marshaller
from onlinepayments.sdk.meta_data_provider import MetaDataProvider
from onlinepayments.sdk.not_found_exception import NotFoundException
from onlinepayments.sdk.pooled_connection import PooledConnection
from onlinepayments.sdk.request_header import RequestHeader
from onlinepayments.sdk.response_exception import ResponseException
from onlinepayments.sdk.response_header import get_header_value


class Communicator(LoggingCapable):
    """
    Used to communicate with the Online Payments platform web services.

    It contains all the logic to transform a request object to a HTTP request
    and a HTTP response to a response object.
    """

    def __init__(self,
                 api_endpoint: Union[str, ParseResult, ParseResultBytes],
                 authenticator: Authenticator,
                 meta_data_provider: MetaDataProvider,
                 connection: Connection = DefaultConnection(),
                 marshaller: Marshaller = DefaultMarshaller.INSTANCE()) -> None:
        if api_endpoint is None:
            raise ValueError("api_endpoint is required")
        if isinstance(api_endpoint, str):
            api_endpoint = urlparse(api_endpoint)
        if not api_endpoint.scheme.lower() in ["http", "https"] or not api_endpoint.netloc:
            raise ValueError("invalid api_endpoint: " + str(api_endpoint))
        if api_endpoint.path:
            raise ValueError("api_endpoint should not contain a path")
        if api_endpoint.username is not None or api_endpoint.query or api_endpoint.fragment:
            raise ValueError(
                "api_endpoint should not contain user info, query or fragment")
        if authenticator is None:
            raise ValueError("authenticator is required")
        if meta_data_provider is None:
            raise ValueError("meta_data_provider is required")
        if connection is None:
            raise ValueError("connection is required")
        if marshaller is None:
            raise ValueError("marshaller is required")
        self.__api_endpoint = api_endpoint
        self.__authenticator = authenticator
        self.__connection = connection
        self.__marshaller = marshaller
        self.__meta_data_provider = meta_data_provider

    def close(self):
        """Releases any system resources associated with this object."""
        self.connection.close()

    def _get(self, relative_path, request_headers, request_parameters, context):
        if request_parameters is None:
            request_parameter_list = None
        else:
            request_parameter_list = request_parameters.to_request_parameters()
        uri = self._to_absolute_uri(relative_path, request_parameter_list)
        if request_headers is None:
            request_headers = []
        self._add_generic_headers("GET", uri, request_headers, context)

        return self.connection.get(uri, request_headers)

    def get(self, relative_path, request_headers, request_parameters, response_type, context):
        """
        Corresponds to the HTTP GET method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param response_type: The type of response to return.
        :param context: The optional call context to use.
        :raise: CommunicationException when an exception occurred communicating with the Online Payments platform
        :raise: ResponseException when an error response was received from the Online Payments platform
        :raise: ApiException when an error response was received from the Online Payments platform which contained a list of errors
        """
        (status, headers, chunks) = self._get(relative_path, request_headers, request_parameters, context)
        return self._process_response(status, chunks, headers, relative_path, response_type, context)

    def _delete(self, relative_path, request_headers, request_parameters, context):
        if request_parameters is None:
            request_parameter_list = None
        else:
            request_parameter_list = request_parameters.to_request_parameters()
        uri = self._to_absolute_uri(relative_path, request_parameter_list)
        if request_headers is None:
            request_headers = []
        self._add_generic_headers("DELETE", uri, request_headers, context)

        return self.connection.delete(uri, request_headers)

    def delete(self, relative_path, request_headers, request_parameters, response_type, context):
        """
        Corresponds to the HTTP DELETE method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param response_type: The type of response to return.
        :param context: The optional call context to use.
        :raise: CommunicationException when an exception occurred communicating with the Online Payments platform
        :raise: ResponseException when an error response was received from the Online Payments platform
        :raise: ApiException when an error response was received from the Online Payments platform which contained a list of errors
        """
        (status, headers, chunks) = self._delete(relative_path, request_headers, request_parameters, context)
        return self._process_response(status, chunks, headers, relative_path, response_type, context)

    def _post(self, relative_path, request_headers, request_parameters, request_body, context):
        if request_parameters is None:
            request_parameter_list = None
        else:
            request_parameter_list = request_parameters.to_request_parameters()
        uri = self._to_absolute_uri(relative_path, request_parameter_list)
        if request_headers is None:
            request_headers = []

        body = None
        if request_body is not None:
            request_headers.append(RequestHeader("Content-Type", "application/json"))
            body = self.__marshaller.marshal(request_body)

        self._add_generic_headers("POST", uri, request_headers, context)
        return self.connection.post(uri, request_headers, body)

    def post(self, relative_path, request_headers, request_parameters, request_body, response_type, context):
        """
        Corresponds to the HTTP POST method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param request_body: The optional request body to send.
        :param response_type: The type of response to return.
        :param context: The optional call context to use.
        :raise: CommunicationException when an exception occurred communicating with the Online Payments platform
        :raise: ResponseException when an error response was received from the Online Payments platform
        :raise: ApiException when an error response was received from the Online Payments platform which contained a list of errors
        """
        (status, headers, chunks) = self._post(relative_path, request_headers, request_parameters, request_body,
                                               context)

        return self._process_response(status, chunks, headers, relative_path, response_type, context)

    def _put(self, relative_path, request_headers, request_parameters, request_body, context):
        if request_parameters is None:
            request_parameter_list = None
        else:
            request_parameter_list = request_parameters.to_request_parameters()
        uri = self._to_absolute_uri(relative_path, request_parameter_list)
        if request_headers is None:
            request_headers = []

        body = None
        if request_body is not None:
            request_headers.append(RequestHeader("Content-Type", "application/json"))
            body = self.__marshaller.marshal(request_body)

        self._add_generic_headers("PUT", uri, request_headers, context)
        return self.connection.put(uri, request_headers, body)

    def put(self, relative_path, request_headers, request_parameters,
            request_body, response_type, context):
        """
        Corresponds to the HTTP PUT method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param request_body: The optional request body to send.
        :param response_type: The type of response to return.
        :param context: The optional call context to use.
        :raise: CommunicationException when an exception occurred communicating with the Online Payments platform
        :raise: ResponseException when an error response was received from the Online Payments platform
        :raise: ApiException when an error response was received from the Online Payments platform which contained a list of errors
        """
        (status, headers, chunks) = self._put(relative_path, request_headers, request_parameters, request_body, context)
        return self._process_response(status, chunks, headers, relative_path, response_type, context)

    @property
    def api_endpoint(self) -> Union[ParseResult, ParseResultBytes]:
        """:return: The Online Payments platform API endpoint URI. This URI's path will be None or empty."""
        return self.__api_endpoint

    @property
    def authenticator(self) -> Authenticator:
        """:return: The Authenticator object associated with this session. Never None."""
        return self.__authenticator

    @property
    def connection(self) -> Connection:
        """:return: The Connection object associated with this session. Never None."""
        return self.__connection

    @property
    def marshaller(self) -> Marshaller:
        """:return: The Marshaller object associated with this communicator. Never None."""
        return self.__marshaller

    @property
    def meta_data_provider(self) -> MetaDataProvider:
        """:return: The MetaDataProvider object associated with this session. Never None."""
        return self.__meta_data_provider

    def _to_absolute_uri(self, relative_path, request_parameters):
        if self.api_endpoint.path:
            raise ValueError("api_endpoint should not contain a path")
        if self.api_endpoint.username is not None or self.api_endpoint.query or \
                self.api_endpoint.fragment:
            raise ValueError("api_endpoint should not contain user info, query or fragment")
        if relative_path.startswith("/"):
            absolute_path = relative_path
        else:
            absolute_path = "/" + relative_path
        uri = self.api_endpoint.geturl() + absolute_path
        flag = False
        if request_parameters is not None:
            for nvp in request_parameters:
                if not flag:
                    uri += "?"
                    flag = True
                else:
                    uri += "&"
                uri += quote(nvp.name) + "=" + quote(nvp.value)
        # no need to revalidate that uri has a valid scheme and netloc
        return urlparse(uri)

    def _add_generic_headers(self, http_method, uri, request_headers, context):
        """
        Adds the necessary headers to the given list of headers. This includes
        the authorization header, which uses other headers, so when you need to
        override this method, make sure to call super.addGenericHeaders at the
        end of your overridden method.
        """
        # add server meta info header
        request_headers.extend(self.meta_data_provider.meta_data_headers)
        # add date header
        request_headers.append(RequestHeader("Date", self._get_header_date_string()))
        if context is not None and context.idempotence_key is not None:
            # add context specific headers
            request_headers.append(RequestHeader("X-GCS-Idempotence-Key", context.idempotence_key))
        # add signature
        authentication_signature = \
            self.authenticator.create_simple_authentication_signature(http_method, uri, request_headers)
        request_headers.append(RequestHeader("Authorization", authentication_signature))

    @staticmethod
    def _get_header_date_string():
        """
        Returns the date in the preferred format for the HTTP date header.
        """
        return datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

    @staticmethod
    def __collect_chunks(chunks):
        collected_body = b""
        for chunk in chunks:
            collected_body += chunk
        return collected_body.decode('utf-8')

    def _process_response(self, status, chunks, headers, request_path, response_type, context):
        if context is not None:
            Communicator._update_context(headers, context)
        body = Communicator.__collect_chunks(chunks)
        Communicator._throw_exception_if_necessary(status, body, headers, request_path)
        return self.__marshaller.unmarshal(body, response_type)

    @staticmethod
    def _update_context(headers, context):
        """
        Updates the given call context based on the contents of the given response.
        """
        idempotence_request_timestamp_value = get_header_value(headers, "X-GCS-Idempotence-Request-Timestamp")
        if idempotence_request_timestamp_value is not None:
            idempotence_request_timestamp = int(idempotence_request_timestamp_value)
            context.idempotence_request_timestamp = idempotence_request_timestamp
        else:
            context.idempotence_request_timestamp = None

    @staticmethod
    def _throw_exception_if_necessary(status, body, headers, request_path):
        """
        Checks the Response for errors and throws an exception if necessary.
        """
        # status codes in the 100 or 300 range are not expected
        if status < 200 or status >= 300:
            Communicator.__throw_exception(status, body, headers, request_path)

    @staticmethod
    def __throw_exception(status, body, headers, request_path):
        if body is not None and not Communicator.__is_json(headers):
            cause = ResponseException(status, body, headers)
            if status == 404:
                raise NotFoundException(cause, "The requested resource was not found; invalid path: " + request_path)
            else:
                raise CommunicationException(cause)
        else:
            raise ResponseException(status, body, headers)

    @staticmethod
    def __is_json(headers):
        content_type = get_header_value(headers, "Content-Type")
        return content_type is None or "application/json".lower() == content_type or content_type.lower().startswith("application/json")

    def close_idle_connections(self, idle_time):
        """
        Utility method that delegates the call to this communicator's session's connection
        if that's an instance of PooledConnection. If not this method does nothing.

        :param idle_time: a datetime.timedelta object indicating the idle time
        """
        if isinstance(self.connection, PooledConnection):
            cast(PooledConnection, self.connection).close_idle_connections(idle_time)

    def close_expired_connections(self):
        """
        Utility method that delegates the call to this communicator's session's connection
        if that's an instanceof PooledConnection. If not this method does nothing.
        """
        if isinstance(self.connection, PooledConnection):
            cast(PooledConnection, self.connection).close_expired_connections()

    def enable_logging(self, communicator_logger):
        # delegate to the connection
        self.connection.enable_logging(communicator_logger)

    def disable_logging(self):
        # delegate to the connection
        self.connection.disable_logging()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
