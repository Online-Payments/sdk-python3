# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .card_payment_method_specific_output_summary_card import CardPaymentMethodSpecificOutputSummaryCard
from .data_object import DataObject


class CardPaymentMethodSpecificOutputSummary(DataObject):

    __card: Optional[CardPaymentMethodSpecificOutputSummaryCard] = None
    __token: Optional[str] = None

    @property
    def card(self) -> Optional[CardPaymentMethodSpecificOutputSummaryCard]:
        """
        | Card details

        Type: :class:`onlinepayments.sdk.domain.card_payment_method_specific_output_summary_card.CardPaymentMethodSpecificOutputSummaryCard`
        """
        return self.__card

    @card.setter
    def card(self, value: Optional[CardPaymentMethodSpecificOutputSummaryCard]) -> None:
        self.__card = value

    @property
    def token(self) -> Optional[str]:
        """
        | ID of the token. This property is populated when the payment was done with a token or when the payment was tokenized.

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: Optional[str]) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super(CardPaymentMethodSpecificOutputSummary, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardPaymentMethodSpecificOutputSummary':
        super(CardPaymentMethodSpecificOutputSummary, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardPaymentMethodSpecificOutputSummaryCard()
            self.card = value.from_dictionary(dictionary['card'])
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
