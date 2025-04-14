# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .address import Address
from .company_information import CompanyInformation
from .data_object import DataObject
from .personal_information_token import PersonalInformationToken


class CustomerToken(DataObject):

    __billing_address: Optional[Address] = None
    __company_information: Optional[CompanyInformation] = None
    __personal_information: Optional[PersonalInformationToken] = None

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
    def personal_information(self) -> Optional[PersonalInformationToken]:
        """
        Type: :class:`onlinepayments.sdk.domain.personal_information_token.PersonalInformationToken`
        """
        return self.__personal_information

    @personal_information.setter
    def personal_information(self, value: Optional[PersonalInformationToken]) -> None:
        self.__personal_information = value

    def to_dictionary(self) -> dict:
        dictionary = super(CustomerToken, self).to_dictionary()
        if self.billing_address is not None:
            dictionary['billingAddress'] = self.billing_address.to_dictionary()
        if self.company_information is not None:
            dictionary['companyInformation'] = self.company_information.to_dictionary()
        if self.personal_information is not None:
            dictionary['personalInformation'] = self.personal_information.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CustomerToken':
        super(CustomerToken, self).from_dictionary(dictionary)
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
        if 'personalInformation' in dictionary:
            if not isinstance(dictionary['personalInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['personalInformation']))
            value = PersonalInformationToken()
            self.personal_information = value.from_dictionary(dictionary['personalInformation'])
        return self
