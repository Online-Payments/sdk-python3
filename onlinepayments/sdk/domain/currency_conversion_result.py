# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CurrencyConversionResult(DataObject):

    __result: Optional[str] = None
    __result_reason: Optional[str] = None

    @property
    def result(self) -> Optional[str]:
        """
        | Functional response to the request:
        
        * Allowed: Dynamic currency conversion may be offered to the cardholder
        * InvalidCard: The card is not valid for dynamic currency conversion
        * InvalidMerchant: The card acceptor has not been recognised
        * NoRate: Exchange rates are not available
        * NotAvailable: Dynamic currency conversion is not available for other reason

        Type: str
        """
        return self.__result

    @result.setter
    def result(self, value: Optional[str]) -> None:
        self.__result = value

    @property
    def result_reason(self) -> Optional[str]:
        """
        | Plain text explaining the result of the currency conversion request

        Type: str
        """
        return self.__result_reason

    @result_reason.setter
    def result_reason(self, value: Optional[str]) -> None:
        self.__result_reason = value

    def to_dictionary(self) -> dict:
        dictionary = super(CurrencyConversionResult, self).to_dictionary()
        if self.result is not None:
            dictionary['result'] = self.result
        if self.result_reason is not None:
            dictionary['resultReason'] = self.result_reason
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CurrencyConversionResult':
        super(CurrencyConversionResult, self).from_dictionary(dictionary)
        if 'result' in dictionary:
            self.result = dictionary['result']
        if 'resultReason' in dictionary:
            self.result_reason = dictionary['resultReason']
        return self
