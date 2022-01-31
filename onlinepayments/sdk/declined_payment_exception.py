from typing import Optional

from onlinepayments.sdk.declined_transaction_exception import DeclinedTransactionException
from onlinepayments.sdk.domain.create_payment_response import CreatePaymentResponse
from onlinepayments.sdk.domain.payment_error_response import PaymentErrorResponse


class DeclinedPaymentException(DeclinedTransactionException):
    """
    Represents an error response from a create payment call.
    """

    def __init__(self, status_code: int, response_body: str, error_response: PaymentErrorResponse):
        if error_response is not None:
            super(DeclinedPaymentException, self).__init__(status_code,
                                                           response_body,
                                                           error_response.error_id,
                                                           error_response.errors,
                                                           DeclinedPaymentException.__create_message(error_response))
        else:
            super(DeclinedPaymentException, self).__init__(status_code,
                                                           response_body,
                                                           None, None,
                                                           DeclinedPaymentException.__create_message())
        self.__error_response = error_response

    @staticmethod
    def __create_message(error_response=None) -> str:
        payment = error_response.payment_result.payment if error_response and error_response.payment_result else None
        if payment is not None:
            return "declined payment '" + payment.id + "' with status '" + payment.status + "'"
        else:
            return "the Online Payments platform returned a declined payment response"

    @property
    def create_payment_result(self) -> Optional[CreatePaymentResponse]:
        """
        :return: The result of creating a payment if available, otherwise None.
        """
        if self.__error_response is None:
            return None
        else:
            return self.__error_response.payment_result
