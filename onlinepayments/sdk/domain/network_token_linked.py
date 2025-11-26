# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class NetworkTokenLinked(DataObject):

    __expiry_date: Optional[str] = None
    __masked_token: Optional[str] = None
    __token_state: Optional[str] = None

    @property
    def expiry_date(self) -> Optional[str]:
        """
        | The expiry date of the network token. Format: MMYY

        Type: str
        """
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value: Optional[str]) -> None:
        self.__expiry_date = value

    @property
    def masked_token(self) -> Optional[str]:
        """
        | The masked Payment Token associated with the Card used for the purchase. Note: This is called Payment Token in the EMVCo documentation.

        Type: str
        """
        return self.__masked_token

    @masked_token.setter
    def masked_token(self, value: Optional[str]) -> None:
        self.__masked_token = value

    @property
    def token_state(self) -> Optional[str]:
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
        return self.__token_state

    @token_state.setter
    def token_state(self, value: Optional[str]) -> None:
        self.__token_state = value

    def to_dictionary(self) -> dict:
        dictionary = super(NetworkTokenLinked, self).to_dictionary()
        if self.expiry_date is not None:
            dictionary['expiryDate'] = self.expiry_date
        if self.masked_token is not None:
            dictionary['maskedToken'] = self.masked_token
        if self.token_state is not None:
            dictionary['tokenState'] = self.token_state
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'NetworkTokenLinked':
        super(NetworkTokenLinked, self).from_dictionary(dictionary)
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        if 'maskedToken' in dictionary:
            self.masked_token = dictionary['maskedToken']
        if 'tokenState' in dictionary:
            self.token_state = dictionary['tokenState']
        return self
