#
# This file was automatically generated.
#
from .data_object import DataObject


class SessionRequest(DataObject):

    __slots__ = (
        "__tokens",
    )

    __tokens: list[str] | None

    def __init__(
        self,
        *,
        tokens: list[str] | None = None,
    ) -> None:
        self.tokens = tokens

    @property
    def tokens(self) -> list[str] | None:
        """
        | List of previously stored tokens linked to the customer that wants to checkout.

        Type: list[str]
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value: list[str] | None) -> None:
        self.__tokens = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.tokens is not None:
            dictionary['tokens'] = []
            for element in self.tokens:
                if element is not None:
                    dictionary['tokens'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SessionRequest':
        super().from_dictionary(dictionary)
        if 'tokens' in dictionary:
            if not isinstance(dictionary['tokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['tokens']))
            self.tokens = []
            for element in dictionary['tokens']:
                self.tokens.append(element)
        return self
