#
# This file was automatically generated.
#
from onlinepayments.sdk.communication.param_request import ParamRequest
from onlinepayments.sdk.communication.request_param import RequestParam


class GetPaymentsReportParams(ParamRequest):
    """
    Query parameters for Get payments report
    """

    __cursor: str | None = None
    __limit: int | None = None

    @property
    def cursor(self) -> str | None:
        """
        | Opaque cursor for pagination. Omit for the first page, use value from previous response for subsequent pages.

        Type: str
        """
        return self.__cursor

    @cursor.setter
    def cursor(self, value: str | None) -> None:
        self.__cursor = value

    @property
    def limit(self) -> int | None:
        """
        | Maximum number of items to return per page.

        Type: int
        """
        return self.__limit

    @limit.setter
    def limit(self, value: int | None) -> None:
        self.__limit = value

    def to_request_parameters(self) -> list[RequestParam]:
        """
        :return: list[RequestParam]
        """
        result = []
        if self.cursor is not None:
            result.append(RequestParam("cursor", self.cursor))
        if self.limit is not None:
            result.append(RequestParam("limit", str(self.limit)))
        return result
