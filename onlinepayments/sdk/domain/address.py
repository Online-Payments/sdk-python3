# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class Address(DataObject):

    __additional_info: Optional[str] = None
    __city: Optional[str] = None
    __country_code: Optional[str] = None
    __house_number: Optional[str] = None
    __state: Optional[str] = None
    __street: Optional[str] = None
    __zip: Optional[str] = None

    @property
    def additional_info(self) -> Optional[str]:
        """
        | Second line of street or additional address information

        Type: str
        """
        return self.__additional_info

    @additional_info.setter
    def additional_info(self, value: Optional[str]) -> None:
        self.__additional_info = value

    @property
    def city(self) -> Optional[str]:
        """
        | City

        Type: str
        """
        return self.__city

    @city.setter
    def city(self, value: Optional[str]) -> None:
        self.__city = value

    @property
    def country_code(self) -> Optional[str]:
        """
        | ISO 3166-1 alpha-2 country code

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
    def state(self) -> Optional[str]:
        """
        | ISO 3166-2 country subdivision code

        Type: str
        """
        return self.__state

    @state.setter
    def state(self, value: Optional[str]) -> None:
        self.__state = value

    @property
    def street(self) -> Optional[str]:
        """
        | Street name

        Type: str
        """
        return self.__street

    @street.setter
    def street(self, value: Optional[str]) -> None:
        self.__street = value

    @property
    def zip(self) -> Optional[str]:
        """
        | Zip code

        Type: str
        """
        return self.__zip

    @zip.setter
    def zip(self, value: Optional[str]) -> None:
        self.__zip = value

    def to_dictionary(self) -> dict:
        dictionary = super(Address, self).to_dictionary()
        if self.additional_info is not None:
            dictionary['additionalInfo'] = self.additional_info
        if self.city is not None:
            dictionary['city'] = self.city
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.house_number is not None:
            dictionary['houseNumber'] = self.house_number
        if self.state is not None:
            dictionary['state'] = self.state
        if self.street is not None:
            dictionary['street'] = self.street
        if self.zip is not None:
            dictionary['zip'] = self.zip
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Address':
        super(Address, self).from_dictionary(dictionary)
        if 'additionalInfo' in dictionary:
            self.additional_info = dictionary['additionalInfo']
        if 'city' in dictionary:
            self.city = dictionary['city']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'houseNumber' in dictionary:
            self.house_number = dictionary['houseNumber']
        if 'state' in dictionary:
            self.state = dictionary['state']
        if 'street' in dictionary:
            self.street = dictionary['street']
        if 'zip' in dictionary:
            self.zip = dictionary['zip']
        return self
