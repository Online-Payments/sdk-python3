# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .acceptance import Acceptance
from .card_essentials import CardEssentials
from .data_object import DataObject


class PayoutCardPaymentMethodSpecificOutput(DataObject):

    __acceptance: Optional[Acceptance] = None
    __authorisation_code: Optional[str] = None
    __card: Optional[CardEssentials] = None
    __payment_product_id: Optional[int] = None

    @property
    def acceptance(self) -> Optional[Acceptance]:
        """
        | This object contains the acceptance information for the card payment authorization.

        Type: :class:`onlinepayments.sdk.domain.acceptance.Acceptance`
        """
        return self.__acceptance

    @acceptance.setter
    def acceptance(self, value: Optional[Acceptance]) -> None:
        self.__acceptance = value

    @property
    def authorisation_code(self) -> Optional[str]:
        """
        | Card Authorization code as returned by the acquirer

        Type: str
        """
        return self.__authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, value: Optional[str]) -> None:
        self.__authorisation_code = value

    @property
    def card(self) -> Optional[CardEssentials]:
        """
        | Object containing card details

        Type: :class:`onlinepayments.sdk.domain.card_essentials.CardEssentials`
        """
        return self.__card

    @card.setter
    def card(self, value: Optional[CardEssentials]) -> None:
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

    def to_dictionary(self) -> dict:
        dictionary = super(PayoutCardPaymentMethodSpecificOutput, self).to_dictionary()
        if self.acceptance is not None:
            dictionary['acceptance'] = self.acceptance.to_dictionary()
        if self.authorisation_code is not None:
            dictionary['authorisationCode'] = self.authorisation_code
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PayoutCardPaymentMethodSpecificOutput':
        super(PayoutCardPaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'acceptance' in dictionary:
            if not isinstance(dictionary['acceptance'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['acceptance']))
            value = Acceptance()
            self.acceptance = value.from_dictionary(dictionary['acceptance'])
        if 'authorisationCode' in dictionary:
            self.authorisation_code = dictionary['authorisationCode']
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardEssentials()
            self.card = value.from_dictionary(dictionary['card'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
