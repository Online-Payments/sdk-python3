from abc import ABC, abstractmethod

from .request_param import RequestParam


class ParamRequest(ABC):
    """
    Represents a set of request parameters.
    """

    @abstractmethod
    def to_request_parameters(self) -> list[RequestParam]:
        """
        :return: list[:class:`onlinepayments.sdk.communication.RequestParam`] representing the HTTP request parameters
        """
        raise NotImplementedError
