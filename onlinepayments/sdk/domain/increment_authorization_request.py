#
# This file was automatically generated.
#
from .amount_of_money import AmountOfMoney
from .data_object import DataObject


class IncrementAuthorizationRequest(DataObject):

    __slots__ = (
        "__amount_of_money",
    )

    __amount_of_money: AmountOfMoney | None

    def __init__(
        self,
        *,
        amount_of_money: AmountOfMoney | None = None,
    ) -> None:
        self.amount_of_money = amount_of_money

    @property
    def amount_of_money(self) -> AmountOfMoney | None:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: AmountOfMoney | None) -> None:
        self.__amount_of_money = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'IncrementAuthorizationRequest':
        super().from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        return self
