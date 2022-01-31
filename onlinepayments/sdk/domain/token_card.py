# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.token_card_data import TokenCardData


class TokenCard(DataObject):
    """
    | Object containing card details
    """

    __alias = None
    __data = None

    @property
    def alias(self) -> str:
        """
        | An alias for the token. This can be used to visually represent the token.

        Type: str
        """
        return self.__alias

    @alias.setter
    def alias(self, value: str):
        self.__alias = value

    @property
    def data(self) -> TokenCardData:
        """
        Type: :class:`onlinepayments.sdk.domain.token_card_data.TokenCardData`
        """
        return self.__data

    @data.setter
    def data(self, value: TokenCardData):
        self.__data = value

    def to_dictionary(self):
        dictionary = super(TokenCard, self).to_dictionary()
        if self.alias is not None:
            dictionary['alias'] = self.alias
        if self.data is not None:
            dictionary['data'] = self.data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenCard, self).from_dictionary(dictionary)
        if 'alias' in dictionary:
            self.alias = dictionary['alias']
        if 'data' in dictionary:
            if not isinstance(dictionary['data'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['data']))
            value = TokenCardData()
            self.data = value.from_dictionary(dictionary['data'])
        return self
