# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_of_money import AmountOfMoney
from .data_object import DataObject
from .operation_payment_references import OperationPaymentReferences
from .payment_references import PaymentReferences
from .refund_card_method_specific_output import RefundCardMethodSpecificOutput
from .refund_e_wallet_method_specific_output import RefundEWalletMethodSpecificOutput
from .refund_mobile_method_specific_output import RefundMobileMethodSpecificOutput
from .refund_redirect_method_specific_output import RefundRedirectMethodSpecificOutput


class RefundOutput(DataObject):

    __amount_of_money: Optional[AmountOfMoney] = None
    __amount_paid: Optional[int] = None
    __card_refund_method_specific_output: Optional[RefundCardMethodSpecificOutput] = None
    __e_wallet_refund_method_specific_output: Optional[RefundEWalletMethodSpecificOutput] = None
    __merchant_parameters: Optional[str] = None
    __mobile_refund_method_specific_output: Optional[RefundMobileMethodSpecificOutput] = None
    __operation_references: Optional[OperationPaymentReferences] = None
    __payment_method: Optional[str] = None
    __redirect_refund_method_specific_output: Optional[RefundRedirectMethodSpecificOutput] = None
    __references: Optional[PaymentReferences] = None

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
        Type: int
        """
        return self.__amount_paid

    @amount_paid.setter
    def amount_paid(self, value: Optional[int]) -> None:
        self.__amount_paid = value

    @property
    def card_refund_method_specific_output(self) -> Optional[RefundCardMethodSpecificOutput]:
        """
        Type: :class:`onlinepayments.sdk.domain.refund_card_method_specific_output.RefundCardMethodSpecificOutput`
        """
        return self.__card_refund_method_specific_output

    @card_refund_method_specific_output.setter
    def card_refund_method_specific_output(self, value: Optional[RefundCardMethodSpecificOutput]) -> None:
        self.__card_refund_method_specific_output = value

    @property
    def e_wallet_refund_method_specific_output(self) -> Optional[RefundEWalletMethodSpecificOutput]:
        """
        Type: :class:`onlinepayments.sdk.domain.refund_e_wallet_method_specific_output.RefundEWalletMethodSpecificOutput`
        """
        return self.__e_wallet_refund_method_specific_output

    @e_wallet_refund_method_specific_output.setter
    def e_wallet_refund_method_specific_output(self, value: Optional[RefundEWalletMethodSpecificOutput]) -> None:
        self.__e_wallet_refund_method_specific_output = value

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
    def mobile_refund_method_specific_output(self) -> Optional[RefundMobileMethodSpecificOutput]:
        """
        Type: :class:`onlinepayments.sdk.domain.refund_mobile_method_specific_output.RefundMobileMethodSpecificOutput`
        """
        return self.__mobile_refund_method_specific_output

    @mobile_refund_method_specific_output.setter
    def mobile_refund_method_specific_output(self, value: Optional[RefundMobileMethodSpecificOutput]) -> None:
        self.__mobile_refund_method_specific_output = value

    @property
    def operation_references(self) -> Optional[OperationPaymentReferences]:
        """
        | Object that holds all reference properties that are linked to this transaction

        Type: :class:`onlinepayments.sdk.domain.operation_payment_references.OperationPaymentReferences`
        """
        return self.__operation_references

    @operation_references.setter
    def operation_references(self, value: Optional[OperationPaymentReferences]) -> None:
        self.__operation_references = value

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
    def redirect_refund_method_specific_output(self) -> Optional[RefundRedirectMethodSpecificOutput]:
        """
        Type: :class:`onlinepayments.sdk.domain.refund_redirect_method_specific_output.RefundRedirectMethodSpecificOutput`
        """
        return self.__redirect_refund_method_specific_output

    @redirect_refund_method_specific_output.setter
    def redirect_refund_method_specific_output(self, value: Optional[RefundRedirectMethodSpecificOutput]) -> None:
        self.__redirect_refund_method_specific_output = value

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

    def to_dictionary(self) -> dict:
        dictionary = super(RefundOutput, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.amount_paid is not None:
            dictionary['amountPaid'] = self.amount_paid
        if self.card_refund_method_specific_output is not None:
            dictionary['cardRefundMethodSpecificOutput'] = self.card_refund_method_specific_output.to_dictionary()
        if self.e_wallet_refund_method_specific_output is not None:
            dictionary['eWalletRefundMethodSpecificOutput'] = self.e_wallet_refund_method_specific_output.to_dictionary()
        if self.merchant_parameters is not None:
            dictionary['merchantParameters'] = self.merchant_parameters
        if self.mobile_refund_method_specific_output is not None:
            dictionary['mobileRefundMethodSpecificOutput'] = self.mobile_refund_method_specific_output.to_dictionary()
        if self.operation_references is not None:
            dictionary['operationReferences'] = self.operation_references.to_dictionary()
        if self.payment_method is not None:
            dictionary['paymentMethod'] = self.payment_method
        if self.redirect_refund_method_specific_output is not None:
            dictionary['redirectRefundMethodSpecificOutput'] = self.redirect_refund_method_specific_output.to_dictionary()
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundOutput':
        super(RefundOutput, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'amountPaid' in dictionary:
            self.amount_paid = dictionary['amountPaid']
        if 'cardRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['cardRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardRefundMethodSpecificOutput']))
            value = RefundCardMethodSpecificOutput()
            self.card_refund_method_specific_output = value.from_dictionary(dictionary['cardRefundMethodSpecificOutput'])
        if 'eWalletRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['eWalletRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['eWalletRefundMethodSpecificOutput']))
            value = RefundEWalletMethodSpecificOutput()
            self.e_wallet_refund_method_specific_output = value.from_dictionary(dictionary['eWalletRefundMethodSpecificOutput'])
        if 'merchantParameters' in dictionary:
            self.merchant_parameters = dictionary['merchantParameters']
        if 'mobileRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['mobileRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobileRefundMethodSpecificOutput']))
            value = RefundMobileMethodSpecificOutput()
            self.mobile_refund_method_specific_output = value.from_dictionary(dictionary['mobileRefundMethodSpecificOutput'])
        if 'operationReferences' in dictionary:
            if not isinstance(dictionary['operationReferences'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['operationReferences']))
            value = OperationPaymentReferences()
            self.operation_references = value.from_dictionary(dictionary['operationReferences'])
        if 'paymentMethod' in dictionary:
            self.payment_method = dictionary['paymentMethod']
        if 'redirectRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['redirectRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectRefundMethodSpecificOutput']))
            value = RefundRedirectMethodSpecificOutput()
            self.redirect_refund_method_specific_output = value.from_dictionary(dictionary['redirectRefundMethodSpecificOutput'])
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = PaymentReferences()
            self.references = value.from_dictionary(dictionary['references'])
        return self
