# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class AmountOfMoney(DataObject):

    __amount: Optional[int] = None
    __currency_code: Optional[str] = None

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

    @property
    def currency_code(self) -> Optional[str]:
        """
        | Three-letter ISO currency code representing the currency for the amount

        Type: str
        """
        return self.__currency_code

    @currency_code.setter
    def currency_code(self, value: Optional[str]) -> None:
        self.__currency_code = value

    def to_dictionary(self) -> dict:
        dictionary = super(AmountOfMoney, self).to_dictionary()
        if self.amount is not None:
            dictionary['amount'] = self.amount
        if self.currency_code is not None:
            dictionary['currencyCode'] = self.currency_code
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AmountOfMoney':
        super(AmountOfMoney, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            self.amount = dictionary['amount']
        if 'currencyCode' in dictionary:
            self.currency_code = dictionary['currencyCode']
        return self
