# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .payment_product5704_auto_capture import PaymentProduct5704AutoCapture


class RedirectPaymentProduct5407SpecificInput(DataObject):

    __payment_product5704_auto_capture: Optional[PaymentProduct5704AutoCapture] = None

    @property
    def payment_product5704_auto_capture(self) -> Optional[PaymentProduct5704AutoCapture]:
        """
        | Object containing the auto capture configuration for the payment.

        Type: :class:`onlinepayments.sdk.domain.payment_product5704_auto_capture.PaymentProduct5704AutoCapture`
        """
        return self.__payment_product5704_auto_capture

    @payment_product5704_auto_capture.setter
    def payment_product5704_auto_capture(self, value: Optional[PaymentProduct5704AutoCapture]) -> None:
        self.__payment_product5704_auto_capture = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct5407SpecificInput, self).to_dictionary()
        if self.payment_product5704_auto_capture is not None:
            dictionary['paymentProduct5704AutoCapture'] = self.payment_product5704_auto_capture.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5407SpecificInput':
        super(RedirectPaymentProduct5407SpecificInput, self).from_dictionary(dictionary)
        if 'paymentProduct5704AutoCapture' in dictionary:
            if not isinstance(dictionary['paymentProduct5704AutoCapture'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5704AutoCapture']))
            value = PaymentProduct5704AutoCapture()
            self.payment_product5704_auto_capture = value.from_dictionary(dictionary['paymentProduct5704AutoCapture'])
        return self
