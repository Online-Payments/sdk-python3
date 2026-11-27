#
# This file was automatically generated.
#
from .data_object import DataObject
from .token_data import TokenData


class TokenCardSpecificInput(DataObject):

    __slots__ = (
        "__data",
    )

    __data: TokenData | None

    def __init__(
        self,
        *,
        data: TokenData | None = None,
    ) -> None:
        self.data = data

    @property
    def data(self) -> TokenData | None:
        """
        | Object containing the token details for a card

        Type: :class:`onlinepayments.sdk.domain.token_data.TokenData`
        """
        return self.__data

    @data.setter
    def data(self, value: TokenData | None) -> None:
        self.__data = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.data is not None:
            dictionary['data'] = self.data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'TokenCardSpecificInput':
        super().from_dictionary(dictionary)
        if 'data' in dictionary:
            if not isinstance(dictionary['data'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['data']))
            value = TokenData()
            self.data = value.from_dictionary(dictionary['data'])
        return self
