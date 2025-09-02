# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .apple_pay_recurring_payment_request import ApplePayRecurringPaymentRequest
from .data_object import DataObject
from .product302_recurring import Product302Recurring


class MobilePaymentProduct302SpecificInput(DataObject):

    __apple_pay_recurring_payment_request: Optional[ApplePayRecurringPaymentRequest] = None
    __is_recurring: Optional[bool] = None
    __recurring: Optional[Product302Recurring] = None
    __tokenize: Optional[bool] = None

    @property
    def apple_pay_recurring_payment_request(self) -> Optional[ApplePayRecurringPaymentRequest]:
        """
        | Object containing information specific to Apple Pay recurring request.

        Type: :class:`onlinepayments.sdk.domain.apple_pay_recurring_payment_request.ApplePayRecurringPaymentRequest`
        """
        return self.__apple_pay_recurring_payment_request

    @apple_pay_recurring_payment_request.setter
    def apple_pay_recurring_payment_request(self, value: Optional[ApplePayRecurringPaymentRequest]) -> None:
        self.__apple_pay_recurring_payment_request = value

    @property
    def is_recurring(self) -> Optional[bool]:
        """
        * true - Indicates that the transaction is part of a scheduled recurring sequence. In addition, recurringPaymentSequenceIndicator indicates if the transaction is the first or subsequent in a recurring sequence.
        * false - Indicates that the transaction is not part of a scheduled recurring sequence. The default value for this property is false. For HostedCheckout use the hostedCheckoutSpecificInput.isRecurring property instead.

        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value: Optional[bool]) -> None:
        self.__is_recurring = value

    @property
    def recurring(self) -> Optional[Product302Recurring]:
        """
        | Object containing information specific to Apple Pay and recurring.

        Type: :class:`onlinepayments.sdk.domain.product302_recurring.Product302Recurring`
        """
        return self.__recurring

    @recurring.setter
    def recurring(self, value: Optional[Product302Recurring]) -> None:
        self.__recurring = value

    @property
    def tokenize(self) -> Optional[bool]:
        """
        | Indicates if this transaction should be tokenized
        
        * true - Tokenize the transaction. Note that a payment on the payment platform that results in a status REDIRECTED cannot be tokenized in this way.
        * false - Do not tokenize the transaction, unless it would be tokenized by other means such as auto-tokenization of recurring payments.

        Type: bool
        """
        return self.__tokenize

    @tokenize.setter
    def tokenize(self, value: Optional[bool]) -> None:
        self.__tokenize = value

    def to_dictionary(self) -> dict:
        dictionary = super(MobilePaymentProduct302SpecificInput, self).to_dictionary()
        if self.apple_pay_recurring_payment_request is not None:
            dictionary['applePayRecurringPaymentRequest'] = self.apple_pay_recurring_payment_request.to_dictionary()
        if self.is_recurring is not None:
            dictionary['isRecurring'] = self.is_recurring
        if self.recurring is not None:
            dictionary['recurring'] = self.recurring.to_dictionary()
        if self.tokenize is not None:
            dictionary['tokenize'] = self.tokenize
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MobilePaymentProduct302SpecificInput':
        super(MobilePaymentProduct302SpecificInput, self).from_dictionary(dictionary)
        if 'applePayRecurringPaymentRequest' in dictionary:
            if not isinstance(dictionary['applePayRecurringPaymentRequest'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['applePayRecurringPaymentRequest']))
            value = ApplePayRecurringPaymentRequest()
            self.apple_pay_recurring_payment_request = value.from_dictionary(dictionary['applePayRecurringPaymentRequest'])
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'recurring' in dictionary:
            if not isinstance(dictionary['recurring'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['recurring']))
            value = Product302Recurring()
            self.recurring = value.from_dictionary(dictionary['recurring'])
        if 'tokenize' in dictionary:
            self.tokenize = dictionary['tokenize']
        return self
