# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .customer_bank_account import CustomerBankAccount
from .data_object import DataObject


class RedirectPaymentProduct5406SpecificInput(DataObject):

    __customer_bank_account: Optional[CustomerBankAccount] = None

    @property
    def customer_bank_account(self) -> Optional[CustomerBankAccount]:
        """
        | Data of customer bank account

        Type: :class:`onlinepayments.sdk.domain.customer_bank_account.CustomerBankAccount`
        """
        return self.__customer_bank_account

    @customer_bank_account.setter
    def customer_bank_account(self, value: Optional[CustomerBankAccount]) -> None:
        self.__customer_bank_account = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct5406SpecificInput, self).to_dictionary()
        if self.customer_bank_account is not None:
            dictionary['customerBankAccount'] = self.customer_bank_account.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5406SpecificInput':
        super(RedirectPaymentProduct5406SpecificInput, self).from_dictionary(dictionary)
        if 'customerBankAccount' in dictionary:
            if not isinstance(dictionary['customerBankAccount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerBankAccount']))
            value = CustomerBankAccount()
            self.customer_bank_account = value.from_dictionary(dictionary['customerBankAccount'])
        return self
