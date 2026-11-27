#
# This file was automatically generated.
#
from .card_without_cvv import CardWithoutCvv
from .crm_token import CrmToken
from .data_object import DataObject
from .external_token_linked import ExternalTokenLinked


class CreatedTokenResponse(DataObject):

    __slots__ = (
        "__card",
        "__crm_token",
        "__external_token_linked",
        "__is_new_token",
        "__token",
        "__token_status",
    )

    __card: CardWithoutCvv | None
    __crm_token: CrmToken | None
    __external_token_linked: ExternalTokenLinked | None
    __is_new_token: bool | None
    __token: str | None
    __token_status: str | None

    def __init__(
        self,
        *,
        card: CardWithoutCvv | None = None,
        crm_token: CrmToken | None = None,
        external_token_linked: ExternalTokenLinked | None = None,
        is_new_token: bool | None = None,
        token: str | None = None,
        token_status: str | None = None,
    ) -> None:
        self.card = card
        self.crm_token = crm_token
        self.external_token_linked = external_token_linked
        self.is_new_token = is_new_token
        self.token = token
        self.token_status = token_status

    @property
    def card(self) -> CardWithoutCvv | None:
        """
        Type: :class:`onlinepayments.sdk.domain.card_without_cvv.CardWithoutCvv`
        """
        return self.__card

    @card.setter
    def card(self, value: CardWithoutCvv | None) -> None:
        self.__card = value

    @property
    def crm_token(self) -> CrmToken | None:
        """
        | The CRM (Customer Relationship Management) token group. CRM tokens are available to enhance knowledge of a merchant's customers by attempting to identify the customer.

        Type: :class:`onlinepayments.sdk.domain.crm_token.CrmToken`
        """
        return self.__crm_token

    @crm_token.setter
    def crm_token(self, value: CrmToken | None) -> None:
        self.__crm_token = value

    @property
    def external_token_linked(self) -> ExternalTokenLinked | None:
        """
        Type: :class:`onlinepayments.sdk.domain.external_token_linked.ExternalTokenLinked`
        """
        return self.__external_token_linked

    @external_token_linked.setter
    def external_token_linked(self, value: ExternalTokenLinked | None) -> None:
        self.__external_token_linked = value

    @property
    def is_new_token(self) -> bool | None:
        """
        | Indicates if a new token was created
        
        * true - A new token was created
        * false - A token with the same card number already exists and is returned. Please note that the existing token has not been updated. When you want to update other data then the card number, you need to update data stored in the token explicitly, as data is never updated during the creation of a token.

        Type: bool
        """
        return self.__is_new_token

    @is_new_token.setter
    def is_new_token(self, value: bool | None) -> None:
        self.__is_new_token = value

    @property
    def token(self) -> str | None:
        """
        | ID of the token

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: str | None) -> None:
        self.__token = value

    @property
    def token_status(self) -> str | None:
        """
        | This is the status of the token in the hosted tokenization session. Possible values are:
        
        * UNCHANGED - The token has not changed
        * CREATED - The token has been created
        * UPDATED - The token has been updated

        Type: str
        """
        return self.__token_status

    @token_status.setter
    def token_status(self, value: str | None) -> None:
        self.__token_status = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.crm_token is not None:
            dictionary['crmToken'] = self.crm_token.to_dictionary()
        if self.external_token_linked is not None:
            dictionary['externalTokenLinked'] = self.external_token_linked.to_dictionary()
        if self.is_new_token is not None:
            dictionary['isNewToken'] = self.is_new_token
        if self.token is not None:
            dictionary['token'] = self.token
        if self.token_status is not None:
            dictionary['tokenStatus'] = self.token_status
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreatedTokenResponse':
        super().from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardWithoutCvv()
            self.card = value.from_dictionary(dictionary['card'])
        if 'crmToken' in dictionary:
            if not isinstance(dictionary['crmToken'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['crmToken']))
            value = CrmToken()
            self.crm_token = value.from_dictionary(dictionary['crmToken'])
        if 'externalTokenLinked' in dictionary:
            if not isinstance(dictionary['externalTokenLinked'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['externalTokenLinked']))
            value = ExternalTokenLinked()
            self.external_token_linked = value.from_dictionary(dictionary['externalTokenLinked'])
        if 'isNewToken' in dictionary:
            self.is_new_token = dictionary['isNewToken']
        if 'token' in dictionary:
            self.token = dictionary['token']
        if 'tokenStatus' in dictionary:
            self.token_status = dictionary['tokenStatus']
        return self
