# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .merchant_action import MerchantAction
from .payment_creation_output import PaymentCreationOutput
from .payment_response import PaymentResponse


class CreatePaymentResponse(DataObject):

    __creation_output: Optional[PaymentCreationOutput] = None
    __merchant_action: Optional[MerchantAction] = None
    __payment: Optional[PaymentResponse] = None

    @property
    def creation_output(self) -> Optional[PaymentCreationOutput]:
        """
        | Object containing the details of the created payment.

        Type: :class:`onlinepayments.sdk.domain.payment_creation_output.PaymentCreationOutput`
        """
        return self.__creation_output

    @creation_output.setter
    def creation_output(self, value: Optional[PaymentCreationOutput]) -> None:
        self.__creation_output = value

    @property
    def merchant_action(self) -> Optional[MerchantAction]:
        """
        | Object that contains the action, including the needed data, that you should perform next, like showing instructions, showing the transaction results or redirect to a third party to complete the payment

        Type: :class:`onlinepayments.sdk.domain.merchant_action.MerchantAction`
        """
        return self.__merchant_action

    @merchant_action.setter
    def merchant_action(self, value: Optional[MerchantAction]) -> None:
        self.__merchant_action = value

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

    def to_dictionary(self) -> dict:
        dictionary = super(CreatePaymentResponse, self).to_dictionary()
        if self.creation_output is not None:
            dictionary['creationOutput'] = self.creation_output.to_dictionary()
        if self.merchant_action is not None:
            dictionary['merchantAction'] = self.merchant_action.to_dictionary()
        if self.payment is not None:
            dictionary['payment'] = self.payment.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreatePaymentResponse':
        super(CreatePaymentResponse, self).from_dictionary(dictionary)
        if 'creationOutput' in dictionary:
            if not isinstance(dictionary['creationOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['creationOutput']))
            value = PaymentCreationOutput()
            self.creation_output = value.from_dictionary(dictionary['creationOutput'])
        if 'merchantAction' in dictionary:
            if not isinstance(dictionary['merchantAction'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['merchantAction']))
            value = MerchantAction()
            self.merchant_action = value.from_dictionary(dictionary['merchantAction'])
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = PaymentResponse()
            self.payment = value.from_dictionary(dictionary['payment'])
        return self
