#
# This file was automatically generated.
#
from .data_object import DataObject


class CurrencyConversionResult(DataObject):

    __slots__ = (
        "__result",
        "__result_reason",
    )

    __result: str | None
    __result_reason: str | None

    def __init__(
        self,
        *,
        result: str | None = None,
        result_reason: str | None = None,
    ) -> None:
        self.result = result
        self.result_reason = result_reason

    @property
    def result(self) -> str | None:
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
    def result(self, value: str | None) -> None:
        self.__result = value

    @property
    def result_reason(self) -> str | None:
        """
        | Plain text explaining the result of the currency conversion request

        Type: str
        """
        return self.__result_reason

    @result_reason.setter
    def result_reason(self, value: str | None) -> None:
        self.__result_reason = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.result is not None:
            dictionary['result'] = self.result
        if self.result_reason is not None:
            dictionary['resultReason'] = self.result_reason
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CurrencyConversionResult':
        super().from_dictionary(dictionary)
        if 'result' in dictionary:
            self.result = dictionary['result']
        if 'resultReason' in dictionary:
            self.result_reason = dictionary['resultReason']
        return self
