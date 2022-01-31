# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.external_token_linked import ExternalTokenLinked
from onlinepayments.sdk.domain.token_card import TokenCard
from onlinepayments.sdk.domain.token_e_wallet import TokenEWallet


class TokenResponse(DataObject):
    __card = None
    __e_wallet = None
    __external_token_linked = None
    __id = None
    __is_temporary = None
    __payment_product_id = None

    @property
    def card(self) -> TokenCard:
        """
        | Object containing card details

        Type: :class:`onlinepayments.sdk.domain.token_card.TokenCard`
        """
        return self.__card

    @card.setter
    def card(self, value: TokenCard):
        self.__card = value

    @property
    def e_wallet(self) -> TokenEWallet:
        """
        | Object containing eWallet details

        Type: :class:`onlinepayments.sdk.domain.token_e_wallet.TokenEWallet`
        """
        return self.__e_wallet

    @e_wallet.setter
    def e_wallet(self, value: TokenEWallet):
        self.__e_wallet = value

    @property
    def external_token_linked(self) -> ExternalTokenLinked:
        """
        Type: :class:`onlinepayments.sdk.domain.external_token_linked.ExternalTokenLinked`
        """
        return self.__external_token_linked

    @external_token_linked.setter
    def external_token_linked(self, value: ExternalTokenLinked):
        self.__external_token_linked = value

    @property
    def id(self) -> str:
        """
        | ID of the token

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value

    @property
    def is_temporary(self) -> bool:
        """
        | Temporary tokens have a lifespan of two hours and can only be used once.

        Type: bool
        """
        return self.__is_temporary

    @is_temporary.setter
    def is_temporary(self, value: bool):
        self.__is_temporary = value

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
        dictionary = super(TokenResponse, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.e_wallet is not None:
            dictionary['eWallet'] = self.e_wallet.to_dictionary()
        if self.external_token_linked is not None:
            dictionary['externalTokenLinked'] = self.external_token_linked.to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.is_temporary is not None:
            dictionary['isTemporary'] = self.is_temporary
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenResponse, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = TokenCard()
            self.card = value.from_dictionary(dictionary['card'])
        if 'eWallet' in dictionary:
            if not isinstance(dictionary['eWallet'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['eWallet']))
            value = TokenEWallet()
            self.e_wallet = value.from_dictionary(dictionary['eWallet'])
        if 'externalTokenLinked' in dictionary:
            if not isinstance(dictionary['externalTokenLinked'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['externalTokenLinked']))
            value = ExternalTokenLinked()
            self.external_token_linked = value.from_dictionary(dictionary['externalTokenLinked'])
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'isTemporary' in dictionary:
            self.is_temporary = dictionary['isTemporary']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
