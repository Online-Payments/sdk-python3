# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.token_data import TokenData


class TokenCardSpecificInput(DataObject):
    """
    | Object containing the token details for a card
    """

    __data = None

    @property
    def data(self) -> TokenData:
        """
        | Object containing the token details for a card

        Type: :class:`onlinepayments.sdk.domain.token_data.TokenData`
        """
        return self.__data

    @data.setter
    def data(self, value: TokenData):
        self.__data = value

    def to_dictionary(self):
        dictionary = super(TokenCardSpecificInput, self).to_dictionary()
        if self.data is not None:
            dictionary['data'] = self.data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenCardSpecificInput, self).from_dictionary(dictionary)
        if 'data' in dictionary:
            if not isinstance(dictionary['data'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['data']))
            value = TokenData()
            self.data = value.from_dictionary(dictionary['data'])
        return self
