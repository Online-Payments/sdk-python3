# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .address import Address
from .data_object import DataObject


class SubMerchant(DataObject):

    __address: Optional[Address] = None
    __company_identification_number: Optional[str] = None
    __company_name: Optional[str] = None
    __merchant_category_code: Optional[str] = None
    __merchant_id: Optional[str] = None

    @property
    def address(self) -> Optional[Address]:
        """
        | Object containing billing address details.

        Type: :class:`onlinepayments.sdk.domain.address.Address`
        """
        return self.__address

    @address.setter
    def address(self, value: Optional[Address]) -> None:
        self.__address = value

    @property
    def company_identification_number(self) -> Optional[str]:
        """
        | Business Establishment Directory Identification System

        Type: str
        """
        return self.__company_identification_number

    @company_identification_number.setter
    def company_identification_number(self, value: Optional[str]) -> None:
        self.__company_identification_number = value

    @property
    def company_name(self) -> Optional[str]:
        """
        | Name of the sales establishment requesting the transaction.

        Type: str
        """
        return self.__company_name

    @company_name.setter
    def company_name(self, value: Optional[str]) -> None:
        self.__company_name = value

    @property
    def merchant_category_code(self) -> Optional[str]:
        """
        | MCC is a four-digit number that classifies the type of goods or services a business offers.

        Type: str
        """
        return self.__merchant_category_code

    @merchant_category_code.setter
    def merchant_category_code(self, value: Optional[str]) -> None:
        self.__merchant_category_code = value

    @property
    def merchant_id(self) -> Optional[str]:
        """
        | Merchant Identifier is a value defined by the acquirer.

        Type: str
        """
        return self.__merchant_id

    @merchant_id.setter
    def merchant_id(self, value: Optional[str]) -> None:
        self.__merchant_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(SubMerchant, self).to_dictionary()
        if self.address is not None:
            dictionary['address'] = self.address.to_dictionary()
        if self.company_identification_number is not None:
            dictionary['companyIdentificationNumber'] = self.company_identification_number
        if self.company_name is not None:
            dictionary['companyName'] = self.company_name
        if self.merchant_category_code is not None:
            dictionary['merchantCategoryCode'] = self.merchant_category_code
        if self.merchant_id is not None:
            dictionary['merchantId'] = self.merchant_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SubMerchant':
        super(SubMerchant, self).from_dictionary(dictionary)
        if 'address' in dictionary:
            if not isinstance(dictionary['address'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['address']))
            value = Address()
            self.address = value.from_dictionary(dictionary['address'])
        if 'companyIdentificationNumber' in dictionary:
            self.company_identification_number = dictionary['companyIdentificationNumber']
        if 'companyName' in dictionary:
            self.company_name = dictionary['companyName']
        if 'merchantCategoryCode' in dictionary:
            self.merchant_category_code = dictionary['merchantCategoryCode']
        if 'merchantId' in dictionary:
            self.merchant_id = dictionary['merchantId']
        return self
