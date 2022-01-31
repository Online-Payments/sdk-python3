# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.api_error import APIError
from onlinepayments.sdk.domain.refund_response import RefundResponse


class RefundErrorResponse(DataObject):
    __error_id = None
    __errors = None
    __refund_result = None

    @property
    def error_id(self) -> str:
        """
        Type: str
        """
        return self.__error_id

    @error_id.setter
    def error_id(self, value: str):
        self.__error_id = value

    @property
    def errors(self) -> List[APIError]:
        """
        Type: list[:class:`onlinepayments.sdk.domain.api_error.APIError`]
        """
        return self.__errors

    @errors.setter
    def errors(self, value: List[APIError]):
        self.__errors = value

    @property
    def refund_result(self) -> RefundResponse:
        """
        | This object has the numeric representation of the current refund status, timestamp of last status change and performable action on the current refund resource. In case of a rejected refund, detailed error information is listed.

        Type: :class:`onlinepayments.sdk.domain.refund_response.RefundResponse`
        """
        return self.__refund_result

    @refund_result.setter
    def refund_result(self, value: RefundResponse):
        self.__refund_result = value

    def to_dictionary(self):
        dictionary = super(RefundErrorResponse, self).to_dictionary()
        if self.error_id is not None:
            dictionary['errorId'] = self.error_id
        if self.errors is not None:
            dictionary['errors'] = []
            for element in self.errors:
                if element is not None:
                    dictionary['errors'].append(element.to_dictionary())
        if self.refund_result is not None:
            dictionary['refundResult'] = self.refund_result.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundErrorResponse, self).from_dictionary(dictionary)
        if 'errorId' in dictionary:
            self.error_id = dictionary['errorId']
        if 'errors' in dictionary:
            if not isinstance(dictionary['errors'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['errors']))
            self.errors = []
            for element in dictionary['errors']:
                value = APIError()
                self.errors.append(value.from_dictionary(element))
        if 'refundResult' in dictionary:
            if not isinstance(dictionary['refundResult'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['refundResult']))
            value = RefundResponse()
            self.refund_result = value.from_dictionary(dictionary['refundResult'])
        return self
