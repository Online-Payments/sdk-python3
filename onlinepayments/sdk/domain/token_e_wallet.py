# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.customer_token import CustomerToken


class TokenEWallet(DataObject):
    """
    | Object containing eWallet details
    """

    __alias = None
    __customer = None

    @property
    def alias(self) -> str:
        """
        | Deprecated: This field is not used by any payment product
        | An alias for the token. This can be used to visually represent the token.

        Type: str
        """
        return self.__alias

    @alias.setter
    def alias(self, value: str):
        self.__alias = value

    @property
    def customer(self) -> CustomerToken:
        """
        Type: :class:`onlinepayments.sdk.domain.customer_token.CustomerToken`
        """
        return self.__customer

    @customer.setter
    def customer(self, value: CustomerToken):
        self.__customer = value

    def to_dictionary(self):
        dictionary = super(TokenEWallet, self).to_dictionary()
        if self.alias is not None:
            dictionary['alias'] = self.alias
        if self.customer is not None:
            dictionary['customer'] = self.customer.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenEWallet, self).from_dictionary(dictionary)
        if 'alias' in dictionary:
            self.alias = dictionary['alias']
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = CustomerToken()
            self.customer = value.from_dictionary(dictionary['customer'])
        return self
