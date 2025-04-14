# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .api_error import APIError
from .create_payment_response import CreatePaymentResponse
from .data_object import DataObject


class PaymentErrorResponse(DataObject):

    __error_id: Optional[str] = None
    __errors: Optional[List[APIError]] = None
    __payment_result: Optional[CreatePaymentResponse] = None

    @property
    def error_id(self) -> Optional[str]:
        """
        | Unique reference, for debugging purposes, of this error response

        Type: str
        """
        return self.__error_id

    @error_id.setter
    def error_id(self, value: Optional[str]) -> None:
        self.__error_id = value

    @property
    def errors(self) -> Optional[List[APIError]]:
        """
        Type: list[:class:`onlinepayments.sdk.domain.api_error.APIError`]
        """
        return self.__errors

    @errors.setter
    def errors(self, value: Optional[List[APIError]]) -> None:
        self.__errors = value

    @property
    def payment_result(self) -> Optional[CreatePaymentResponse]:
        """
        | Object that contains details on the created payment in case one has been created.

        Type: :class:`onlinepayments.sdk.domain.create_payment_response.CreatePaymentResponse`
        """
        return self.__payment_result

    @payment_result.setter
    def payment_result(self, value: Optional[CreatePaymentResponse]) -> None:
        self.__payment_result = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentErrorResponse, self).to_dictionary()
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
        super(PaymentErrorResponse, self).from_dictionary(dictionary)
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
