# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.address_personal import AddressPersonal


class PaymentProduct3203SpecificOutput(DataObject):
    """
    | PostFinancePay (payment product 3203) specific details
    """

    __billing_address = None
    __shipping_address = None

    @property
    def billing_address(self) -> AddressPersonal:
        """
        | Object containing address information

        Type: :class:`onlinepayments.sdk.domain.address_personal.AddressPersonal`
        """
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value: AddressPersonal):
        self.__billing_address = value

    @property
    def shipping_address(self) -> AddressPersonal:
        """
        | Object containing address information

        Type: :class:`onlinepayments.sdk.domain.address_personal.AddressPersonal`
        """
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, value: AddressPersonal):
        self.__shipping_address = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct3203SpecificOutput, self).to_dictionary()
        if self.billing_address is not None:
            dictionary['billingAddress'] = self.billing_address.to_dictionary()
        if self.shipping_address is not None:
            dictionary['shippingAddress'] = self.shipping_address.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
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
