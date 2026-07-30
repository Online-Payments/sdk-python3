# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from onlinepayments.sdk.communication.param_request import ParamRequest
from onlinepayments.sdk.communication.request_param import RequestParam


class GetPaymentsReportParams(ParamRequest):
    """
    Query parameters for Get payments report
    """

    __cursor: Optional[str] = None
    __limit: Optional[int] = None

    @property
    def cursor(self) -> Optional[str]:
        """
        | Opaque cursor for pagination. Omit for the first page, use value from previous response for subsequent pages.

        Type: str
        """
        return self.__cursor

    @cursor.setter
    def cursor(self, value: Optional[str]) -> None:
        self.__cursor = value

    @property
    def limit(self) -> Optional[int]:
        """
        | Maximum number of items to return per page.

        Type: int
        """
        return self.__limit

    @limit.setter
    def limit(self, value: Optional[int]) -> None:
        self.__limit = value

    def to_request_parameters(self) -> List[RequestParam]:
        """
        :return: list[RequestParam]
        """
        result = []
        if self.cursor is not None:
            result.append(RequestParam("cursor", self.cursor))
        if self.limit is not None:
            result.append(RequestParam("limit", str(self.limit)))
        return result
