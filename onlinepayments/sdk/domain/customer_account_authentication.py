# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CustomerAccountAuthentication(DataObject):

    __data: Optional[str] = None
    __method: Optional[str] = None
    __utc_timestamp: Optional[str] = None

    @property
    def data(self) -> Optional[str]:
        """
        | Data about the authentication procedure of the customer to their account with you

        Type: str
        """
        return self.__data

    @data.setter
    def data(self, value: Optional[str]) -> None:
        self.__data = value

    @property
    def method(self) -> Optional[str]:
        """
        | Authentication used by the customer on your website Possible values are
        
        * guest = no login occurred, customer is logged in as guest
        * merchant-credentials = the customer logged in using credentials that are specific to you
        * federated-id = the customer logged in using a federated ID
        * issuer-credentials = the customer logged in using credentials from the card issuer (of the card used in this transaction)
        * third-party-authentication = the customer logged in using third-party authentication
        * fido-authentication = the customer logged in using a FIDO authenticator
        * cico-b-connect-token = the customer logged in using Check-in/Check-out b.connect

        Type: str
        """
        return self.__method

    @method.setter
    def method(self, value: Optional[str]) -> None:
        self.__method = value

    @property
    def utc_timestamp(self) -> Optional[str]:
        """
        | Timestamp (YYYYMMDDHHmm) of the authentication of the customer to their account with you

        Type: str
        """
        return self.__utc_timestamp

    @utc_timestamp.setter
    def utc_timestamp(self, value: Optional[str]) -> None:
        self.__utc_timestamp = value

    def to_dictionary(self) -> dict:
        dictionary = super(CustomerAccountAuthentication, self).to_dictionary()
        if self.data is not None:
            dictionary['data'] = self.data
        if self.method is not None:
            dictionary['method'] = self.method
        if self.utc_timestamp is not None:
            dictionary['utcTimestamp'] = self.utc_timestamp
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CustomerAccountAuthentication':
        super(CustomerAccountAuthentication, self).from_dictionary(dictionary)
        if 'data' in dictionary:
            self.data = dictionary['data']
        if 'method' in dictionary:
            self.method = dictionary['method']
        if 'utcTimestamp' in dictionary:
            self.utc_timestamp = dictionary['utcTimestamp']
        return self
