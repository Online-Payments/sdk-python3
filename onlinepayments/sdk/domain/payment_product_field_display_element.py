# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProductFieldDisplayElement(DataObject):

    __id: Optional[str] = None
    __label: Optional[str] = None
    __type: Optional[str] = None
    __value: Optional[str] = None

    @property
    def id(self) -> Optional[str]:
        """
        | The ID of the display element.

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: Optional[str]) -> None:
        self.__id = value

    @property
    def label(self) -> Optional[str]:
        """
        | The label of the display element.

        Type: str
        """
        return self.__label

    @label.setter
    def label(self, value: Optional[str]) -> None:
        self.__label = value

    @property
    def type(self) -> Optional[str]:
        """
        | The type of the display element. Indicates how the value should be presented. Possible values are:
        
        * STRING - as plain text
        * CURRENCY - as an amount in cents displayed with a decimal separator and the currency of the payment
        * PERCENTAGE - as a number with a percentage sign
        * INTEGER - as an integer
        * URI - as a link

        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: Optional[str]) -> None:
        self.__type = value

    @property
    def value(self) -> Optional[str]:
        """
        | the value of the display element.

        Type: str
        """
        return self.__value

    @value.setter
    def value(self, value: Optional[str]) -> None:
        self.__value = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProductFieldDisplayElement, self).to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.label is not None:
            dictionary['label'] = self.label
        if self.type is not None:
            dictionary['type'] = self.type
        if self.value is not None:
            dictionary['value'] = self.value
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductFieldDisplayElement':
        super(PaymentProductFieldDisplayElement, self).from_dictionary(dictionary)
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'label' in dictionary:
            self.label = dictionary['label']
        if 'type' in dictionary:
            self.type = dictionary['type']
        if 'value' in dictionary:
            self.value = dictionary['value']
        return self
