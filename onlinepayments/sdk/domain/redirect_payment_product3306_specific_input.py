# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class RedirectPaymentProduct3306SpecificInput(DataObject):
    """
    | Object containing specific input required for Klarna payments (Payment product ID 3306)
    """

    __extra_merchant_data = None

    @property
    def extra_merchant_data(self) -> str:
        """
        | In some cases, Klarna require additional information regarding the customer and the purchase in order to make 
        | a correct risk assessment. This information, called extra merchant data (EMD), may consist of data 
        | about the customer performing the transaction, the product/services associated with the transaction, 
        | or the seller and their affiliates.

        Type: str
        """
        return self.__extra_merchant_data

    @extra_merchant_data.setter
    def extra_merchant_data(self, value: str):
        self.__extra_merchant_data = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct3306SpecificInput, self).to_dictionary()
        if self.extra_merchant_data is not None:
            dictionary['extraMerchantData'] = self.extra_merchant_data
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct3306SpecificInput, self).from_dictionary(dictionary)
        if 'extraMerchantData' in dictionary:
            self.extra_merchant_data = dictionary['extraMerchantData']
        return self
