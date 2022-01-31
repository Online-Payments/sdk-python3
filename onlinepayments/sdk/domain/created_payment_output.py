# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payment_response import PaymentResponse


class CreatedPaymentOutput(DataObject):
    """
    | When a payment has been created during the hosted checkout session this object will return the details
    """

    __payment = None
    __payment_status_category = None

    @property
    def payment(self) -> PaymentResponse:
        """
        | Object that holds the payment related properties

        Type: :class:`onlinepayments.sdk.domain.payment_response.PaymentResponse`
        """
        return self.__payment

    @payment.setter
    def payment(self, value: PaymentResponse):
        self.__payment = value

    @property
    def payment_status_category(self) -> str:
        """
        Type: str
        """
        return self.__payment_status_category

    @payment_status_category.setter
    def payment_status_category(self, value: str):
        self.__payment_status_category = value

    def to_dictionary(self):
        dictionary = super(CreatedPaymentOutput, self).to_dictionary()
        if self.payment is not None:
            dictionary['payment'] = self.payment.to_dictionary()
        if self.payment_status_category is not None:
            dictionary['paymentStatusCategory'] = self.payment_status_category
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatedPaymentOutput, self).from_dictionary(dictionary)
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = PaymentResponse()
            self.payment = value.from_dictionary(dictionary['payment'])
        if 'paymentStatusCategory' in dictionary:
            self.payment_status_category = dictionary['paymentStatusCategory']
        return self
