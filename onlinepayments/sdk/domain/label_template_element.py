# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class LabelTemplateElement(DataObject):

    __attribute_key: Optional[str] = None
    __mask: Optional[str] = None

    @property
    def attribute_key(self) -> Optional[str]:
        """
        | Name of the attribute that is shown to the customer on selection pages or screens

        Type: str
        """
        return self.__attribute_key

    @attribute_key.setter
    def attribute_key(self, value: Optional[str]) -> None:
        self.__attribute_key = value

    @property
    def mask(self) -> Optional[str]:
        """
        | Regular mask for the attributeKey Note: The mask is optional as not every field has a mask

        Type: str
        """
        return self.__mask

    @mask.setter
    def mask(self, value: Optional[str]) -> None:
        self.__mask = value

    def to_dictionary(self) -> dict:
        dictionary = super(LabelTemplateElement, self).to_dictionary()
        if self.attribute_key is not None:
            dictionary['attributeKey'] = self.attribute_key
        if self.mask is not None:
            dictionary['mask'] = self.mask
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'LabelTemplateElement':
        super(LabelTemplateElement, self).from_dictionary(dictionary)
        if 'attributeKey' in dictionary:
            self.attribute_key = dictionary['attributeKey']
        if 'mask' in dictionary:
            self.mask = dictionary['mask']
        return self
