#
# This file was automatically generated.
#
from onlinepayments.sdk.communication.param_request import ParamRequest
from onlinepayments.sdk.communication.request_param import RequestParam


class GetCardDataByPaymentsParams(ParamRequest):
    """
    Query parameters for Get sensitive card details by card payment identifiers
    """

    __payments: list[str] | None = None

    @property
    def payments(self) -> list[str] | None:
        """
        | This object contains the details for detokenizing a payment token.

        Type: list[str]
        """
        return self.__payments

    @payments.setter
    def payments(self, value: list[str] | None) -> None:
        self.__payments = value

    def add_payments(self, value: str) -> None:
        """
        :param value: str
        """
        if self.payments is None:
            self.payments = []
        self.payments.append(value)

    def to_request_parameters(self) -> list[RequestParam]:
        """
        :return: list[RequestParam]
        """
        result = []
        if self.payments is not None:
            for payments_element in self.payments:
                if payments_element is not None:
                    result.append(RequestParam("payments", payments_element))
        return result
