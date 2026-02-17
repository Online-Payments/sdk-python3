# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct840(DataObject):

    __order_id: Optional[str] = None

    @property
    def order_id(self) -> Optional[str]:
        """
        | Contains an identifier supplied by PayPal which must be provided to the PayPal JavaScript SDK.

        Type: str
        """
        return self.__order_id

    @order_id.setter
    def order_id(self, value: Optional[str]) -> None:
        self.__order_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct840, self).to_dictionary()
        if self.order_id is not None:
            dictionary['orderId'] = self.order_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct840':
        super(PaymentProduct840, self).from_dictionary(dictionary)
        if 'orderId' in dictionary:
            self.order_id = dictionary['orderId']
        return self
