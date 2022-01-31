# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payment_product import PaymentProduct


class GetPaymentProductsResponse(DataObject):
    """
    | The response contains an array of payment products that match the filters supplied in the request.
    """

    __payment_products = None

    @property
    def payment_products(self) -> List[PaymentProduct]:
        """
        | Array containing payment products and their characteristics

        Type: list[:class:`onlinepayments.sdk.domain.payment_product.PaymentProduct`]
        """
        return self.__payment_products

    @payment_products.setter
    def payment_products(self, value: List[PaymentProduct]):
        self.__payment_products = value

    def to_dictionary(self):
        dictionary = super(GetPaymentProductsResponse, self).to_dictionary()
        if self.payment_products is not None:
            dictionary['paymentProducts'] = []
            for element in self.payment_products:
                if element is not None:
                    dictionary['paymentProducts'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary):
        super(GetPaymentProductsResponse, self).from_dictionary(dictionary)
        if 'paymentProducts' in dictionary:
            if not isinstance(dictionary['paymentProducts'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['paymentProducts']))
            self.payment_products = []
            for element in dictionary['paymentProducts']:
                value = PaymentProduct()
                self.payment_products.append(value.from_dictionary(element))
        return self
