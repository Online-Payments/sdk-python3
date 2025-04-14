# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject


class SessionResponse(DataObject):

    __asset_url: Optional[str] = None
    __client_api_url: Optional[str] = None
    __client_session_id: Optional[str] = None
    __customer_id: Optional[str] = None
    __invalid_tokens: Optional[List[str]] = None

    @property
    def asset_url(self) -> Optional[str]:
        """
        | The datacenter-specific base url for assets. This value needs to be passed to the Client SDK to make sure that the client software connects to the right datacenter.

        Type: str
        """
        return self.__asset_url

    @asset_url.setter
    def asset_url(self, value: Optional[str]) -> None:
        self.__asset_url = value

    @property
    def client_api_url(self) -> Optional[str]:
        """
        | The datacenter-specific base url for client requests. This value needs to be passed to the Client SDK to make sure that the client software connects to the right datacenter.

        Type: str
        """
        return self.__client_api_url

    @client_api_url.setter
    def client_api_url(self, value: Optional[str]) -> None:
        self.__client_api_url = value

    @property
    def client_session_id(self) -> Optional[str]:
        """
        | The identifier of the session that has been created.

        Type: str
        """
        return self.__client_session_id

    @client_session_id.setter
    def client_session_id(self, value: Optional[str]) -> None:
        self.__client_session_id = value

    @property
    def customer_id(self) -> Optional[str]:
        """
        | The session is built up around the customer in the form of the customerId. All client APIs use this customerId in the URI to identify the customer.

        Type: str
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value: Optional[str]) -> None:
        self.__customer_id = value

    @property
    def invalid_tokens(self) -> Optional[List[str]]:
        """
        Type: list[str]
        """
        return self.__invalid_tokens

    @invalid_tokens.setter
    def invalid_tokens(self, value: Optional[List[str]]) -> None:
        self.__invalid_tokens = value

    def to_dictionary(self) -> dict:
        dictionary = super(SessionResponse, self).to_dictionary()
        if self.asset_url is not None:
            dictionary['assetUrl'] = self.asset_url
        if self.client_api_url is not None:
            dictionary['clientApiUrl'] = self.client_api_url
        if self.client_session_id is not None:
            dictionary['clientSessionId'] = self.client_session_id
        if self.customer_id is not None:
            dictionary['customerId'] = self.customer_id
        if self.invalid_tokens is not None:
            dictionary['invalidTokens'] = []
            for element in self.invalid_tokens:
                if element is not None:
                    dictionary['invalidTokens'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SessionResponse':
        super(SessionResponse, self).from_dictionary(dictionary)
        if 'assetUrl' in dictionary:
            self.asset_url = dictionary['assetUrl']
        if 'clientApiUrl' in dictionary:
            self.client_api_url = dictionary['clientApiUrl']
        if 'clientSessionId' in dictionary:
            self.client_session_id = dictionary['clientSessionId']
        if 'customerId' in dictionary:
            self.customer_id = dictionary['customerId']
        if 'invalidTokens' in dictionary:
            if not isinstance(dictionary['invalidTokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['invalidTokens']))
            self.invalid_tokens = []
            for element in dictionary['invalidTokens']:
                self.invalid_tokens.append(element)
        return self
