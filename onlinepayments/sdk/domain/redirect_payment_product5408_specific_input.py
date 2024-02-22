# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.customer_bank_account import CustomerBankAccount


class RedirectPaymentProduct5408SpecificInput(DataObject):
    """
    | Object containing specific input for Account to Account payments (Payment product ID 5408)
    """

    __customer_bank_account = None
    __instant_payment_only = None

    @property
    def customer_bank_account(self) -> CustomerBankAccount:
        """
        | Data of customer bank account

        Type: :class:`onlinepayments.sdk.domain.customer_bank_account.CustomerBankAccount`
        """
        return self.__customer_bank_account

    @customer_bank_account.setter
    def customer_bank_account(self, value: CustomerBankAccount):
        self.__customer_bank_account = value

    @property
    def instant_payment_only(self) -> bool:
        """
        | * true - consumer can only use instant payment for Account to Account Bank transfer payments
        | * false - consumer can only use standard payment for Account to Account Bank transfer payments

        Type: bool
        """
        return self.__instant_payment_only

    @instant_payment_only.setter
    def instant_payment_only(self, value: bool):
        self.__instant_payment_only = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct5408SpecificInput, self).to_dictionary()
        if self.customer_bank_account is not None:
            dictionary['customerBankAccount'] = self.customer_bank_account.to_dictionary()
        if self.instant_payment_only is not None:
            dictionary['instantPaymentOnly'] = self.instant_payment_only
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct5408SpecificInput, self).from_dictionary(dictionary)
        if 'customerBankAccount' in dictionary:
            if not isinstance(dictionary['customerBankAccount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerBankAccount']))
            value = CustomerBankAccount()
            self.customer_bank_account = value.from_dictionary(dictionary['customerBankAccount'])
        if 'instantPaymentOnly' in dictionary:
            self.instant_payment_only = dictionary['instantPaymentOnly']
        return self
