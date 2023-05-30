# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.card_info import CardInfo
from onlinepayments.sdk.domain.transaction import Transaction


class CurrencyConversionRequest(DataObject):
    __card = None
    __transaction = None

    @property
    def card(self) -> CardInfo:
        """
        Type: :class:`onlinepayments.sdk.domain.card_info.CardInfo`
        """
        return self.__card

    @card.setter
    def card(self, value: CardInfo):
        self.__card = value

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
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.transaction is not None:
            dictionary['transaction'] = self.transaction.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CurrencyConversionRequest, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardInfo()
            self.card = value.from_dictionary(dictionary['card'])
        if 'transaction' in dictionary:
            if not isinstance(dictionary['transaction'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['transaction']))
            value = Transaction()
            self.transaction = value.from_dictionary(dictionary['transaction'])
        return self
