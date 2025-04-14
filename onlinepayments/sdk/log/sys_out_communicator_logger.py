from datetime import datetime
from threading import Lock
from typing import Optional

from .communicator_logger import CommunicatorLogger


class SysOutCommunicatorLogger(CommunicatorLogger):
    """
    A communicator logger that prints its message to sys.stdout
    It includes a timestamp in yyyy-MM-ddTHH:mm:ss format in the system time zone.
    """

    _global_lock = Lock()
    _old_print = print

    @staticmethod
    def instance() -> 'SysOutCommunicatorLogger':
        return _SYS_OUT_COMMUNICATOR_LOGGER_INSTANCE

    def __print(self, *a) -> None:
        with self._global_lock:
            self._old_print(*a)

    def log(self, message: str, thrown: Optional[Exception] = None) -> None:
        # Make sure the same object is used for locking and printing
        self.__print(self.__get_date_prefix() + message)
        if thrown:
            self.__print(str(thrown))

    @staticmethod
    def __get_date_prefix() -> str:
        return datetime.now().strftime("%Y-%m-%dT%H:%M:%S ")


_SYS_OUT_COMMUNICATOR_LOGGER_INSTANCE = SysOutCommunicatorLogger()
