# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class RedirectPaymentProduct809SpecificInput(DataObject):
    """
    | Object containing specific input required for iDeal payments (Payment product ID 809)
    """

    __issuer_id = None

    @property
    def issuer_id(self) -> str:
        """
        | Unique ID of the issuing bank of the customer

        Type: str
        """
        return self.__issuer_id

    @issuer_id.setter
    def issuer_id(self, value: str):
        self.__issuer_id = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct809SpecificInput, self).to_dictionary()
        if self.issuer_id is not None:
            dictionary['issuerId'] = self.issuer_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct809SpecificInput, self).from_dictionary(dictionary)
        if 'issuerId' in dictionary:
            self.issuer_id = dictionary['issuerId']
        return self
