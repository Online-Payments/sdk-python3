# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class OmnichannelPayoutSpecificInput(DataObject):
    """
    | Object containing the additional payout details for a Omnichannel merchants
    """

    __payment_id = None

    @property
    def payment_id(self) -> str:
        """
        | The Payment Id of the transaction (either in-store or online), from which you request to make a refund.

        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: str):
        self.__payment_id = value

    def to_dictionary(self):
        dictionary = super(OmnichannelPayoutSpecificInput, self).to_dictionary()
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(OmnichannelPayoutSpecificInput, self).from_dictionary(dictionary)
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        return self
