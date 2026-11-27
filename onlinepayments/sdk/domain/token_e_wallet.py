#
# This file was automatically generated.
#
from .customer_token import CustomerToken
from .data_object import DataObject


class TokenEWallet(DataObject):

    __slots__ = (
        "__alias",
        "__customer",
    )

    __alias: str | None
    __customer: CustomerToken | None

    def __init__(
        self,
        *,
        alias: str | None = None,
        customer: CustomerToken | None = None,
    ) -> None:
        self.alias = alias
        self.customer = customer

    @property
    def alias(self) -> str | None:
        """
        | Deprecated: This field is not used by any payment product An alias for the token. This can be used to visually represent the token.

        Type: str

        Deprecated; This field is not used by any payment product An alias for the token. This can be used to visually represent the token.
        """
        return self.__alias

    @alias.setter
    def alias(self, value: str | None) -> None:
        self.__alias = value

    @property
    def customer(self) -> CustomerToken | None:
        """
        Type: :class:`onlinepayments.sdk.domain.customer_token.CustomerToken`
        """
        return self.__customer

    @customer.setter
    def customer(self, value: CustomerToken | None) -> None:
        self.__customer = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.alias is not None:
            dictionary['alias'] = self.alias
        if self.customer is not None:
            dictionary['customer'] = self.customer.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'TokenEWallet':
        super().from_dictionary(dictionary)
        if 'alias' in dictionary:
            self.alias = dictionary['alias']
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = CustomerToken()
            self.customer = value.from_dictionary(dictionary['customer'])
        return self
