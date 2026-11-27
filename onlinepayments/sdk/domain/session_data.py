#
# This file was automatically generated.
#
from .data_object import DataObject


class SessionData(DataObject):

    __slots__ = (
        "__hosted_fields_session_id",
        "__locale",
        "__platform_url",
        "__session_token",
        "__tokens",
    )

    __hosted_fields_session_id: str | None
    __locale: str | None
    __platform_url: str | None
    __session_token: str | None
    __tokens: list[str] | None

    def __init__(
        self,
        *,
        hosted_fields_session_id: str | None = None,
        locale: str | None = None,
        platform_url: str | None = None,
        session_token: str | None = None,
        tokens: list[str] | None = None,
    ) -> None:
        self.hosted_fields_session_id = hosted_fields_session_id
        self.locale = locale
        self.platform_url = platform_url
        self.session_token = session_token
        self.tokens = tokens

    @property
    def hosted_fields_session_id(self) -> str | None:
        """
        | Id of the created session

        Type: str
        """
        return self.__hosted_fields_session_id

    @hosted_fields_session_id.setter
    def hosted_fields_session_id(self, value: str | None) -> None:
        self.__hosted_fields_session_id = value

    @property
    def locale(self) -> str | None:
        """
        | Locale used in the GUI towards the consumer.

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: str | None) -> None:
        self.__locale = value

    @property
    def platform_url(self) -> str | None:
        """
        | This is the URL to Worldline's payment platform.

        Type: str
        """
        return self.__platform_url

    @platform_url.setter
    def platform_url(self, value: str | None) -> None:
        self.__platform_url = value

    @property
    def session_token(self) -> str | None:
        """
        | The CSRF token used to authorize iframe's calls

        Type: str
        """
        return self.__session_token

    @session_token.setter
    def session_token(self, value: str | None) -> None:
        self.__session_token = value

    @property
    def tokens(self) -> list[str] | None:
        """
        | This is a list of card tokens

        Type: list[str]
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value: list[str] | None) -> None:
        self.__tokens = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.hosted_fields_session_id is not None:
            dictionary['hostedFieldsSessionId'] = self.hosted_fields_session_id
        if self.locale is not None:
            dictionary['locale'] = self.locale
        if self.platform_url is not None:
            dictionary['platformUrl'] = self.platform_url
        if self.session_token is not None:
            dictionary['sessionToken'] = self.session_token
        if self.tokens is not None:
            dictionary['tokens'] = []
            for element in self.tokens:
                if element is not None:
                    dictionary['tokens'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SessionData':
        super().from_dictionary(dictionary)
        if 'hostedFieldsSessionId' in dictionary:
            self.hosted_fields_session_id = dictionary['hostedFieldsSessionId']
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'platformUrl' in dictionary:
            self.platform_url = dictionary['platformUrl']
        if 'sessionToken' in dictionary:
            self.session_token = dictionary['sessionToken']
        if 'tokens' in dictionary:
            if not isinstance(dictionary['tokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['tokens']))
            self.tokens = []
            for element in dictionary['tokens']:
                self.tokens.append(element)
        return self
