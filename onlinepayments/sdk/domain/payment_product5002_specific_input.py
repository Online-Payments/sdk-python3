# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct5002SpecificInput(DataObject):

    __checkout_response_signature: Optional[str] = None
    __credit_card_brand: Optional[str] = None

    @property
    def checkout_response_signature(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__checkout_response_signature

    @checkout_response_signature.setter
    def checkout_response_signature(self, value: Optional[str]) -> None:
        self.__checkout_response_signature = value

    @property
    def credit_card_brand(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__credit_card_brand

    @credit_card_brand.setter
    def credit_card_brand(self, value: Optional[str]) -> None:
        self.__credit_card_brand = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct5002SpecificInput, self).to_dictionary()
        if self.checkout_response_signature is not None:
            dictionary['checkoutResponseSignature'] = self.checkout_response_signature
        if self.credit_card_brand is not None:
            dictionary['creditCardBrand'] = self.credit_card_brand
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct5002SpecificInput':
        super(PaymentProduct5002SpecificInput, self).from_dictionary(dictionary)
        if 'checkoutResponseSignature' in dictionary:
            self.checkout_response_signature = dictionary['checkoutResponseSignature']
        if 'creditCardBrand' in dictionary:
            self.credit_card_brand = dictionary['creditCardBrand']
        return self
