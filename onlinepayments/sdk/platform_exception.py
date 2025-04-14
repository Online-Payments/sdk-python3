# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .api_exception import ApiException

from onlinepayments.sdk.domain.api_error import APIError


class PlatformException(ApiException):
    """
    Represents an error response from the payment platform when something went wrong at the payment platform or further downstream.
    """

    def __init__(self, status_code: int, response_body: str, error_id: Optional[str], errors: Optional[List[APIError]],
                 message: str = "the payment platform returned an error response"):
        super(PlatformException, self).__init__(status_code, response_body, error_id, errors, message)
