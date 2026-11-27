from datetime import datetime

class CallContext:
    """
    A call context can be used to send extra information with a request, and to receive extra information from a response.

    Please note that this class is not thread-safe. Each request should get its own call context instance.
    """
    __idempotence_key: str | None = None
    __idempotence_request_timestamp: int | None = None
    __idempotence_response_date_time: datetime | None = None
    __gzip: bool | None = None

    def __init__(self, idempotence_key: str | None = None, gzip: bool | None = None):
        self.__idempotence_key = idempotence_key
        self.__gzip = gzip

    @property
    def idempotence_key(self) -> str | None:
        """
        :return: The idempotence key.
        """
        return self.__idempotence_key

    @property
    def idempotence_request_timestamp(self) -> int | None:
        """
        :return: The idempotence request timestamp from the response to the last
         request for which this call context was used, or None if no idempotence
         request timestamp was present.
        """
        return self.__idempotence_request_timestamp

    @idempotence_request_timestamp.setter
    def idempotence_request_timestamp(self, idempotence_request_timestamp: int | None) -> None:
        """
        Sets the idempotence request timestamp.
        This method should only be called by Communicator objects based on the
        response to the request for which this call context was used.
        """
        self.__idempotence_request_timestamp = idempotence_request_timestamp

    @property
    def idempotence_response_date_time(self) -> datetime | None:
        """
        :return: The idempotence response date/time from the response to the
         last request for which this call context was used, or None if no idempotence
         response date/time was present.
        """
        return self.__idempotence_response_date_time

    @idempotence_response_date_time.setter
    def idempotence_response_date_time(self, idempotence_response_date_time: datetime | None) -> None:
        """
        Sets the idempotence response date/time.
        This method should only be called by Communicator objects based on the
        response to the request for which this call context was used.
        """
        self.__idempotence_response_date_time = idempotence_response_date_time

    @property
    def gzip(self) -> bool | None:
        """Per-request gzip toggle."""
        return self.__gzip

    @gzip.setter
    def gzip(self, enabled: bool | None) -> None:
        """
        Sets the gzip field true/false.
        """
        self.__gzip = enabled
