# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .address import Address
from .company_information import CompanyInformation
from .contact_details import ContactDetails
from .customer_account import CustomerAccount
from .customer_device import CustomerDevice
from .data_object import DataObject
from .personal_information import PersonalInformation


class Customer(DataObject):

    __account: Optional[CustomerAccount] = None
    __account_type: Optional[str] = None
    __billing_address: Optional[Address] = None
    __company_information: Optional[CompanyInformation] = None
    __contact_details: Optional[ContactDetails] = None
    __device: Optional[CustomerDevice] = None
    __fiscal_number: Optional[str] = None
    __locale: Optional[str] = None
    __merchant_customer_id: Optional[str] = None
    __personal_information: Optional[PersonalInformation] = None

    @property
    def account(self) -> Optional[CustomerAccount]:
        """
        | Object containing data related to the account the customer has with you

        Type: :class:`onlinepayments.sdk.domain.customer_account.CustomerAccount`
        """
        return self.__account

    @account.setter
    def account(self, value: Optional[CustomerAccount]) -> None:
        self.__account = value

    @property
    def account_type(self) -> Optional[str]:
        """
        | Type of the customer account that is used to place this order. Can have one of the following values:
        
        * none - The account that was used to place the order with is a guest account or no account was used at all
        * created - The customer account was created during this transaction
        * existing - The customer account was an already existing account prior to this transaction

        Type: str
        """
        return self.__account_type

    @account_type.setter
    def account_type(self, value: Optional[str]) -> None:
        self.__account_type = value

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
    def company_information(self) -> Optional[CompanyInformation]:
        """
        | Object containing company information

        Type: :class:`onlinepayments.sdk.domain.company_information.CompanyInformation`
        """
        return self.__company_information

    @company_information.setter
    def company_information(self, value: Optional[CompanyInformation]) -> None:
        self.__company_information = value

    @property
    def contact_details(self) -> Optional[ContactDetails]:
        """
        | Object containing contact details like email address and phone number

        Type: :class:`onlinepayments.sdk.domain.contact_details.ContactDetails`
        """
        return self.__contact_details

    @contact_details.setter
    def contact_details(self, value: Optional[ContactDetails]) -> None:
        self.__contact_details = value

    @property
    def device(self) -> Optional[CustomerDevice]:
        """
        | Object containing information on the device and browser of the customer

        Type: :class:`onlinepayments.sdk.domain.customer_device.CustomerDevice`
        """
        return self.__device

    @device.setter
    def device(self, value: Optional[CustomerDevice]) -> None:
        self.__device = value

    @property
    def fiscal_number(self) -> Optional[str]:
        """
        | Fiscal registration number of the customer or the tax registration number of the company for a business customer. Please find below specifics per country:
        
        * Brazil - Consumer (CPF) with a length of 11 digits
        * Brazil - Company (CNPJ) with a length of 14 digits
        * Denmark - Consumer (CPR-nummer or personnummer) with a length of 10 digits
        * Finland - Consumer (Finnish: henkilötunnus (abbreviated as HETU), Swedish: personbeteckning) with a length of 11 characters
        * Norway - Consumer (fødselsnummer) with a length of 11 digits
        * Sweden - Consumer (personnummer) with a length of 10 or 12 digits

        Type: str
        """
        return self.__fiscal_number

    @fiscal_number.setter
    def fiscal_number(self, value: Optional[str]) -> None:
        self.__fiscal_number = value

    @property
    def locale(self) -> Optional[str]:
        """
        | The locale that the customer should be addressed in (for 3rd parties). Note that some 3rd party providers only support the languageCode part of the locale, in those cases we will only use part of the locale provided.

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: Optional[str]) -> None:
        self.__locale = value

    @property
    def merchant_customer_id(self) -> Optional[str]:
        """
        | Your identifier for the customer. It is used in the fraud-screening process for payments on the payment platform.

        Type: str
        """
        return self.__merchant_customer_id

    @merchant_customer_id.setter
    def merchant_customer_id(self, value: Optional[str]) -> None:
        self.__merchant_customer_id = value

    @property
    def personal_information(self) -> Optional[PersonalInformation]:
        """
        | Object containing personal information like name, date of birth and gender.

        Type: :class:`onlinepayments.sdk.domain.personal_information.PersonalInformation`
        """
        return self.__personal_information

    @personal_information.setter
    def personal_information(self, value: Optional[PersonalInformation]) -> None:
        self.__personal_information = value

    def to_dictionary(self) -> dict:
        dictionary = super(Customer, self).to_dictionary()
        if self.account is not None:
            dictionary['account'] = self.account.to_dictionary()
        if self.account_type is not None:
            dictionary['accountType'] = self.account_type
        if self.billing_address is not None:
            dictionary['billingAddress'] = self.billing_address.to_dictionary()
        if self.company_information is not None:
            dictionary['companyInformation'] = self.company_information.to_dictionary()
        if self.contact_details is not None:
            dictionary['contactDetails'] = self.contact_details.to_dictionary()
        if self.device is not None:
            dictionary['device'] = self.device.to_dictionary()
        if self.fiscal_number is not None:
            dictionary['fiscalNumber'] = self.fiscal_number
        if self.locale is not None:
            dictionary['locale'] = self.locale
        if self.merchant_customer_id is not None:
            dictionary['merchantCustomerId'] = self.merchant_customer_id
        if self.personal_information is not None:
            dictionary['personalInformation'] = self.personal_information.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Customer':
        super(Customer, self).from_dictionary(dictionary)
        if 'account' in dictionary:
            if not isinstance(dictionary['account'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['account']))
            value = CustomerAccount()
            self.account = value.from_dictionary(dictionary['account'])
        if 'accountType' in dictionary:
            self.account_type = dictionary['accountType']
        if 'billingAddress' in dictionary:
            if not isinstance(dictionary['billingAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['billingAddress']))
            value = Address()
            self.billing_address = value.from_dictionary(dictionary['billingAddress'])
        if 'companyInformation' in dictionary:
            if not isinstance(dictionary['companyInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['companyInformation']))
            value = CompanyInformation()
            self.company_information = value.from_dictionary(dictionary['companyInformation'])
        if 'contactDetails' in dictionary:
            if not isinstance(dictionary['contactDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['contactDetails']))
            value = ContactDetails()
            self.contact_details = value.from_dictionary(dictionary['contactDetails'])
        if 'device' in dictionary:
            if not isinstance(dictionary['device'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['device']))
            value = CustomerDevice()
            self.device = value.from_dictionary(dictionary['device'])
        if 'fiscalNumber' in dictionary:
            self.fiscal_number = dictionary['fiscalNumber']
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'merchantCustomerId' in dictionary:
            self.merchant_customer_id = dictionary['merchantCustomerId']
        if 'personalInformation' in dictionary:
            if not isinstance(dictionary['personalInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['personalInformation']))
            value = PersonalInformation()
            self.personal_information = value.from_dictionary(dictionary['personalInformation'])
        return self
