from abc import ABC, abstractmethod


class LoggingCapable(ABC):
    """
    Classes that extend this class have support for log messages from
    communicators.
    """

    @abstractmethod
    def enable_logging(self, communicator_logger):
        """
        Turns on logging using the given communicator logger.

        :raise: ValueError If the given communicator logger is None.
        """

    @abstractmethod
    def disable_logging(self):
        """
        Turns off logging.
        """
