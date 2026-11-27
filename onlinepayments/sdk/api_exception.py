#
# This file was automatically generated.
#
import copyreg

from onlinepayments.sdk.domain.api_error import APIError
from onlinepayments.sdk.log.body_obfuscator import BodyObfuscator


class ApiException(RuntimeError):
    """
    Represents an error response from the payment platform which contains an ID and a list of errors.
    """

    def __init__(self, status_code: int, response_body: str, error_id: str | None, errors: list[APIError] | None,
                 message: str = "the payment platform returned an error response"):
        super().__init__(message)
        self.__status_code = status_code
        self.__response_body = response_body
        self.__error_id = error_id
        if errors is None:
            self.__errors = []
        elif isinstance(errors, list):
            self.__errors = errors
        else:
            self.__errors = list(errors)

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
    def error_id(self) -> str | None:
        """
        :return: The errorId received from the Payment platform if available.
        """
        return self.__error_id

    @property
    def errors(self) -> list[APIError]:
        """
        :return: The errors received from the Payment platform if available. Never None.
        """
        return self.__errors

    def __reduce__(self):
        # Recreate the exception without calling __init__, so subclasses with other constructor arguments
        # can be pickled too (for example to pass them between processes); the fields are restored from __dict__.
        return copyreg.__newobj__, (type(self), *self.args), self.__dict__

    def __str__(self):
        string = super().__str__()
        if self.__status_code > 0:
            string += "; status_code=" + str(self.__status_code)
        if self.__response_body:
            response_body = BodyObfuscator.default_body_obfuscator().obfuscate_body(self.__response_body)
            string += "; response_body='" + response_body + "'"
        return str(string)
