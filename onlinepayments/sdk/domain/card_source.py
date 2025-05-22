# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .surcharge_calculation_card import SurchargeCalculationCard


class CardSource(DataObject):

    __card: Optional[SurchargeCalculationCard] = None
    __encrypted_customer_input: Optional[str] = None
    __hosted_tokenization_id: Optional[str] = None
    __token: Optional[str] = None

    @property
    def card(self) -> Optional[SurchargeCalculationCard]:
        """
        | An object containing card number and payment product id, which is used to determine surcharge product type

        Type: :class:`onlinepayments.sdk.domain.surcharge_calculation_card.SurchargeCalculationCard`
        """
        return self.__card

    @card.setter
    def card(self, value: Optional[SurchargeCalculationCard]) -> None:
        self.__card = value

    @property
    def encrypted_customer_input(self) -> Optional[str]:
        """
        | Data that was encrypted client side containing all customer entered data elements like card data. Note: Because this data can only be submitted once to our system and contains encrypted card data you should not store it. As the data was captured within the context of a client session you also need to submit it to us before the session has expired.

        Type: str
        """
        return self.__encrypted_customer_input

    @encrypted_customer_input.setter
    def encrypted_customer_input(self, value: Optional[str]) -> None:
        self.__encrypted_customer_input = value

    @property
    def hosted_tokenization_id(self) -> Optional[str]:
        """
        | An Id of a hosted tokenization session

        Type: str
        """
        return self.__hosted_tokenization_id

    @hosted_tokenization_id.setter
    def hosted_tokenization_id(self, value: Optional[str]) -> None:
        self.__hosted_tokenization_id = value

    @property
    def token(self) -> Optional[str]:
        """
        | An identifier that represents card details that have been previously stored

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: Optional[str]) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super(CardSource, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.encrypted_customer_input is not None:
            dictionary['encryptedCustomerInput'] = self.encrypted_customer_input
        if self.hosted_tokenization_id is not None:
            dictionary['hostedTokenizationId'] = self.hosted_tokenization_id
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardSource':
        super(CardSource, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = SurchargeCalculationCard()
            self.card = value.from_dictionary(dictionary['card'])
        if 'encryptedCustomerInput' in dictionary:
            self.encrypted_customer_input = dictionary['encryptedCustomerInput']
        if 'hostedTokenizationId' in dictionary:
            self.hosted_tokenization_id = dictionary['hostedTokenizationId']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
