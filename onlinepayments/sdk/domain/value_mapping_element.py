# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject
from .payment_product_field_display_element import PaymentProductFieldDisplayElement


class ValueMappingElement(DataObject):

    __display_elements: Optional[List[PaymentProductFieldDisplayElement]] = None
    __value: Optional[str] = None

    @property
    def display_elements(self) -> Optional[List[PaymentProductFieldDisplayElement]]:
        """
        Type: list[:class:`onlinepayments.sdk.domain.payment_product_field_display_element.PaymentProductFieldDisplayElement`]
        """
        return self.__display_elements

    @display_elements.setter
    def display_elements(self, value: Optional[List[PaymentProductFieldDisplayElement]]) -> None:
        self.__display_elements = value

    @property
    def value(self) -> Optional[str]:
        """
        | Value corresponding to the key

        Type: str
        """
        return self.__value

    @value.setter
    def value(self, value: Optional[str]) -> None:
        self.__value = value

    def to_dictionary(self) -> dict:
        dictionary = super(ValueMappingElement, self).to_dictionary()
        if self.display_elements is not None:
            dictionary['displayElements'] = []
            for element in self.display_elements:
                if element is not None:
                    dictionary['displayElements'].append(element.to_dictionary())
        if self.value is not None:
            dictionary['value'] = self.value
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ValueMappingElement':
        super(ValueMappingElement, self).from_dictionary(dictionary)
        if 'displayElements' in dictionary:
            if not isinstance(dictionary['displayElements'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['displayElements']))
            self.display_elements = []
            for element in dictionary['displayElements']:
                value = PaymentProductFieldDisplayElement()
                self.display_elements.append(value.from_dictionary(element))
        if 'value' in dictionary:
            self.value = dictionary['value']
        return self
