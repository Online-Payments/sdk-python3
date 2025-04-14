# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .hosted_checkout_specific_output import HostedCheckoutSpecificOutput
from .payment_output import PaymentOutput
from .payment_status_output import PaymentStatusOutput


class PaymentResponse(DataObject):

    __hosted_checkout_specific_output: Optional[HostedCheckoutSpecificOutput] = None
    __id: Optional[str] = None
    __payment_output: Optional[PaymentOutput] = None
    __status: Optional[str] = None
    __status_output: Optional[PaymentStatusOutput] = None

    @property
    def hosted_checkout_specific_output(self) -> Optional[HostedCheckoutSpecificOutput]:
        """
        | Hosted Checkout specific information. Populated if the payment was created on the platform through a Hosted Checkout.

        Type: :class:`onlinepayments.sdk.domain.hosted_checkout_specific_output.HostedCheckoutSpecificOutput`
        """
        return self.__hosted_checkout_specific_output

    @hosted_checkout_specific_output.setter
    def hosted_checkout_specific_output(self, value: Optional[HostedCheckoutSpecificOutput]) -> None:
        self.__hosted_checkout_specific_output = value

    @property
    def id(self) -> Optional[str]:
        """
        | Our unique payment transaction identifier

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: Optional[str]) -> None:
        self.__id = value

    @property
    def payment_output(self) -> Optional[PaymentOutput]:
        """
        | Object containing payment details

        Type: :class:`onlinepayments.sdk.domain.payment_output.PaymentOutput`
        """
        return self.__payment_output

    @payment_output.setter
    def payment_output(self, value: Optional[PaymentOutput]) -> None:
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
    def status_output(self) -> Optional[PaymentStatusOutput]:
        """
        | This object has the numeric representation of the current payment status, timestamp of last status change and performable action on the current payment resource. In case of failed payments and negative scenarios, detailed error information is listed.

        Type: :class:`onlinepayments.sdk.domain.payment_status_output.PaymentStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value: Optional[PaymentStatusOutput]) -> None:
        self.__status_output = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentResponse, self).to_dictionary()
        if self.hosted_checkout_specific_output is not None:
            dictionary['hostedCheckoutSpecificOutput'] = self.hosted_checkout_specific_output.to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.payment_output is not None:
            dictionary['paymentOutput'] = self.payment_output.to_dictionary()
        if self.status is not None:
            dictionary['status'] = self.status
        if self.status_output is not None:
            dictionary['statusOutput'] = self.status_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentResponse':
        super(PaymentResponse, self).from_dictionary(dictionary)
        if 'hostedCheckoutSpecificOutput' in dictionary:
            if not isinstance(dictionary['hostedCheckoutSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['hostedCheckoutSpecificOutput']))
            value = HostedCheckoutSpecificOutput()
            self.hosted_checkout_specific_output = value.from_dictionary(dictionary['hostedCheckoutSpecificOutput'])
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'paymentOutput' in dictionary:
            if not isinstance(dictionary['paymentOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentOutput']))
            value = PaymentOutput()
            self.payment_output = value.from_dictionary(dictionary['paymentOutput'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = PaymentStatusOutput()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self
