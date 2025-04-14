# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .api_error import APIError
from .data_object import DataObject


class OrderStatusOutput(DataObject):

    __errors: Optional[List[APIError]] = None
    __is_cancellable: Optional[bool] = None
    __status_category: Optional[str] = None
    __status_code: Optional[int] = None
    __status_code_change_date_time: Optional[str] = None

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
    def is_cancellable(self) -> Optional[bool]:
        """
        | Flag indicating if the payment can be cancelled
        
        * true
        * false

        Type: bool
        """
        return self.__is_cancellable

    @is_cancellable.setter
    def is_cancellable(self, value: Optional[bool]) -> None:
        self.__is_cancellable = value

    @property
    def status_category(self) -> Optional[str]:
        """
        | Highlevel status of the payment, payout or refund.

        Type: str
        """
        return self.__status_category

    @status_category.setter
    def status_category(self, value: Optional[str]) -> None:
        self.__status_category = value

    @property
    def status_code(self) -> Optional[int]:
        """
        | Numeric status code of the legacy API. The value can also be found in the BackOffice and in report files.

        Type: int
        """
        return self.__status_code

    @status_code.setter
    def status_code(self, value: Optional[int]) -> None:
        self.__status_code = value

    @property
    def status_code_change_date_time(self) -> Optional[str]:
        """
        | Timestamp of the latest status change

        Type: str
        """
        return self.__status_code_change_date_time

    @status_code_change_date_time.setter
    def status_code_change_date_time(self, value: Optional[str]) -> None:
        self.__status_code_change_date_time = value

    def to_dictionary(self) -> dict:
        dictionary = super(OrderStatusOutput, self).to_dictionary()
        if self.errors is not None:
            dictionary['errors'] = []
            for element in self.errors:
                if element is not None:
                    dictionary['errors'].append(element.to_dictionary())
        if self.is_cancellable is not None:
            dictionary['isCancellable'] = self.is_cancellable
        if self.status_category is not None:
            dictionary['statusCategory'] = self.status_category
        if self.status_code is not None:
            dictionary['statusCode'] = self.status_code
        if self.status_code_change_date_time is not None:
            dictionary['statusCodeChangeDateTime'] = self.status_code_change_date_time
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OrderStatusOutput':
        super(OrderStatusOutput, self).from_dictionary(dictionary)
        if 'errors' in dictionary:
            if not isinstance(dictionary['errors'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['errors']))
            self.errors = []
            for element in dictionary['errors']:
                value = APIError()
                self.errors.append(value.from_dictionary(element))
        if 'isCancellable' in dictionary:
            self.is_cancellable = dictionary['isCancellable']
        if 'statusCategory' in dictionary:
            self.status_category = dictionary['statusCategory']
        if 'statusCode' in dictionary:
            self.status_code = dictionary['statusCode']
        if 'statusCodeChangeDateTime' in dictionary:
            self.status_code_change_date_time = dictionary['statusCodeChangeDateTime']
        return self
