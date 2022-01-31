from typing import Any, Dict, Optional, Tuple

from onlinepayments.sdk.response_header import get_header, get_header_value


class ResponseException(RuntimeError):
    """
    Thrown when a response was received from the Online Payments platform which
    indicates an error.
    """

    def __init__(self, status_code: int, body: Optional[str], headers: Dict[str, str]):
        super(ResponseException, self).__init__("the Online Payments platform returned an error response")
        self.__status_code = status_code
        self.__headers = headers if headers is not None else {}
        self.__body = body

    @property
    def status_code(self) -> int:
        """
        :return: The HTTP status code that was returned by the Online Payments platform.
        """
        return self.__status_code

    @property
    def body(self) -> Optional[str]:
        """
        :return: The raw response body that was returned by the Online Payments platform.
        """
        return self.__body

    @property
    def headers(self) -> Dict[str, str]:
        """
        :return: The headers that were returned by the Online Payments platform.
         Never None.
        """
        return self.__headers

    def get_header(self, header_name) -> Optional[Tuple[str, Any]]:
        """
        :return: The header with the given name, or None if there was no such header.
        """
        return get_header(self.__headers, header_name)

    def get_header_value(self, header_name) -> str:
        """
        :return: The value header with the given name, or None if there was no such header.
        """
        return get_header_value(self.__headers, header_name)

    def __str__(self):
        string = super(ResponseException, self).__str__()
        status_code = self.__status_code
        if status_code > 0:
            string += "; status_code=" + str(status_code)
        response_body = self.__body
        if response_body:
            string += "; response_body='" + response_body + "'"
        return str(string)
