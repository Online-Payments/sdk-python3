# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional, Sequence

from onlinepayments.sdk.domain.api_error import APIError


class ApiException(RuntimeError):
    """
    Represents an error response from the payment platform which contains an ID and a list of errors.
    """

    def __init__(self, status_code: int, response_body: str, error_id: Optional[str], errors: Optional[List[APIError]],
                 message: str = "the payment platform returned an error response"):
        super(ApiException, self).__init__(message)
        self.__status_code = status_code
        self.__response_body = response_body
        self.__error_id = error_id
        if errors is None:
            self.__errors = ()
        else:
            self.__errors = errors

    @property
    def status_code(self) -> int:
        """
        :return: The HTTP status code that was returned by the Payment platform.
        """
        return self.__status_code

    @property
    def response_body(self) -> str:
        """
        :return: The raw response body that was returned by the Payment platform.
        """
        return self.__response_body

    @property
    def error_id(self) -> Optional[str]:
        """
        :return: The errorId received from the Payment platform if available.
        """
        return self.__error_id

    @property
    def errors(self) -> Sequence[APIError]:
        """
        :return: The errors received from the Payment platform if available. Never None.
        """
        return self.__errors

    def __str__(self):
        string = super(ApiException, self).__str__()
        if self.__status_code > 0:
            string += "; status_code=" + str(self.__status_code)
        if self.__response_body:
            string += "; response_body='" + self.__response_body + "'"
        return str(string)
