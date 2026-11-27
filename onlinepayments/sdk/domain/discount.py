#
# This file was automatically generated.
#
from .data_object import DataObject


class Discount(DataObject):

    __slots__ = (
        "__amount",
    )

    __amount: int | None

    def __init__(
        self,
        *,
        amount: int | None = None,
    ) -> None:
        self.amount = amount

    @property
    def amount(self) -> int | None:
        """
        | Amount in the smallest currency unit, i.e.:
        
        * EUR is a 2-decimals currency, the value 1234 will result in EUR 12.34
        * KWD is a 3-decimals currency, the value 1234 will result in KWD 1.234
        * JPY is a zero-decimal currency, the value 1234 will result in JPY 1234

        Type: int
        """
        return self.__amount

    @amount.setter
    def amount(self, value: int | None) -> None:
        self.__amount = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.amount is not None:
            dictionary['amount'] = self.amount
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Discount':
        super().from_dictionary(dictionary)
        if 'amount' in dictionary:
            self.amount = dictionary['amount']
        return self
