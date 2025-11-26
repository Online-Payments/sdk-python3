# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class NetworkTokenEssentials(DataObject):

    __bin: Optional[str] = None
    __country_code: Optional[str] = None
    __network_token: Optional[str] = None
    __network_token_state: Optional[str] = None
    __network_token_used: Optional[bool] = None
    __token_expiry_date: Optional[str] = None

    @property
    def bin(self) -> Optional[str]:
        """
        | The first digits of the network token number from left to right with a minimum of 6 digits.

        Type: str
        """
        return self.__bin

    @bin.setter
    def bin(self, value: Optional[str]) -> None:
        self.__bin = value

    @property
    def country_code(self) -> Optional[str]:
        """
        | ISO 3166-1 alpha-2 country code

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: Optional[str]) -> None:
        self.__country_code = value

    @property
    def network_token(self) -> Optional[str]:
        """
        | The masked Payment Token associated with the Card used for the purchase. Note: This is called Payment Token in the EMVCo documentation.

        Type: str
        """
        return self.__network_token

    @network_token.setter
    def network_token(self, value: Optional[str]) -> None:
        self.__network_token = value

    @property
    def network_token_state(self) -> Optional[str]:
        """
        | Describes the state of the linked network token:
        
        * requested - A Network Token has been requested from the scheme.
        * denied - A Network Token request has been denied from the scheme.
        * active - The linked Network Token is active and can be used for the subsequent payment in the payment series.
        * suspended - The linked Network Token is suspended and can not be used for the subsequent payment in the payment series. Instead PAN details would be used for the subsequent payment in the payment series.
        * deleted - The linked Network Token is deleted and can not be used for the subsequent payment in the payment series. Instead PAN details would be used for the subsequent payment in the payment series.
        * failed - An attempt was made to request a Network Token, but it was not successful.

        Type: str
        """
        return self.__network_token_state

    @network_token_state.setter
    def network_token_state(self, value: Optional[str]) -> None:
        self.__network_token_state = value

    @property
    def network_token_used(self) -> Optional[bool]:
        """
        | Whether or not a network token was used in the transaction

        Type: bool
        """
        return self.__network_token_used

    @network_token_used.setter
    def network_token_used(self, value: Optional[bool]) -> None:
        self.__network_token_used = value

    @property
    def token_expiry_date(self) -> Optional[str]:
        """
        | The expiry date of the network token. Format: MMYY

        Type: str
        """
        return self.__token_expiry_date

    @token_expiry_date.setter
    def token_expiry_date(self, value: Optional[str]) -> None:
        self.__token_expiry_date = value

    def to_dictionary(self) -> dict:
        dictionary = super(NetworkTokenEssentials, self).to_dictionary()
        if self.bin is not None:
            dictionary['bin'] = self.bin
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.network_token is not None:
            dictionary['networkToken'] = self.network_token
        if self.network_token_state is not None:
            dictionary['networkTokenState'] = self.network_token_state
        if self.network_token_used is not None:
            dictionary['networkTokenUsed'] = self.network_token_used
        if self.token_expiry_date is not None:
            dictionary['tokenExpiryDate'] = self.token_expiry_date
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'NetworkTokenEssentials':
        super(NetworkTokenEssentials, self).from_dictionary(dictionary)
        if 'bin' in dictionary:
            self.bin = dictionary['bin']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'networkToken' in dictionary:
            self.network_token = dictionary['networkToken']
        if 'networkTokenState' in dictionary:
            self.network_token_state = dictionary['networkTokenState']
        if 'networkTokenUsed' in dictionary:
            self.network_token_used = dictionary['networkTokenUsed']
        if 'tokenExpiryDate' in dictionary:
            self.token_expiry_date = dictionary['tokenExpiryDate']
        return self
