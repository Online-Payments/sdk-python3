# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CarRentalPickupReturnData(DataObject):

    __address: Optional[str] = None
    __city: Optional[str] = None
    __country: Optional[int] = None
    __date: Optional[str] = None
    __location: Optional[str] = None
    __postcode: Optional[str] = None
    __state: Optional[str] = None

    @property
    def address(self) -> Optional[str]:
        """
        | Address of the pickup/return location

        Type: str
        """
        return self.__address

    @address.setter
    def address(self, value: Optional[str]) -> None:
        self.__address = value

    @property
    def city(self) -> Optional[str]:
        """
        | City of the pickup/return location

        Type: str
        """
        return self.__city

    @city.setter
    def city(self, value: Optional[str]) -> None:
        self.__city = value

    @property
    def country(self) -> Optional[int]:
        """
        | Country of the pickup/return location ISO 3166-1 numeric

        Type: int
        """
        return self.__country

    @country.setter
    def country(self, value: Optional[int]) -> None:
        self.__country = value

    @property
    def date(self) -> Optional[str]:
        """
        | UTC Time at which the vehicle was rented/picked up or returned.

        Type: str
        """
        return self.__date

    @date.setter
    def date(self, value: Optional[str]) -> None:
        self.__date = value

    @property
    def location(self) -> Optional[str]:
        """
        | This field contains data that uniquely identifies the location where the car was picked up or returned (e.g., DBA name, hotel, airport, etc.).

        Type: str
        """
        return self.__location

    @location.setter
    def location(self, value: Optional[str]) -> None:
        self.__location = value

    @property
    def postcode(self) -> Optional[str]:
        """
        | Postal code of the pickup/return location

        Type: str
        """
        return self.__postcode

    @postcode.setter
    def postcode(self, value: Optional[str]) -> None:
        self.__postcode = value

    @property
    def state(self) -> Optional[str]:
        """
        | State/region of the pickup/return location

        Type: str
        """
        return self.__state

    @state.setter
    def state(self, value: Optional[str]) -> None:
        self.__state = value

    def to_dictionary(self) -> dict:
        dictionary = super(CarRentalPickupReturnData, self).to_dictionary()
        if self.address is not None:
            dictionary['address'] = self.address
        if self.city is not None:
            dictionary['city'] = self.city
        if self.country is not None:
            dictionary['country'] = self.country
        if self.date is not None:
            dictionary['date'] = self.date
        if self.location is not None:
            dictionary['location'] = self.location
        if self.postcode is not None:
            dictionary['postcode'] = self.postcode
        if self.state is not None:
            dictionary['state'] = self.state
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CarRentalPickupReturnData':
        super(CarRentalPickupReturnData, self).from_dictionary(dictionary)
        if 'address' in dictionary:
            self.address = dictionary['address']
        if 'city' in dictionary:
            self.city = dictionary['city']
        if 'country' in dictionary:
            self.country = dictionary['country']
        if 'date' in dictionary:
            self.date = dictionary['date']
        if 'location' in dictionary:
            self.location = dictionary['location']
        if 'postcode' in dictionary:
            self.postcode = dictionary['postcode']
        if 'state' in dictionary:
            self.state = dictionary['state']
        return self
