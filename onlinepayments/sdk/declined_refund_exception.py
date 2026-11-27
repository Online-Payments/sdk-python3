#
# This file was automatically generated.
#
from .declined_transaction_exception import DeclinedTransactionException

from onlinepayments.sdk.domain.refund_error_response import RefundErrorResponse
from onlinepayments.sdk.domain.refund_response import RefundResponse


class DeclinedRefundException(DeclinedTransactionException):
    """
    Represents an error response from a refund call.
    """

    def __init__(self, status_code: int, response_body: str, response: RefundErrorResponse | None):
        if response is not None:
            super().__init__(
                status_code,
                response_body,
                response.error_id,
                response.errors,
                DeclinedRefundException.__create_message(response),
            )
        else:
            super().__init__(
                status_code,
                response_body,
                None,
                None,
                DeclinedRefundException.__create_message(response),
            )
        self.__response = response

    @staticmethod
    def __create_message(response: RefundErrorResponse | None) -> str:
        if response is not None:
            refund_result = response.refund_result
        else:
            refund_result = None
        if refund_result is not None:
            return f"declined refund '{refund_result.id}' with status '{refund_result.status}'"
        else:
            return "the payment platform returned a declined refund response"

    @property
    def refund_response(self) -> RefundResponse | None:
        """
        :return: The result of creating a refund if available, otherwise None.
        """
        if self.__response is None:
            return None
        else:
            return self.__response.refund_result
