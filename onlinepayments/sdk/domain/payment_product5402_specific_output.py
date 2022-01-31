# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PaymentProduct5402SpecificOutput(DataObject):
    """
    | Meal vouchers (payment product 5402) specific details
    """

    __brand = None

    @property
    def brand(self) -> str:
        """
        | The specific meal voucher brand used for the transaction

        Type: str
        """
        return self.__brand

    @brand.setter
    def brand(self, value: str):
        self.__brand = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct5402SpecificOutput, self).to_dictionary()
        if self.brand is not None:
            dictionary['brand'] = self.brand
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct5402SpecificOutput, self).from_dictionary(dictionary)
        if 'brand' in dictionary:
            self.brand = dictionary['brand']
        return self
