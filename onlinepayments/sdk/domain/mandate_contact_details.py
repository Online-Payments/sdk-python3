# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class MandateContactDetails(DataObject):

    __email_address: Optional[str] = None

    @property
    def email_address(self) -> Optional[str]:
        """
        | Email address of the customer

        Type: str
        """
        return self.__email_address

    @email_address.setter
    def email_address(self, value: Optional[str]) -> None:
        self.__email_address = value

    def to_dictionary(self) -> dict:
        dictionary = super(MandateContactDetails, self).to_dictionary()
        if self.email_address is not None:
            dictionary['emailAddress'] = self.email_address
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MandateContactDetails':
        super(MandateContactDetails, self).from_dictionary(dictionary)
        if 'emailAddress' in dictionary:
            self.email_address = dictionary['emailAddress']
        return self
