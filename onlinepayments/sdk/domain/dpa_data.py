# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class DpaData(DataObject):

    __dpa_name: Optional[str] = None

    @property
    def dpa_name(self) -> Optional[str]:
        """
        | Legal name of registered DPA.

        Type: str
        """
        return self.__dpa_name

    @dpa_name.setter
    def dpa_name(self, value: Optional[str]) -> None:
        self.__dpa_name = value

    def to_dictionary(self) -> dict:
        dictionary = super(DpaData, self).to_dictionary()
        if self.dpa_name is not None:
            dictionary['dpaName'] = self.dpa_name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DpaData':
        super(DpaData, self).from_dictionary(dictionary)
        if 'dpaName' in dictionary:
            self.dpa_name = dictionary['dpaName']
        return self
