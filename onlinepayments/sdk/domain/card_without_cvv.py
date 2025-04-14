# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CardWithoutCvv(DataObject):

    __card_number: Optional[str] = None
    __cardholder_name: Optional[str] = None
    __expiry_date: Optional[str] = None

    @property
    def card_number(self) -> Optional[str]:
        """
        | The obfuscated card number

        Type: str
        """
        return self.__card_number

    @card_number.setter
    def card_number(self, value: Optional[str]) -> None:
        self.__card_number = value

    @property
    def cardholder_name(self) -> Optional[str]:
        """
        | The card holder's name on the card.

        Type: str
        """
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value: Optional[str]) -> None:
        self.__cardholder_name = value

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
        dictionary = super(CardWithoutCvv, self).to_dictionary()
        if self.card_number is not None:
            dictionary['cardNumber'] = self.card_number
        if self.cardholder_name is not None:
            dictionary['cardholderName'] = self.cardholder_name
        if self.expiry_date is not None:
            dictionary['expiryDate'] = self.expiry_date
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardWithoutCvv':
        super(CardWithoutCvv, self).from_dictionary(dictionary)
        if 'cardNumber' in dictionary:
            self.card_number = dictionary['cardNumber']
        if 'cardholderName' in dictionary:
            self.cardholder_name = dictionary['cardholderName']
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        return self
