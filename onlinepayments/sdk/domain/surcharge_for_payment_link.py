# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class SurchargeForPaymentLink(DataObject):
    """
    | Object containing details how surcharge will be applied to a payment link.
    """

    __surcharge_mode = None

    @property
    def surcharge_mode(self) -> str:
        """
        | The surcharge mode which defines how a merchant will apply surcharging.
        | * pass-through - Merchant to define and apply surcharge amount for a transaction for processing. This mode is not supported on Create Hosted Checkout Session.
        | * on-behalf-of - Merchant to instruct the payment platform to calculate and apply a surcharge amount to a transaction, based on the merchant’s surcharge configuration, net amount, and payment product type.

        Type: str
        """
        return self.__surcharge_mode

    @surcharge_mode.setter
    def surcharge_mode(self, value: str):
        self.__surcharge_mode = value

    def to_dictionary(self):
        dictionary = super(SurchargeForPaymentLink, self).to_dictionary()
        if self.surcharge_mode is not None:
            dictionary['surchargeMode'] = self.surcharge_mode
        return dictionary

    def from_dictionary(self, dictionary):
        super(SurchargeForPaymentLink, self).from_dictionary(dictionary)
        if 'surchargeMode' in dictionary:
            self.surcharge_mode = dictionary['surchargeMode']
        return self
