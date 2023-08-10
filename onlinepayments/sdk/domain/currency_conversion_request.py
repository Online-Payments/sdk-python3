# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.dcc_card_source import DccCardSource
from onlinepayments.sdk.domain.transaction import Transaction


class CurrencyConversionRequest(DataObject):
    __card_source = None
    __transaction = None

    @property
    def card_source(self) -> DccCardSource:
        """
        Type: :class:`onlinepayments.sdk.domain.dcc_card_source.DccCardSource`
        """
        return self.__card_source

    @card_source.setter
    def card_source(self, value: DccCardSource):
        self.__card_source = value

    @property
    def transaction(self) -> Transaction:
        """
        Type: :class:`onlinepayments.sdk.domain.transaction.Transaction`
        """
        return self.__transaction

    @transaction.setter
    def transaction(self, value: Transaction):
        self.__transaction = value

    def to_dictionary(self):
        dictionary = super(CurrencyConversionRequest, self).to_dictionary()
        if self.card_source is not None:
            dictionary['cardSource'] = self.card_source.to_dictionary()
        if self.transaction is not None:
            dictionary['transaction'] = self.transaction.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CurrencyConversionRequest, self).from_dictionary(dictionary)
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
