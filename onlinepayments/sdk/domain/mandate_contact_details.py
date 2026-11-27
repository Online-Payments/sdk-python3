#
# This file was automatically generated.
#
from .data_object import DataObject


class MandateContactDetails(DataObject):

    __slots__ = (
        "__email_address",
        "__phone_number",
    )

    __email_address: str | None
    __phone_number: str | None

    def __init__(
        self,
        *,
        email_address: str | None = None,
        phone_number: str | None = None,
    ) -> None:
        self.email_address = email_address
        self.phone_number = phone_number

    @property
    def email_address(self) -> str | None:
        """
        | Email address of the customer

        Type: str
        """
        return self.__email_address

    @email_address.setter
    def email_address(self, value: str | None) -> None:
        self.__email_address = value

    @property
    def phone_number(self) -> str | None:
        """
        | International version of the phone number of the customer including the leading + (i.e. +4917612345678)

        Type: str
        """
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str | None) -> None:
        self.__phone_number = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.email_address is not None:
            dictionary['emailAddress'] = self.email_address
        if self.phone_number is not None:
            dictionary['phoneNumber'] = self.phone_number
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MandateContactDetails':
        super().from_dictionary(dictionary)
        if 'emailAddress' in dictionary:
            self.email_address = dictionary['emailAddress']
        if 'phoneNumber' in dictionary:
            self.phone_number = dictionary['phoneNumber']
        return self
