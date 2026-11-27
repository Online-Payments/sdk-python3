#
# This file was automatically generated.
#
from .data_object import DataObject
from .detokenized_token_response import DetokenizedTokenResponse


class DetokenizationResponse(DataObject):

    __slots__ = (
        "__tokens",
    )

    __tokens: list[DetokenizedTokenResponse] | None

    def __init__(
        self,
        *,
        tokens: list[DetokenizedTokenResponse] | None = None,
    ) -> None:
        self.tokens = tokens

    @property
    def tokens(self) -> list[DetokenizedTokenResponse] | None:
        """
        | The response contains an array of detokenized data for the provided token IDs, which includes card details and expiration dates.

        Type: list[:class:`onlinepayments.sdk.domain.detokenized_token_response.DetokenizedTokenResponse`]
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value: list[DetokenizedTokenResponse] | None) -> None:
        self.__tokens = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.tokens is not None:
            dictionary['tokens'] = []
            for element in self.tokens:
                if element is not None:
                    dictionary['tokens'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DetokenizationResponse':
        super().from_dictionary(dictionary)
        if 'tokens' in dictionary:
            if not isinstance(dictionary['tokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['tokens']))
            self.tokens = []
            for element in dictionary['tokens']:
                value = DetokenizedTokenResponse()
                self.tokens.append(value.from_dictionary(element))
        return self
