# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class Discount(DataObject):

    __amount: Optional[int] = None

    @property
    def amount(self) -> Optional[int]:
        """
        | Amount in the smallest currency unit, i.e.:
        
        * EUR is a 2-decimals currency, the value 1234 will result in EUR 12.34
        * KWD is a 3-decimals currency, the value 1234 will result in KWD 1.234
        * JPY is a zero-decimal currency, the value 1234 will result in JPY 1234

        Type: int
        """
        return self.__amount

    @amount.setter
    def amount(self, value: Optional[int]) -> None:
        self.__amount = value

    def to_dictionary(self) -> dict:
        dictionary = super(Discount, self).to_dictionary()
        if self.amount is not None:
            dictionary['amount'] = self.amount
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Discount':
        super(Discount, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            self.amount = dictionary['amount']
        return self
