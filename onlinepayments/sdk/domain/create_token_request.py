# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.token_card_specific_input import TokenCardSpecificInput


class CreateTokenRequest(DataObject):
    """
    | Object containing the token details
    """

    __card = None
    __payment_product_id = None

    @property
    def card(self) -> TokenCardSpecificInput:
        """
        | Object containing the token details for a card

        Type: :class:`onlinepayments.sdk.domain.token_card_specific_input.TokenCardSpecificInput`
        """
        return self.__card

    @card.setter
    def card(self, value: TokenCardSpecificInput):
        self.__card = value

    @property
    def payment_product_id(self) -> int:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: int):
        self.__payment_product_id = value

    def to_dictionary(self):
        dictionary = super(CreateTokenRequest, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateTokenRequest, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = TokenCardSpecificInput()
            self.card = value.from_dictionary(dictionary['card'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
