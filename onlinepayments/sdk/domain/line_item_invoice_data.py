# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class LineItemInvoiceData(DataObject):

    __description: Optional[str] = None

    @property
    def description(self) -> Optional[str]:
        """
        | Shopping cart item description

        Type: str
        """
        return self.__description

    @description.setter
    def description(self, value: Optional[str]) -> None:
        self.__description = value

    def to_dictionary(self) -> dict:
        dictionary = super(LineItemInvoiceData, self).to_dictionary()
        if self.description is not None:
            dictionary['description'] = self.description
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'LineItemInvoiceData':
        super(LineItemInvoiceData, self).from_dictionary(dictionary)
        if 'description' in dictionary:
            self.description = dictionary['description']
        return self
