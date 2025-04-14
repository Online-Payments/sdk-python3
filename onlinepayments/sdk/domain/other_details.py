# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class OtherDetails(DataObject):

    __meta_data: Optional[str] = None
    __travel_data: Optional[str] = None

    @property
    def meta_data(self) -> Optional[str]:
        """
        | Information used by the following PaymentProducts [5300] to provide details on the item such as the color, size, etc. The field is in JSON format, with keys and values expected by the payment method at transaction creation. Please refer to the payment mean documentation.

        Type: str
        """
        return self.__meta_data

    @meta_data.setter
    def meta_data(self, value: Optional[str]) -> None:
        self.__meta_data = value

    @property
    def travel_data(self) -> Optional[str]:
        """
        | Information used by the following PaymentProducts [5110,5111,5112,5125,3104,3107,3108,3109].

        Type: str
        """
        return self.__travel_data

    @travel_data.setter
    def travel_data(self, value: Optional[str]) -> None:
        self.__travel_data = value

    def to_dictionary(self) -> dict:
        dictionary = super(OtherDetails, self).to_dictionary()
        if self.meta_data is not None:
            dictionary['metaData'] = self.meta_data
        if self.travel_data is not None:
            dictionary['travelData'] = self.travel_data
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OtherDetails':
        super(OtherDetails, self).from_dictionary(dictionary)
        if 'metaData' in dictionary:
            self.meta_data = dictionary['metaData']
        if 'travelData' in dictionary:
            self.travel_data = dictionary['travelData']
        return self
