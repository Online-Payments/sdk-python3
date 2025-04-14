# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class LodgingData(DataObject):

    __check_in_date: Optional[str] = None

    @property
    def check_in_date(self) -> Optional[str]:
        """
        | The date the guest checks into (or plans to check in to) the facility. Format YYYYMMDD

        Type: str
        """
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value: Optional[str]) -> None:
        self.__check_in_date = value

    def to_dictionary(self) -> dict:
        dictionary = super(LodgingData, self).to_dictionary()
        if self.check_in_date is not None:
            dictionary['checkInDate'] = self.check_in_date
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'LodgingData':
        super(LodgingData, self).from_dictionary(dictionary)
        if 'checkInDate' in dictionary:
            self.check_in_date = dictionary['checkInDate']
        return self
