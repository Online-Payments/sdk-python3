# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .address_personal import AddressPersonal
from .data_object import DataObject


class PaymentProduct3203SpecificOutput(DataObject):

    __billing_address: Optional[AddressPersonal] = None
    __shipping_address: Optional[AddressPersonal] = None

    @property
    def billing_address(self) -> Optional[AddressPersonal]:
        """
        | Object containing address information

        Type: :class:`onlinepayments.sdk.domain.address_personal.AddressPersonal`
        """
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value: Optional[AddressPersonal]) -> None:
        self.__billing_address = value

    @property
    def shipping_address(self) -> Optional[AddressPersonal]:
        """
        | Object containing address information

        Type: :class:`onlinepayments.sdk.domain.address_personal.AddressPersonal`
        """
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, value: Optional[AddressPersonal]) -> None:
        self.__shipping_address = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct3203SpecificOutput, self).to_dictionary()
        if self.billing_address is not None:
            dictionary['billingAddress'] = self.billing_address.to_dictionary()
        if self.shipping_address is not None:
            dictionary['shippingAddress'] = self.shipping_address.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct3203SpecificOutput':
        super(PaymentProduct3203SpecificOutput, self).from_dictionary(dictionary)
        if 'billingAddress' in dictionary:
            if not isinstance(dictionary['billingAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['billingAddress']))
            value = AddressPersonal()
            self.billing_address = value.from_dictionary(dictionary['billingAddress'])
        if 'shippingAddress' in dictionary:
            if not isinstance(dictionary['shippingAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['shippingAddress']))
            value = AddressPersonal()
            self.shipping_address = value.from_dictionary(dictionary['shippingAddress'])
        return self
