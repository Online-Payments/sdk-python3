# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from datetime import datetime
from typing import Optional

from .amount_of_money import AmountOfMoney
from .card_payment_method_specific_output_summary import CardPaymentMethodSpecificOutputSummary
from .data_object import DataObject
from .payment_references import PaymentReferences


class PaymentOutputSummary(DataObject):

    __amount_of_money: Optional[AmountOfMoney] = None
    __card_payment_method_specific_output: Optional[CardPaymentMethodSpecificOutputSummary] = None
    __references: Optional[PaymentReferences] = None
    __transaction_date: Optional[datetime] = None

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
    def card_payment_method_specific_output(self) -> Optional[CardPaymentMethodSpecificOutputSummary]:
        """
        | Summary of card payment method details for reporting

        Type: :class:`onlinepayments.sdk.domain.card_payment_method_specific_output_summary.CardPaymentMethodSpecificOutputSummary`
        """
        return self.__card_payment_method_specific_output

    @card_payment_method_specific_output.setter
    def card_payment_method_specific_output(self, value: Optional[CardPaymentMethodSpecificOutputSummary]) -> None:
        self.__card_payment_method_specific_output = value

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
    def transaction_date(self) -> Optional[datetime]:
        """
        | Date and time the payment was created in UTC

        Type: datetime
        """
        return self.__transaction_date

    @transaction_date.setter
    def transaction_date(self, value: Optional[datetime]) -> None:
        self.__transaction_date = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentOutputSummary, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.card_payment_method_specific_output is not None:
            dictionary['cardPaymentMethodSpecificOutput'] = self.card_payment_method_specific_output.to_dictionary()
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        if self.transaction_date is not None:
            dictionary['transactionDate'] = DataObject.format_datetime(self.transaction_date)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentOutputSummary':
        super(PaymentOutputSummary, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'cardPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificOutput']))
            value = CardPaymentMethodSpecificOutputSummary()
            self.card_payment_method_specific_output = value.from_dictionary(dictionary['cardPaymentMethodSpecificOutput'])
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = PaymentReferences()
            self.references = value.from_dictionary(dictionary['references'])
        if 'transactionDate' in dictionary:
            self.transaction_date = DataObject.parse_datetime(dictionary['transactionDate'])
        return self
