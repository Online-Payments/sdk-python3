# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject
from .payment_product import PaymentProduct


class GetPaymentProductsResponse(DataObject):

    __payment_products: Optional[List[PaymentProduct]] = None

    @property
    def payment_products(self) -> Optional[List[PaymentProduct]]:
        """
        Type: list[:class:`onlinepayments.sdk.domain.payment_product.PaymentProduct`]
        """
        return self.__payment_products

    @payment_products.setter
    def payment_products(self, value: Optional[List[PaymentProduct]]) -> None:
        self.__payment_products = value

    def to_dictionary(self) -> dict:
        dictionary = super(GetPaymentProductsResponse, self).to_dictionary()
        if self.payment_products is not None:
            dictionary['paymentProducts'] = []
            for element in self.payment_products:
                if element is not None:
                    dictionary['paymentProducts'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetPaymentProductsResponse':
        super(GetPaymentProductsResponse, self).from_dictionary(dictionary)
        if 'paymentProducts' in dictionary:
            if not isinstance(dictionary['paymentProducts'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['paymentProducts']))
            self.payment_products = []
            for element in dictionary['paymentProducts']:
                value = PaymentProduct()
                self.payment_products.append(value.from_dictionary(element))
        return self
