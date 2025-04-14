# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .payment_response import PaymentResponse


class SubsequentPaymentResponse(DataObject):

    __payment: Optional[PaymentResponse] = None

    @property
    def payment(self) -> Optional[PaymentResponse]:
        """
        | Object that holds the payment related properties

        Type: :class:`onlinepayments.sdk.domain.payment_response.PaymentResponse`
        """
        return self.__payment

    @payment.setter
    def payment(self, value: Optional[PaymentResponse]) -> None:
        self.__payment = value

    def to_dictionary(self) -> dict:
        dictionary = super(SubsequentPaymentResponse, self).to_dictionary()
        if self.payment is not None:
            dictionary['payment'] = self.payment.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SubsequentPaymentResponse':
        super(SubsequentPaymentResponse, self).from_dictionary(dictionary)
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = PaymentResponse()
            self.payment = value.from_dictionary(dictionary['payment'])
        return self
