# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CarRentalVehicleData(DataObject):

    __class_id: Optional[str] = None
    __identification_number: Optional[str] = None

    @property
    def class_id(self) -> Optional[str]:
        """
        | This field contains a code that corresponds to the classification of the rental vehicle.

        Type: str
        """
        return self.__class_id

    @class_id.setter
    def class_id(self, value: Optional[str]) -> None:
        self.__class_id = value

    @property
    def identification_number(self) -> Optional[str]:
        """
        | This field contains a unique identifier assigned by the taxi company to the vehicle.

        Type: str
        """
        return self.__identification_number

    @identification_number.setter
    def identification_number(self, value: Optional[str]) -> None:
        self.__identification_number = value

    def to_dictionary(self) -> dict:
        dictionary = super(CarRentalVehicleData, self).to_dictionary()
        if self.class_id is not None:
            dictionary['classId'] = self.class_id
        if self.identification_number is not None:
            dictionary['identificationNumber'] = self.identification_number
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CarRentalVehicleData':
        super(CarRentalVehicleData, self).from_dictionary(dictionary)
        if 'classId' in dictionary:
            self.class_id = dictionary['classId']
        if 'identificationNumber' in dictionary:
            self.identification_number = dictionary['identificationNumber']
        return self
