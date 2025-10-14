# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .token_card_specific_input import TokenCardSpecificInput


class CreateTokenRequest(DataObject):

    __card: Optional[TokenCardSpecificInput] = None
    __encrypted_customer_input: Optional[str] = None
    __payment_product_id: Optional[int] = None

    @property
    def card(self) -> Optional[TokenCardSpecificInput]:
        """
        | Object containing the token details for a card

        Type: :class:`onlinepayments.sdk.domain.token_card_specific_input.TokenCardSpecificInput`
        """
        return self.__card

    @card.setter
    def card(self, value: Optional[TokenCardSpecificInput]) -> None:
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
    def payment_product_id(self) -> Optional[int]:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: Optional[int]) -> None:
        self.__payment_product_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(CreateTokenRequest, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.encrypted_customer_input is not None:
            dictionary['encryptedCustomerInput'] = self.encrypted_customer_input
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreateTokenRequest':
        super(CreateTokenRequest, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = TokenCardSpecificInput()
            self.card = value.from_dictionary(dictionary['card'])
        if 'encryptedCustomerInput' in dictionary:
            self.encrypted_customer_input = dictionary['encryptedCustomerInput']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
