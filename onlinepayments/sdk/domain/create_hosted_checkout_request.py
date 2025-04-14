# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .card_payment_method_specific_input_base import CardPaymentMethodSpecificInputBase
from .data_object import DataObject
from .feedbacks import Feedbacks
from .fraud_fields import FraudFields
from .hosted_checkout_specific_input import HostedCheckoutSpecificInput
from .mobile_payment_method_hosted_checkout_specific_input import MobilePaymentMethodHostedCheckoutSpecificInput
from .order import Order
from .redirect_payment_method_specific_input import RedirectPaymentMethodSpecificInput
from .sepa_direct_debit_payment_method_specific_input_base import SepaDirectDebitPaymentMethodSpecificInputBase


class CreateHostedCheckoutRequest(DataObject):

    __card_payment_method_specific_input: Optional[CardPaymentMethodSpecificInputBase] = None
    __feedbacks: Optional[Feedbacks] = None
    __fraud_fields: Optional[FraudFields] = None
    __hosted_checkout_specific_input: Optional[HostedCheckoutSpecificInput] = None
    __mobile_payment_method_specific_input: Optional[MobilePaymentMethodHostedCheckoutSpecificInput] = None
    __order: Optional[Order] = None
    __redirect_payment_method_specific_input: Optional[RedirectPaymentMethodSpecificInput] = None
    __sepa_direct_debit_payment_method_specific_input: Optional[SepaDirectDebitPaymentMethodSpecificInputBase] = None

    @property
    def card_payment_method_specific_input(self) -> Optional[CardPaymentMethodSpecificInputBase]:
        """
        | Object containing the specific input details for card payments

        Type: :class:`onlinepayments.sdk.domain.card_payment_method_specific_input_base.CardPaymentMethodSpecificInputBase`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value: Optional[CardPaymentMethodSpecificInputBase]) -> None:
        self.__card_payment_method_specific_input = value

    @property
    def feedbacks(self) -> Optional[Feedbacks]:
        """
        | This section will contain feedback Urls to provide feedback on the payment.

        Type: :class:`onlinepayments.sdk.domain.feedbacks.Feedbacks`
        """
        return self.__feedbacks

    @feedbacks.setter
    def feedbacks(self, value: Optional[Feedbacks]) -> None:
        self.__feedbacks = value

    @property
    def fraud_fields(self) -> Optional[FraudFields]:
        """
        | Object containing additional data that will be used to assess the risk of fraud

        Type: :class:`onlinepayments.sdk.domain.fraud_fields.FraudFields`
        """
        return self.__fraud_fields

    @fraud_fields.setter
    def fraud_fields(self, value: Optional[FraudFields]) -> None:
        self.__fraud_fields = value

    @property
    def hosted_checkout_specific_input(self) -> Optional[HostedCheckoutSpecificInput]:
        """
        | Object containing hosted checkout specific data

        Type: :class:`onlinepayments.sdk.domain.hosted_checkout_specific_input.HostedCheckoutSpecificInput`
        """
        return self.__hosted_checkout_specific_input

    @hosted_checkout_specific_input.setter
    def hosted_checkout_specific_input(self, value: Optional[HostedCheckoutSpecificInput]) -> None:
        self.__hosted_checkout_specific_input = value

    @property
    def mobile_payment_method_specific_input(self) -> Optional[MobilePaymentMethodHostedCheckoutSpecificInput]:
        """
        | Object containing the specific input details for mobile payments

        Type: :class:`onlinepayments.sdk.domain.mobile_payment_method_hosted_checkout_specific_input.MobilePaymentMethodHostedCheckoutSpecificInput`
        """
        return self.__mobile_payment_method_specific_input

    @mobile_payment_method_specific_input.setter
    def mobile_payment_method_specific_input(self, value: Optional[MobilePaymentMethodHostedCheckoutSpecificInput]) -> None:
        self.__mobile_payment_method_specific_input = value

    @property
    def order(self) -> Optional[Order]:
        """
        | Order object containing order related data Please note that this object is required to be able to submit the amount.

        Type: :class:`onlinepayments.sdk.domain.order.Order`
        """
        return self.__order

    @order.setter
    def order(self, value: Optional[Order]) -> None:
        self.__order = value

    @property
    def redirect_payment_method_specific_input(self) -> Optional[RedirectPaymentMethodSpecificInput]:
        """
        | Object containing the specific input details for payments that involve redirects to 3rd parties to complete, like iDeal and PayPal

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_method_specific_input.RedirectPaymentMethodSpecificInput`
        """
        return self.__redirect_payment_method_specific_input

    @redirect_payment_method_specific_input.setter
    def redirect_payment_method_specific_input(self, value: Optional[RedirectPaymentMethodSpecificInput]) -> None:
        self.__redirect_payment_method_specific_input = value

    @property
    def sepa_direct_debit_payment_method_specific_input(self) -> Optional[SepaDirectDebitPaymentMethodSpecificInputBase]:
        """
        | Object containing the specific input details for SEPA direct debit payments

        Type: :class:`onlinepayments.sdk.domain.sepa_direct_debit_payment_method_specific_input_base.SepaDirectDebitPaymentMethodSpecificInputBase`
        """
        return self.__sepa_direct_debit_payment_method_specific_input

    @sepa_direct_debit_payment_method_specific_input.setter
    def sepa_direct_debit_payment_method_specific_input(self, value: Optional[SepaDirectDebitPaymentMethodSpecificInputBase]) -> None:
        self.__sepa_direct_debit_payment_method_specific_input = value

    def to_dictionary(self) -> dict:
        dictionary = super(CreateHostedCheckoutRequest, self).to_dictionary()
        if self.card_payment_method_specific_input is not None:
            dictionary['cardPaymentMethodSpecificInput'] = self.card_payment_method_specific_input.to_dictionary()
        if self.feedbacks is not None:
            dictionary['feedbacks'] = self.feedbacks.to_dictionary()
        if self.fraud_fields is not None:
            dictionary['fraudFields'] = self.fraud_fields.to_dictionary()
        if self.hosted_checkout_specific_input is not None:
            dictionary['hostedCheckoutSpecificInput'] = self.hosted_checkout_specific_input.to_dictionary()
        if self.mobile_payment_method_specific_input is not None:
            dictionary['mobilePaymentMethodSpecificInput'] = self.mobile_payment_method_specific_input.to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        if self.redirect_payment_method_specific_input is not None:
            dictionary['redirectPaymentMethodSpecificInput'] = self.redirect_payment_method_specific_input.to_dictionary()
        if self.sepa_direct_debit_payment_method_specific_input is not None:
            dictionary['sepaDirectDebitPaymentMethodSpecificInput'] = self.sepa_direct_debit_payment_method_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreateHostedCheckoutRequest':
        super(CreateHostedCheckoutRequest, self).from_dictionary(dictionary)
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CardPaymentMethodSpecificInputBase()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
        if 'feedbacks' in dictionary:
            if not isinstance(dictionary['feedbacks'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['feedbacks']))
            value = Feedbacks()
            self.feedbacks = value.from_dictionary(dictionary['feedbacks'])
        if 'fraudFields' in dictionary:
            if not isinstance(dictionary['fraudFields'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudFields']))
            value = FraudFields()
            self.fraud_fields = value.from_dictionary(dictionary['fraudFields'])
        if 'hostedCheckoutSpecificInput' in dictionary:
            if not isinstance(dictionary['hostedCheckoutSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['hostedCheckoutSpecificInput']))
            value = HostedCheckoutSpecificInput()
            self.hosted_checkout_specific_input = value.from_dictionary(dictionary['hostedCheckoutSpecificInput'])
        if 'mobilePaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['mobilePaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobilePaymentMethodSpecificInput']))
            value = MobilePaymentMethodHostedCheckoutSpecificInput()
            self.mobile_payment_method_specific_input = value.from_dictionary(dictionary['mobilePaymentMethodSpecificInput'])
        if 'order' in dictionary:
            if not isinstance(dictionary['order'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['order']))
            value = Order()
            self.order = value.from_dictionary(dictionary['order'])
        if 'redirectPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['redirectPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectPaymentMethodSpecificInput']))
            value = RedirectPaymentMethodSpecificInput()
            self.redirect_payment_method_specific_input = value.from_dictionary(dictionary['redirectPaymentMethodSpecificInput'])
        if 'sepaDirectDebitPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['sepaDirectDebitPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['sepaDirectDebitPaymentMethodSpecificInput']))
            value = SepaDirectDebitPaymentMethodSpecificInputBase()
            self.sepa_direct_debit_payment_method_specific_input = value.from_dictionary(dictionary['sepaDirectDebitPaymentMethodSpecificInput'])
        return self
