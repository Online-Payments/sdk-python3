from typing import Optional

from onlinepayments.sdk.declined_transaction_exception import DeclinedTransactionException
from onlinepayments.sdk.domain.refund_error_response import RefundErrorResponse
from onlinepayments.sdk.domain.refund_response import RefundResponse


class DeclinedRefundException(DeclinedTransactionException):
    """
    Represents an error response from a refund call.
    """

    def __init__(self, status_code: int, response_body: str, error_response: RefundErrorResponse):
        if error_response is not None:
            super(DeclinedRefundException, self).__init__(status_code,
                                                          response_body,
                                                          error_response.error_id,
                                                          error_response.errors,
                                                          DeclinedRefundException.__create_message(error_response))
        else:
            super(DeclinedRefundException, self).__init__(status_code, response_body, None, None,
                                                          DeclinedRefundException.__create_message())
        self.__error_response = error_response

    @staticmethod
    def __create_message(error_response=None) -> str:
        refund = error_response.refund_result if error_response else None
        if refund is not None:
            return "declined refund '" + refund.id + "' with status '" + refund.status + "'"
        else:
            return "the Online Payments platform returned a declined refund response"

    @property
    def refund_result(self) -> Optional[RefundResponse]:
        """
        :return: The result of creating a refund if available, otherwise None.
        """
        if self.__error_response is None:
            return None
        else:
            return self.__error_response.refund_result
