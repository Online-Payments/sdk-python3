# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class ShippingMethod(DataObject):
    """
    | Object containing information regarding shipping method
    """

    __details = None
    __name = None
    __speed = None
    __type = None

    @property
    def details(self) -> str:
        """
        | Details about the shipping method

        Type: str
        """
        return self.__details

    @details.setter
    def details(self, value: str):
        self.__details = value

    @property
    def name(self) -> str:
        """
        | Name of the shipping method

        Type: str
        """
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def speed(self) -> int:
        """
        | Number of hours to delivery

        Type: int
        """
        return self.__speed

    @speed.setter
    def speed(self, value: int):
        self.__speed = value

    @property
    def type(self) -> str:
        """
        | Shipping method type

        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: str):
        self.__type = value

    def to_dictionary(self):
        dictionary = super(ShippingMethod, self).to_dictionary()
        if self.details is not None:
            dictionary['details'] = self.details
        if self.name is not None:
            dictionary['name'] = self.name
        if self.speed is not None:
            dictionary['speed'] = self.speed
        if self.type is not None:
            dictionary['type'] = self.type
        return dictionary

    def from_dictionary(self, dictionary):
        super(ShippingMethod, self).from_dictionary(dictionary)
        if 'details' in dictionary:
            self.details = dictionary['details']
        if 'name' in dictionary:
            self.name = dictionary['name']
        if 'speed' in dictionary:
            self.speed = dictionary['speed']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self
