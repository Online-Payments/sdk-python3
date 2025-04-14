# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .customer_bank_account import CustomerBankAccount
from .data_object import DataObject


class RedirectPaymentProduct5408SpecificInput(DataObject):

    __customer_bank_account: Optional[CustomerBankAccount] = None
    __instant_payment_only: Optional[bool] = None

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

    @property
    def instant_payment_only(self) -> Optional[bool]:
        """
        * true - consumer can only use instant payment for Account to Account Bank transfer payments
        * false - consumer can only use standard payment for Account to Account Bank transfer payments

        Type: bool
        """
        return self.__instant_payment_only

    @instant_payment_only.setter
    def instant_payment_only(self, value: Optional[bool]) -> None:
        self.__instant_payment_only = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct5408SpecificInput, self).to_dictionary()
        if self.customer_bank_account is not None:
            dictionary['customerBankAccount'] = self.customer_bank_account.to_dictionary()
        if self.instant_payment_only is not None:
            dictionary['instantPaymentOnly'] = self.instant_payment_only
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5408SpecificInput':
        super(RedirectPaymentProduct5408SpecificInput, self).from_dictionary(dictionary)
        if 'customerBankAccount' in dictionary:
            if not isinstance(dictionary['customerBankAccount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerBankAccount']))
            value = CustomerBankAccount()
            self.customer_bank_account = value.from_dictionary(dictionary['customerBankAccount'])
        if 'instantPaymentOnly' in dictionary:
            self.instant_payment_only = dictionary['instantPaymentOnly']
        return self
