#
# This file was automatically generated.
#
from .data_object import DataObject


class LineItemDetail(DataObject):

    __slots__ = (
        "__discount_amount",
        "__line_item_id",
        "__quantity",
    )

    __discount_amount: int | None
    __line_item_id: str | None
    __quantity: int | None

    def __init__(
        self,
        *,
        discount_amount: int | None = None,
        line_item_id: str | None = None,
        quantity: int | None = None,
    ) -> None:
        self.discount_amount = discount_amount
        self.line_item_id = line_item_id
        self.quantity = quantity

    @property
    def discount_amount(self) -> int | None:
        """
        | Amount in the smallest currency unit, i.e.:
        
        * EUR is a 2-decimals currency, the value 1234 will result in EUR 12.34
        * KWD is a 3-decimals currency, the value 1234 will result in KWD 1.234
        * JPY is a zero-decimal currency, the value 1234 will result in JPY 1234

        Type: int
        """
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, value: int | None) -> None:
        self.__discount_amount = value

    @property
    def line_item_id(self) -> str | None:
        """
        | The unique ID for each line item.

        Type: str
        """
        return self.__line_item_id

    @line_item_id.setter
    def line_item_id(self, value: str | None) -> None:
        self.__line_item_id = value

    @property
    def quantity(self) -> int | None:
        """
        | Quantity of the units being purchased, should be greater than zero Note: Must not be all spaces or all zeros

        Type: int
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int | None) -> None:
        self.__quantity = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.discount_amount is not None:
            dictionary['discountAmount'] = self.discount_amount
        if self.line_item_id is not None:
            dictionary['lineItemId'] = self.line_item_id
        if self.quantity is not None:
            dictionary['quantity'] = self.quantity
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'LineItemDetail':
        super().from_dictionary(dictionary)
        if 'discountAmount' in dictionary:
            self.discount_amount = dictionary['discountAmount']
        if 'lineItemId' in dictionary:
            self.line_item_id = dictionary['lineItemId']
        if 'quantity' in dictionary:
            self.quantity = dictionary['quantity']
        return self
