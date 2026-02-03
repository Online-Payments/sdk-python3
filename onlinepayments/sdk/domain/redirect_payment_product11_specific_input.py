# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from datetime import date
from typing import Optional

from .data_object import DataObject


class RedirectPaymentProduct11SpecificInput(DataObject):

    __first_installment_payment_date: Optional[date] = None

    @property
    def first_installment_payment_date(self) -> Optional[date]:
        """
        | The first installment date must be given in the YYYYMMDD format.

        Type: date
        """
        return self.__first_installment_payment_date

    @first_installment_payment_date.setter
    def first_installment_payment_date(self, value: Optional[date]) -> None:
        self.__first_installment_payment_date = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct11SpecificInput, self).to_dictionary()
        if self.first_installment_payment_date is not None:
            dictionary['firstInstallmentPaymentDate'] = DataObject.format_date(self.first_installment_payment_date)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct11SpecificInput':
        super(RedirectPaymentProduct11SpecificInput, self).from_dictionary(dictionary)
        if 'firstInstallmentPaymentDate' in dictionary:
            self.first_installment_payment_date = DataObject.parse_date(dictionary['firstInstallmentPaymentDate'])
        return self
