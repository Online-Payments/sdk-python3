#
# This file was automatically generated.
#
from .data_object import DataObject
from .token_info import TokenInfo


class GetHostedFieldsSessionResponse(DataObject):

    __slots__ = (
        "__session_id",
        "__token",
    )

    __session_id: str | None
    __token: TokenInfo | None

    def __init__(
        self,
        *,
        session_id: str | None = None,
        token: TokenInfo | None = None,
    ) -> None:
        self.session_id = session_id
        self.token = token

    @property
    def session_id(self) -> str | None:
        """
        | The ID of the hosted fields session.

        Type: str
        """
        return self.__session_id

    @session_id.setter
    def session_id(self, value: str | None) -> None:
        self.__session_id = value

    @property
    def token(self) -> TokenInfo | None:
        """
        | Object containing token information that is used in the hosted fields session

        Type: :class:`onlinepayments.sdk.domain.token_info.TokenInfo`
        """
        return self.__token

    @token.setter
    def token(self, value: TokenInfo | None) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.session_id is not None:
            dictionary['sessionId'] = self.session_id
        if self.token is not None:
            dictionary['token'] = self.token.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetHostedFieldsSessionResponse':
        super().from_dictionary(dictionary)
        if 'sessionId' in dictionary:
            self.session_id = dictionary['sessionId']
        if 'token' in dictionary:
            if not isinstance(dictionary['token'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['token']))
            value = TokenInfo()
            self.token = value.from_dictionary(dictionary['token'])
        return self
