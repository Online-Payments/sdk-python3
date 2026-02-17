# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .session_data import SessionData


class CreateHostedFieldsSessionResponse(DataObject):

    __sdk_sri: Optional[str] = None
    __sdk_url: Optional[str] = None
    __session_data: Optional[SessionData] = None

    @property
    def sdk_sri(self) -> Optional[str]:
        """
        | This is the cryptographic hash used for Subresource Integrity validation.

        Type: str
        """
        return self.__sdk_sri

    @sdk_sri.setter
    def sdk_sri(self, value: Optional[str]) -> None:
        self.__sdk_sri = value

    @property
    def sdk_url(self) -> Optional[str]:
        """
        | The URL points to the hosted fields SDK.

        Type: str
        """
        return self.__sdk_url

    @sdk_url.setter
    def sdk_url(self, value: Optional[str]) -> None:
        self.__sdk_url = value

    @property
    def session_data(self) -> Optional[SessionData]:
        """
        | This contains the data required to initialize the Hosted Fields SDK.

        Type: :class:`onlinepayments.sdk.domain.session_data.SessionData`
        """
        return self.__session_data

    @session_data.setter
    def session_data(self, value: Optional[SessionData]) -> None:
        self.__session_data = value

    def to_dictionary(self) -> dict:
        dictionary = super(CreateHostedFieldsSessionResponse, self).to_dictionary()
        if self.sdk_sri is not None:
            dictionary['sdkSri'] = self.sdk_sri
        if self.sdk_url is not None:
            dictionary['sdkUrl'] = self.sdk_url
        if self.session_data is not None:
            dictionary['sessionData'] = self.session_data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreateHostedFieldsSessionResponse':
        super(CreateHostedFieldsSessionResponse, self).from_dictionary(dictionary)
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
