#
# This file was automatically generated.
#
from .amount_of_money import AmountOfMoney
from .data_object import DataObject


class SurchargeSpecificInput(DataObject):

    __slots__ = (
        "__mode",
        "__surcharge_amount",
    )

    __mode: str | None
    __surcharge_amount: AmountOfMoney | None

    def __init__(
        self,
        *,
        mode: str | None = None,
        surcharge_amount: AmountOfMoney | None = None,
    ) -> None:
        self.mode = mode
        self.surcharge_amount = surcharge_amount

    @property
    def mode(self) -> str | None:
        """
        | The surcharge mode to be applied to an order.

        Type: str
        """
        return self.__mode

    @mode.setter
    def mode(self, value: str | None) -> None:
        self.__mode = value

    @property
    def surcharge_amount(self) -> AmountOfMoney | None:
        """
        | The surcharge amount of money to be applied to an order given that the merchant is in pass-through mode.

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__surcharge_amount

    @surcharge_amount.setter
    def surcharge_amount(self, value: AmountOfMoney | None) -> None:
        self.__surcharge_amount = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.mode is not None:
            dictionary['mode'] = self.mode
        if self.surcharge_amount is not None:
            dictionary['surchargeAmount'] = self.surcharge_amount.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SurchargeSpecificInput':
        super().from_dictionary(dictionary)
        if 'mode' in dictionary:
            self.mode = dictionary['mode']
        if 'surchargeAmount' in dictionary:
            if not isinstance(dictionary['surchargeAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeAmount']))
            value = AmountOfMoney()
            self.surcharge_amount = value.from_dictionary(dictionary['surchargeAmount'])
        return self
