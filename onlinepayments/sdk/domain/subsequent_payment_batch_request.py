# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .subsequent_payment_request import SubsequentPaymentRequest


class SubsequentPaymentBatchRequest(DataObject):

    __payment_id: Optional[str] = None
    __subsequent: Optional[SubsequentPaymentRequest] = None

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

    @property
    def subsequent(self) -> Optional[SubsequentPaymentRequest]:
        """
        Type: :class:`onlinepayments.sdk.domain.subsequent_payment_request.SubsequentPaymentRequest`
        """
        return self.__subsequent

    @subsequent.setter
    def subsequent(self, value: Optional[SubsequentPaymentRequest]) -> None:
        self.__subsequent = value

    def to_dictionary(self) -> dict:
        dictionary = super(SubsequentPaymentBatchRequest, self).to_dictionary()
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        if self.subsequent is not None:
            dictionary['subsequent'] = self.subsequent.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SubsequentPaymentBatchRequest':
        super(SubsequentPaymentBatchRequest, self).from_dictionary(dictionary)
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        if 'subsequent' in dictionary:
            if not isinstance(dictionary['subsequent'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['subsequent']))
            value = SubsequentPaymentRequest()
            self.subsequent = value.from_dictionary(dictionary['subsequent'])
        return self
