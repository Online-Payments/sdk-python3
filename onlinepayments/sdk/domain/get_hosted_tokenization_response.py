# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .token_response import TokenResponse


class GetHostedTokenizationResponse(DataObject):

    __token: Optional[TokenResponse] = None
    __token_status: Optional[str] = None

    @property
    def token(self) -> Optional[TokenResponse]:
        """
        Type: :class:`onlinepayments.sdk.domain.token_response.TokenResponse`
        """
        return self.__token

    @token.setter
    def token(self, value: Optional[TokenResponse]) -> None:
        self.__token = value

    @property
    def token_status(self) -> Optional[str]:
        """
        | This is the status of the token in the hosted tokenization session. Possible values are:
        
        * UNCHANGED - The token has not changed
        * CREATED - The token has been created
        * UPDATED - The token has been updated

        Type: str
        """
        return self.__token_status

    @token_status.setter
    def token_status(self, value: Optional[str]) -> None:
        self.__token_status = value

    def to_dictionary(self) -> dict:
        dictionary = super(GetHostedTokenizationResponse, self).to_dictionary()
        if self.token is not None:
            dictionary['token'] = self.token.to_dictionary()
        if self.token_status is not None:
            dictionary['tokenStatus'] = self.token_status
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetHostedTokenizationResponse':
        super(GetHostedTokenizationResponse, self).from_dictionary(dictionary)
        if 'token' in dictionary:
            if not isinstance(dictionary['token'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['token']))
            value = TokenResponse()
            self.token = value.from_dictionary(dictionary['token'])
        if 'tokenStatus' in dictionary:
            self.token_status = dictionary['tokenStatus']
        return self
