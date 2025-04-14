from abc import ABC, abstractmethod
from typing import Iterable, Mapping, Sequence, Tuple, Union
from urllib.parse import ParseResult

from .multipart_form_data_object import MultipartFormDataObject
from .request_header import RequestHeader

from onlinepayments.sdk.log.logging_capable import LoggingCapable
from onlinepayments.sdk.log.obfuscation_capable import ObfuscationCapable


URI = Union[str, ParseResult]
RequestBody = Union[str, MultipartFormDataObject, None]
Response = Tuple[int, Mapping[str, str], Iterable[bytes]]


class Connection(LoggingCapable, ObfuscationCapable, ABC):
    """
    Represents a connection to the Online Payments platform server.
    """

    @abstractmethod
    def get(self, url: URI, request_headers: Sequence[RequestHeader]) -> Response:
        """
        Send a GET request to the Online Payments platform and return the response.

        :param url: The URI to call, including any necessary query parameters.
        :param request_headers: An optional sequence of request headers.
        :return: The response from the Online Payments platform as a tuple with
         the status code, headers and a generator of body chunks
        :raise CommunicationException: when an exception occurred communicating
         with the Online Payments platform
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, url: URI, request_headers: Sequence[RequestHeader]) -> Response:
        """
        Send a DELETE request to the Online Payments platform and return the response.

        :param url: The URI to call, including any necessary query parameters.
        :param request_headers: An optional sequence of request headers.
        :return: The response from the Online Payments platform as a tuple with
         the status code, headers and a generator of body chunks
        :raise CommunicationException: when an exception occurred communicating
         with the Online Payments platform
        """
        raise NotImplementedError

    @abstractmethod
    def post(self, url: URI, request_headers: Sequence[RequestHeader], body: RequestBody) -> Response:
        """
        Send a POST request to the Online Payments platform and return the response.

        :param url: The URI to call, including any necessary query parameters.
        :param request_headers: An optional sequence of request headers.
        :param body: The optional body to send.
        :return: The response from the Online Payments platform as a tuple with
         the status code, headers and a generator of body chunks
        :raise CommunicationException: when an exception occurred communicating
         with the Online Payments platform
        """
        raise NotImplementedError

    @abstractmethod
    def put(self, url: URI, request_headers: Sequence[RequestHeader], body: RequestBody) -> Response:
        """
        Send a PUT request to the Online Payments platform and return the response.

        :param url: The URI to call, including any necessary query parameters.
        :param request_headers: An optional sequence of request headers.
        :param body: The optional body to send.
        :return: The response from the Online Payments platform as a tuple with
         the status code, headers and a generator of body chunks
        :raise CommunicationException: when an exception occurred communicating
         with the Online Payments platform
        """
        raise NotImplementedError

    def close(self) -> None:
        """
        Releases any system resources associated with this object.
        """
        pass
