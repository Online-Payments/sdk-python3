# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_of_money import AmountOfMoney
from .data_object import DataObject


class CancelPaymentRequest(DataObject):

    __amount_of_money: Optional[AmountOfMoney] = None
    __is_final: Optional[bool] = None

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

    @property
    def is_final(self) -> Optional[bool]:
        """
        | This property indicates whether this will be the final operation. The default value for this property is false.

        Type: bool
        """
        return self.__is_final

    @is_final.setter
    def is_final(self, value: Optional[bool]) -> None:
        self.__is_final = value

    def to_dictionary(self) -> dict:
        dictionary = super(CancelPaymentRequest, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.is_final is not None:
            dictionary['isFinal'] = self.is_final
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CancelPaymentRequest':
        super(CancelPaymentRequest, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'isFinal' in dictionary:
            self.is_final = dictionary['isFinal']
        return self
