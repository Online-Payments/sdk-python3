# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class OperationPaymentReferences(DataObject):

    __merchant_reference: Optional[str] = None

    @property
    def merchant_reference(self) -> Optional[str]:
        """
        | Your unique reference of the transaction that is also returned in our report files. This is almost always used for your reconciliation of our report files. It is highly recommended to provide a single MerchantReference per unique order on your side

        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value: Optional[str]) -> None:
        self.__merchant_reference = value

    def to_dictionary(self) -> dict:
        dictionary = super(OperationPaymentReferences, self).to_dictionary()
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OperationPaymentReferences':
        super(OperationPaymentReferences, self).from_dictionary(dictionary)
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        return self
