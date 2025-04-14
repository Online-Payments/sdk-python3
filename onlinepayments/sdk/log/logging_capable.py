from abc import ABC, abstractmethod

from .communicator_logger import CommunicatorLogger


class LoggingCapable(ABC):
    """
    Classes that extend this class have support for log messages from
    communicators.
    """

    @abstractmethod
    def enable_logging(self, communicator_logger: CommunicatorLogger) -> None:
        """
        Turns on logging using the given communicator logger.

        :raise ValueError: If the given communicator logger is None.
        """
        raise NotImplementedError

    @abstractmethod
    def disable_logging(self) -> None:
        """
        Turns off logging.
        """
        raise NotImplementedError
