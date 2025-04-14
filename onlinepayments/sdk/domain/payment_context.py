# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_of_money import AmountOfMoney
from .data_object import DataObject


class PaymentContext(DataObject):

    __amount_of_money: Optional[AmountOfMoney] = None
    __country_code: Optional[str] = None
    __is_recurring: Optional[bool] = None

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
    def country_code(self) -> Optional[str]:
        """
        | The country the payment takes place in

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: Optional[str]) -> None:
        self.__country_code = value

    @property
    def is_recurring(self) -> Optional[bool]:
        """
        | True if the payment is recurring

        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value: Optional[bool]) -> None:
        self.__is_recurring = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentContext, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.is_recurring is not None:
            dictionary['isRecurring'] = self.is_recurring
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentContext':
        super(PaymentContext, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        return self
