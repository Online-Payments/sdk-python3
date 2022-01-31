from typing import List, Optional

from onlinepayments.sdk.domain.api_error import APIError


class ApiException(RuntimeError):
    """
    Represents an error response from the Online Payments platform which contains
    an ID and a list of errors.
    """

    def __init__(self, status_code, response_body, error_id, errors,
                 message="the Online Payments platform returned an error response"):
        super(ApiException, self).__init__(message)
        self.__status_code = status_code
        self.__response_body = response_body
        self.__error_id = error_id
        self.__errors = errors if errors else ()

    @property
    def status_code(self) -> int:
        """
        :return: The HTTP status code that was returned by the Online Payments platform.
        """
        return self.__status_code

    @property
    def response_body(self) -> Optional[str]:
        """
        :return: The raw response body that was returned by the Online Payments platform.
        """
        return self.__response_body

    @property
    def error_id(self) -> str:
        """
        :return: The error ID received from the Online Payments platform if available.
        """
        return self.__error_id

    @property
    def errors(self) -> List[APIError]:
        """
        :return: The error list received from the Online Payments platform if available. Never None.
        """
        return self.__errors

    def __str__(self):
        string = super(ApiException, self).__str__()
        if self.__status_code > 0:
            string += "; status_code=" + str(self.__status_code)
        if self.__response_body:
            string += "; response_body='" + self.__response_body + "'"
        return str(string)
