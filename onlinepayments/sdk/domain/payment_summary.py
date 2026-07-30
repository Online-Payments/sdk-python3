# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .payment_output_summary import PaymentOutputSummary
from .payment_status_output_summary import PaymentStatusOutputSummary


class PaymentSummary(DataObject):

    __id: Optional[str] = None
    __payment_output: Optional[PaymentOutputSummary] = None
    __status: Optional[str] = None
    __status_output: Optional[PaymentStatusOutputSummary] = None

    @property
    def id(self) -> Optional[str]:
        """
        | This is our unique payment transaction identifier.

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: Optional[str]) -> None:
        self.__id = value

    @property
    def payment_output(self) -> Optional[PaymentOutputSummary]:
        """
        | Summary of payment output details

        Type: :class:`onlinepayments.sdk.domain.payment_output_summary.PaymentOutputSummary`
        """
        return self.__payment_output

    @payment_output.setter
    def payment_output(self, value: Optional[PaymentOutputSummary]) -> None:
        self.__payment_output = value

    @property
    def status(self) -> Optional[str]:
        """
        | Current high-level status of the payment in a human-readable form.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: Optional[str]) -> None:
        self.__status = value

    @property
    def status_output(self) -> Optional[PaymentStatusOutputSummary]:
        """
        | Summary of payment status output with essential information

        Type: :class:`onlinepayments.sdk.domain.payment_status_output_summary.PaymentStatusOutputSummary`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value: Optional[PaymentStatusOutputSummary]) -> None:
        self.__status_output = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentSummary, self).to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.payment_output is not None:
            dictionary['paymentOutput'] = self.payment_output.to_dictionary()
        if self.status is not None:
            dictionary['status'] = self.status
        if self.status_output is not None:
            dictionary['statusOutput'] = self.status_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentSummary':
        super(PaymentSummary, self).from_dictionary(dictionary)
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'paymentOutput' in dictionary:
            if not isinstance(dictionary['paymentOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentOutput']))
            value = PaymentOutputSummary()
            self.payment_output = value.from_dictionary(dictionary['paymentOutput'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = PaymentStatusOutputSummary()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self
