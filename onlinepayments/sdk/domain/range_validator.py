# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RangeValidator(DataObject):

    __max_value: Optional[int] = None
    __min_value: Optional[int] = None

    @property
    def max_value(self) -> Optional[int]:
        """
        Type: int
        """
        return self.__max_value

    @max_value.setter
    def max_value(self, value: Optional[int]) -> None:
        self.__max_value = value

    @property
    def min_value(self) -> Optional[int]:
        """
        Type: int
        """
        return self.__min_value

    @min_value.setter
    def min_value(self, value: Optional[int]) -> None:
        self.__min_value = value

    def to_dictionary(self) -> dict:
        dictionary = super(RangeValidator, self).to_dictionary()
        if self.max_value is not None:
            dictionary['maxValue'] = self.max_value
        if self.min_value is not None:
            dictionary['minValue'] = self.min_value
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RangeValidator':
        super(RangeValidator, self).from_dictionary(dictionary)
        if 'maxValue' in dictionary:
            self.max_value = dictionary['maxValue']
        if 'minValue' in dictionary:
            self.min_value = dictionary['minValue']
        return self
