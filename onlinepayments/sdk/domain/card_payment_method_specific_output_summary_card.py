# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CardPaymentMethodSpecificOutputSummaryCard(DataObject):

    __card_number: Optional[str] = None

    @property
    def card_number(self) -> Optional[str]:
        """
        | The masked credit/debit card number

        Type: str
        """
        return self.__card_number

    @card_number.setter
    def card_number(self, value: Optional[str]) -> None:
        self.__card_number = value

    def to_dictionary(self) -> dict:
        dictionary = super(CardPaymentMethodSpecificOutputSummaryCard, self).to_dictionary()
        if self.card_number is not None:
            dictionary['cardNumber'] = self.card_number
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardPaymentMethodSpecificOutputSummaryCard':
        super(CardPaymentMethodSpecificOutputSummaryCard, self).from_dictionary(dictionary)
        if 'cardNumber' in dictionary:
            self.card_number = dictionary['cardNumber']
        return self
