#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProduct3013SpecificInput(DataObject):

    __slots__ = (
        "__market_number",
        "__purchasing_buyer_reference1",
        "__purchasing_buyer_reference2",
    )

    __market_number: str | None
    __purchasing_buyer_reference1: str | None
    __purchasing_buyer_reference2: str | None

    def __init__(
        self,
        *,
        market_number: str | None = None,
        purchasing_buyer_reference1: str | None = None,
        purchasing_buyer_reference2: str | None = None,
    ) -> None:
        self.market_number = market_number
        self.purchasing_buyer_reference1 = purchasing_buyer_reference1
        self.purchasing_buyer_reference2 = purchasing_buyer_reference2

    @property
    def market_number(self) -> str | None:
        """
        | An identifier that refers to the public tender

        Type: str
        """
        return self.__market_number

    @market_number.setter
    def market_number(self, value: str | None) -> None:
        self.__market_number = value

    @property
    def purchasing_buyer_reference1(self) -> str | None:
        """
        | An identifier allocated by the government

        Type: str
        """
        return self.__purchasing_buyer_reference1

    @purchasing_buyer_reference1.setter
    def purchasing_buyer_reference1(self, value: str | None) -> None:
        self.__purchasing_buyer_reference1 = value

    @property
    def purchasing_buyer_reference2(self) -> str | None:
        """
        | An identifier allocated by the government

        Type: str
        """
        return self.__purchasing_buyer_reference2

    @purchasing_buyer_reference2.setter
    def purchasing_buyer_reference2(self, value: str | None) -> None:
        self.__purchasing_buyer_reference2 = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.market_number is not None:
            dictionary['marketNumber'] = self.market_number
        if self.purchasing_buyer_reference1 is not None:
            dictionary['purchasingBuyerReference1'] = self.purchasing_buyer_reference1
        if self.purchasing_buyer_reference2 is not None:
            dictionary['purchasingBuyerReference2'] = self.purchasing_buyer_reference2
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct3013SpecificInput':
        super().from_dictionary(dictionary)
        if 'marketNumber' in dictionary:
            self.market_number = dictionary['marketNumber']
        if 'purchasingBuyerReference1' in dictionary:
            self.purchasing_buyer_reference1 = dictionary['purchasingBuyerReference1']
        if 'purchasingBuyerReference2' in dictionary:
            self.purchasing_buyer_reference2 = dictionary['purchasingBuyerReference2']
        return self
