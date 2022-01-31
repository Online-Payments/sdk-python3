# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class ContactDetails(DataObject):
    """
    | Object containing contact details like email address and phone number
    """

    __email_address = None
    __fax_number = None
    __mobile_phone_number = None
    __phone_number = None
    __work_phone_number = None

    @property
    def email_address(self) -> str:
        """
        | Email address of the customer

        Type: str
        """
        return self.__email_address

    @email_address.setter
    def email_address(self, value: str):
        self.__email_address = value

    @property
    def fax_number(self) -> str:
        """
        | Fax number of the customer

        Type: str
        """
        return self.__fax_number

    @fax_number.setter
    def fax_number(self, value: str):
        self.__fax_number = value

    @property
    def mobile_phone_number(self) -> str:
        """
        | International version of the mobile phone number of the customer including the leading + (i.e. +16127779311)

        Type: str
        """
        return self.__mobile_phone_number

    @mobile_phone_number.setter
    def mobile_phone_number(self, value: str):
        self.__mobile_phone_number = value

    @property
    def phone_number(self) -> str:
        """
        | Phone number of the customer

        Type: str
        """
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        self.__phone_number = value

    @property
    def work_phone_number(self) -> str:
        """
        | International version of the work phone number of the customer including the leading + (i.e. +31235671500)

        Type: str
        """
        return self.__work_phone_number

    @work_phone_number.setter
    def work_phone_number(self, value: str):
        self.__work_phone_number = value

    def to_dictionary(self):
        dictionary = super(ContactDetails, self).to_dictionary()
        if self.email_address is not None:
            dictionary['emailAddress'] = self.email_address
        if self.fax_number is not None:
            dictionary['faxNumber'] = self.fax_number
        if self.mobile_phone_number is not None:
            dictionary['mobilePhoneNumber'] = self.mobile_phone_number
        if self.phone_number is not None:
            dictionary['phoneNumber'] = self.phone_number
        if self.work_phone_number is not None:
            dictionary['workPhoneNumber'] = self.work_phone_number
        return dictionary

    def from_dictionary(self, dictionary):
        super(ContactDetails, self).from_dictionary(dictionary)
        if 'emailAddress' in dictionary:
            self.email_address = dictionary['emailAddress']
        if 'faxNumber' in dictionary:
            self.fax_number = dictionary['faxNumber']
        if 'mobilePhoneNumber' in dictionary:
            self.mobile_phone_number = dictionary['mobilePhoneNumber']
        if 'phoneNumber' in dictionary:
            self.phone_number = dictionary['phoneNumber']
        if 'workPhoneNumber' in dictionary:
            self.work_phone_number = dictionary['workPhoneNumber']
        return self
