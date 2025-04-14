# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CardInfo(DataObject):

    __card_number: Optional[str] = None
    __payment_product_id: Optional[int] = None

    @property
    def card_number(self) -> Optional[str]:
        """
        | The complete credit/debit card number (also know as the PAN) The card number is always obfuscated in any of our responses

        Type: str
        """
        return self.__card_number

    @card_number.setter
    def card_number(self, value: Optional[str]) -> None:
        self.__card_number = value

    @property
    def payment_product_id(self) -> Optional[int]:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: Optional[int]) -> None:
        self.__payment_product_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(CardInfo, self).to_dictionary()
        if self.card_number is not None:
            dictionary['cardNumber'] = self.card_number
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardInfo':
        super(CardInfo, self).from_dictionary(dictionary)
        if 'cardNumber' in dictionary:
            self.card_number = dictionary['cardNumber']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
