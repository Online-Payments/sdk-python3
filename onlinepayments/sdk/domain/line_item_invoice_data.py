# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class LineItemInvoiceData(DataObject):
    """
    | Object containing the line items of the invoice or shopping cart
    """

    __description = None

    @property
    def description(self) -> str:
        """
        | Shopping cart item description

        Type: str
        """
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value

    def to_dictionary(self):
        dictionary = super(LineItemInvoiceData, self).to_dictionary()
        if self.description is not None:
            dictionary['description'] = self.description
        return dictionary

    def from_dictionary(self, dictionary):
        super(LineItemInvoiceData, self).from_dictionary(dictionary)
        if 'description' in dictionary:
            self.description = dictionary['description']
        return self
