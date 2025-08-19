# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .address import Address
from .address_personal import AddressPersonal
from .data_object import DataObject
from .payment_product840_customer_account import PaymentProduct840CustomerAccount
from .protection_eligibility import ProtectionEligibility


class PaymentProduct840SpecificOutput(DataObject):

    __billing_address: Optional[Address] = None
    __billing_personal_address: Optional[AddressPersonal] = None
    __customer_account: Optional[PaymentProduct840CustomerAccount] = None
    __customer_address: Optional[Address] = None
    __protection_eligibility: Optional[ProtectionEligibility] = None

    @property
    def billing_address(self) -> Optional[Address]:
        """
        | Object containing billing address details.

        Type: :class:`onlinepayments.sdk.domain.address.Address`
        """
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value: Optional[Address]) -> None:
        self.__billing_address = value

    @property
    def billing_personal_address(self) -> Optional[AddressPersonal]:
        """
        | Object containing address information

        Type: :class:`onlinepayments.sdk.domain.address_personal.AddressPersonal`
        """
        return self.__billing_personal_address

    @billing_personal_address.setter
    def billing_personal_address(self, value: Optional[AddressPersonal]) -> None:
        self.__billing_personal_address = value

    @property
    def customer_account(self) -> Optional[PaymentProduct840CustomerAccount]:
        """
        | Object containing the details of the PayPal account

        Type: :class:`onlinepayments.sdk.domain.payment_product840_customer_account.PaymentProduct840CustomerAccount`
        """
        return self.__customer_account

    @customer_account.setter
    def customer_account(self, value: Optional[PaymentProduct840CustomerAccount]) -> None:
        self.__customer_account = value

    @property
    def customer_address(self) -> Optional[Address]:
        """
        | Object containing billing address details.

        Type: :class:`onlinepayments.sdk.domain.address.Address`
        """
        return self.__customer_address

    @customer_address.setter
    def customer_address(self, value: Optional[Address]) -> None:
        self.__customer_address = value

    @property
    def protection_eligibility(self) -> Optional[ProtectionEligibility]:
        """
        | Kind of seller protection in force for the PayPal transaction

        Type: :class:`onlinepayments.sdk.domain.protection_eligibility.ProtectionEligibility`
        """
        return self.__protection_eligibility

    @protection_eligibility.setter
    def protection_eligibility(self, value: Optional[ProtectionEligibility]) -> None:
        self.__protection_eligibility = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct840SpecificOutput, self).to_dictionary()
        if self.billing_address is not None:
            dictionary['billingAddress'] = self.billing_address.to_dictionary()
        if self.billing_personal_address is not None:
            dictionary['billingPersonalAddress'] = self.billing_personal_address.to_dictionary()
        if self.customer_account is not None:
            dictionary['customerAccount'] = self.customer_account.to_dictionary()
        if self.customer_address is not None:
            dictionary['customerAddress'] = self.customer_address.to_dictionary()
        if self.protection_eligibility is not None:
            dictionary['protectionEligibility'] = self.protection_eligibility.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct840SpecificOutput':
        super(PaymentProduct840SpecificOutput, self).from_dictionary(dictionary)
        if 'billingAddress' in dictionary:
            if not isinstance(dictionary['billingAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['billingAddress']))
            value = Address()
            self.billing_address = value.from_dictionary(dictionary['billingAddress'])
        if 'billingPersonalAddress' in dictionary:
            if not isinstance(dictionary['billingPersonalAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['billingPersonalAddress']))
            value = AddressPersonal()
            self.billing_personal_address = value.from_dictionary(dictionary['billingPersonalAddress'])
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
