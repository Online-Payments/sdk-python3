# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class ClickToPay(DataObject):

    __is_click_to_pay_payment: Optional[bool] = None

    @property
    def is_click_to_pay_payment(self) -> Optional[bool]:
        """
        | A flag indicating whether the payment is made using Click to Pay

        Type: bool
        """
        return self.__is_click_to_pay_payment

    @is_click_to_pay_payment.setter
    def is_click_to_pay_payment(self, value: Optional[bool]) -> None:
        self.__is_click_to_pay_payment = value

    def to_dictionary(self) -> dict:
        dictionary = super(ClickToPay, self).to_dictionary()
        if self.is_click_to_pay_payment is not None:
            dictionary['IsClickToPayPayment'] = self.is_click_to_pay_payment
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ClickToPay':
        super(ClickToPay, self).from_dictionary(dictionary)
        if 'IsClickToPayPayment' in dictionary:
            self.is_click_to_pay_payment = dictionary['IsClickToPayPayment']
        return self
