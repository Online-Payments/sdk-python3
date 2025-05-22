# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .apple_pay_recurring_payment_request import ApplePayRecurringPaymentRequest
from .data_object import DataObject


class MobilePaymentProduct302SpecificInput(DataObject):

    __apple_pay_recurring_payment_request: Optional[ApplePayRecurringPaymentRequest] = None

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

    def to_dictionary(self) -> dict:
        dictionary = super(MobilePaymentProduct302SpecificInput, self).to_dictionary()
        if self.apple_pay_recurring_payment_request is not None:
            dictionary['applePayRecurringPaymentRequest'] = self.apple_pay_recurring_payment_request.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MobilePaymentProduct302SpecificInput':
        super(MobilePaymentProduct302SpecificInput, self).from_dictionary(dictionary)
        if 'applePayRecurringPaymentRequest' in dictionary:
            if not isinstance(dictionary['applePayRecurringPaymentRequest'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['applePayRecurringPaymentRequest']))
            value = ApplePayRecurringPaymentRequest()
            self.apple_pay_recurring_payment_request = value.from_dictionary(dictionary['applePayRecurringPaymentRequest'])
        return self
