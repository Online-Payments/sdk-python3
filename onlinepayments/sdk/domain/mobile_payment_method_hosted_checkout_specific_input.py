# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .mobile_payment_product302_specific_input import MobilePaymentProduct302SpecificInput
from .mobile_payment_product320_specific_input import MobilePaymentProduct320SpecificInput


class MobilePaymentMethodHostedCheckoutSpecificInput(DataObject):

    __authorization_mode: Optional[str] = None
    __payment_product302_specific_input: Optional[MobilePaymentProduct302SpecificInput] = None
    __payment_product320_specific_input: Optional[MobilePaymentProduct320SpecificInput] = None
    __payment_product_id: Optional[int] = None

    @property
    def authorization_mode(self) -> Optional[str]:
        """
        | Determines the type of the authorization that will be used. Allowed values:
        
        * FINAL_AUTHORIZATION - The payment creation results in an authorization that is ready for capture. Final authorizations can't be reversed and need to be captured for the full amount within 7 days.
        * PRE_AUTHORIZATION - The payment creation results in a pre-authorization that is ready for capture. Pre-authortizations can be reversed and can be captured within 30 days. The capture amount can be lower than the authorized amount.
        * SALE - The payment creation results in an authorization that is already captured at the moment of approval.
        
        | Only used with some acquirers, ignored for acquirers that do not support this. In case the acquirer does not allow this to be specified the authorizationMode is 'unspecified', which behaves similar to a final authorization.

        Type: str
        """
        return self.__authorization_mode

    @authorization_mode.setter
    def authorization_mode(self, value: Optional[str]) -> None:
        self.__authorization_mode = value

    @property
    def payment_product302_specific_input(self) -> Optional[MobilePaymentProduct302SpecificInput]:
        """
        | Object containing information specific to Apple Pay.

        Type: :class:`onlinepayments.sdk.domain.mobile_payment_product302_specific_input.MobilePaymentProduct302SpecificInput`
        """
        return self.__payment_product302_specific_input

    @payment_product302_specific_input.setter
    def payment_product302_specific_input(self, value: Optional[MobilePaymentProduct302SpecificInput]) -> None:
        self.__payment_product302_specific_input = value

    @property
    def payment_product320_specific_input(self) -> Optional[MobilePaymentProduct320SpecificInput]:
        """
        | Object containing information specific to Google Pay. Required for payments with product 320.

        Type: :class:`onlinepayments.sdk.domain.mobile_payment_product320_specific_input.MobilePaymentProduct320SpecificInput`
        """
        return self.__payment_product320_specific_input

    @payment_product320_specific_input.setter
    def payment_product320_specific_input(self, value: Optional[MobilePaymentProduct320SpecificInput]) -> None:
        self.__payment_product320_specific_input = value

    @property
    def payment_product_id(self) -> Optional[int]:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: Optional[int]) -> None:
        self.__payment_product_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(MobilePaymentMethodHostedCheckoutSpecificInput, self).to_dictionary()
        if self.authorization_mode is not None:
            dictionary['authorizationMode'] = self.authorization_mode
        if self.payment_product302_specific_input is not None:
            dictionary['paymentProduct302SpecificInput'] = self.payment_product302_specific_input.to_dictionary()
        if self.payment_product320_specific_input is not None:
            dictionary['paymentProduct320SpecificInput'] = self.payment_product320_specific_input.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MobilePaymentMethodHostedCheckoutSpecificInput':
        super(MobilePaymentMethodHostedCheckoutSpecificInput, self).from_dictionary(dictionary)
        if 'authorizationMode' in dictionary:
            self.authorization_mode = dictionary['authorizationMode']
        if 'paymentProduct302SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct302SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct302SpecificInput']))
            value = MobilePaymentProduct302SpecificInput()
            self.payment_product302_specific_input = value.from_dictionary(dictionary['paymentProduct302SpecificInput'])
        if 'paymentProduct320SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct320SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct320SpecificInput']))
            value = MobilePaymentProduct320SpecificInput()
            self.payment_product320_specific_input = value.from_dictionary(dictionary['paymentProduct320SpecificInput'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
