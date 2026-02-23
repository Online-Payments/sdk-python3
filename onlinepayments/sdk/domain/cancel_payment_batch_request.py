# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .cancel_payment_request import CancelPaymentRequest
from .data_object import DataObject


class CancelPaymentBatchRequest(DataObject):

    __cancel: Optional[CancelPaymentRequest] = None
    __payment_id: Optional[str] = None

    @property
    def cancel(self) -> Optional[CancelPaymentRequest]:
        """
        Type: :class:`onlinepayments.sdk.domain.cancel_payment_request.CancelPaymentRequest`
        """
        return self.__cancel

    @cancel.setter
    def cancel(self, value: Optional[CancelPaymentRequest]) -> None:
        self.__cancel = value

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
        dictionary = super(CancelPaymentBatchRequest, self).to_dictionary()
        if self.cancel is not None:
            dictionary['cancel'] = self.cancel.to_dictionary()
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CancelPaymentBatchRequest':
        super(CancelPaymentBatchRequest, self).from_dictionary(dictionary)
        if 'cancel' in dictionary:
            if not isinstance(dictionary['cancel'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cancel']))
            value = CancelPaymentRequest()
            self.cancel = value.from_dictionary(dictionary['cancel'])
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        return self
