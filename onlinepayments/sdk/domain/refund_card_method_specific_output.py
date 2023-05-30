# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.currency_conversion import CurrencyConversion


class RefundCardMethodSpecificOutput(DataObject):
    __currency_conversion = None
    __total_amount_paid = None
    __total_amount_refunded = None

    @property
    def currency_conversion(self) -> CurrencyConversion:
        """
        Type: :class:`onlinepayments.sdk.domain.currency_conversion.CurrencyConversion`
        """
        return self.__currency_conversion

    @currency_conversion.setter
    def currency_conversion(self, value: CurrencyConversion):
        self.__currency_conversion = value

    @property
    def total_amount_paid(self) -> int:
        """
        Type: int
        """
        return self.__total_amount_paid

    @total_amount_paid.setter
    def total_amount_paid(self, value: int):
        self.__total_amount_paid = value

    @property
    def total_amount_refunded(self) -> int:
        """
        Type: int
        """
        return self.__total_amount_refunded

    @total_amount_refunded.setter
    def total_amount_refunded(self, value: int):
        self.__total_amount_refunded = value

    def to_dictionary(self):
        dictionary = super(RefundCardMethodSpecificOutput, self).to_dictionary()
        if self.currency_conversion is not None:
            dictionary['currencyConversion'] = self.currency_conversion.to_dictionary()
        if self.total_amount_paid is not None:
            dictionary['totalAmountPaid'] = self.total_amount_paid
        if self.total_amount_refunded is not None:
            dictionary['totalAmountRefunded'] = self.total_amount_refunded
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundCardMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'currencyConversion' in dictionary:
            if not isinstance(dictionary['currencyConversion'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['currencyConversion']))
            value = CurrencyConversion()
            self.currency_conversion = value.from_dictionary(dictionary['currencyConversion'])
        if 'totalAmountPaid' in dictionary:
            self.total_amount_paid = dictionary['totalAmountPaid']
        if 'totalAmountRefunded' in dictionary:
            self.total_amount_refunded = dictionary['totalAmountRefunded']
        return self
