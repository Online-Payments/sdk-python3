#
# This file was automatically generated.
#
from .api_exception import ApiException

from onlinepayments.sdk.domain.api_error import APIError


class ReferenceException(ApiException):
    """
    Represents an error response from the payment platform when a non-existing or removed object is trying to be accessed.
    """

    def __init__(self, status_code: int, response_body: str, error_id: str | None, errors: list[APIError] | None,
                 message: str = "the payment platform returned a reference error response"):
        super().__init__(status_code, response_body, error_id, errors, message)
