# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from datetime import date
from typing import Optional

from .data_object import DataObject


class RedirectPaymentProduct5410SpecificInput(DataObject):

    __second_installment_payment_date: Optional[date] = None

    @property
    def second_installment_payment_date(self) -> Optional[date]:
        """
        | The date of the second installment (YYYYMMDD)

        Type: date
        """
        return self.__second_installment_payment_date

    @second_installment_payment_date.setter
    def second_installment_payment_date(self, value: Optional[date]) -> None:
        self.__second_installment_payment_date = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct5410SpecificInput, self).to_dictionary()
        if self.second_installment_payment_date is not None:
            dictionary['secondInstallmentPaymentDate'] = DataObject.format_date(self.second_installment_payment_date)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5410SpecificInput':
        super(RedirectPaymentProduct5410SpecificInput, self).from_dictionary(dictionary)
        if 'secondInstallmentPaymentDate' in dictionary:
            self.second_installment_payment_date = DataObject.parse_date(dictionary['secondInstallmentPaymentDate'])
        return self
