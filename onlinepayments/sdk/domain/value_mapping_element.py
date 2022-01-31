# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payment_product_field_display_element import PaymentProductFieldDisplayElement


class ValueMappingElement(DataObject):
    """
    | An array of values and displayNames that should be used to populate the list object in the GUI
    """

    __display_elements = None
    __value = None

    @property
    def display_elements(self) -> List[PaymentProductFieldDisplayElement]:
        """
        Type: list[:class:`onlinepayments.sdk.domain.payment_product_field_display_element.PaymentProductFieldDisplayElement`]
        """
        return self.__display_elements

    @display_elements.setter
    def display_elements(self, value: List[PaymentProductFieldDisplayElement]):
        self.__display_elements = value

    @property
    def value(self) -> str:
        """
        | Value corresponding to the key

        Type: str
        """
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def to_dictionary(self):
        dictionary = super(ValueMappingElement, self).to_dictionary()
        if self.display_elements is not None:
            dictionary['displayElements'] = []
            for element in self.display_elements:
                if element is not None:
                    dictionary['displayElements'].append(element.to_dictionary())
        if self.value is not None:
            dictionary['value'] = self.value
        return dictionary

    def from_dictionary(self, dictionary):
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
