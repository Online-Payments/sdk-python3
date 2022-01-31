# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class BankAccountIban(DataObject):
    """
    | Object containing IBAN information
    """

    __iban = None

    @property
    def iban(self) -> str:
        """
        | The IBAN is the International Bank Account Number. It is an internationally agreed format for the BBAN and includes the ISO country code and two check digits.
        | Required for the creation of a Payout
        | Required for Create and Update token.
        | Required for Create mandate and Create payment with mandate calls.

        Type: str
        """
        return self.__iban

    @iban.setter
    def iban(self, value: str):
        self.__iban = value

    def to_dictionary(self):
        dictionary = super(BankAccountIban, self).to_dictionary()
        if self.iban is not None:
            dictionary['iban'] = self.iban
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankAccountIban, self).from_dictionary(dictionary)
        if 'iban' in dictionary:
            self.iban = dictionary['iban']
        return self
