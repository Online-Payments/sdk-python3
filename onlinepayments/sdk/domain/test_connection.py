# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class TestConnection(DataObject):
    __result = None

    @property
    def result(self) -> str:
        """
        Type: str
        """
        return self.__result

    @result.setter
    def result(self, value: str):
        self.__result = value

    def to_dictionary(self):
        dictionary = super(TestConnection, self).to_dictionary()
        if self.result is not None:
            dictionary['result'] = self.result
        return dictionary

    def from_dictionary(self, dictionary):
        super(TestConnection, self).from_dictionary(dictionary)
        if 'result' in dictionary:
            self.result = dictionary['result']
        return self
