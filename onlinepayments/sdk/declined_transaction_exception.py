#
# This file was automatically generated.
#
from .api_exception import ApiException

from onlinepayments.sdk.domain.api_error import APIError


class DeclinedTransactionException(ApiException):
    """
    Represents an error response from a create payment, payout or refund call.
    """

    def __init__(self, status_code: int, response_body: str, error_id: str | None, errors: list[APIError] | None,
                 message: str | None = None):
        if message:
            super().__init__(status_code, response_body, error_id, errors, message)
        else:
            super().__init__(status_code, response_body, error_id, errors)
