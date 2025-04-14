from abc import ABC, abstractmethod
from typing import Optional, Sequence
from urllib.parse import ParseResult

from onlinepayments.sdk.communication.request_header import RequestHeader


class Authenticator(ABC):
    """
    Used to authenticate requests to the Online Payments platform.
    """

    @abstractmethod
    def get_authorization(self, http_method: str, resource_uri: ParseResult,
                          request_headers: Optional[Sequence[RequestHeader]]) -> str:
        """
        Returns a value that can be used for the "Authorization" header.

        :param http_method: The HTTP method.
        :param resource_uri: The URI of the resource.
        :param request_headers: A sequence of RequestHeaders.
         This sequence may not be modified and may not contain headers with the same name.
        """
        raise NotImplementedError
