# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from datetime import datetime
from typing import Optional

from .amount_of_money import AmountOfMoney
from .data_object import DataObject
from .payment_references import PaymentReferences
from .payout_card_payment_method_specific_output import PayoutCardPaymentMethodSpecificOutput


class PayoutOutput(DataObject):

    __amount_of_money: Optional[AmountOfMoney] = None
    __payout_card_payment_method_specific_output: Optional[PayoutCardPaymentMethodSpecificOutput] = None
    __payout_reason: Optional[str] = None
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
    def payout_card_payment_method_specific_output(self) -> Optional[PayoutCardPaymentMethodSpecificOutput]:
        """
        | Object containing the card payment method details in a Payout context

        Type: :class:`onlinepayments.sdk.domain.payout_card_payment_method_specific_output.PayoutCardPaymentMethodSpecificOutput`
        """
        return self.__payout_card_payment_method_specific_output

    @payout_card_payment_method_specific_output.setter
    def payout_card_payment_method_specific_output(self, value: Optional[PayoutCardPaymentMethodSpecificOutput]) -> None:
        self.__payout_card_payment_method_specific_output = value

    @property
    def payout_reason(self) -> Optional[str]:
        """
        | Allows you to additionally specify the reason for initiating the payout for authorization purposes. If this field is not specified, authorization of the payment will be made according to your merchant profile. Possible values are:
        
        * Gambling
        * Refund
        * Loyalty

        Type: str
        """
        return self.__payout_reason

    @payout_reason.setter
    def payout_reason(self, value: Optional[str]) -> None:
        self.__payout_reason = value

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
        | It is the server-side processing date and time of the transaction.

        Type: datetime
        """
        return self.__transaction_date

    @transaction_date.setter
    def transaction_date(self, value: Optional[datetime]) -> None:
        self.__transaction_date = value

    def to_dictionary(self) -> dict:
        dictionary = super(PayoutOutput, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.payout_card_payment_method_specific_output is not None:
            dictionary['payoutCardPaymentMethodSpecificOutput'] = self.payout_card_payment_method_specific_output.to_dictionary()
        if self.payout_reason is not None:
            dictionary['payoutReason'] = self.payout_reason
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        if self.transaction_date is not None:
            dictionary['transactionDate'] = DataObject.format_datetime(self.transaction_date)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PayoutOutput':
        super(PayoutOutput, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'payoutCardPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['payoutCardPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payoutCardPaymentMethodSpecificOutput']))
            value = PayoutCardPaymentMethodSpecificOutput()
            self.payout_card_payment_method_specific_output = value.from_dictionary(dictionary['payoutCardPaymentMethodSpecificOutput'])
        if 'payoutReason' in dictionary:
            self.payout_reason = dictionary['payoutReason']
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = PaymentReferences()
            self.references = value.from_dictionary(dictionary['references'])
        if 'transactionDate' in dictionary:
            self.transaction_date = DataObject.parse_datetime(dictionary['transactionDate'])
        return self
