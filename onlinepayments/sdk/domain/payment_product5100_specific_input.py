# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct5100SpecificInput(DataObject):

    __brand: Optional[str] = None

    @property
    def brand(self) -> Optional[str]:
        """
        | Indicate whether to use a specific Cpay brand. Brands are configurable at the payment method level. See BackOffice Cpay configuration for allowed values.

        Type: str
        """
        return self.__brand

    @brand.setter
    def brand(self, value: Optional[str]) -> None:
        self.__brand = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct5100SpecificInput, self).to_dictionary()
        if self.brand is not None:
            dictionary['brand'] = self.brand
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct5100SpecificInput':
        super(PaymentProduct5100SpecificInput, self).from_dictionary(dictionary)
        if 'brand' in dictionary:
            self.brand = dictionary['brand']
        return self
