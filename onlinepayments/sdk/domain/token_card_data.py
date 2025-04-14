# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .card_without_cvv import CardWithoutCvv
from .data_object import DataObject


class TokenCardData(DataObject):

    __card_without_cvv: Optional[CardWithoutCvv] = None
    __cobrand_selection_indicator: Optional[str] = None

    @property
    def card_without_cvv(self) -> Optional[CardWithoutCvv]:
        """
        Type: :class:`onlinepayments.sdk.domain.card_without_cvv.CardWithoutCvv`
        """
        return self.__card_without_cvv

    @card_without_cvv.setter
    def card_without_cvv(self, value: Optional[CardWithoutCvv]) -> None:
        self.__card_without_cvv = value

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
        dictionary = super(TokenCardData, self).to_dictionary()
        if self.card_without_cvv is not None:
            dictionary['cardWithoutCvv'] = self.card_without_cvv.to_dictionary()
        if self.cobrand_selection_indicator is not None:
            dictionary['cobrandSelectionIndicator'] = self.cobrand_selection_indicator
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'TokenCardData':
        super(TokenCardData, self).from_dictionary(dictionary)
        if 'cardWithoutCvv' in dictionary:
            if not isinstance(dictionary['cardWithoutCvv'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardWithoutCvv']))
            value = CardWithoutCvv()
            self.card_without_cvv = value.from_dictionary(dictionary['cardWithoutCvv'])
        if 'cobrandSelectionIndicator' in dictionary:
            self.cobrand_selection_indicator = dictionary['cobrandSelectionIndicator']
        return self
