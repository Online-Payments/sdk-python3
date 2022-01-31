# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class Address(DataObject):
    """
    | Object containing billing address details
    """

    __additional_info = None
    __city = None
    __country_code = None
    __house_number = None
    __state = None
    __street = None
    __zip = None

    @property
    def additional_info(self) -> str:
        """
        | Second line of street or additional address information

        Type: str
        """
        return self.__additional_info

    @additional_info.setter
    def additional_info(self, value: str):
        self.__additional_info = value

    @property
    def city(self) -> str:
        """
        | City

        Type: str
        """
        return self.__city

    @city.setter
    def city(self, value: str):
        self.__city = value

    @property
    def country_code(self) -> str:
        """
        | ISO 3166-1 alpha-2 country code

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: str):
        self.__country_code = value

    @property
    def house_number(self) -> str:
        """
        | House number

        Type: str
        """
        return self.__house_number

    @house_number.setter
    def house_number(self, value: str):
        self.__house_number = value

    @property
    def state(self) -> str:
        """
        | Full name of the state or province

        Type: str
        """
        return self.__state

    @state.setter
    def state(self, value: str):
        self.__state = value

    @property
    def street(self) -> str:
        """
        | Street name

        Type: str
        """
        return self.__street

    @street.setter
    def street(self, value: str):
        self.__street = value

    @property
    def zip(self) -> str:
        """
        | Zip code

        Type: str
        """
        return self.__zip

    @zip.setter
    def zip(self, value: str):
        self.__zip = value

    def to_dictionary(self):
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

    def from_dictionary(self, dictionary):
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
