# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject


class SessionData(DataObject):

    __hosted_fields_session_id: Optional[str] = None
    __locale: Optional[str] = None
    __platform_url: Optional[str] = None
    __session_token: Optional[str] = None
    __tokens: Optional[List[str]] = None

    @property
    def hosted_fields_session_id(self) -> Optional[str]:
        """
        | Id of the created session

        Type: str
        """
        return self.__hosted_fields_session_id

    @hosted_fields_session_id.setter
    def hosted_fields_session_id(self, value: Optional[str]) -> None:
        self.__hosted_fields_session_id = value

    @property
    def locale(self) -> Optional[str]:
        """
        | Locale used in the GUI towards the consumer.

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: Optional[str]) -> None:
        self.__locale = value

    @property
    def platform_url(self) -> Optional[str]:
        """
        | This is the URL to Worldline's payment platform.

        Type: str
        """
        return self.__platform_url

    @platform_url.setter
    def platform_url(self, value: Optional[str]) -> None:
        self.__platform_url = value

    @property
    def session_token(self) -> Optional[str]:
        """
        | The JWT token used to authorize calls between iframes and server

        Type: str
        """
        return self.__session_token

    @session_token.setter
    def session_token(self, value: Optional[str]) -> None:
        self.__session_token = value

    @property
    def tokens(self) -> Optional[List[str]]:
        """
        | This is a list of validated, previously stored card tokens available for use in this checkout session.

        Type: list[str]
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value: Optional[List[str]]) -> None:
        self.__tokens = value

    def to_dictionary(self) -> dict:
        dictionary = super(SessionData, self).to_dictionary()
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
        super(SessionData, self).from_dictionary(dictionary)
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
