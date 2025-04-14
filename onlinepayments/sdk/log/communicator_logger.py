from abc import ABC, abstractmethod
from typing import Optional

from .request_log_message import RequestLogMessage
from .response_log_message import ResponseLogMessage


class CommunicatorLogger(ABC):
    """
    Used to log messages from communicators.
    """

    def log_request(self, request_log_message: RequestLogMessage) -> None:
        """
        Logs a request message object

        """
        self.log(request_log_message.get_message())

    def log_response(self, response_log_message: ResponseLogMessage) -> None:
        """
        Logs a response message object

        """
        self.log(response_log_message.get_message())

    @abstractmethod
    def log(self, message: str, thrown: Optional[Exception] = None) -> None:
        """
        Logs a throwable with an accompanying message.

        :param message: The message accompanying the throwable.
        :param thrown: The throwable to log.
        """
        raise NotImplementedError
