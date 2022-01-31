# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PaymentProductFieldTooltip(DataObject):
    """
    | Object that contains an optional tooltip to assist the customer
    """

    __image = None
    __label = None

    @property
    def image(self) -> str:
        """
        | Deprecated: This field is not used by any payment product
        | Relative URL that can be used to retrieve an image for the tooltip image.

        Type: str
        """
        return self.__image

    @image.setter
    def image(self, value: str):
        self.__image = value

    @property
    def label(self) -> str:
        """
        | A text explaining the field in more detail. This is meant to be used for displaying to the customer.

        Type: str
        """
        return self.__label

    @label.setter
    def label(self, value: str):
        self.__label = value

    def to_dictionary(self):
        dictionary = super(PaymentProductFieldTooltip, self).to_dictionary()
        if self.image is not None:
            dictionary['image'] = self.image
        if self.label is not None:
            dictionary['label'] = self.label
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFieldTooltip, self).from_dictionary(dictionary)
        if 'image' in dictionary:
            self.image = dictionary['image']
        if 'label' in dictionary:
            self.label = dictionary['label']
        return self
