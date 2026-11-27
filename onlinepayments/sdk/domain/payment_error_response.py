#
# This file was automatically generated.
#
from .api_error import APIError
from .create_payment_response import CreatePaymentResponse
from .data_object import DataObject


class PaymentErrorResponse(DataObject):

    __slots__ = (
        "__error_id",
        "__errors",
        "__payment_result",
    )

    __error_id: str | None
    __errors: list[APIError] | None
    __payment_result: CreatePaymentResponse | None

    def __init__(
        self,
        *,
        error_id: str | None = None,
        errors: list[APIError] | None = None,
        payment_result: CreatePaymentResponse | None = None,
    ) -> None:
        self.error_id = error_id
        self.errors = errors
        self.payment_result = payment_result

    @property
    def error_id(self) -> str | None:
        """
        | Unique reference, for debugging purposes, of this error response

        Type: str
        """
        return self.__error_id

    @error_id.setter
    def error_id(self, value: str | None) -> None:
        self.__error_id = value

    @property
    def errors(self) -> list[APIError] | None:
        """
        Type: list[:class:`onlinepayments.sdk.domain.api_error.APIError`]
        """
        return self.__errors

    @errors.setter
    def errors(self, value: list[APIError] | None) -> None:
        self.__errors = value

    @property
    def payment_result(self) -> CreatePaymentResponse | None:
        """
        | This object contains details about the created payment if one has been generated.

        Type: :class:`onlinepayments.sdk.domain.create_payment_response.CreatePaymentResponse`
        """
        return self.__payment_result

    @payment_result.setter
    def payment_result(self, value: CreatePaymentResponse | None) -> None:
        self.__payment_result = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.error_id is not None:
            dictionary['errorId'] = self.error_id
        if self.errors is not None:
            dictionary['errors'] = []
            for element in self.errors:
                if element is not None:
                    dictionary['errors'].append(element.to_dictionary())
        if self.payment_result is not None:
            dictionary['paymentResult'] = self.payment_result.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentErrorResponse':
        super().from_dictionary(dictionary)
        if 'errorId' in dictionary:
            self.error_id = dictionary['errorId']
        if 'errors' in dictionary:
            if not isinstance(dictionary['errors'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['errors']))
            self.errors = []
            for element in dictionary['errors']:
                value = APIError()
                self.errors.append(value.from_dictionary(element))
        if 'paymentResult' in dictionary:
            if not isinstance(dictionary['paymentResult'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentResult']))
            value = CreatePaymentResponse()
            self.payment_result = value.from_dictionary(dictionary['paymentResult'])
        return self
