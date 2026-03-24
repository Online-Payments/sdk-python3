# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class LineItemDetail(DataObject):

    __discount_amount: Optional[int] = None
    __line_item_id: Optional[str] = None
    __quantity: Optional[int] = None
    __tax_amount: Optional[int] = None

    @property
    def discount_amount(self) -> Optional[int]:
        """
        | Amount in the smallest currency unit, i.e.:
        
        * EUR is a 2-decimals currency, the value 1234 will result in EUR 12.34
        * KWD is a 3-decimals currency, the value 1234 will result in KWD 1.234
        * JPY is a zero-decimal currency, the value 1234 will result in JPY 1234

        Type: int
        """
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, value: Optional[int]) -> None:
        self.__discount_amount = value

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

    @property
    def tax_amount(self) -> Optional[int]:
        """
        | Amount in the smallest currency unit, i.e.:
        
        * EUR is a 2-decimals currency, the value 1234 will result in EUR 12.34
        * KWD is a 3-decimals currency, the value 1234 will result in KWD 1.234
        * JPY is a zero-decimal currency, the value 1234 will result in JPY 1234

        Type: int
        """
        return self.__tax_amount

    @tax_amount.setter
    def tax_amount(self, value: Optional[int]) -> None:
        self.__tax_amount = value

    def to_dictionary(self) -> dict:
        dictionary = super(LineItemDetail, self).to_dictionary()
        if self.discount_amount is not None:
            dictionary['discountAmount'] = self.discount_amount
        if self.line_item_id is not None:
            dictionary['lineItemId'] = self.line_item_id
        if self.quantity is not None:
            dictionary['quantity'] = self.quantity
        if self.tax_amount is not None:
            dictionary['taxAmount'] = self.tax_amount
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'LineItemDetail':
        super(LineItemDetail, self).from_dictionary(dictionary)
        if 'discountAmount' in dictionary:
            self.discount_amount = dictionary['discountAmount']
        if 'lineItemId' in dictionary:
            self.line_item_id = dictionary['lineItemId']
        if 'quantity' in dictionary:
            self.quantity = dictionary['quantity']
        if 'taxAmount' in dictionary:
            self.tax_amount = dictionary['taxAmount']
        return self
