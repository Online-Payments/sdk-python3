# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .payment_response import PaymentResponse


class CreatedPaymentOutput(DataObject):

    __payment: Optional[PaymentResponse] = None
    __payment_status_category: Optional[str] = None

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

    @property
    def payment_status_category(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__payment_status_category

    @payment_status_category.setter
    def payment_status_category(self, value: Optional[str]) -> None:
        self.__payment_status_category = value

    def to_dictionary(self) -> dict:
        dictionary = super(CreatedPaymentOutput, self).to_dictionary()
        if self.payment is not None:
            dictionary['payment'] = self.payment.to_dictionary()
        if self.payment_status_category is not None:
            dictionary['paymentStatusCategory'] = self.payment_status_category
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreatedPaymentOutput':
        super(CreatedPaymentOutput, self).from_dictionary(dictionary)
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = PaymentResponse()
            self.payment = value.from_dictionary(dictionary['payment'])
        if 'paymentStatusCategory' in dictionary:
            self.payment_status_category = dictionary['paymentStatusCategory']
        return self
