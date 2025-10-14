# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RedirectPaymentProduct5412SpecificInput(DataObject):

    __adjustable_amount: Optional[bool] = None

    @property
    def adjustable_amount(self) -> Optional[bool]:
        """
        | If true, the customer can adjust the portion of the total amount paid using this payment method in the ANCV app at authentication time.

        Type: bool
        """
        return self.__adjustable_amount

    @adjustable_amount.setter
    def adjustable_amount(self, value: Optional[bool]) -> None:
        self.__adjustable_amount = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct5412SpecificInput, self).to_dictionary()
        if self.adjustable_amount is not None:
            dictionary['adjustableAmount'] = self.adjustable_amount
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5412SpecificInput':
        super(RedirectPaymentProduct5412SpecificInput, self).from_dictionary(dictionary)
        if 'adjustableAmount' in dictionary:
            self.adjustable_amount = dictionary['adjustableAmount']
        return self
