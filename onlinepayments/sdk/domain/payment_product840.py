# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PaymentProduct840(DataObject):
    """
    | Contains the third party data for payment product 840 (PayPal)
    """

    __order_id = None

    @property
    def order_id(self) -> str:
        """
        | Contains an identifier supplied by PayPal which must be provided to the PayPal JavaScript SDK.

        Type: str
        """
        return self.__order_id

    @order_id.setter
    def order_id(self, value: str):
        self.__order_id = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct840, self).to_dictionary()
        if self.order_id is not None:
            dictionary['orderId'] = self.order_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct840, self).from_dictionary(dictionary)
        if 'orderId' in dictionary:
            self.order_id = dictionary['orderId']
        return self
