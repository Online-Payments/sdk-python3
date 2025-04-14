# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .created_payment_output import CreatedPaymentOutput
from .data_object import DataObject


class GetHostedCheckoutResponse(DataObject):

    __created_payment_output: Optional[CreatedPaymentOutput] = None
    __status: Optional[str] = None

    @property
    def created_payment_output(self) -> Optional[CreatedPaymentOutput]:
        """
        | This object will return the details of the payment after the payment is cancelled by the customer, rejected or authorized

        Type: :class:`onlinepayments.sdk.domain.created_payment_output.CreatedPaymentOutput`
        """
        return self.__created_payment_output

    @created_payment_output.setter
    def created_payment_output(self, value: Optional[CreatedPaymentOutput]) -> None:
        self.__created_payment_output = value

    @property
    def status(self) -> Optional[str]:
        """
        | This is the status of the hosted checkout. Possible values are:
        
        * IN_PROGRESS - The checkout is still in progress and has not finished yet
        * PAYMENT_CREATED - A payment has been created
        * CANCELLED_BY_CONSUMER - The HostedCheckout session have been cancelled by the customer

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: Optional[str]) -> None:
        self.__status = value

    def to_dictionary(self) -> dict:
        dictionary = super(GetHostedCheckoutResponse, self).to_dictionary()
        if self.created_payment_output is not None:
            dictionary['createdPaymentOutput'] = self.created_payment_output.to_dictionary()
        if self.status is not None:
            dictionary['status'] = self.status
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetHostedCheckoutResponse':
        super(GetHostedCheckoutResponse, self).from_dictionary(dictionary)
        if 'createdPaymentOutput' in dictionary:
            if not isinstance(dictionary['createdPaymentOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['createdPaymentOutput']))
            value = CreatedPaymentOutput()
            self.created_payment_output = value.from_dictionary(dictionary['createdPaymentOutput'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        return self
