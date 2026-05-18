# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RedirectPaymentProduct5301SpecificInput(DataObject):

    __payment_method_type: Optional[str] = None

    @property
    def payment_method_type(self) -> Optional[str]:
        """
        * invoice - The transaction is an invoice payment, transaction amount should be greater than €10 and less than €1500. * direct_debit - The transaction is a direct debit payment, transaction amount should be greater than €10 and less than €1500.

        Type: str
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value: Optional[str]) -> None:
        self.__payment_method_type = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct5301SpecificInput, self).to_dictionary()
        if self.payment_method_type is not None:
            dictionary['paymentMethodType'] = self.payment_method_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5301SpecificInput':
        super(RedirectPaymentProduct5301SpecificInput, self).from_dictionary(dictionary)
        if 'paymentMethodType' in dictionary:
            self.payment_method_type = dictionary['paymentMethodType']
        return self
