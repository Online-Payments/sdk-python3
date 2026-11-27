#
# This file was automatically generated.
#
from .data_object import DataObject


class ClickToPay(DataObject):

    __slots__ = (
        "__is_click_to_pay_payment",
    )

    __is_click_to_pay_payment: bool | None

    def __init__(
        self,
        *,
        is_click_to_pay_payment: bool | None = None,
    ) -> None:
        self.is_click_to_pay_payment = is_click_to_pay_payment

    @property
    def is_click_to_pay_payment(self) -> bool | None:
        """
        | A flag indicating whether the payment is made using Click to Pay

        Type: bool
        """
        return self.__is_click_to_pay_payment

    @is_click_to_pay_payment.setter
    def is_click_to_pay_payment(self, value: bool | None) -> None:
        self.__is_click_to_pay_payment = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.is_click_to_pay_payment is not None:
            dictionary['IsClickToPayPayment'] = self.is_click_to_pay_payment
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ClickToPay':
        super().from_dictionary(dictionary)
        if 'IsClickToPayPayment' in dictionary:
            self.is_click_to_pay_payment = dictionary['IsClickToPayPayment']
        return self
