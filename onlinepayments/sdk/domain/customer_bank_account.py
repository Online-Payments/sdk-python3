# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class CustomerBankAccount(DataObject):
    """
    | Data of customer bank account
    """

    __account_holder_name = None
    __bic = None
    __iban = None

    @property
    def account_holder_name(self) -> str:
        """
        | Name of account holder

        Type: str
        """
        return self.__account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, value: str):
        self.__account_holder_name = value

    @property
    def bic(self) -> str:
        """
        | Bank Identification Code

        Type: str
        """
        return self.__bic

    @bic.setter
    def bic(self, value: str):
        self.__bic = value

    @property
    def iban(self) -> str:
        """
        | The IBAN is the International Bank Account Number. It is an internationally agreed format for the BBAN and includes the ISO country code and two check digits.

        Type: str
        """
        return self.__iban

    @iban.setter
    def iban(self, value: str):
        self.__iban = value

    def to_dictionary(self):
        dictionary = super(CustomerBankAccount, self).to_dictionary()
        if self.account_holder_name is not None:
            dictionary['accountHolderName'] = self.account_holder_name
        if self.bic is not None:
            dictionary['bic'] = self.bic
        if self.iban is not None:
            dictionary['iban'] = self.iban
        return dictionary

    def from_dictionary(self, dictionary):
        super(CustomerBankAccount, self).from_dictionary(dictionary)
        if 'accountHolderName' in dictionary:
            self.account_holder_name = dictionary['accountHolderName']
        if 'bic' in dictionary:
            self.bic = dictionary['bic']
        if 'iban' in dictionary:
            self.iban = dictionary['iban']
        return self
