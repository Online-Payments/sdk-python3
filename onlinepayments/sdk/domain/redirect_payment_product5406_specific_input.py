# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.customer_bank_account import CustomerBankAccount


class RedirectPaymentProduct5406SpecificInput(DataObject):
    """
    | Object containing specific input for EPS payments (Payment product ID 5406)
    """

    __customer_bank_account = None

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

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct5406SpecificInput, self).to_dictionary()
        if self.customer_bank_account is not None:
            dictionary['customerBankAccount'] = self.customer_bank_account.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct5406SpecificInput, self).from_dictionary(dictionary)
        if 'customerBankAccount' in dictionary:
            if not isinstance(dictionary['customerBankAccount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerBankAccount']))
            value = CustomerBankAccount()
            self.customer_bank_account = value.from_dictionary(dictionary['customerBankAccount'])
        return self
