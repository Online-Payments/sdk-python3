# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class CurrencyConversionSpecificInput(DataObject):
    """
    | Object containing specific input required for Dynamic Currency Conversion.
    """

    __dcc_enabled = None

    @property
    def dcc_enabled(self) -> bool:
        """
        | Indicates if this transaction is Dynamic Currency Conversion (DCC) enabled.
        | * true - Dynamic Currency Conversion (DCC) is enabled in this transaction.
        | * false - Dynamic Currency Conversion (DCC) is disabled in this transaction. The default value for this property is false.

        Type: bool
        """
        return self.__dcc_enabled

    @dcc_enabled.setter
    def dcc_enabled(self, value: bool):
        self.__dcc_enabled = value

    def to_dictionary(self):
        dictionary = super(CurrencyConversionSpecificInput, self).to_dictionary()
        if self.dcc_enabled is not None:
            dictionary['dccEnabled'] = self.dcc_enabled
        return dictionary

    def from_dictionary(self, dictionary):
        super(CurrencyConversionSpecificInput, self).from_dictionary(dictionary)
        if 'dccEnabled' in dictionary:
            self.dcc_enabled = dictionary['dccEnabled']
        return self
