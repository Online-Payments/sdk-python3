# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class OmnichannelPayoutSpecificInput(DataObject):

    __payment_id: Optional[str] = None

    @property
    def payment_id(self) -> Optional[str]:
        """
        | The Payment Id of the transaction (either in-store or online), from which you request to make a refund.

        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: Optional[str]) -> None:
        self.__payment_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(OmnichannelPayoutSpecificInput, self).to_dictionary()
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OmnichannelPayoutSpecificInput':
        super(OmnichannelPayoutSpecificInput, self).from_dictionary(dictionary)
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        return self
