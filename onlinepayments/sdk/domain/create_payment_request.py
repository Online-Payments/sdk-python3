# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .card_payment_method_specific_input import CardPaymentMethodSpecificInput
from .data_object import DataObject
from .feedbacks import Feedbacks
from .fraud_fields import FraudFields
from .mobile_payment_method_specific_input import MobilePaymentMethodSpecificInput
from .order import Order
from .redirect_payment_method_specific_input import RedirectPaymentMethodSpecificInput
from .sepa_direct_debit_payment_method_specific_input import SepaDirectDebitPaymentMethodSpecificInput


class CreatePaymentRequest(DataObject):

    __card_payment_method_specific_input: Optional[CardPaymentMethodSpecificInput] = None
    __encrypted_customer_input: Optional[str] = None
    __feedbacks: Optional[Feedbacks] = None
    __fraud_fields: Optional[FraudFields] = None
    __hosted_tokenization_id: Optional[str] = None
    __mobile_payment_method_specific_input: Optional[MobilePaymentMethodSpecificInput] = None
    __order: Optional[Order] = None
    __redirect_payment_method_specific_input: Optional[RedirectPaymentMethodSpecificInput] = None
    __sepa_direct_debit_payment_method_specific_input: Optional[SepaDirectDebitPaymentMethodSpecificInput] = None

    @property
    def card_payment_method_specific_input(self) -> Optional[CardPaymentMethodSpecificInput]:
        """
        | Object containing the specific input details for card payments

        Type: :class:`onlinepayments.sdk.domain.card_payment_method_specific_input.CardPaymentMethodSpecificInput`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value: Optional[CardPaymentMethodSpecificInput]) -> None:
        self.__card_payment_method_specific_input = value

    @property
    def encrypted_customer_input(self) -> Optional[str]:
        """
        | Data that was encrypted client side containing all customer entered data elements like card data. Note: Because this data can only be submitted once to our system and contains encrypted card data you should not store it. As the data was captured within the context of a client session you also need to submit it to us before the session has expired.

        Type: str
        """
        return self.__encrypted_customer_input

    @encrypted_customer_input.setter
    def encrypted_customer_input(self, value: Optional[str]) -> None:
        self.__encrypted_customer_input = value

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
    def hosted_tokenization_id(self) -> Optional[str]:
        """
        | Use this field after a successful Hosted Tokenization session to create a payment with the tokenized payment method details.

        Type: str
        """
        return self.__hosted_tokenization_id

    @hosted_tokenization_id.setter
    def hosted_tokenization_id(self, value: Optional[str]) -> None:
        self.__hosted_tokenization_id = value

    @property
    def mobile_payment_method_specific_input(self) -> Optional[MobilePaymentMethodSpecificInput]:
        """
        | Object containing the specific input details for mobile payments

        Type: :class:`onlinepayments.sdk.domain.mobile_payment_method_specific_input.MobilePaymentMethodSpecificInput`
        """
        return self.__mobile_payment_method_specific_input

    @mobile_payment_method_specific_input.setter
    def mobile_payment_method_specific_input(self, value: Optional[MobilePaymentMethodSpecificInput]) -> None:
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
    def sepa_direct_debit_payment_method_specific_input(self) -> Optional[SepaDirectDebitPaymentMethodSpecificInput]:
        """
        | Object containing the specific input details for SEPA direct debit payments

        Type: :class:`onlinepayments.sdk.domain.sepa_direct_debit_payment_method_specific_input.SepaDirectDebitPaymentMethodSpecificInput`
        """
        return self.__sepa_direct_debit_payment_method_specific_input

    @sepa_direct_debit_payment_method_specific_input.setter
    def sepa_direct_debit_payment_method_specific_input(self, value: Optional[SepaDirectDebitPaymentMethodSpecificInput]) -> None:
        self.__sepa_direct_debit_payment_method_specific_input = value

    def to_dictionary(self) -> dict:
        dictionary = super(CreatePaymentRequest, self).to_dictionary()
        if self.card_payment_method_specific_input is not None:
            dictionary['cardPaymentMethodSpecificInput'] = self.card_payment_method_specific_input.to_dictionary()
        if self.encrypted_customer_input is not None:
            dictionary['encryptedCustomerInput'] = self.encrypted_customer_input
        if self.feedbacks is not None:
            dictionary['feedbacks'] = self.feedbacks.to_dictionary()
        if self.fraud_fields is not None:
            dictionary['fraudFields'] = self.fraud_fields.to_dictionary()
        if self.hosted_tokenization_id is not None:
            dictionary['hostedTokenizationId'] = self.hosted_tokenization_id
        if self.mobile_payment_method_specific_input is not None:
            dictionary['mobilePaymentMethodSpecificInput'] = self.mobile_payment_method_specific_input.to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        if self.redirect_payment_method_specific_input is not None:
            dictionary['redirectPaymentMethodSpecificInput'] = self.redirect_payment_method_specific_input.to_dictionary()
        if self.sepa_direct_debit_payment_method_specific_input is not None:
            dictionary['sepaDirectDebitPaymentMethodSpecificInput'] = self.sepa_direct_debit_payment_method_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreatePaymentRequest':
        super(CreatePaymentRequest, self).from_dictionary(dictionary)
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CardPaymentMethodSpecificInput()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
        if 'encryptedCustomerInput' in dictionary:
            self.encrypted_customer_input = dictionary['encryptedCustomerInput']
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
        if 'hostedTokenizationId' in dictionary:
            self.hosted_tokenization_id = dictionary['hostedTokenizationId']
        if 'mobilePaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['mobilePaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobilePaymentMethodSpecificInput']))
            value = MobilePaymentMethodSpecificInput()
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
            value = SepaDirectDebitPaymentMethodSpecificInput()
            self.sepa_direct_debit_payment_method_specific_input = value.from_dictionary(dictionary['sepaDirectDebitPaymentMethodSpecificInput'])
        return self
