# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .car_rental_data import CarRentalData
from .data_object import DataObject


class UpdateAuthorizationAdditionalDataRequest(DataObject):

    __car_rental_data: Optional[CarRentalData] = None

    @property
    def car_rental_data(self) -> Optional[CarRentalData]:
        """
        | Object that holds car rental specific data

        Type: :class:`onlinepayments.sdk.domain.car_rental_data.CarRentalData`
        """
        return self.__car_rental_data

    @car_rental_data.setter
    def car_rental_data(self, value: Optional[CarRentalData]) -> None:
        self.__car_rental_data = value

    def to_dictionary(self) -> dict:
        dictionary = super(UpdateAuthorizationAdditionalDataRequest, self).to_dictionary()
        if self.car_rental_data is not None:
            dictionary['carRentalData'] = self.car_rental_data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'UpdateAuthorizationAdditionalDataRequest':
        super(UpdateAuthorizationAdditionalDataRequest, self).from_dictionary(dictionary)
        if 'carRentalData' in dictionary:
            if not isinstance(dictionary['carRentalData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['carRentalData']))
            value = CarRentalData()
            self.car_rental_data = value.from_dictionary(dictionary['carRentalData'])
        return self
