# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.card_without_cvv import CardWithoutCvv
from onlinepayments.sdk.domain.external_token_linked import ExternalTokenLinked


class CreatedTokenResponse(DataObject):
    __card = None
    __external_token_linked = None
    __is_new_token = None
    __token = None
    __token_status = None

    @property
    def card(self) -> CardWithoutCvv:
        """
        Type: :class:`onlinepayments.sdk.domain.card_without_cvv.CardWithoutCvv`
        """
        return self.__card

    @card.setter
    def card(self, value: CardWithoutCvv):
        self.__card = value

    @property
    def external_token_linked(self) -> ExternalTokenLinked:
        """
        Type: :class:`onlinepayments.sdk.domain.external_token_linked.ExternalTokenLinked`
        """
        return self.__external_token_linked

    @external_token_linked.setter
    def external_token_linked(self, value: ExternalTokenLinked):
        self.__external_token_linked = value

    @property
    def is_new_token(self) -> bool:
        """
        | Indicates if a new token was created 
        |  * true - A new token was created 
        |  * false - A token with the same card number already exists and is returned. Please note that the existing token has not been updated. When you want to update other data then the card number, you need to update data stored in the token explicitly, as data is never updated during the creation of a token.

        Type: bool
        """
        return self.__is_new_token

    @is_new_token.setter
    def is_new_token(self, value: bool):
        self.__is_new_token = value

    @property
    def token(self) -> str:
        """
        | ID of the token

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: str):
        self.__token = value

    @property
    def token_status(self) -> str:
        """
        | This is the status of the token in the hosted tokenization session. Possible values are:
        | * UNCHANGED - The token has not changed
        | * CREATED - The token has been created
        | * UPDATED - The token has been updated

        Type: str
        """
        return self.__token_status

    @token_status.setter
    def token_status(self, value: str):
        self.__token_status = value

    def to_dictionary(self):
        dictionary = super(CreatedTokenResponse, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.external_token_linked is not None:
            dictionary['externalTokenLinked'] = self.external_token_linked.to_dictionary()
        if self.is_new_token is not None:
            dictionary['isNewToken'] = self.is_new_token
        if self.token is not None:
            dictionary['token'] = self.token
        if self.token_status is not None:
            dictionary['tokenStatus'] = self.token_status
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatedTokenResponse, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardWithoutCvv()
            self.card = value.from_dictionary(dictionary['card'])
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
