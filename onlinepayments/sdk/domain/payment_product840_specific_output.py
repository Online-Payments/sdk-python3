# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.address import Address
from onlinepayments.sdk.domain.payment_product840_customer_account import PaymentProduct840CustomerAccount
from onlinepayments.sdk.domain.protection_eligibility import ProtectionEligibility


class PaymentProduct840SpecificOutput(DataObject):
    """
    | PayPal (payment product 840) specific details
    """

    __billing_address = None
    __customer_account = None
    __customer_address = None
    __protection_eligibility = None

    @property
    def billing_address(self) -> Address:
        """
        | Object containing billing address details

        Type: :class:`onlinepayments.sdk.domain.address.Address`
        """
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value: Address):
        self.__billing_address = value

    @property
    def customer_account(self) -> PaymentProduct840CustomerAccount:
        """
        | Object containing the details of the PayPal account

        Type: :class:`onlinepayments.sdk.domain.payment_product840_customer_account.PaymentProduct840CustomerAccount`
        """
        return self.__customer_account

    @customer_account.setter
    def customer_account(self, value: PaymentProduct840CustomerAccount):
        self.__customer_account = value

    @property
    def customer_address(self) -> Address:
        """
        | Object containing billing address details

        Type: :class:`onlinepayments.sdk.domain.address.Address`
        """
        return self.__customer_address

    @customer_address.setter
    def customer_address(self, value: Address):
        self.__customer_address = value

    @property
    def protection_eligibility(self) -> ProtectionEligibility:
        """
        | Kind of seller protection in force for the PayPal transaction

        Type: :class:`onlinepayments.sdk.domain.protection_eligibility.ProtectionEligibility`
        """
        return self.__protection_eligibility

    @protection_eligibility.setter
    def protection_eligibility(self, value: ProtectionEligibility):
        self.__protection_eligibility = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct840SpecificOutput, self).to_dictionary()
        if self.billing_address is not None:
            dictionary['billingAddress'] = self.billing_address.to_dictionary()
        if self.customer_account is not None:
            dictionary['customerAccount'] = self.customer_account.to_dictionary()
        if self.customer_address is not None:
            dictionary['customerAddress'] = self.customer_address.to_dictionary()
        if self.protection_eligibility is not None:
            dictionary['protectionEligibility'] = self.protection_eligibility.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct840SpecificOutput, self).from_dictionary(dictionary)
        if 'billingAddress' in dictionary:
            if not isinstance(dictionary['billingAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['billingAddress']))
            value = Address()
            self.billing_address = value.from_dictionary(dictionary['billingAddress'])
        if 'customerAccount' in dictionary:
            if not isinstance(dictionary['customerAccount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerAccount']))
            value = PaymentProduct840CustomerAccount()
            self.customer_account = value.from_dictionary(dictionary['customerAccount'])
        if 'customerAddress' in dictionary:
            if not isinstance(dictionary['customerAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerAddress']))
            value = Address()
            self.customer_address = value.from_dictionary(dictionary['customerAddress'])
        if 'protectionEligibility' in dictionary:
            if not isinstance(dictionary['protectionEligibility'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['protectionEligibility']))
            value = ProtectionEligibility()
            self.protection_eligibility = value.from_dictionary(dictionary['protectionEligibility'])
        return self
