# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PaymentProduct3208SpecificInput(DataObject):
    """
    | Object containing specific input required for OneyDuplo Leroy Merlin payments.
    """

    __merchant_finance_code = None

    @property
    def merchant_finance_code(self) -> str:
        """
        | This field indicates the finance code provided by the merchant after the buyer has selected the proper financing option.

        Type: str
        """
        return self.__merchant_finance_code

    @merchant_finance_code.setter
    def merchant_finance_code(self, value: str):
        self.__merchant_finance_code = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct3208SpecificInput, self).to_dictionary()
        if self.merchant_finance_code is not None:
            dictionary['merchantFinanceCode'] = self.merchant_finance_code
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct3208SpecificInput, self).from_dictionary(dictionary)
        if 'merchantFinanceCode' in dictionary:
            self.merchant_finance_code = dictionary['merchantFinanceCode']
        return self
