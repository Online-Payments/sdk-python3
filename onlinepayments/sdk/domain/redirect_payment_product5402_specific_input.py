# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RedirectPaymentProduct5402SpecificInput(DataObject):

    __complete_remaining_payment_amount: Optional[bool] = None

    @property
    def complete_remaining_payment_amount(self) -> Optional[bool]:
        """
        | Determines how the remaining payment amount is handled if the initial payment is insufficient.
        
        * ``true``: The payment process will continue on our side, allowing the customer to pay the outstanding amount using a different payment method.
        * ``false``: Merchant must create and process a separate payment for the remaining amount independently.

        Type: bool
        """
        return self.__complete_remaining_payment_amount

    @complete_remaining_payment_amount.setter
    def complete_remaining_payment_amount(self, value: Optional[bool]) -> None:
        self.__complete_remaining_payment_amount = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct5402SpecificInput, self).to_dictionary()
        if self.complete_remaining_payment_amount is not None:
            dictionary['completeRemainingPaymentAmount'] = self.complete_remaining_payment_amount
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5402SpecificInput':
        super(RedirectPaymentProduct5402SpecificInput, self).from_dictionary(dictionary)
        if 'completeRemainingPaymentAmount' in dictionary:
            self.complete_remaining_payment_amount = dictionary['completeRemainingPaymentAmount']
        return self
