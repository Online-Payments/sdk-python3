# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class MandateContactDetails(DataObject):
    """
    | Object containing contact details like email address and phone number
    """

    __email_address = None

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

    def to_dictionary(self):
        dictionary = super(MandateContactDetails, self).to_dictionary()
        if self.email_address is not None:
            dictionary['emailAddress'] = self.email_address
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateContactDetails, self).from_dictionary(dictionary)
        if 'emailAddress' in dictionary:
            self.email_address = dictionary['emailAddress']
        return self
