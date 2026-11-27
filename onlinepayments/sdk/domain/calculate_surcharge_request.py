#
# This file was automatically generated.
#
from .amount_of_money import AmountOfMoney
from .card_source import CardSource
from .data_object import DataObject


class CalculateSurchargeRequest(DataObject):

    __slots__ = (
        "__amount_of_money",
        "__card_source",
    )

    __amount_of_money: AmountOfMoney | None
    __card_source: CardSource | None

    def __init__(
        self,
        *,
        amount_of_money: AmountOfMoney | None = None,
        card_source: CardSource | None = None,
    ) -> None:
        self.amount_of_money = amount_of_money
        self.card_source = card_source

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

    @property
    def card_source(self) -> CardSource | None:
        """
        | Contains elements from which card number can be obtained.

        Type: :class:`onlinepayments.sdk.domain.card_source.CardSource`
        """
        return self.__card_source

    @card_source.setter
    def card_source(self, value: CardSource | None) -> None:
        self.__card_source = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.card_source is not None:
            dictionary['cardSource'] = self.card_source.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CalculateSurchargeRequest':
        super().from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'cardSource' in dictionary:
            if not isinstance(dictionary['cardSource'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardSource']))
            value = CardSource()
            self.card_source = value.from_dictionary(dictionary['cardSource'])
        return self
