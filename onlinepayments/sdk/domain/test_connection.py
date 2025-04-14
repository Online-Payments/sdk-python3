# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class TestConnection(DataObject):

    __result: Optional[str] = None

    @property
    def result(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__result

    @result.setter
    def result(self, value: Optional[str]) -> None:
        self.__result = value

    def to_dictionary(self) -> dict:
        dictionary = super(TestConnection, self).to_dictionary()
        if self.result is not None:
            dictionary['result'] = self.result
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'TestConnection':
        super(TestConnection, self).from_dictionary(dictionary)
        if 'result' in dictionary:
            self.result = dictionary['result']
        return self
