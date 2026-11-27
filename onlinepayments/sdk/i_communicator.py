from abc import abstractmethod
from typing import Any, Self
from collections.abc import Mapping, Iterable

from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.communication.param_request import ParamRequest
from onlinepayments.sdk.communication.request_header import RequestHeader
from onlinepayments.sdk.json.marshaller import Marshaller, T
from onlinepayments.sdk.log.logging_capable import LoggingCapable
from onlinepayments.sdk.log.obfuscation_capable import ObfuscationCapable


class BinaryResponse(tuple[Mapping[str, str], Iterable[bytes]]):
    """
    The headers and body chunks of a binary response. It unpacks as headers, chunks.

    The underlying connection stays in use until all chunks are read. Use it in a with block,
    or call close(), to release the connection without reading all chunks:

        with communicator.get_with_binary_response(...) as (headers, chunks):
            ...
    """

    def __new__(cls, headers: Mapping[str, str], chunks: Iterable[bytes]) -> Self:
        return super().__new__(cls, (headers, chunks))

    @property
    def headers(self) -> Mapping[str, str]:
        return self[0]

    @property
    def chunks(self) -> Iterable[bytes]:
        return self[1]

    def close(self) -> None:
        """
        Releases the underlying connection. Chunks that have not been read yet are discarded.
        """
        close = getattr(self[1], "close", None)
        if callable(close):
            close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()


class ICommunicator(LoggingCapable, ObfuscationCapable):
    """
    Used to communicate with the Online Payments platform web services.

    It contains all the logic to transform a request object to an HTTP request and an HTTP response to a response object.
    It can be used in a with block, which closes it at the end of the block.
    """

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()

    @abstractmethod
    def close(self) -> None:
        """
        Releases any system resources associated with this object.
        """

    @abstractmethod
    def get(self, relative_path: str, request_headers: list[RequestHeader] | None,
            request_parameters: ParamRequest | None,
            response_type: type[T],
            context: CallContext | None) -> T | None:
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

    @abstractmethod
    def get_with_binary_response(self, relative_path: str, request_headers: list[RequestHeader] | None,
                                 request_parameters: ParamRequest | None,
                                 context: CallContext | None) -> BinaryResponse:
        """
        Corresponds to the HTTP GET method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param context: The optional call context to use.
        :raise CommunicationException: when an exception occurred communicating with the Online Payments platform
        :raise ResponseException: when an error response was received from the Online Payments platform
        """

    @abstractmethod
    def delete(self, relative_path: str, request_headers: list[RequestHeader] | None,
               request_parameters: ParamRequest | None,
               response_type: type[T],
               context: CallContext | None) -> T | None:
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

    @abstractmethod
    def delete_with_binary_response(self, relative_path: str, request_headers: list[RequestHeader] | None,
                                    request_parameters: ParamRequest | None,
                                    context: CallContext | None) -> BinaryResponse:
        """
        Corresponds to the HTTP DELETE method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param context: The optional call context to use.
        :raise CommunicationException: when an exception occurred communicating with the Online Payments platform
        :raise ResponseException: when an error response was received from the Online Payments platform
        """

    @abstractmethod
    def post_with_binary_response(self, relative_path: str, request_headers: list[RequestHeader] | None,
                                  request_parameters: ParamRequest | None, request_body: Any,
                                  context: CallContext | None) -> BinaryResponse:
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

    @abstractmethod
    def post(self, relative_path: str, request_headers: list[RequestHeader] | None,
             request_parameters: ParamRequest | None, request_body: Any,
             response_type: type[T],
             context: CallContext | None) -> T | None:
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

    @abstractmethod
    def put_with_binary_response(self, relative_path: str, request_headers: list[RequestHeader] | None,
                                 request_parameters: ParamRequest | None, request_body: Any,
                                 context: CallContext | None) -> BinaryResponse:
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

    @abstractmethod
    def put(self, relative_path: str, request_headers: list[RequestHeader] | None,
            request_parameters: ParamRequest | None, request_body: Any,
            response_type: type[T],
            context: CallContext | None) -> T | None:
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

    @abstractmethod
    def close_idle_connections(self, idle_time):
        """
        Utility method that delegates the call to this communicator's connection
        if that's an instance of PooledConnection. If not this method does nothing.

        :param idle_time: a datetime.timedelta object indicating the idle time
        """

    @abstractmethod
    def close_expired_connections(self):
        """
        Utility method that delegates the call to this communicator's connection
        if that's an instance of PooledConnection. If not this method does nothing.
        """

    @property
    @abstractmethod
    def marshaller(self) -> Marshaller:
        """
        :return: The Marshaller object associated with this communicator. Never None.
        """
