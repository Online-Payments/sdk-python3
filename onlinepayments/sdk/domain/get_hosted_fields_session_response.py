# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .token_info import TokenInfo


class GetHostedFieldsSessionResponse(DataObject):

    __session_id: Optional[str] = None
    __token: Optional[TokenInfo] = None

    @property
    def session_id(self) -> Optional[str]:
        """
        | The ID of the hosted fields session.

        Type: str
        """
        return self.__session_id

    @session_id.setter
    def session_id(self, value: Optional[str]) -> None:
        self.__session_id = value

    @property
    def token(self) -> Optional[TokenInfo]:
        """
        | Object containing token information that is used in the hosted fields session

        Type: :class:`onlinepayments.sdk.domain.token_info.TokenInfo`
        """
        return self.__token

    @token.setter
    def token(self, value: Optional[TokenInfo]) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super(GetHostedFieldsSessionResponse, self).to_dictionary()
        if self.session_id is not None:
            dictionary['sessionId'] = self.session_id
        if self.token is not None:
            dictionary['token'] = self.token.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetHostedFieldsSessionResponse':
        super(GetHostedFieldsSessionResponse, self).from_dictionary(dictionary)
        if 'sessionId' in dictionary:
            self.session_id = dictionary['sessionId']
        if 'token' in dictionary:
            if not isinstance(dictionary['token'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['token']))
            value = TokenInfo()
            self.token = value.from_dictionary(dictionary['token'])
        return self
