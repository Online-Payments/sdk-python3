# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .card import Card
from .data_object import DataObject


class CardPayoutMethodSpecificInput(DataObject):

    __card: Optional[Card] = None
    __payment_product_id: Optional[int] = None
    __payout_reason: Optional[str] = None
    __token: Optional[str] = None

    @property
    def card(self) -> Optional[Card]:
        """
        | Object containing card details

        Type: :class:`onlinepayments.sdk.domain.card.Card`
        """
        return self.__card

    @card.setter
    def card(self, value: Optional[Card]) -> None:
        self.__card = value

    @property
    def payment_product_id(self) -> Optional[int]:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: Optional[int]) -> None:
        self.__payment_product_id = value

    @property
    def payout_reason(self) -> Optional[str]:
        """
        | Allows you to additionally specify the reason for initiating the payout for authorization purposes. If this field is not specified, authorisation of the payment will be made according to your merchant profile. Possible values are:
        
        * Gambling
        * Refund
        * Loyalty

        Type: str
        """
        return self.__payout_reason

    @payout_reason.setter
    def payout_reason(self, value: Optional[str]) -> None:
        self.__payout_reason = value

    @property
    def token(self) -> Optional[str]:
        """
        | ID of the token

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: Optional[str]) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super(CardPayoutMethodSpecificInput, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.payout_reason is not None:
            dictionary['payoutReason'] = self.payout_reason
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardPayoutMethodSpecificInput':
        super(CardPayoutMethodSpecificInput, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = Card()
            self.card = value.from_dictionary(dictionary['card'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'payoutReason' in dictionary:
            self.payout_reason = dictionary['payoutReason']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
