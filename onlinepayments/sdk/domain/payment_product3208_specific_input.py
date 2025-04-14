# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct3208SpecificInput(DataObject):

    __merchant_finance_code: Optional[str] = None

    @property
    def merchant_finance_code(self) -> Optional[str]:
        """
        | This field indicates the finance code provided by the merchant after the buyer has selected the proper financing option.

        Type: str
        """
        return self.__merchant_finance_code

    @merchant_finance_code.setter
    def merchant_finance_code(self, value: Optional[str]) -> None:
        self.__merchant_finance_code = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct3208SpecificInput, self).to_dictionary()
        if self.merchant_finance_code is not None:
            dictionary['merchantFinanceCode'] = self.merchant_finance_code
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct3208SpecificInput':
        super(PaymentProduct3208SpecificInput, self).from_dictionary(dictionary)
        if 'merchantFinanceCode' in dictionary:
            self.merchant_finance_code = dictionary['merchantFinanceCode']
        return self
