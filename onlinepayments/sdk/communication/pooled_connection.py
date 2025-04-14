from abc import ABC, abstractmethod
from datetime import timedelta

from .connection import Connection


class PooledConnection(Connection, ABC):
    """
    Represents a pooled connection to the Online Payments platform server.
    Instead of setting up a new HTTP connection for each request, this
    connection uses a pool of HTTP connections.
    """

    @abstractmethod
    def close_idle_connections(self, idle_time: timedelta) -> None:
        """
        Closes all HTTP connections that have been idle for the specified time.
        This should also include all expired HTTP connections.

        :param idle_time: a datetime.timedelta object indicating the idle time
        """
        raise NotImplementedError

    @abstractmethod
    def close_expired_connections(self) -> None:
        """
        Closes all expired HTTP connections.
        """
        raise NotImplementedError
