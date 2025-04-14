# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_of_money import AmountOfMoney
from .card_source import CardSource
from .data_object import DataObject


class CalculateSurchargeRequest(DataObject):

    __amount_of_money: Optional[AmountOfMoney] = None
    __card_source: Optional[CardSource] = None

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
    def card_source(self) -> Optional[CardSource]:
        """
        | Contains elements from which card number can be obtained.

        Type: :class:`onlinepayments.sdk.domain.card_source.CardSource`
        """
        return self.__card_source

    @card_source.setter
    def card_source(self, value: Optional[CardSource]) -> None:
        self.__card_source = value

    def to_dictionary(self) -> dict:
        dictionary = super(CalculateSurchargeRequest, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.card_source is not None:
            dictionary['cardSource'] = self.card_source.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CalculateSurchargeRequest':
        super(CalculateSurchargeRequest, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'cardSource' in dictionary:
            if not isinstance(dictionary['cardSource'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardSource']))
            value = CardSource()
            self.card_source = value.from_dictionary(dictionary['cardSource'])
        return self
