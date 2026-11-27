#
# This file was automatically generated.
#
from .api_exception import ApiException

from onlinepayments.sdk.domain.problem_details_response import ProblemDetailsResponse


class ProblemDetailsException(ApiException):
    """
    Represents an error response from the payment platform containing problem details.
    """

    def __init__(self, status_code: int, response_body: str, response: ProblemDetailsResponse | None):
        super().__init__(
            status_code,
            response_body,
            None,
            None,
            "the payment platform returned a problem details error response",
        )
        self.__response = response

    @property
    def response(self) -> ProblemDetailsResponse | None:
        """
        :return: The problem details response if available, otherwise None.
        """
        return self.__response
