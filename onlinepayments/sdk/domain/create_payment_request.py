# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.card_payment_method_specific_input import CardPaymentMethodSpecificInput
from onlinepayments.sdk.domain.fraud_fields import FraudFields
from onlinepayments.sdk.domain.mobile_payment_method_specific_input import MobilePaymentMethodSpecificInput
from onlinepayments.sdk.domain.order import Order
from onlinepayments.sdk.domain.redirect_payment_method_specific_input import RedirectPaymentMethodSpecificInput
from onlinepayments.sdk.domain.sepa_direct_debit_payment_method_specific_input import SepaDirectDebitPaymentMethodSpecificInput


class CreatePaymentRequest(DataObject):
    __card_payment_method_specific_input = None
    __encrypted_customer_input = None
    __fraud_fields = None
    __hosted_tokenization_id = None
    __mobile_payment_method_specific_input = None
    __order = None
    __redirect_payment_method_specific_input = None
    __sepa_direct_debit_payment_method_specific_input = None

    @property
    def card_payment_method_specific_input(self) -> CardPaymentMethodSpecificInput:
        """
        | Object containing the specific input details for card payments

        Type: :class:`onlinepayments.sdk.domain.card_payment_method_specific_input.CardPaymentMethodSpecificInput`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value: CardPaymentMethodSpecificInput):
        self.__card_payment_method_specific_input = value

    @property
    def encrypted_customer_input(self) -> str:
        """
        | Data that was encrypted client side containing all customer entered data elements like card data.
        | Note: Because this data can only be submitted once to our system and contains encrypted card data you should not store it. As the data was captured within the context of a client session you also need to submit it to us before the session has expired.

        Type: str
        """
        return self.__encrypted_customer_input

    @encrypted_customer_input.setter
    def encrypted_customer_input(self, value: str):
        self.__encrypted_customer_input = value

    @property
    def fraud_fields(self) -> FraudFields:
        """
        | Object containing additional data that will be used to assess the risk of fraud

        Type: :class:`onlinepayments.sdk.domain.fraud_fields.FraudFields`
        """
        return self.__fraud_fields

    @fraud_fields.setter
    def fraud_fields(self, value: FraudFields):
        self.__fraud_fields = value

    @property
    def hosted_tokenization_id(self) -> str:
        """
        | Use this field after a successful Hosted Tokenization session to create a payment with the tokenized payment method details.

        Type: str
        """
        return self.__hosted_tokenization_id

    @hosted_tokenization_id.setter
    def hosted_tokenization_id(self, value: str):
        self.__hosted_tokenization_id = value

    @property
    def mobile_payment_method_specific_input(self) -> MobilePaymentMethodSpecificInput:
        """
        | Object containing the specific input details for mobile payments

        Type: :class:`onlinepayments.sdk.domain.mobile_payment_method_specific_input.MobilePaymentMethodSpecificInput`
        """
        return self.__mobile_payment_method_specific_input

    @mobile_payment_method_specific_input.setter
    def mobile_payment_method_specific_input(self, value: MobilePaymentMethodSpecificInput):
        self.__mobile_payment_method_specific_input = value

    @property
    def order(self) -> Order:
        """
        | Order object containing order related data 
        |  Please note that this object is required to be able to submit the amount.

        Type: :class:`onlinepayments.sdk.domain.order.Order`
        """
        return self.__order

    @order.setter
    def order(self, value: Order):
        self.__order = value

    @property
    def redirect_payment_method_specific_input(self) -> RedirectPaymentMethodSpecificInput:
        """
        | Object containing the specific input details for payments that involve redirects to 3rd parties to complete, like iDeal and PayPal

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_method_specific_input.RedirectPaymentMethodSpecificInput`
        """
        return self.__redirect_payment_method_specific_input

    @redirect_payment_method_specific_input.setter
    def redirect_payment_method_specific_input(self, value: RedirectPaymentMethodSpecificInput):
        self.__redirect_payment_method_specific_input = value

    @property
    def sepa_direct_debit_payment_method_specific_input(self) -> SepaDirectDebitPaymentMethodSpecificInput:
        """
        | Object containing the specific input details for SEPA direct debit payments

        Type: :class:`onlinepayments.sdk.domain.sepa_direct_debit_payment_method_specific_input.SepaDirectDebitPaymentMethodSpecificInput`
        """
        return self.__sepa_direct_debit_payment_method_specific_input

    @sepa_direct_debit_payment_method_specific_input.setter
    def sepa_direct_debit_payment_method_specific_input(self, value: SepaDirectDebitPaymentMethodSpecificInput):
        self.__sepa_direct_debit_payment_method_specific_input = value

    def to_dictionary(self):
        dictionary = super(CreatePaymentRequest, self).to_dictionary()
        if self.card_payment_method_specific_input is not None:
            dictionary['cardPaymentMethodSpecificInput'] = self.card_payment_method_specific_input.to_dictionary()
        if self.encrypted_customer_input is not None:
            dictionary['encryptedCustomerInput'] = self.encrypted_customer_input
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

    def from_dictionary(self, dictionary):
        super(CreatePaymentRequest, self).from_dictionary(dictionary)
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CardPaymentMethodSpecificInput()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
        if 'encryptedCustomerInput' in dictionary:
            self.encrypted_customer_input = dictionary['encryptedCustomerInput']
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
