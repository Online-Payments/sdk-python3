# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.hosted_checkout_specific_output import HostedCheckoutSpecificOutput
from onlinepayments.sdk.domain.payment_output import PaymentOutput
from onlinepayments.sdk.domain.payment_status_output import PaymentStatusOutput


class PaymentResponse(DataObject):
    """
    | Object that holds the payment related properties
    """

    __hosted_checkout_specific_output = None
    __id = None
    __payment_output = None
    __status = None
    __status_output = None

    @property
    def hosted_checkout_specific_output(self) -> HostedCheckoutSpecificOutput:
        """
        | Hosted Checkout specific information. Populated if the payment was created on the platform through a Hosted Checkout.

        Type: :class:`onlinepayments.sdk.domain.hosted_checkout_specific_output.HostedCheckoutSpecificOutput`
        """
        return self.__hosted_checkout_specific_output

    @hosted_checkout_specific_output.setter
    def hosted_checkout_specific_output(self, value: HostedCheckoutSpecificOutput):
        self.__hosted_checkout_specific_output = value

    @property
    def id(self) -> str:
        """
        | Our unique payment transaction identifier

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value

    @property
    def payment_output(self) -> PaymentOutput:
        """
        | Object containing payment details

        Type: :class:`onlinepayments.sdk.domain.payment_output.PaymentOutput`
        """
        return self.__payment_output

    @payment_output.setter
    def payment_output(self, value: PaymentOutput):
        self.__payment_output = value

    @property
    def status(self) -> str:
        """
        | Current high-level status of the payment in a human-readable form.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: str):
        self.__status = value

    @property
    def status_output(self) -> PaymentStatusOutput:
        """
        | This object has the numeric representation of the current payment status, timestamp of last status change and performable action on the current payment resource. In case of failed payments and negative scenarios, detailed error information is listed.

        Type: :class:`onlinepayments.sdk.domain.payment_status_output.PaymentStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value: PaymentStatusOutput):
        self.__status_output = value

    def to_dictionary(self):
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

    def from_dictionary(self, dictionary):
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
