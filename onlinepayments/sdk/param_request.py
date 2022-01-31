from abc import ABC, abstractmethod


class ParamRequest(ABC):
    """
    Represents a set of request parameters.
    """

    @abstractmethod
    def to_request_parameters(self):
        """
        :return: list[:class:`onlinepayments.sdk.RequestParam`] representing the HTTP request parameters
        """
