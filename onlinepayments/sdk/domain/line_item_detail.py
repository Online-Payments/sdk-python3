# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class LineItemDetail(DataObject):

    __line_item_id: Optional[str] = None
    __quantity: Optional[int] = None

    @property
    def line_item_id(self) -> Optional[str]:
        """
        | The unique ID for each line item.

        Type: str
        """
        return self.__line_item_id

    @line_item_id.setter
    def line_item_id(self, value: Optional[str]) -> None:
        self.__line_item_id = value

    @property
    def quantity(self) -> Optional[int]:
        """
        | Quantity of the units being purchased, should be greater than zero Note: Must not be all spaces or all zeros

        Type: int
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value: Optional[int]) -> None:
        self.__quantity = value

    def to_dictionary(self) -> dict:
        dictionary = super(LineItemDetail, self).to_dictionary()
        if self.line_item_id is not None:
            dictionary['lineItemId'] = self.line_item_id
        if self.quantity is not None:
            dictionary['quantity'] = self.quantity
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'LineItemDetail':
        super(LineItemDetail, self).from_dictionary(dictionary)
        if 'lineItemId' in dictionary:
            self.line_item_id = dictionary['lineItemId']
        if 'quantity' in dictionary:
            self.quantity = dictionary['quantity']
        return self
