#
# This file was automatically generated.
#
from .declined_transaction_exception import DeclinedTransactionException

from onlinepayments.sdk.domain.create_payment_response import CreatePaymentResponse
from onlinepayments.sdk.domain.payment_error_response import PaymentErrorResponse


class DeclinedPaymentException(DeclinedTransactionException):
    """
    Represents an error response from a create payment call.
    """

    def __init__(self, status_code: int, response_body: str, response: PaymentErrorResponse | None):
        if response is not None:
            super().__init__(
                status_code,
                response_body,
                response.error_id,
                response.errors,
                DeclinedPaymentException.__create_message(response),
            )
        else:
            super().__init__(
                status_code,
                response_body,
                None,
                None,
                DeclinedPaymentException.__create_message(response),
            )
        self.__response = response

    @staticmethod
    def __create_message(response: PaymentErrorResponse | None) -> str:
        if response is not None and response.payment_result is not None:
            payment = response.payment_result.payment
        else:
            payment = None
        if payment is not None:
            return f"declined payment '{payment.id}' with status '{payment.status}'"
        else:
            return "the payment platform returned a declined payment response"

    @property
    def create_payment_response(self) -> CreatePaymentResponse | None:
        """
        :return: The result of creating a payment if available, otherwise None.
        """
        if self.__response is None:
            return None
        else:
            return self.__response.payment_result
