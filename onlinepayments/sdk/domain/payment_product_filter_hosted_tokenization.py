# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject


class PaymentProductFilterHostedTokenization(DataObject):
    """
    | The payment product ids to be be excluded or restricted to from the payment products available for the payment. Note that you can add exclusions on top of the 'restrictTo' filter.
    """

    __products = None

    @property
    def products(self) -> List[int]:
        """
        | List containing all payment product ids that should either be restricted to in or excluded from the payment context.

        Type: list[int]
        """
        return self.__products

    @products.setter
    def products(self, value: List[int]):
        self.__products = value

    def to_dictionary(self):
        dictionary = super(PaymentProductFilterHostedTokenization, self).to_dictionary()
        if self.products is not None:
            dictionary['products'] = []
            for element in self.products:
                if element is not None:
                    dictionary['products'].append(element)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFilterHostedTokenization, self).from_dictionary(dictionary)
        if 'products' in dictionary:
            if not isinstance(dictionary['products'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['products']))
            self.products = []
            for element in dictionary['products']:
                self.products.append(element)
        return self
