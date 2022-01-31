# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject


class PaymentProductFilter(DataObject):
    """
    | Contains the payment product ids and payment product groups that should be excluded from the payment products available for the payment. Note that excluding a payment product will ensure exclusion, even if the payment product is also present in the restrictTo filter, and that excluding a payment product group will exclude all payment products that are a part of that group, even if one or more of them are present in the restrictTo filters.
    """

    __groups = None
    __products = None

    @property
    def groups(self) -> List[str]:
        """
        | List containing all payment product groups that should either be restricted to in or excluded from the payment context. Currently, there is only one group, called 'cards'.

        Type: list[str]
        """
        return self.__groups

    @groups.setter
    def groups(self, value: List[str]):
        self.__groups = value

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

    def from_dictionary(self, dictionary):
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
