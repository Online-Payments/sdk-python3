# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .capture_payment_request import CapturePaymentRequest
from .data_object import DataObject


class CapturePaymentBatchRequest(DataObject):

    __capture: Optional[CapturePaymentRequest] = None
    __payment_id: Optional[str] = None

    @property
    def capture(self) -> Optional[CapturePaymentRequest]:
        """
        Type: :class:`onlinepayments.sdk.domain.capture_payment_request.CapturePaymentRequest`
        """
        return self.__capture

    @capture.setter
    def capture(self, value: Optional[CapturePaymentRequest]) -> None:
        self.__capture = value

    @property
    def payment_id(self) -> Optional[str]:
        """
        | This is our unique payment transaction identifier.

        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: Optional[str]) -> None:
        self.__payment_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(CapturePaymentBatchRequest, self).to_dictionary()
        if self.capture is not None:
            dictionary['capture'] = self.capture.to_dictionary()
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CapturePaymentBatchRequest':
        super(CapturePaymentBatchRequest, self).from_dictionary(dictionary)
        if 'capture' in dictionary:
            if not isinstance(dictionary['capture'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['capture']))
            value = CapturePaymentRequest()
            self.capture = value.from_dictionary(dictionary['capture'])
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        return self
