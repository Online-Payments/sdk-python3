# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PayoutStatusOutput(DataObject):

    __is_cancellable: Optional[bool] = None
    __status_category: Optional[str] = None
    __status_code: Optional[int] = None

    @property
    def is_cancellable(self) -> Optional[bool]:
        """
        | Flag indicating if the payout can be cancelled
        
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

    def to_dictionary(self) -> dict:
        dictionary = super(PayoutStatusOutput, self).to_dictionary()
        if self.is_cancellable is not None:
            dictionary['isCancellable'] = self.is_cancellable
        if self.status_category is not None:
            dictionary['statusCategory'] = self.status_category
        if self.status_code is not None:
            dictionary['statusCode'] = self.status_code
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PayoutStatusOutput':
        super(PayoutStatusOutput, self).from_dictionary(dictionary)
        if 'isCancellable' in dictionary:
            self.is_cancellable = dictionary['isCancellable']
        if 'statusCategory' in dictionary:
            self.status_category = dictionary['statusCategory']
        if 'statusCode' in dictionary:
            self.status_code = dictionary['statusCode']
        return self
