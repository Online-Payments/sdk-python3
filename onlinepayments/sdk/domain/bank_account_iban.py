# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class BankAccountIban(DataObject):

    __iban: Optional[str] = None

    @property
    def iban(self) -> Optional[str]:
        """
        | The IBAN is the International Bank Account Number. It is an internationally agreed format for the BBAN and includes the ISO country code and two check digits. Required for the creation of a Payout Required for Create and Update token. Required for Create mandate and Create payment with mandate calls.

        Type: str
        """
        return self.__iban

    @iban.setter
    def iban(self, value: Optional[str]) -> None:
        self.__iban = value

    def to_dictionary(self) -> dict:
        dictionary = super(BankAccountIban, self).to_dictionary()
        if self.iban is not None:
            dictionary['iban'] = self.iban
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'BankAccountIban':
        super(BankAccountIban, self).from_dictionary(dictionary)
        if 'iban' in dictionary:
            self.iban = dictionary['iban']
        return self
