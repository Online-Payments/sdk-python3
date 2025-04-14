# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject


class PaymentProductFilter(DataObject):

    __groups: Optional[List[str]] = None
    __products: Optional[List[int]] = None

    @property
    def groups(self) -> Optional[List[str]]:
        """
        | List containing all payment product groups that should either be restricted to in or excluded from the payment context. Currently, there is only one group, called 'cards'.

        Type: list[str]
        """
        return self.__groups

    @groups.setter
    def groups(self, value: Optional[List[str]]) -> None:
        self.__groups = value

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
        dictionary = super(PaymentProductFilter, self).to_dictionary()
        if self.groups is not None:
            dictionary['groups'] = []
            for element in self.groups:
                if element is not None:
                    dictionary['groups'].append(element)
        if self.products is not None:
            dictionary['products'] = []
            for element in self.products:
                if element is not None:
                    dictionary['products'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductFilter':
        super(PaymentProductFilter, self).from_dictionary(dictionary)
        if 'groups' in dictionary:
            if not isinstance(dictionary['groups'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['groups']))
            self.groups = []
            for element in dictionary['groups']:
                self.groups.append(element)
        if 'products' in dictionary:
            if not isinstance(dictionary['products'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['products']))
            self.products = []
            for element in dictionary['products']:
                self.products.append(element)
        return self
