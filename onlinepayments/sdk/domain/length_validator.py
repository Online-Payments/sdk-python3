# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class LengthValidator(DataObject):

    __max_length: Optional[int] = None
    __min_length: Optional[int] = None

    @property
    def max_length(self) -> Optional[int]:
        """
        Type: int
        """
        return self.__max_length

    @max_length.setter
    def max_length(self, value: Optional[int]) -> None:
        self.__max_length = value

    @property
    def min_length(self) -> Optional[int]:
        """
        Type: int
        """
        return self.__min_length

    @min_length.setter
    def min_length(self, value: Optional[int]) -> None:
        self.__min_length = value

    def to_dictionary(self) -> dict:
        dictionary = super(LengthValidator, self).to_dictionary()
        if self.max_length is not None:
            dictionary['maxLength'] = self.max_length
        if self.min_length is not None:
            dictionary['minLength'] = self.min_length
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'LengthValidator':
        super(LengthValidator, self).from_dictionary(dictionary)
        if 'maxLength' in dictionary:
            self.max_length = dictionary['maxLength']
        if 'minLength' in dictionary:
            self.min_length = dictionary['minLength']
        return self
