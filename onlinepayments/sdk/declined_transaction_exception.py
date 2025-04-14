# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .api_exception import ApiException

from onlinepayments.sdk.domain.api_error import APIError


class DeclinedTransactionException(ApiException):
    """
    Represents an error response from a create payment, payout or refund call.
    """

    def __init__(self, status_code: int, response_body: str, error_id: Optional[str], errors: Optional[List[APIError]],
                 message: Optional[str] = None):
        if message:
            super(DeclinedTransactionException, self).__init__(status_code, response_body, error_id, errors, message)
        else:
            super(DeclinedTransactionException, self).__init__(status_code, response_body, error_id, errors)
