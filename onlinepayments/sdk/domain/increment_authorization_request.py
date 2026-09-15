# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_of_money import AmountOfMoney
from .data_object import DataObject


class IncrementAuthorizationRequest(DataObject):

    __amount_of_money: Optional[AmountOfMoney] = None

    @property
    def amount_of_money(self) -> Optional[AmountOfMoney]:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: Optional[AmountOfMoney]) -> None:
        self.__amount_of_money = value

    def to_dictionary(self) -> dict:
        dictionary = super(IncrementAuthorizationRequest, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'IncrementAuthorizationRequest':
        super(IncrementAuthorizationRequest, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        return self
