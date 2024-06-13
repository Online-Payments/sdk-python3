# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PaymentProduct5002SpecificInput(DataObject):
    """
    | Object containing specific input required for Click to Pay payments.
    """

    __checkout_response_signature = None
    __credit_card_brand = None
    __dpa_id = None

    @property
    def checkout_response_signature(self) -> str:
        """
        Type: str
        """
        return self.__checkout_response_signature

    @checkout_response_signature.setter
    def checkout_response_signature(self, value: str):
        self.__checkout_response_signature = value

    @property
    def credit_card_brand(self) -> str:
        """
        Type: str
        """
        return self.__credit_card_brand

    @credit_card_brand.setter
    def credit_card_brand(self, value: str):
        self.__credit_card_brand = value

    @property
    def dpa_id(self) -> str:
        """
        | DPA Identifier provided during onboarding. Registered identifier for the DPA accessing the service.

        Type: str
        """
        return self.__dpa_id

    @dpa_id.setter
    def dpa_id(self, value: str):
        self.__dpa_id = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct5002SpecificInput, self).to_dictionary()
        if self.checkout_response_signature is not None:
            dictionary['checkoutResponseSignature'] = self.checkout_response_signature
        if self.credit_card_brand is not None:
            dictionary['creditCardBrand'] = self.credit_card_brand
        if self.dpa_id is not None:
            dictionary['dpaId'] = self.dpa_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct5002SpecificInput, self).from_dictionary(dictionary)
        if 'checkoutResponseSignature' in dictionary:
            self.checkout_response_signature = dictionary['checkoutResponseSignature']
        if 'creditCardBrand' in dictionary:
            self.credit_card_brand = dictionary['creditCardBrand']
        if 'dpaId' in dictionary:
            self.dpa_id = dictionary['dpaId']
        return self
