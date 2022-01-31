# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PaymentProduct5100SpecificInput(DataObject):
    """
    | Object containing specific input required for Cpay payments.
    """

    __brand = None

    @property
    def brand(self) -> str:
        """
        | Indicate whether to use a specific Cpay brand. Brands are configurable at the payment method level. See BackOffice Cpay configuration for allowed values.

        Type: str
        """
        return self.__brand

    @brand.setter
    def brand(self, value: str):
        self.__brand = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct5100SpecificInput, self).to_dictionary()
        if self.brand is not None:
            dictionary['brand'] = self.brand
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct5100SpecificInput, self).from_dictionary(dictionary)
        if 'brand' in dictionary:
            self.brand = dictionary['brand']
        return self
