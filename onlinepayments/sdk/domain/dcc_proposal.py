#
# This file was automatically generated.
#
from .amount_of_money import AmountOfMoney
from .data_object import DataObject
from .rate_details import RateDetails


class DccProposal(DataObject):

    __slots__ = (
        "__base_amount",
        "__disclaimer_display",
        "__disclaimer_receipt",
        "__rate",
        "__target_amount",
    )

    __base_amount: AmountOfMoney | None
    __disclaimer_display: str | None
    __disclaimer_receipt: str | None
    __rate: RateDetails | None
    __target_amount: AmountOfMoney | None

    def __init__(
        self,
        *,
        base_amount: AmountOfMoney | None = None,
        disclaimer_display: str | None = None,
        disclaimer_receipt: str | None = None,
        rate: RateDetails | None = None,
        target_amount: AmountOfMoney | None = None,
    ) -> None:
        self.base_amount = base_amount
        self.disclaimer_display = disclaimer_display
        self.disclaimer_receipt = disclaimer_receipt
        self.rate = rate
        self.target_amount = target_amount

    @property
    def base_amount(self) -> AmountOfMoney | None:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__base_amount

    @base_amount.setter
    def base_amount(self, value: AmountOfMoney | None) -> None:
        self.__base_amount = value

    @property
    def disclaimer_display(self) -> str | None:
        """
        | Card scheme disclaimer to present to the cardholder

        Type: str
        """
        return self.__disclaimer_display

    @disclaimer_display.setter
    def disclaimer_display(self, value: str | None) -> None:
        self.__disclaimer_display = value

    @property
    def disclaimer_receipt(self) -> str | None:
        """
        | Card scheme disclaimer to print within cardholder receipt

        Type: str
        """
        return self.__disclaimer_receipt

    @disclaimer_receipt.setter
    def disclaimer_receipt(self, value: str | None) -> None:
        self.__disclaimer_receipt = value

    @property
    def rate(self) -> RateDetails | None:
        """
        | Rate details given by the Dynamic Currency Conversion(DCC) provider

        Type: :class:`onlinepayments.sdk.domain.rate_details.RateDetails`
        """
        return self.__rate

    @rate.setter
    def rate(self, value: RateDetails | None) -> None:
        self.__rate = value

    @property
    def target_amount(self) -> AmountOfMoney | None:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__target_amount

    @target_amount.setter
    def target_amount(self, value: AmountOfMoney | None) -> None:
        self.__target_amount = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.base_amount is not None:
            dictionary['baseAmount'] = self.base_amount.to_dictionary()
        if self.disclaimer_display is not None:
            dictionary['disclaimerDisplay'] = self.disclaimer_display
        if self.disclaimer_receipt is not None:
            dictionary['disclaimerReceipt'] = self.disclaimer_receipt
        if self.rate is not None:
            dictionary['rate'] = self.rate.to_dictionary()
        if self.target_amount is not None:
            dictionary['targetAmount'] = self.target_amount.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DccProposal':
        super().from_dictionary(dictionary)
        if 'baseAmount' in dictionary:
            if not isinstance(dictionary['baseAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['baseAmount']))
            value = AmountOfMoney()
            self.base_amount = value.from_dictionary(dictionary['baseAmount'])
        if 'disclaimerDisplay' in dictionary:
            self.disclaimer_display = dictionary['disclaimerDisplay']
        if 'disclaimerReceipt' in dictionary:
            self.disclaimer_receipt = dictionary['disclaimerReceipt']
        if 'rate' in dictionary:
            if not isinstance(dictionary['rate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['rate']))
            value = RateDetails()
            self.rate = value.from_dictionary(dictionary['rate'])
        if 'targetAmount' in dictionary:
            if not isinstance(dictionary['targetAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['targetAmount']))
            value = AmountOfMoney()
            self.target_amount = value.from_dictionary(dictionary['targetAmount'])
        return self
