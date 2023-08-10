# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.card_info import CardInfo


class DccCardSource(DataObject):
    __card = None
    __encrypted_customer_input = None
    __hosted_tokenization_id = None
    __token = None

    @property
    def card(self) -> CardInfo:
        """
        Type: :class:`onlinepayments.sdk.domain.card_info.CardInfo`
        """
        return self.__card

    @card.setter
    def card(self, value: CardInfo):
        self.__card = value

    @property
    def encrypted_customer_input(self) -> str:
        """
        | Data that was encrypted client-side that contains all customer-entered data elements, such as card data.

        Type: str
        """
        return self.__encrypted_customer_input

    @encrypted_customer_input.setter
    def encrypted_customer_input(self, value: str):
        self.__encrypted_customer_input = value

    @property
    def hosted_tokenization_id(self) -> str:
        """
        | An Id of a hosted tokenization session

        Type: str
        """
        return self.__hosted_tokenization_id

    @hosted_tokenization_id.setter
    def hosted_tokenization_id(self, value: str):
        self.__hosted_tokenization_id = value

    @property
    def token(self) -> str:
        """
        | An identifier that represents card details that have previously been stored

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: str):
        self.__token = value

    def to_dictionary(self):
        dictionary = super(DccCardSource, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.encrypted_customer_input is not None:
            dictionary['encryptedCustomerInput'] = self.encrypted_customer_input
        if self.hosted_tokenization_id is not None:
            dictionary['hostedTokenizationId'] = self.hosted_tokenization_id
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary):
        super(DccCardSource, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardInfo()
            self.card = value.from_dictionary(dictionary['card'])
        if 'encryptedCustomerInput' in dictionary:
            self.encrypted_customer_input = dictionary['encryptedCustomerInput']
        if 'hostedTokenizationId' in dictionary:
            self.hosted_tokenization_id = dictionary['hostedTokenizationId']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
