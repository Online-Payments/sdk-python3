# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct3013SpecificInput(DataObject):

    __market_number: Optional[str] = None
    __purchasing_buyer_reference1: Optional[str] = None
    __purchasing_buyer_reference2: Optional[str] = None

    @property
    def market_number(self) -> Optional[str]:
        """
        | An identifier that refers to the public tender

        Type: str
        """
        return self.__market_number

    @market_number.setter
    def market_number(self, value: Optional[str]) -> None:
        self.__market_number = value

    @property
    def purchasing_buyer_reference1(self) -> Optional[str]:
        """
        | An identifier allocated by the government

        Type: str
        """
        return self.__purchasing_buyer_reference1

    @purchasing_buyer_reference1.setter
    def purchasing_buyer_reference1(self, value: Optional[str]) -> None:
        self.__purchasing_buyer_reference1 = value

    @property
    def purchasing_buyer_reference2(self) -> Optional[str]:
        """
        | An identifier allocated by the government

        Type: str
        """
        return self.__purchasing_buyer_reference2

    @purchasing_buyer_reference2.setter
    def purchasing_buyer_reference2(self, value: Optional[str]) -> None:
        self.__purchasing_buyer_reference2 = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct3013SpecificInput, self).to_dictionary()
        if self.market_number is not None:
            dictionary['marketNumber'] = self.market_number
        if self.purchasing_buyer_reference1 is not None:
            dictionary['purchasingBuyerReference1'] = self.purchasing_buyer_reference1
        if self.purchasing_buyer_reference2 is not None:
            dictionary['purchasingBuyerReference2'] = self.purchasing_buyer_reference2
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct3013SpecificInput':
        super(PaymentProduct3013SpecificInput, self).from_dictionary(dictionary)
        if 'marketNumber' in dictionary:
            self.market_number = dictionary['marketNumber']
        if 'purchasingBuyerReference1' in dictionary:
            self.purchasing_buyer_reference1 = dictionary['purchasingBuyerReference1']
        if 'purchasingBuyerReference2' in dictionary:
            self.purchasing_buyer_reference2 = dictionary['purchasingBuyerReference2']
        return self
