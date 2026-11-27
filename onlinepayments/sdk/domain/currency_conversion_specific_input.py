#
# This file was automatically generated.
#
from .data_object import DataObject


class CurrencyConversionSpecificInput(DataObject):

    __slots__ = (
        "__dcc_enabled",
    )

    __dcc_enabled: bool | None

    def __init__(
        self,
        *,
        dcc_enabled: bool | None = None,
    ) -> None:
        self.dcc_enabled = dcc_enabled

    @property
    def dcc_enabled(self) -> bool | None:
        """
        | Indicates if this transaction is Dynamic Currency Conversion (DCC) enabled.
        
        * true - Dynamic Currency Conversion (DCC) is enabled in this transaction.
        * false - Dynamic Currency Conversion (DCC) is disabled in this transaction. The default value for this property is false.

        Type: bool
        """
        return self.__dcc_enabled

    @dcc_enabled.setter
    def dcc_enabled(self, value: bool | None) -> None:
        self.__dcc_enabled = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.dcc_enabled is not None:
            dictionary['dccEnabled'] = self.dcc_enabled
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CurrencyConversionSpecificInput':
        super().from_dictionary(dictionary)
        if 'dccEnabled' in dictionary:
            self.dcc_enabled = dictionary['dccEnabled']
        return self
