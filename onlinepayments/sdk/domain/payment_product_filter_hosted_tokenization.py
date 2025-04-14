# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject


class PaymentProductFilterHostedTokenization(DataObject):

    __products: Optional[List[int]] = None

    @property
    def products(self) -> Optional[List[int]]:
        """
        Type: list[int]
        """
        return self.__products

    @products.setter
    def products(self, value: Optional[List[int]]) -> None:
        self.__products = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProductFilterHostedTokenization, self).to_dictionary()
        if self.products is not None:
            dictionary['products'] = []
            for element in self.products:
                if element is not None:
                    dictionary['products'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductFilterHostedTokenization':
        super(PaymentProductFilterHostedTokenization, self).from_dictionary(dictionary)
        if 'products' in dictionary:
            if not isinstance(dictionary['products'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['products']))
            self.products = []
            for element in dictionary['products']:
                self.products.append(element)
        return self
