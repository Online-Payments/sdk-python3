# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class ShowInstructionsData(DataObject):

    __show_data: Optional[str] = None

    @property
    def show_data(self) -> Optional[str]:
        """
        | The data that should be shown to the customer that can be used to render the instructions in your own application or website.

        Type: str
        """
        return self.__show_data

    @show_data.setter
    def show_data(self, value: Optional[str]) -> None:
        self.__show_data = value

    def to_dictionary(self) -> dict:
        dictionary = super(ShowInstructionsData, self).to_dictionary()
        if self.show_data is not None:
            dictionary['showData'] = self.show_data
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ShowInstructionsData':
        super(ShowInstructionsData, self).from_dictionary(dictionary)
        if 'showData' in dictionary:
            self.show_data = dictionary['showData']
        return self
