# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PaymentProductFieldDisplayElement(DataObject):
    """
    | List of extra data of the value.
    """

    __id = None
    __label = None
    __type = None
    __value = None

    @property
    def id(self) -> str:
        """
        | The ID of the display element.

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value

    @property
    def label(self) -> str:
        """
        | The label of the display element.

        Type: str
        """
        return self.__label

    @label.setter
    def label(self, value: str):
        self.__label = value

    @property
    def type(self) -> str:
        """
        | The type of the display element. Indicates how the value should be presented. Possible values are:
        | * STRING - as plain text
        | * CURRENCY - as an amount in cents displayed with a decimal separator and the currency of the payment
        | * PERCENTAGE - as a number with a percentage sign
        | * INTEGER - as an integer
        | * URI - as a link

        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: str):
        self.__type = value

    @property
    def value(self) -> str:
        """
        | the value of the display element.

        Type: str
        """
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def to_dictionary(self):
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

    def from_dictionary(self, dictionary):
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
