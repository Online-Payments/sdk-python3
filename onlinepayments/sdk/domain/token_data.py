# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .card import Card
from .data_object import DataObject


class TokenData(DataObject):

    __card: Optional[Card] = None
    __cobrand_selection_indicator: Optional[str] = None

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
    def cobrand_selection_indicator(self) -> Optional[str]:
        """
        | For cobranded cards, this field indicates the brand selection method:
        
        * default - The holder implicitly accepted the default brand.
        * alternative - The holder explicitly selected an alternative brand.
        * notApplicable - The card is not cobranded.

        Type: str
        """
        return self.__cobrand_selection_indicator

    @cobrand_selection_indicator.setter
    def cobrand_selection_indicator(self, value: Optional[str]) -> None:
        self.__cobrand_selection_indicator = value

    def to_dictionary(self) -> dict:
        dictionary = super(TokenData, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.cobrand_selection_indicator is not None:
            dictionary['cobrandSelectionIndicator'] = self.cobrand_selection_indicator
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'TokenData':
        super(TokenData, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = Card()
            self.card = value.from_dictionary(dictionary['card'])
        if 'cobrandSelectionIndicator' in dictionary:
            self.cobrand_selection_indicator = dictionary['cobrandSelectionIndicator']
        return self
