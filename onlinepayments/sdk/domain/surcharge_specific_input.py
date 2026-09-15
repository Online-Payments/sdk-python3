# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_of_money import AmountOfMoney
from .data_object import DataObject


class SurchargeSpecificInput(DataObject):

    __mode: Optional[str] = None
    __surcharge_amount: Optional[AmountOfMoney] = None

    @property
    def mode(self) -> Optional[str]:
        """
        | The surcharge mode to be applied to an order.

        Type: str
        """
        return self.__mode

    @mode.setter
    def mode(self, value: Optional[str]) -> None:
        self.__mode = value

    @property
    def surcharge_amount(self) -> Optional[AmountOfMoney]:
        """
        | The surcharge amount of money to be applied to an order given that the merchant is in pass-through mode.

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__surcharge_amount

    @surcharge_amount.setter
    def surcharge_amount(self, value: Optional[AmountOfMoney]) -> None:
        self.__surcharge_amount = value

    def to_dictionary(self) -> dict:
        dictionary = super(SurchargeSpecificInput, self).to_dictionary()
        if self.mode is not None:
            dictionary['mode'] = self.mode
        if self.surcharge_amount is not None:
            dictionary['surchargeAmount'] = self.surcharge_amount.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SurchargeSpecificInput':
        super(SurchargeSpecificInput, self).from_dictionary(dictionary)
        if 'mode' in dictionary:
            self.mode = dictionary['mode']
        if 'surchargeAmount' in dictionary:
            if not isinstance(dictionary['surchargeAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeAmount']))
            value = AmountOfMoney()
            self.surcharge_amount = value.from_dictionary(dictionary['surchargeAmount'])
        return self
