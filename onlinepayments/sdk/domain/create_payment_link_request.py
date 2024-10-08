# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.card_payment_method_specific_input_base import CardPaymentMethodSpecificInputBase
from onlinepayments.sdk.domain.fraud_fields import FraudFields
from onlinepayments.sdk.domain.hosted_checkout_specific_input import HostedCheckoutSpecificInput
from onlinepayments.sdk.domain.mobile_payment_method_hosted_checkout_specific_input import MobilePaymentMethodHostedCheckoutSpecificInput
from onlinepayments.sdk.domain.order import Order
from onlinepayments.sdk.domain.payment_link_order_input import PaymentLinkOrderInput
from onlinepayments.sdk.domain.payment_link_specific_input import PaymentLinkSpecificInput
from onlinepayments.sdk.domain.redirect_payment_method_specific_input import RedirectPaymentMethodSpecificInput
from onlinepayments.sdk.domain.sepa_direct_debit_payment_method_specific_input_base import SepaDirectDebitPaymentMethodSpecificInputBase


class CreatePaymentLinkRequest(DataObject):
    """
    | An object containing the Create PaymentLink request.
    """

    __card_payment_method_specific_input = None
    __description = None
    __expiration_date = None
    __fraud_fields = None
    __hosted_checkout_specific_input = None
    __mobile_payment_method_specific_input = None
    __order = None
    __payment_link_order = None
    __payment_link_specific_input = None
    __recipient_name = None
    __redirect_payment_method_specific_input = None
    __sepa_direct_debit_payment_method_specific_input = None

    @property
    def card_payment_method_specific_input(self) -> CardPaymentMethodSpecificInputBase:
        """
        | Object containing the specific input details for card payments

        Type: :class:`onlinepayments.sdk.domain.card_payment_method_specific_input_base.CardPaymentMethodSpecificInputBase`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value: CardPaymentMethodSpecificInputBase):
        self.__card_payment_method_specific_input = value

    @property
    def description(self) -> str:
        """
        | A note related to the created payment link.
        
        | Deprecated: Use `paymentLinkSpecificInput/description` instead.

        Type: str
        """
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value

    @property
    def expiration_date(self) -> str:
        """
        | The date after which the payment link will not be usable to complete the payment. The date sent cannot be more than 6 months in the future or a past date. It must also contain the UTC offset.
        
        | Deprecated: Use `paymentLinkSpecificInput/expirationDate` instead.

        Type: str
        """
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value: str):
        self.__expiration_date = value

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
    def hosted_checkout_specific_input(self) -> HostedCheckoutSpecificInput:
        """
        | Object containing hosted checkout specific data

        Type: :class:`onlinepayments.sdk.domain.hosted_checkout_specific_input.HostedCheckoutSpecificInput`
        """
        return self.__hosted_checkout_specific_input

    @hosted_checkout_specific_input.setter
    def hosted_checkout_specific_input(self, value: HostedCheckoutSpecificInput):
        self.__hosted_checkout_specific_input = value

    @property
    def mobile_payment_method_specific_input(self) -> MobilePaymentMethodHostedCheckoutSpecificInput:
        """
        | Object containing the specific input details for mobile payments

        Type: :class:`onlinepayments.sdk.domain.mobile_payment_method_hosted_checkout_specific_input.MobilePaymentMethodHostedCheckoutSpecificInput`
        """
        return self.__mobile_payment_method_specific_input

    @mobile_payment_method_specific_input.setter
    def mobile_payment_method_specific_input(self, value: MobilePaymentMethodHostedCheckoutSpecificInput):
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
    def payment_link_order(self) -> PaymentLinkOrderInput:
        """
        | An object containing the details of the related payment input.
        
        | Deprecated: All properties in `paymentLinkOrder` are deprecated.  
        | Use corresponding values as noted below:  
        | | Property | Replacement |
        | | - | - |
        | | merchantReference | `order/references/merchantReference` |  
        | | amount | `order/amountOfMoney` |  
        | | surchargeSpecificInput | `order/surchargeSpecificInput` |

        Type: :class:`onlinepayments.sdk.domain.payment_link_order_input.PaymentLinkOrderInput`
        """
        return self.__payment_link_order

    @payment_link_order.setter
    def payment_link_order(self, value: PaymentLinkOrderInput):
        self.__payment_link_order = value

    @property
    def payment_link_specific_input(self) -> PaymentLinkSpecificInput:
        """
        | An object containing details specific to payment link creation

        Type: :class:`onlinepayments.sdk.domain.payment_link_specific_input.PaymentLinkSpecificInput`
        """
        return self.__payment_link_specific_input

    @payment_link_specific_input.setter
    def payment_link_specific_input(self, value: PaymentLinkSpecificInput):
        self.__payment_link_specific_input = value

    @property
    def recipient_name(self) -> str:
        """
        | The payment link recipient name.
        
        | Deprecated: Use `paymentLinkSpecificInput/recipientName` instead.

        Type: str
        """
        return self.__recipient_name

    @recipient_name.setter
    def recipient_name(self, value: str):
        self.__recipient_name = value

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
    def sepa_direct_debit_payment_method_specific_input(self) -> SepaDirectDebitPaymentMethodSpecificInputBase:
        """
        | Object containing the specific input details for SEPA direct debit payments

        Type: :class:`onlinepayments.sdk.domain.sepa_direct_debit_payment_method_specific_input_base.SepaDirectDebitPaymentMethodSpecificInputBase`
        """
        return self.__sepa_direct_debit_payment_method_specific_input

    @sepa_direct_debit_payment_method_specific_input.setter
    def sepa_direct_debit_payment_method_specific_input(self, value: SepaDirectDebitPaymentMethodSpecificInputBase):
        self.__sepa_direct_debit_payment_method_specific_input = value

    def to_dictionary(self):
        dictionary = super(CreatePaymentLinkRequest, self).to_dictionary()
        if self.card_payment_method_specific_input is not None:
            dictionary['cardPaymentMethodSpecificInput'] = self.card_payment_method_specific_input.to_dictionary()
        if self.description is not None:
            dictionary['description'] = self.description
        if self.expiration_date is not None:
            dictionary['expirationDate'] = self.expiration_date
        if self.fraud_fields is not None:
            dictionary['fraudFields'] = self.fraud_fields.to_dictionary()
        if self.hosted_checkout_specific_input is not None:
            dictionary['hostedCheckoutSpecificInput'] = self.hosted_checkout_specific_input.to_dictionary()
        if self.mobile_payment_method_specific_input is not None:
            dictionary['mobilePaymentMethodSpecificInput'] = self.mobile_payment_method_specific_input.to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        if self.payment_link_order is not None:
            dictionary['paymentLinkOrder'] = self.payment_link_order.to_dictionary()
        if self.payment_link_specific_input is not None:
            dictionary['paymentLinkSpecificInput'] = self.payment_link_specific_input.to_dictionary()
        if self.recipient_name is not None:
            dictionary['recipientName'] = self.recipient_name
        if self.redirect_payment_method_specific_input is not None:
            dictionary['redirectPaymentMethodSpecificInput'] = self.redirect_payment_method_specific_input.to_dictionary()
        if self.sepa_direct_debit_payment_method_specific_input is not None:
            dictionary['sepaDirectDebitPaymentMethodSpecificInput'] = self.sepa_direct_debit_payment_method_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatePaymentLinkRequest, self).from_dictionary(dictionary)
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CardPaymentMethodSpecificInputBase()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
        if 'description' in dictionary:
            self.description = dictionary['description']
        if 'expirationDate' in dictionary:
            self.expiration_date = dictionary['expirationDate']
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
        if 'paymentLinkOrder' in dictionary:
            if not isinstance(dictionary['paymentLinkOrder'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentLinkOrder']))
            value = PaymentLinkOrderInput()
            self.payment_link_order = value.from_dictionary(dictionary['paymentLinkOrder'])
        if 'paymentLinkSpecificInput' in dictionary:
            if not isinstance(dictionary['paymentLinkSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentLinkSpecificInput']))
            value = PaymentLinkSpecificInput()
            self.payment_link_specific_input = value.from_dictionary(dictionary['paymentLinkSpecificInput'])
        if 'recipientName' in dictionary:
            self.recipient_name = dictionary['recipientName']
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
