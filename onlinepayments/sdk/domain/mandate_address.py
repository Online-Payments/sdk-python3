# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class MandateAddress(DataObject):

    __city: Optional[str] = None
    __country_code: Optional[str] = None
    __house_number: Optional[str] = None
    __street: Optional[str] = None
    __zip: Optional[str] = None

    @property
    def city(self) -> Optional[str]:
        """
        | City Required for Create mandate and Create payment calls. Required for Create hostedCheckout calls where the IBAN is also provided.

        Type: str
        """
        return self.__city

    @city.setter
    def city(self, value: Optional[str]) -> None:
        self.__city = value

    @property
    def country_code(self) -> Optional[str]:
        """
        | ISO 3166-1 alpha-2 country code. Required for Create mandate and Create payment calls. Required for Create hostedCheckout calls where the IBAN is also provided.

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: Optional[str]) -> None:
        self.__country_code = value

    @property
    def house_number(self) -> Optional[str]:
        """
        | House number

        Type: str
        """
        return self.__house_number

    @house_number.setter
    def house_number(self, value: Optional[str]) -> None:
        self.__house_number = value

    @property
    def street(self) -> Optional[str]:
        """
        | Streetname. Required for Create mandate and Create payment calls. Required for Create hostedCheckout calls where the IBAN is also provided.

        Type: str
        """
        return self.__street

    @street.setter
    def street(self, value: Optional[str]) -> None:
        self.__street = value

    @property
    def zip(self) -> Optional[str]:
        """
        | Zip code. Required for Create mandate and Create payment calls. Required for Create hostedCheckout calls where the IBAN is also provided.

        Type: str
        """
        return self.__zip

    @zip.setter
    def zip(self, value: Optional[str]) -> None:
        self.__zip = value

    def to_dictionary(self) -> dict:
        dictionary = super(MandateAddress, self).to_dictionary()
        if self.city is not None:
            dictionary['city'] = self.city
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.house_number is not None:
            dictionary['houseNumber'] = self.house_number
        if self.street is not None:
            dictionary['street'] = self.street
        if self.zip is not None:
            dictionary['zip'] = self.zip
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MandateAddress':
        super(MandateAddress, self).from_dictionary(dictionary)
        if 'city' in dictionary:
            self.city = dictionary['city']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'houseNumber' in dictionary:
            self.house_number = dictionary['houseNumber']
        if 'street' in dictionary:
            self.street = dictionary['street']
        if 'zip' in dictionary:
            self.zip = dictionary['zip']
        return self
