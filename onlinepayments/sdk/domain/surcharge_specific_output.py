#
# This file was automatically generated.
#
from .amount_of_money import AmountOfMoney
from .data_object import DataObject
from .surcharge_rate import SurchargeRate


class SurchargeSpecificOutput(DataObject):

    __slots__ = (
        "__mode",
        "__surcharge_amount",
        "__surcharge_rate",
    )

    __mode: str | None
    __surcharge_amount: AmountOfMoney | None
    __surcharge_rate: SurchargeRate | None

    def __init__(
        self,
        *,
        mode: str | None = None,
        surcharge_amount: AmountOfMoney | None = None,
        surcharge_rate: SurchargeRate | None = None,
    ) -> None:
        self.mode = mode
        self.surcharge_amount = surcharge_amount
        self.surcharge_rate = surcharge_rate

    @property
    def mode(self) -> str | None:
        """
        | The surcharge mode applied to an order.

        Type: str
        """
        return self.__mode

    @mode.setter
    def mode(self, value: str | None) -> None:
        self.__mode = value

    @property
    def surcharge_amount(self) -> AmountOfMoney | None:
        """
        | The surcharge amount of money applied to an order.

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__surcharge_amount

    @surcharge_amount.setter
    def surcharge_amount(self, value: AmountOfMoney | None) -> None:
        self.__surcharge_amount = value

    @property
    def surcharge_rate(self) -> SurchargeRate | None:
        """
        | A summary of surcharge details used in the calculation of the surcharge amount.  Null if result = NO_SURCHARGE

        Type: :class:`onlinepayments.sdk.domain.surcharge_rate.SurchargeRate`
        """
        return self.__surcharge_rate

    @surcharge_rate.setter
    def surcharge_rate(self, value: SurchargeRate | None) -> None:
        self.__surcharge_rate = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.mode is not None:
            dictionary['mode'] = self.mode
        if self.surcharge_amount is not None:
            dictionary['surchargeAmount'] = self.surcharge_amount.to_dictionary()
        if self.surcharge_rate is not None:
            dictionary['surchargeRate'] = self.surcharge_rate.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SurchargeSpecificOutput':
        super().from_dictionary(dictionary)
        if 'mode' in dictionary:
            self.mode = dictionary['mode']
        if 'surchargeAmount' in dictionary:
            if not isinstance(dictionary['surchargeAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeAmount']))
            value = AmountOfMoney()
            self.surcharge_amount = value.from_dictionary(dictionary['surchargeAmount'])
        if 'surchargeRate' in dictionary:
            if not isinstance(dictionary['surchargeRate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeRate']))
            value = SurchargeRate()
            self.surcharge_rate = value.from_dictionary(dictionary['surchargeRate'])
        return self
