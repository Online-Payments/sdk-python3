#
# This file was automatically generated.
#
from .amount_of_money import AmountOfMoney
from .data_object import DataObject


class Transaction(DataObject):

    __slots__ = (
        "__amount",
    )

    __amount: AmountOfMoney | None

    def __init__(
        self,
        *,
        amount: AmountOfMoney | None = None,
    ) -> None:
        self.amount = amount

    @property
    def amount(self) -> AmountOfMoney | None:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount

    @amount.setter
    def amount(self, value: AmountOfMoney | None) -> None:
        self.__amount = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.amount is not None:
            dictionary['amount'] = self.amount.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Transaction':
        super().from_dictionary(dictionary)
        if 'amount' in dictionary:
            if not isinstance(dictionary['amount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amount']))
            value = AmountOfMoney()
            self.amount = value.from_dictionary(dictionary['amount'])
        return self
