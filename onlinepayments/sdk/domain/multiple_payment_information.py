# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class MultiplePaymentInformation(DataObject):

    __payment_pattern: Optional[str] = None
    __total_number_of_payments: Optional[int] = None

    @property
    def payment_pattern(self) -> Optional[str]:
        """
        | Typology of multiple payment. Allowed values:
        
        * PartialShipment

        Type: str
        """
        return self.__payment_pattern

    @payment_pattern.setter
    def payment_pattern(self, value: Optional[str]) -> None:
        self.__payment_pattern = value

    @property
    def total_number_of_payments(self) -> Optional[int]:
        """
        | Total number of payments. If a payment is implied by this call, it implicitly has ordinal number 1.

        Type: int
        """
        return self.__total_number_of_payments

    @total_number_of_payments.setter
    def total_number_of_payments(self, value: Optional[int]) -> None:
        self.__total_number_of_payments = value

    def to_dictionary(self) -> dict:
        dictionary = super(MultiplePaymentInformation, self).to_dictionary()
        if self.payment_pattern is not None:
            dictionary['paymentPattern'] = self.payment_pattern
        if self.total_number_of_payments is not None:
            dictionary['totalNumberOfPayments'] = self.total_number_of_payments
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MultiplePaymentInformation':
        super(MultiplePaymentInformation, self).from_dictionary(dictionary)
        if 'paymentPattern' in dictionary:
            self.payment_pattern = dictionary['paymentPattern']
        if 'totalNumberOfPayments' in dictionary:
            self.total_number_of_payments = dictionary['totalNumberOfPayments']
        return self
