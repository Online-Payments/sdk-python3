#
# This file was automatically generated.
#
from .data_object import DataObject
from .token_card_data import TokenCardData


class TokenCard(DataObject):

    __slots__ = (
        "__alias",
        "__data",
    )

    __alias: str | None
    __data: TokenCardData | None

    def __init__(
        self,
        *,
        alias: str | None = None,
        data: TokenCardData | None = None,
    ) -> None:
        self.alias = alias
        self.data = data

    @property
    def alias(self) -> str | None:
        """
        | An alias for the token. This can be used to visually represent the token.

        Type: str
        """
        return self.__alias

    @alias.setter
    def alias(self, value: str | None) -> None:
        self.__alias = value

    @property
    def data(self) -> TokenCardData | None:
        """
        Type: :class:`onlinepayments.sdk.domain.token_card_data.TokenCardData`
        """
        return self.__data

    @data.setter
    def data(self, value: TokenCardData | None) -> None:
        self.__data = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.alias is not None:
            dictionary['alias'] = self.alias
        if self.data is not None:
            dictionary['data'] = self.data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'TokenCard':
        super().from_dictionary(dictionary)
        if 'alias' in dictionary:
            self.alias = dictionary['alias']
        if 'data' in dictionary:
            if not isinstance(dictionary['data'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['data']))
            value = TokenCardData()
            self.data = value.from_dictionary(dictionary['data'])
        return self
