# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProductSession302SpecificInput(DataObject):

    __display_name: Optional[str] = None
    __domain_name: Optional[str] = None

    @property
    def display_name(self) -> Optional[str]:
        """
        | A human-readable name for the merchant, as it would be displayed to the user within the Apple Pay interface.

        Type: str
        """
        return self.__display_name

    @display_name.setter
    def display_name(self, value: Optional[str]) -> None:
        self.__display_name = value

    @property
    def domain_name(self) -> Optional[str]:
        """
        | The fully qualified domain name of the web page that will host the Apple Pay session.

        Type: str
        """
        return self.__domain_name

    @domain_name.setter
    def domain_name(self, value: Optional[str]) -> None:
        self.__domain_name = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProductSession302SpecificInput, self).to_dictionary()
        if self.display_name is not None:
            dictionary['displayName'] = self.display_name
        if self.domain_name is not None:
            dictionary['domainName'] = self.domain_name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductSession302SpecificInput':
        super(PaymentProductSession302SpecificInput, self).from_dictionary(dictionary)
        if 'displayName' in dictionary:
            self.display_name = dictionary['displayName']
        if 'domainName' in dictionary:
            self.domain_name = dictionary['domainName']
        return self
