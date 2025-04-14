# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class MobilePaymentData(DataObject):

    __dpan: Optional[str] = None
    __expiry_date: Optional[str] = None

    @property
    def dpan(self) -> Optional[str]:
        """
        | The obfuscated DPAN. Only the last four digits are visible.

        Type: str
        """
        return self.__dpan

    @dpan.setter
    def dpan(self, value: Optional[str]) -> None:
        self.__dpan = value

    @property
    def expiry_date(self) -> Optional[str]:
        """
        | Expiry date of the tokenized card. Format: MMYY

        Type: str
        """
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value: Optional[str]) -> None:
        self.__expiry_date = value

    def to_dictionary(self) -> dict:
        dictionary = super(MobilePaymentData, self).to_dictionary()
        if self.dpan is not None:
            dictionary['dpan'] = self.dpan
        if self.expiry_date is not None:
            dictionary['expiryDate'] = self.expiry_date
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MobilePaymentData':
        super(MobilePaymentData, self).from_dictionary(dictionary)
        if 'dpan' in dictionary:
            self.dpan = dictionary['dpan']
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        return self
