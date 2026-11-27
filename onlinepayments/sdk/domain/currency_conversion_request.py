#
# This file was automatically generated.
#
from .data_object import DataObject
from .dcc_card_source import DccCardSource
from .transaction import Transaction


class CurrencyConversionRequest(DataObject):

    __slots__ = (
        "__card_source",
        "__transaction",
    )

    __card_source: DccCardSource | None
    __transaction: Transaction | None

    def __init__(
        self,
        *,
        card_source: DccCardSource | None = None,
        transaction: Transaction | None = None,
    ) -> None:
        self.card_source = card_source
        self.transaction = transaction

    @property
    def card_source(self) -> DccCardSource | None:
        """
        Type: :class:`onlinepayments.sdk.domain.dcc_card_source.DccCardSource`
        """
        return self.__card_source

    @card_source.setter
    def card_source(self, value: DccCardSource | None) -> None:
        self.__card_source = value

    @property
    def transaction(self) -> Transaction | None:
        """
        Type: :class:`onlinepayments.sdk.domain.transaction.Transaction`
        """
        return self.__transaction

    @transaction.setter
    def transaction(self, value: Transaction | None) -> None:
        self.__transaction = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.card_source is not None:
            dictionary['cardSource'] = self.card_source.to_dictionary()
        if self.transaction is not None:
            dictionary['transaction'] = self.transaction.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CurrencyConversionRequest':
        super().from_dictionary(dictionary)
        if 'cardSource' in dictionary:
            if not isinstance(dictionary['cardSource'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardSource']))
            value = DccCardSource()
            self.card_source = value.from_dictionary(dictionary['cardSource'])
        if 'transaction' in dictionary:
            if not isinstance(dictionary['transaction'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['transaction']))
            value = Transaction()
            self.transaction = value.from_dictionary(dictionary['transaction'])
        return self
