#
# This file was automatically generated.
#
from .amount_of_money import AmountOfMoney
from .data_object import DataObject


class GiftCardPurchase(DataObject):

    __slots__ = (
        "__amount_of_money",
        "__number_of_gift_cards",
    )

    __amount_of_money: AmountOfMoney | None
    __number_of_gift_cards: int | None

    def __init__(
        self,
        *,
        amount_of_money: AmountOfMoney | None = None,
        number_of_gift_cards: int | None = None,
    ) -> None:
        self.amount_of_money = amount_of_money
        self.number_of_gift_cards = number_of_gift_cards

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
    def number_of_gift_cards(self) -> int | None:
        """
        | Number of gift cards that are purchased through this transaction

        Type: int
        """
        return self.__number_of_gift_cards

    @number_of_gift_cards.setter
    def number_of_gift_cards(self, value: int | None) -> None:
        self.__number_of_gift_cards = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.number_of_gift_cards is not None:
            dictionary['numberOfGiftCards'] = self.number_of_gift_cards
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GiftCardPurchase':
        super().from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'numberOfGiftCards' in dictionary:
            self.number_of_gift_cards = dictionary['numberOfGiftCards']
        return self
