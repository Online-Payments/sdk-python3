#
# This file was automatically generated.
#
from .card_token import CardToken
from .data_object import DataObject
from .session_data import SessionData


class CreateHostedFieldsSessionResponse(DataObject):

    __slots__ = (
        "__card_tokens",
        "__hosted_fields_session_id",
        "__invalid_tokens",
        "__sdk_sri",
        "__sdk_url",
        "__session_data",
    )

    __card_tokens: list[CardToken] | None
    __hosted_fields_session_id: str | None
    __invalid_tokens: list[str] | None
    __sdk_sri: str | None
    __sdk_url: str | None
    __session_data: SessionData | None

    def __init__(
        self,
        *,
        card_tokens: list[CardToken] | None = None,
        hosted_fields_session_id: str | None = None,
        invalid_tokens: list[str] | None = None,
        sdk_sri: str | None = None,
        sdk_url: str | None = None,
        session_data: SessionData | None = None,
    ) -> None:
        self.card_tokens = card_tokens
        self.hosted_fields_session_id = hosted_fields_session_id
        self.invalid_tokens = invalid_tokens
        self.sdk_sri = sdk_sri
        self.sdk_url = sdk_url
        self.session_data = session_data

    @property
    def card_tokens(self) -> list[CardToken] | None:
        """
        | This is a list of validated, previously stored card tokens available for use in this checkout session.

        Type: list[:class:`onlinepayments.sdk.domain.card_token.CardToken`]
        """
        return self.__card_tokens

    @card_tokens.setter
    def card_tokens(self, value: list[CardToken] | None) -> None:
        self.__card_tokens = value

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
    def invalid_tokens(self) -> list[str] | None:
        """
        | This is a list of tokens that failed validation.

        Type: list[str]
        """
        return self.__invalid_tokens

    @invalid_tokens.setter
    def invalid_tokens(self, value: list[str] | None) -> None:
        self.__invalid_tokens = value

    @property
    def sdk_sri(self) -> str | None:
        """
        | This is the cryptographic hash used for Subresource Integrity validation.

        Type: str
        """
        return self.__sdk_sri

    @sdk_sri.setter
    def sdk_sri(self, value: str | None) -> None:
        self.__sdk_sri = value

    @property
    def sdk_url(self) -> str | None:
        """
        | The URL points to the hosted fields SDK.

        Type: str
        """
        return self.__sdk_url

    @sdk_url.setter
    def sdk_url(self, value: str | None) -> None:
        self.__sdk_url = value

    @property
    def session_data(self) -> SessionData | None:
        """
        | This contains the data required to initialize the Hosted Fields SDK.

        Type: :class:`onlinepayments.sdk.domain.session_data.SessionData`
        """
        return self.__session_data

    @session_data.setter
    def session_data(self, value: SessionData | None) -> None:
        self.__session_data = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.card_tokens is not None:
            dictionary['cardTokens'] = []
            for element in self.card_tokens:
                if element is not None:
                    dictionary['cardTokens'].append(element.to_dictionary())
        if self.hosted_fields_session_id is not None:
            dictionary['hostedFieldsSessionId'] = self.hosted_fields_session_id
        if self.invalid_tokens is not None:
            dictionary['invalidTokens'] = []
            for element in self.invalid_tokens:
                if element is not None:
                    dictionary['invalidTokens'].append(element)
        if self.sdk_sri is not None:
            dictionary['sdkSri'] = self.sdk_sri
        if self.sdk_url is not None:
            dictionary['sdkUrl'] = self.sdk_url
        if self.session_data is not None:
            dictionary['sessionData'] = self.session_data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreateHostedFieldsSessionResponse':
        super().from_dictionary(dictionary)
        if 'cardTokens' in dictionary:
            if not isinstance(dictionary['cardTokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['cardTokens']))
            self.card_tokens = []
            for element in dictionary['cardTokens']:
                value = CardToken()
                self.card_tokens.append(value.from_dictionary(element))
        if 'hostedFieldsSessionId' in dictionary:
            self.hosted_fields_session_id = dictionary['hostedFieldsSessionId']
        if 'invalidTokens' in dictionary:
            if not isinstance(dictionary['invalidTokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['invalidTokens']))
            self.invalid_tokens = []
            for element in dictionary['invalidTokens']:
                self.invalid_tokens.append(element)
        if 'sdkSri' in dictionary:
            self.sdk_sri = dictionary['sdkSri']
        if 'sdkUrl' in dictionary:
            self.sdk_url = dictionary['sdkUrl']
        if 'sessionData' in dictionary:
            if not isinstance(dictionary['sessionData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['sessionData']))
            value = SessionData()
            self.session_data = value.from_dictionary(dictionary['sessionData'])
        return self
