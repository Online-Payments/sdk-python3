# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .bank_account_iban import BankAccountIban
from .data_object import DataObject
from .mandate_address import MandateAddress
from .mandate_contact_details import MandateContactDetails
from .mandate_personal_information import MandatePersonalInformation


class MandateCustomer(DataObject):

    __bank_account_iban: Optional[BankAccountIban] = None
    __company_name: Optional[str] = None
    __contact_details: Optional[MandateContactDetails] = None
    __mandate_address: Optional[MandateAddress] = None
    __personal_information: Optional[MandatePersonalInformation] = None

    @property
    def bank_account_iban(self) -> Optional[BankAccountIban]:
        """
        | Object containing IBAN information

        Type: :class:`onlinepayments.sdk.domain.bank_account_iban.BankAccountIban`
        """
        return self.__bank_account_iban

    @bank_account_iban.setter
    def bank_account_iban(self, value: Optional[BankAccountIban]) -> None:
        self.__bank_account_iban = value

    @property
    def company_name(self) -> Optional[str]:
        """
        | Name of company, as a customer

        Type: str
        """
        return self.__company_name

    @company_name.setter
    def company_name(self, value: Optional[str]) -> None:
        self.__company_name = value

    @property
    def contact_details(self) -> Optional[MandateContactDetails]:
        """
        | Object containing email address

        Type: :class:`onlinepayments.sdk.domain.mandate_contact_details.MandateContactDetails`
        """
        return self.__contact_details

    @contact_details.setter
    def contact_details(self, value: Optional[MandateContactDetails]) -> None:
        self.__contact_details = value

    @property
    def mandate_address(self) -> Optional[MandateAddress]:
        """
        | Object containing consumer address details. Required for Create mandate and Create payment calls. Required for Create hostedCheckout calls where the IBAN is also provided.

        Type: :class:`onlinepayments.sdk.domain.mandate_address.MandateAddress`
        """
        return self.__mandate_address

    @mandate_address.setter
    def mandate_address(self, value: Optional[MandateAddress]) -> None:
        self.__mandate_address = value

    @property
    def personal_information(self) -> Optional[MandatePersonalInformation]:
        """
        | Object containing personal information of the customer. Required for Create mandate and Create payment calls.

        Type: :class:`onlinepayments.sdk.domain.mandate_personal_information.MandatePersonalInformation`
        """
        return self.__personal_information

    @personal_information.setter
    def personal_information(self, value: Optional[MandatePersonalInformation]) -> None:
        self.__personal_information = value

    def to_dictionary(self) -> dict:
        dictionary = super(MandateCustomer, self).to_dictionary()
        if self.bank_account_iban is not None:
            dictionary['bankAccountIban'] = self.bank_account_iban.to_dictionary()
        if self.company_name is not None:
            dictionary['companyName'] = self.company_name
        if self.contact_details is not None:
            dictionary['contactDetails'] = self.contact_details.to_dictionary()
        if self.mandate_address is not None:
            dictionary['mandateAddress'] = self.mandate_address.to_dictionary()
        if self.personal_information is not None:
            dictionary['personalInformation'] = self.personal_information.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MandateCustomer':
        super(MandateCustomer, self).from_dictionary(dictionary)
        if 'bankAccountIban' in dictionary:
            if not isinstance(dictionary['bankAccountIban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountIban']))
            value = BankAccountIban()
            self.bank_account_iban = value.from_dictionary(dictionary['bankAccountIban'])
        if 'companyName' in dictionary:
            self.company_name = dictionary['companyName']
        if 'contactDetails' in dictionary:
            if not isinstance(dictionary['contactDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['contactDetails']))
            value = MandateContactDetails()
            self.contact_details = value.from_dictionary(dictionary['contactDetails'])
        if 'mandateAddress' in dictionary:
            if not isinstance(dictionary['mandateAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandateAddress']))
            value = MandateAddress()
            self.mandate_address = value.from_dictionary(dictionary['mandateAddress'])
        if 'personalInformation' in dictionary:
            if not isinstance(dictionary['personalInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['personalInformation']))
            value = MandatePersonalInformation()
            self.personal_information = value.from_dictionary(dictionary['personalInformation'])
        return self
