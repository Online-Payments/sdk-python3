# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_of_money import AmountOfMoney
from .card_payment_method_specific_output import CardPaymentMethodSpecificOutput
from .customer_output import CustomerOutput
from .data_object import DataObject
from .discount import Discount
from .mobile_payment_method_specific_output import MobilePaymentMethodSpecificOutput
from .payment_references import PaymentReferences
from .redirect_payment_method_specific_output import RedirectPaymentMethodSpecificOutput
from .sepa_direct_debit_payment_method_specific_output import SepaDirectDebitPaymentMethodSpecificOutput
from .surcharge_specific_output import SurchargeSpecificOutput


class PaymentOutput(DataObject):

    __acquired_amount: Optional[AmountOfMoney] = None
    __amount_of_money: Optional[AmountOfMoney] = None
    __amount_paid: Optional[int] = None
    __card_payment_method_specific_output: Optional[CardPaymentMethodSpecificOutput] = None
    __customer: Optional[CustomerOutput] = None
    __discount: Optional[Discount] = None
    __merchant_parameters: Optional[str] = None
    __mobile_payment_method_specific_output: Optional[MobilePaymentMethodSpecificOutput] = None
    __payment_method: Optional[str] = None
    __redirect_payment_method_specific_output: Optional[RedirectPaymentMethodSpecificOutput] = None
    __references: Optional[PaymentReferences] = None
    __sepa_direct_debit_payment_method_specific_output: Optional[SepaDirectDebitPaymentMethodSpecificOutput] = None
    __surcharge_specific_output: Optional[SurchargeSpecificOutput] = None

    @property
    def acquired_amount(self) -> Optional[AmountOfMoney]:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__acquired_amount

    @acquired_amount.setter
    def acquired_amount(self, value: Optional[AmountOfMoney]) -> None:
        self.__acquired_amount = value

    @property
    def amount_of_money(self) -> Optional[AmountOfMoney]:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: Optional[AmountOfMoney]) -> None:
        self.__amount_of_money = value

    @property
    def amount_paid(self) -> Optional[int]:
        """
        | Amount that has been paid. This is deprecated. Use acquiredAmount instead.

        Type: int

        Deprecated; Amount that has been paid. This is deprecated. Use acquiredAmount instead.
        """
        return self.__amount_paid

    @amount_paid.setter
    def amount_paid(self, value: Optional[int]) -> None:
        self.__amount_paid = value

    @property
    def card_payment_method_specific_output(self) -> Optional[CardPaymentMethodSpecificOutput]:
        """
        | Object containing the card payment method details

        Type: :class:`onlinepayments.sdk.domain.card_payment_method_specific_output.CardPaymentMethodSpecificOutput`
        """
        return self.__card_payment_method_specific_output

    @card_payment_method_specific_output.setter
    def card_payment_method_specific_output(self, value: Optional[CardPaymentMethodSpecificOutput]) -> None:
        self.__card_payment_method_specific_output = value

    @property
    def customer(self) -> Optional[CustomerOutput]:
        """
        | Object containing the details of the customer

        Type: :class:`onlinepayments.sdk.domain.customer_output.CustomerOutput`
        """
        return self.__customer

    @customer.setter
    def customer(self, value: Optional[CustomerOutput]) -> None:
        self.__customer = value

    @property
    def discount(self) -> Optional[Discount]:
        """
        | Object to apply a discount to the total basket by adding a discount line.

        Type: :class:`onlinepayments.sdk.domain.discount.Discount`
        """
        return self.__discount

    @discount.setter
    def discount(self, value: Optional[Discount]) -> None:
        self.__discount = value

    @property
    def merchant_parameters(self) -> Optional[str]:
        """
        | It allows you to store additional parameters for the transaction in the format you prefer (e.g.-> key-value query string, JSON, etc.) These parameters are then echoed back to you in API GET calls and Webhook notifications. This field must not contain any personal data.

        Type: str
        """
        return self.__merchant_parameters

    @merchant_parameters.setter
    def merchant_parameters(self, value: Optional[str]) -> None:
        self.__merchant_parameters = value

    @property
    def mobile_payment_method_specific_output(self) -> Optional[MobilePaymentMethodSpecificOutput]:
        """
        | Object containing the mobile payment method details

        Type: :class:`onlinepayments.sdk.domain.mobile_payment_method_specific_output.MobilePaymentMethodSpecificOutput`
        """
        return self.__mobile_payment_method_specific_output

    @mobile_payment_method_specific_output.setter
    def mobile_payment_method_specific_output(self, value: Optional[MobilePaymentMethodSpecificOutput]) -> None:
        self.__mobile_payment_method_specific_output = value

    @property
    def payment_method(self) -> Optional[str]:
        """
        | Payment method identifier used by the our payment engine.

        Type: str
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value: Optional[str]) -> None:
        self.__payment_method = value

    @property
    def redirect_payment_method_specific_output(self) -> Optional[RedirectPaymentMethodSpecificOutput]:
        """
        | Object containing the redirect payment product details

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_method_specific_output.RedirectPaymentMethodSpecificOutput`
        """
        return self.__redirect_payment_method_specific_output

    @redirect_payment_method_specific_output.setter
    def redirect_payment_method_specific_output(self, value: Optional[RedirectPaymentMethodSpecificOutput]) -> None:
        self.__redirect_payment_method_specific_output = value

    @property
    def references(self) -> Optional[PaymentReferences]:
        """
        | Object that holds all reference properties that are linked to this transaction. **Deprecated for capture/refund**: Use operationReferences instead.

        Type: :class:`onlinepayments.sdk.domain.payment_references.PaymentReferences`
        """
        return self.__references

    @references.setter
    def references(self, value: Optional[PaymentReferences]) -> None:
        self.__references = value

    @property
    def sepa_direct_debit_payment_method_specific_output(self) -> Optional[SepaDirectDebitPaymentMethodSpecificOutput]:
        """
        | Object containing the SEPA direct debit details

        Type: :class:`onlinepayments.sdk.domain.sepa_direct_debit_payment_method_specific_output.SepaDirectDebitPaymentMethodSpecificOutput`
        """
        return self.__sepa_direct_debit_payment_method_specific_output

    @sepa_direct_debit_payment_method_specific_output.setter
    def sepa_direct_debit_payment_method_specific_output(self, value: Optional[SepaDirectDebitPaymentMethodSpecificOutput]) -> None:
        self.__sepa_direct_debit_payment_method_specific_output = value

    @property
    def surcharge_specific_output(self) -> Optional[SurchargeSpecificOutput]:
        """
        | Object containing specific surcharging attributes applied to an order.

        Type: :class:`onlinepayments.sdk.domain.surcharge_specific_output.SurchargeSpecificOutput`
        """
        return self.__surcharge_specific_output

    @surcharge_specific_output.setter
    def surcharge_specific_output(self, value: Optional[SurchargeSpecificOutput]) -> None:
        self.__surcharge_specific_output = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentOutput, self).to_dictionary()
        if self.acquired_amount is not None:
            dictionary['acquiredAmount'] = self.acquired_amount.to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.amount_paid is not None:
            dictionary['amountPaid'] = self.amount_paid
        if self.card_payment_method_specific_output is not None:
            dictionary['cardPaymentMethodSpecificOutput'] = self.card_payment_method_specific_output.to_dictionary()
        if self.customer is not None:
            dictionary['customer'] = self.customer.to_dictionary()
        if self.discount is not None:
            dictionary['discount'] = self.discount.to_dictionary()
        if self.merchant_parameters is not None:
            dictionary['merchantParameters'] = self.merchant_parameters
        if self.mobile_payment_method_specific_output is not None:
            dictionary['mobilePaymentMethodSpecificOutput'] = self.mobile_payment_method_specific_output.to_dictionary()
        if self.payment_method is not None:
            dictionary['paymentMethod'] = self.payment_method
        if self.redirect_payment_method_specific_output is not None:
            dictionary['redirectPaymentMethodSpecificOutput'] = self.redirect_payment_method_specific_output.to_dictionary()
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        if self.sepa_direct_debit_payment_method_specific_output is not None:
            dictionary['sepaDirectDebitPaymentMethodSpecificOutput'] = self.sepa_direct_debit_payment_method_specific_output.to_dictionary()
        if self.surcharge_specific_output is not None:
            dictionary['surchargeSpecificOutput'] = self.surcharge_specific_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentOutput':
        super(PaymentOutput, self).from_dictionary(dictionary)
        if 'acquiredAmount' in dictionary:
            if not isinstance(dictionary['acquiredAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['acquiredAmount']))
            value = AmountOfMoney()
            self.acquired_amount = value.from_dictionary(dictionary['acquiredAmount'])
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'amountPaid' in dictionary:
            self.amount_paid = dictionary['amountPaid']
        if 'cardPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificOutput']))
            value = CardPaymentMethodSpecificOutput()
            self.card_payment_method_specific_output = value.from_dictionary(dictionary['cardPaymentMethodSpecificOutput'])
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = CustomerOutput()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'discount' in dictionary:
            if not isinstance(dictionary['discount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['discount']))
            value = Discount()
            self.discount = value.from_dictionary(dictionary['discount'])
        if 'merchantParameters' in dictionary:
            self.merchant_parameters = dictionary['merchantParameters']
        if 'mobilePaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['mobilePaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobilePaymentMethodSpecificOutput']))
            value = MobilePaymentMethodSpecificOutput()
            self.mobile_payment_method_specific_output = value.from_dictionary(dictionary['mobilePaymentMethodSpecificOutput'])
        if 'paymentMethod' in dictionary:
            self.payment_method = dictionary['paymentMethod']
        if 'redirectPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['redirectPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectPaymentMethodSpecificOutput']))
            value = RedirectPaymentMethodSpecificOutput()
            self.redirect_payment_method_specific_output = value.from_dictionary(dictionary['redirectPaymentMethodSpecificOutput'])
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = PaymentReferences()
            self.references = value.from_dictionary(dictionary['references'])
        if 'sepaDirectDebitPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['sepaDirectDebitPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['sepaDirectDebitPaymentMethodSpecificOutput']))
            value = SepaDirectDebitPaymentMethodSpecificOutput()
            self.sepa_direct_debit_payment_method_specific_output = value.from_dictionary(dictionary['sepaDirectDebitPaymentMethodSpecificOutput'])
        if 'surchargeSpecificOutput' in dictionary:
            if not isinstance(dictionary['surchargeSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeSpecificOutput']))
            value = SurchargeSpecificOutput()
            self.surcharge_specific_output = value.from_dictionary(dictionary['surchargeSpecificOutput'])
        return self
