# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct840CustomerAccount(DataObject):

    __account_id: Optional[str] = None
    __company_name: Optional[str] = None
    __country_code: Optional[str] = None
    __customer_account_status: Optional[str] = None
    __customer_address_status: Optional[str] = None
    __first_name: Optional[str] = None
    __payer_id: Optional[str] = None
    __surname: Optional[str] = None

    @property
    def account_id(self) -> Optional[str]:
        """
        | Username with which the PayPal account holder has registered at PayPal

        Type: str
        """
        return self.__account_id

    @account_id.setter
    def account_id(self, value: Optional[str]) -> None:
        self.__account_id = value

    @property
    def company_name(self) -> Optional[str]:
        """
        | Name of the company in case the PayPal account is owned by a business

        Type: str
        """
        return self.__company_name

    @company_name.setter
    def company_name(self, value: Optional[str]) -> None:
        self.__company_name = value

    @property
    def country_code(self) -> Optional[str]:
        """
        | ISO 3166-1 alpha-2 country code

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: Optional[str]) -> None:
        self.__country_code = value

    @property
    def customer_account_status(self) -> Optional[str]:
        """
        | Status of the PayPal account
        
        * verified - PayPal has verified the funding means for this account
        * unverified - PayPal has not verified the funding means for this account

        Type: str
        """
        return self.__customer_account_status

    @customer_account_status.setter
    def customer_account_status(self, value: Optional[str]) -> None:
        self.__customer_account_status = value

    @property
    def customer_address_status(self) -> Optional[str]:
        """
        | Status of the customer's shipping address as registered by PayPal
        
        * none - Status is unknown at PayPal
        * confirmed - The address has been confirmed
        * unconfirmed - The address has not been confirmed

        Type: str
        """
        return self.__customer_address_status

    @customer_address_status.setter
    def customer_address_status(self, value: Optional[str]) -> None:
        self.__customer_address_status = value

    @property
    def first_name(self) -> Optional[str]:
        """
        | First name of the PayPal account holder

        Type: str
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value: Optional[str]) -> None:
        self.__first_name = value

    @property
    def payer_id(self) -> Optional[str]:
        """
        | The unique identifier of a PayPal account and will never change in the life cycle of a PayPal account

        Type: str
        """
        return self.__payer_id

    @payer_id.setter
    def payer_id(self, value: Optional[str]) -> None:
        self.__payer_id = value

    @property
    def surname(self) -> Optional[str]:
        """
        | Surname of the PayPal account holder

        Type: str
        """
        return self.__surname

    @surname.setter
    def surname(self, value: Optional[str]) -> None:
        self.__surname = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct840CustomerAccount, self).to_dictionary()
        if self.account_id is not None:
            dictionary['accountId'] = self.account_id
        if self.company_name is not None:
            dictionary['companyName'] = self.company_name
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.customer_account_status is not None:
            dictionary['customerAccountStatus'] = self.customer_account_status
        if self.customer_address_status is not None:
            dictionary['customerAddressStatus'] = self.customer_address_status
        if self.first_name is not None:
            dictionary['firstName'] = self.first_name
        if self.payer_id is not None:
            dictionary['payerId'] = self.payer_id
        if self.surname is not None:
            dictionary['surname'] = self.surname
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct840CustomerAccount':
        super(PaymentProduct840CustomerAccount, self).from_dictionary(dictionary)
        if 'accountId' in dictionary:
            self.account_id = dictionary['accountId']
        if 'companyName' in dictionary:
            self.company_name = dictionary['companyName']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'customerAccountStatus' in dictionary:
            self.customer_account_status = dictionary['customerAccountStatus']
        if 'customerAddressStatus' in dictionary:
            self.customer_address_status = dictionary['customerAddressStatus']
        if 'firstName' in dictionary:
            self.first_name = dictionary['firstName']
        if 'payerId' in dictionary:
            self.payer_id = dictionary['payerId']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        return self
