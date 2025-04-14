# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .api_error import APIError
from .data_object import DataObject
from .payout_result import PayoutResult


class PayoutErrorResponse(DataObject):

    __error_id: Optional[str] = None
    __errors: Optional[List[APIError]] = None
    __payout_result: Optional[PayoutResult] = None

    @property
    def error_id(self) -> Optional[str]:
        """
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
    def payout_result(self) -> Optional[PayoutResult]:
        """
        Type: :class:`onlinepayments.sdk.domain.payout_result.PayoutResult`
        """
        return self.__payout_result

    @payout_result.setter
    def payout_result(self, value: Optional[PayoutResult]) -> None:
        self.__payout_result = value

    def to_dictionary(self) -> dict:
        dictionary = super(PayoutErrorResponse, self).to_dictionary()
        if self.error_id is not None:
            dictionary['errorId'] = self.error_id
        if self.errors is not None:
            dictionary['errors'] = []
            for element in self.errors:
                if element is not None:
                    dictionary['errors'].append(element.to_dictionary())
        if self.payout_result is not None:
            dictionary['payoutResult'] = self.payout_result.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PayoutErrorResponse':
        super(PayoutErrorResponse, self).from_dictionary(dictionary)
        if 'errorId' in dictionary:
            self.error_id = dictionary['errorId']
        if 'errors' in dictionary:
            if not isinstance(dictionary['errors'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['errors']))
            self.errors = []
            for element in dictionary['errors']:
                value = APIError()
                self.errors.append(value.from_dictionary(element))
        if 'payoutResult' in dictionary:
            if not isinstance(dictionary['payoutResult'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payoutResult']))
            value = PayoutResult()
            self.payout_result = value.from_dictionary(dictionary['payoutResult'])
        return self
