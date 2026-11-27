#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProduct840(DataObject):

    __slots__ = (
        "__order_id",
    )

    __order_id: str | None

    def __init__(
        self,
        *,
        order_id: str | None = None,
    ) -> None:
        self.order_id = order_id

    @property
    def order_id(self) -> str | None:
        """
        | Contains an identifier supplied by PayPal which must be provided to the PayPal JavaScript SDK.

        Type: str
        """
        return self.__order_id

    @order_id.setter
    def order_id(self, value: str | None) -> None:
        self.__order_id = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.order_id is not None:
            dictionary['orderId'] = self.order_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct840':
        super().from_dictionary(dictionary)
        if 'orderId' in dictionary:
            self.order_id = dictionary['orderId']
        return self
