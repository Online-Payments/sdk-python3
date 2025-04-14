# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class AirlinePassenger(DataObject):

    __airline_loyalty_status: Optional[str] = None
    __first_name: Optional[str] = None
    __passenger_type: Optional[str] = None
    __surname: Optional[str] = None
    __surname_prefix: Optional[str] = None
    __title: Optional[str] = None

    @property
    def airline_loyalty_status(self) -> Optional[str]:
        """
        | Airline loyalty program level for the passenger on the itinerary.

        Type: str
        """
        return self.__airline_loyalty_status

    @airline_loyalty_status.setter
    def airline_loyalty_status(self, value: Optional[str]) -> None:
        self.__airline_loyalty_status = value

    @property
    def first_name(self) -> Optional[str]:
        """
        | First name of the passenger This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value: Optional[str]) -> None:
        self.__first_name = value

    @property
    def passenger_type(self) -> Optional[str]:
        """
        | Type of passenger on the itinerary.

        Type: str
        """
        return self.__passenger_type

    @passenger_type.setter
    def passenger_type(self, value: Optional[str]) -> None:
        self.__passenger_type = value

    @property
    def surname(self) -> Optional[str]:
        """
        | Surname of the passenger This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__surname

    @surname.setter
    def surname(self, value: Optional[str]) -> None:
        self.__surname = value

    @property
    def surname_prefix(self) -> Optional[str]:
        """
        | Surname prefix or middle name of the passenger This field is used by the following payment products: 840

        Type: str
        """
        return self.__surname_prefix

    @surname_prefix.setter
    def surname_prefix(self, value: Optional[str]) -> None:
        self.__surname_prefix = value

    @property
    def title(self) -> Optional[str]:
        """
        | Deprecated: This field is not used by any payment product Title of the passenger (this property is used for fraud screening on the payment platform)

        Type: str

        Deprecated; This field is not used by any payment product Title of the passenger (this property is used for fraud screening on the payment platform)
        """
        return self.__title

    @title.setter
    def title(self, value: Optional[str]) -> None:
        self.__title = value

    def to_dictionary(self) -> dict:
        dictionary = super(AirlinePassenger, self).to_dictionary()
        if self.airline_loyalty_status is not None:
            dictionary['airlineLoyaltyStatus'] = self.airline_loyalty_status
        if self.first_name is not None:
            dictionary['firstName'] = self.first_name
        if self.passenger_type is not None:
            dictionary['passengerType'] = self.passenger_type
        if self.surname is not None:
            dictionary['surname'] = self.surname
        if self.surname_prefix is not None:
            dictionary['surnamePrefix'] = self.surname_prefix
        if self.title is not None:
            dictionary['title'] = self.title
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AirlinePassenger':
        super(AirlinePassenger, self).from_dictionary(dictionary)
        if 'airlineLoyaltyStatus' in dictionary:
            self.airline_loyalty_status = dictionary['airlineLoyaltyStatus']
        if 'firstName' in dictionary:
            self.first_name = dictionary['firstName']
        if 'passengerType' in dictionary:
            self.passenger_type = dictionary['passengerType']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        if 'surnamePrefix' in dictionary:
            self.surname_prefix = dictionary['surnamePrefix']
        if 'title' in dictionary:
            self.title = dictionary['title']
        return self
