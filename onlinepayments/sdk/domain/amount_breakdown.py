# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class AmountBreakdown(DataObject):

    __amount: Optional[int] = None
    __type: Optional[str] = None

    @property
    def amount(self) -> Optional[int]:
        """
        | Amount in cents and always having 2 decimals

        Type: int
        """
        return self.__amount

    @amount.setter
    def amount(self, value: Optional[int]) -> None:
        self.__amount = value

    @property
    def type(self) -> Optional[str]:
        """
        | Type of the amount. Each type is only allowed to be provided once. Allowed values:
        
        * AIRPORT_TAX - The amount of tax paid for the airport, with the last 2 digits implied as decimal places.
        * CONSUMPTION_TAX - The amount of consumption tax paid by the customer, with the last 2 digits implied as decimal places.
        * DISCOUNT - Discount on the entire transaction, with the last 2 digits implied as decimal places.
        * DUTY - Duty on the entire transaction, with the last 2 digits implied as decimal places.
        * SHIPPING - Shipping cost on the entire transaction, with the last 2 digits implied as decimal places.
        * VAT - Total amount of VAT paid on the transaction, with the last 2 digits implied as decimal places.
        * BASE_AMOUNT - Order amount excluding all taxes, discount & shipping costs, with the last 2 digits implied as decimal places. Note: BASE_AMOUNT is only supported by the payment platform.

        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: Optional[str]) -> None:
        self.__type = value

    def to_dictionary(self) -> dict:
        dictionary = super(AmountBreakdown, self).to_dictionary()
        if self.amount is not None:
            dictionary['amount'] = self.amount
        if self.type is not None:
            dictionary['type'] = self.type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AmountBreakdown':
        super(AmountBreakdown, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            self.amount = dictionary['amount']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self
