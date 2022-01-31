# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.value_mapping_element import ValueMappingElement


class PaymentProductFieldFormElement(DataObject):
    """
    | Object detailing the type of form element that should be used to present the field
    """

    __type = None
    __value_mapping = None

    @property
    def type(self) -> str:
        """
        | Type of form element to be used. The following types can be returned:
        | * text - A normal text input field
        | * list - A list of values that the customer needs to choose from, is detailed in the valueMapping array
        | * currency - Currency fields should be split into two fields, with the second one being specifically for the cents
        | * boolean - Boolean fields should offer the customer a choice, like accepting the terms and conditions of a product.
        | * date - let the customer pick a date.

        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: str):
        self.__type = value

    @property
    def value_mapping(self) -> List[ValueMappingElement]:
        """
        | Deprecated: This field is not used by any payment product

        Type: list[:class:`onlinepayments.sdk.domain.value_mapping_element.ValueMappingElement`]
        """
        return self.__value_mapping

    @value_mapping.setter
    def value_mapping(self, value: List[ValueMappingElement]):
        self.__value_mapping = value

    def to_dictionary(self):
        dictionary = super(PaymentProductFieldFormElement, self).to_dictionary()
        if self.type is not None:
            dictionary['type'] = self.type
        if self.value_mapping is not None:
            dictionary['valueMapping'] = []
            for element in self.value_mapping:
                if element is not None:
                    dictionary['valueMapping'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFieldFormElement, self).from_dictionary(dictionary)
        if 'type' in dictionary:
            self.type = dictionary['type']
        if 'valueMapping' in dictionary:
            if not isinstance(dictionary['valueMapping'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['valueMapping']))
            self.value_mapping = []
            for element in dictionary['valueMapping']:
                value = ValueMappingElement()
                self.value_mapping.append(value.from_dictionary(element))
        return self
