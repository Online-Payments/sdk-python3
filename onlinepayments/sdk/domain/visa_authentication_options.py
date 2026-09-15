# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class VisaAuthenticationOptions(DataObject):

    __acquirer_bin: Optional[str] = None
    __acquirer_merchant_id: Optional[str] = None
    __merchant_name: Optional[str] = None

    @property
    def acquirer_bin(self) -> Optional[str]:
        """
        | Acquirer identification code as assigned by the Directory Server.

        Type: str
        """
        return self.__acquirer_bin

    @acquirer_bin.setter
    def acquirer_bin(self, value: Optional[str]) -> None:
        self.__acquirer_bin = value

    @property
    def acquirer_merchant_id(self) -> Optional[str]:
        """
        | Acquirer-assigned Merchant identifier.

        Type: str
        """
        return self.__acquirer_merchant_id

    @acquirer_merchant_id.setter
    def acquirer_merchant_id(self, value: Optional[str]) -> None:
        self.__acquirer_merchant_id = value

    @property
    def merchant_name(self) -> Optional[str]:
        """
        | Merchant name assigned by the Acquirer or Payment System.

        Type: str
        """
        return self.__merchant_name

    @merchant_name.setter
    def merchant_name(self, value: Optional[str]) -> None:
        self.__merchant_name = value

    def to_dictionary(self) -> dict:
        dictionary = super(VisaAuthenticationOptions, self).to_dictionary()
        if self.acquirer_bin is not None:
            dictionary['acquirerBIN'] = self.acquirer_bin
        if self.acquirer_merchant_id is not None:
            dictionary['acquirerMerchantId'] = self.acquirer_merchant_id
        if self.merchant_name is not None:
            dictionary['merchantName'] = self.merchant_name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'VisaAuthenticationOptions':
        super(VisaAuthenticationOptions, self).from_dictionary(dictionary)
        if 'acquirerBIN' in dictionary:
            self.acquirer_bin = dictionary['acquirerBIN']
        if 'acquirerMerchantId' in dictionary:
            self.acquirer_merchant_id = dictionary['acquirerMerchantId']
        if 'merchantName' in dictionary:
            self.merchant_name = dictionary['merchantName']
        return self
