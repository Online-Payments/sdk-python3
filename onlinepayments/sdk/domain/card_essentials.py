# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CardEssentials(DataObject):

    __bin: Optional[str] = None
    __card_number: Optional[str] = None
    __country_code: Optional[str] = None
    __expiry_date: Optional[str] = None

    @property
    def bin(self) -> Optional[str]:
        """
        | The first digits of the credit card number from left to right with a minimum of 6 digits.

        Type: str
        """
        return self.__bin

    @bin.setter
    def bin(self, value: Optional[str]) -> None:
        self.__bin = value

    @property
    def card_number(self) -> Optional[str]:
        """
        | The masked credit/debit card number

        Type: str
        """
        return self.__card_number

    @card_number.setter
    def card_number(self, value: Optional[str]) -> None:
        self.__card_number = value

    @property
    def country_code(self) -> Optional[str]:
        """
        | ISO 3166-1 alpha-2 country code

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: Optional[str]) -> None:
        self.__country_code = value

    @property
    def expiry_date(self) -> Optional[str]:
        """
        | Expiry date of the card Format: MMYY

        Type: str
        """
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value: Optional[str]) -> None:
        self.__expiry_date = value

    def to_dictionary(self) -> dict:
        dictionary = super(CardEssentials, self).to_dictionary()
        if self.bin is not None:
            dictionary['bin'] = self.bin
        if self.card_number is not None:
            dictionary['cardNumber'] = self.card_number
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.expiry_date is not None:
            dictionary['expiryDate'] = self.expiry_date
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardEssentials':
        super(CardEssentials, self).from_dictionary(dictionary)
        if 'bin' in dictionary:
            self.bin = dictionary['bin']
        if 'cardNumber' in dictionary:
            self.card_number = dictionary['cardNumber']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        return self
