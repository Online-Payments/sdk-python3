# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject
from .line_item_detail import LineItemDetail


class ShoppingCartOutput(DataObject):

    __line_item_details: Optional[List[LineItemDetail]] = None

    @property
    def line_item_details(self) -> Optional[List[LineItemDetail]]:
        """
        | List of lineItemIds and quantities for capture/refund/cancellation.

        Type: list[:class:`onlinepayments.sdk.domain.line_item_detail.LineItemDetail`]
        """
        return self.__line_item_details

    @line_item_details.setter
    def line_item_details(self, value: Optional[List[LineItemDetail]]) -> None:
        self.__line_item_details = value

    def to_dictionary(self) -> dict:
        dictionary = super(ShoppingCartOutput, self).to_dictionary()
        if self.line_item_details is not None:
            dictionary['lineItemDetails'] = []
            for element in self.line_item_details:
                if element is not None:
                    dictionary['lineItemDetails'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ShoppingCartOutput':
        super(ShoppingCartOutput, self).from_dictionary(dictionary)
        if 'lineItemDetails' in dictionary:
            if not isinstance(dictionary['lineItemDetails'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['lineItemDetails']))
            self.line_item_details = []
            for element in dictionary['lineItemDetails']:
                value = LineItemDetail()
                self.line_item_details.append(value.from_dictionary(element))
        return self
