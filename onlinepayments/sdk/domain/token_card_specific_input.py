# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .token_data import TokenData


class TokenCardSpecificInput(DataObject):

    __data: Optional[TokenData] = None

    @property
    def data(self) -> Optional[TokenData]:
        """
        | Object containing the token details for a card

        Type: :class:`onlinepayments.sdk.domain.token_data.TokenData`
        """
        return self.__data

    @data.setter
    def data(self, value: Optional[TokenData]) -> None:
        self.__data = value

    def to_dictionary(self) -> dict:
        dictionary = super(TokenCardSpecificInput, self).to_dictionary()
        if self.data is not None:
            dictionary['data'] = self.data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'TokenCardSpecificInput':
        super(TokenCardSpecificInput, self).from_dictionary(dictionary)
        if 'data' in dictionary:
            if not isinstance(dictionary['data'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['data']))
            value = TokenData()
            self.data = value.from_dictionary(dictionary['data'])
        return self
