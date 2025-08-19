# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class Product320Recurring(DataObject):

    __recurring_payment_sequence_indicator: Optional[str] = None

    @property
    def recurring_payment_sequence_indicator(self) -> Optional[str]:
        """
        * first = This transaction is the first of a series of recurring transactions

        Type: str
        """
        return self.__recurring_payment_sequence_indicator

    @recurring_payment_sequence_indicator.setter
    def recurring_payment_sequence_indicator(self, value: Optional[str]) -> None:
        self.__recurring_payment_sequence_indicator = value

    def to_dictionary(self) -> dict:
        dictionary = super(Product320Recurring, self).to_dictionary()
        if self.recurring_payment_sequence_indicator is not None:
            dictionary['recurringPaymentSequenceIndicator'] = self.recurring_payment_sequence_indicator
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Product320Recurring':
        super(Product320Recurring, self).from_dictionary(dictionary)
        if 'recurringPaymentSequenceIndicator' in dictionary:
            self.recurring_payment_sequence_indicator = dictionary['recurringPaymentSequenceIndicator']
        return self
