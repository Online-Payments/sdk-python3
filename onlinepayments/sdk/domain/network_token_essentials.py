# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class NetworkTokenEssentials(DataObject):
    """
    | Object containing network token details
    """

    __bin = None
    __country_code = None
    __network_token = None
    __token_expiry_date = None

    @property
    def bin(self) -> str:
        """
        | The first digits of the network token number from left to right with a minimum of 6 digits.

        Type: str
        """
        return self.__bin

    @bin.setter
    def bin(self, value: str):
        self.__bin = value

    @property
    def country_code(self) -> str:
        """
        | ISO 3166-1 alpha-2 country code

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: str):
        self.__country_code = value

    @property
    def network_token(self) -> str:
        """
        | The masked Payment Token associated with the Card used for the purchase. 
        | Note: This is called Payment Token in the EMVCo documentation.

        Type: str
        """
        return self.__network_token

    @network_token.setter
    def network_token(self, value: str):
        self.__network_token = value

    @property
    def token_expiry_date(self) -> str:
        """
        | The expiry date of the network token.
        | Format: MMYY

        Type: str
        """
        return self.__token_expiry_date

    @token_expiry_date.setter
    def token_expiry_date(self, value: str):
        self.__token_expiry_date = value

    def to_dictionary(self):
        dictionary = super(NetworkTokenEssentials, self).to_dictionary()
        if self.bin is not None:
            dictionary['bin'] = self.bin
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.network_token is not None:
            dictionary['networkToken'] = self.network_token
        if self.token_expiry_date is not None:
            dictionary['tokenExpiryDate'] = self.token_expiry_date
        return dictionary

    def from_dictionary(self, dictionary):
        super(NetworkTokenEssentials, self).from_dictionary(dictionary)
        if 'bin' in dictionary:
            self.bin = dictionary['bin']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'networkToken' in dictionary:
            self.network_token = dictionary['networkToken']
        if 'tokenExpiryDate' in dictionary:
            self.token_expiry_date = dictionary['tokenExpiryDate']
        return self
