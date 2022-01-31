from typing import Optional

from onlinepayments.sdk.declined_transaction_exception import DeclinedTransactionException
from onlinepayments.sdk.domain.payout_error_response import PayoutErrorResponse
from onlinepayments.sdk.domain.payout_result import PayoutResult


class DeclinedPayoutException(DeclinedTransactionException):
    """
    Represents an error response from a payout call.
    """

    def __init__(self, status_code: int, response_body: str, error_response: PayoutErrorResponse):
        if error_response is not None:
            super(DeclinedPayoutException, self).__init__(status_code,
                                                          response_body,
                                                          error_response.error_id,
                                                          error_response.errors,
                                                          DeclinedPayoutException.__create_message(error_response))
        else:
            super(DeclinedPayoutException, self).__init__(status_code, response_body, None, None,
                                                          DeclinedPayoutException.__create_message())
        self.__error_response = error_response

    @staticmethod
    def __create_message(error_response=None) -> str:
        payout = error_response.payout_result if error_response else None
        if payout is not None:
            return "declined payout '" + payout.id + "' with status '" + payout.status + "'"
        else:
            return "the Online Payments platform returned a declined payout response"

    @property
    def payout_result(self) -> Optional[PayoutResult]:
        """
        :return: The result of creating a payout if available, otherwise None.
        """
        if self.__error_response is None:
            return None
        else:
            return self.__error_response.payout_result
