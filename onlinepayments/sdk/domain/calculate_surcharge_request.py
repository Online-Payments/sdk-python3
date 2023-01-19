# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.card_source import CardSource


class CalculateSurchargeRequest(DataObject):
    __amount_of_money = None
    __card_source = None

    @property
    def amount_of_money(self) -> AmountOfMoney:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: AmountOfMoney):
        self.__amount_of_money = value

    @property
    def card_source(self) -> CardSource:
        """
        | Contains elements from which card number can be obtained.

        Type: :class:`onlinepayments.sdk.domain.card_source.CardSource`
        """
        return self.__card_source

    @card_source.setter
    def card_source(self, value: CardSource):
        self.__card_source = value

    def to_dictionary(self):
        dictionary = super(CalculateSurchargeRequest, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.card_source is not None:
            dictionary['cardSource'] = self.card_source.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
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
