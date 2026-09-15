# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class MultiplePaymentInformation(DataObject):

    __payment_pattern: Optional[str] = None
    __total_number_of_payments: Optional[int] = None

    @property
    def payment_pattern(self) -> Optional[str]:
        """
        | Typology of multiple payment. Allowed values:
        
        * PartialShipment - I-P e-Commerce scenario whereby credentials have been stored to enable subsequent MITs per shipment. For this type of use case, PartialShipment is expected on both the initial CIT and eventual subsequent MITs to complete the order.
        * Recurring - Transactions processed at fixed amount, regular intervals not to exceed one year between Transactions, representing an agreement between a cardholder and a merchant to purchase goods or services provided over a period of time. Note that a recurring MIT transaction is initiated by the merchant (payee) not the customer (payer) and so is out of scope of PSD2. Recurring transactions that are in scope of PSD2 (and therefore may benefit from the recurring transaction exemption) are those that are customer (payer) initiates, e.g. standing orders set up from a bank account.
        * Unscheduled - A transaction using a stored credential for a variable amount that does not occur on a scheduled or regularly occurring transaction date, where the cardholder has provided consent for the merchant to initiate one or more future transactions which are not initiated by the cardholder. This transaction type is based on an agreement with the cardholder and is not to be confused with cardholder initiated transactions performed with stored credentials (CITs are in scope of PSD2 whereas UCOF transactions are MITs and thus out of scope).
        * RecurringVariable - Transactions processed at variable amount, regular intervals not to exceed one year between Transactions, representing an agreement between a cardholder and a merchant to purchase goods or services provided over a period of time. Note that a recurring MIT transaction is initiated by the merchant (payee) not the customer (payer) and so is out of scope of PSD2. Recurring transactions that are in scope of PSD2 (and therefore may benefit from the recurring transaction exemption) are those that are customer (payer) initiates, e.g. standing orders set up from a bank account.
        * UnscheduledFixed - A transaction using a stored credential for a fixed amount that does not occur on a scheduled or regularly occurring transaction date, where the cardholder has provided consent for the merchant to initiate one or more future transactions which are not initiated by the cardholder. This transaction type is based on an agreement with the cardholder and is not to be confused with cardholder initiated transactions performed with stored credentials (CITs are in scope of PSD2 whereas UCOF transactions are MITs and thus out of scope).

        Type: str
        """
        return self.__payment_pattern

    @payment_pattern.setter
    def payment_pattern(self, value: Optional[str]) -> None:
        self.__payment_pattern = value

    @property
    def total_number_of_payments(self) -> Optional[int]:
        """
        | Total number of payments. If a payment is implied by this call, it implicitly has ordinal number 1.

        Type: int
        """
        return self.__total_number_of_payments

    @total_number_of_payments.setter
    def total_number_of_payments(self, value: Optional[int]) -> None:
        self.__total_number_of_payments = value

    def to_dictionary(self) -> dict:
        dictionary = super(MultiplePaymentInformation, self).to_dictionary()
        if self.payment_pattern is not None:
            dictionary['paymentPattern'] = self.payment_pattern
        if self.total_number_of_payments is not None:
            dictionary['totalNumberOfPayments'] = self.total_number_of_payments
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MultiplePaymentInformation':
        super(MultiplePaymentInformation, self).from_dictionary(dictionary)
        if 'paymentPattern' in dictionary:
            self.payment_pattern = dictionary['paymentPattern']
        if 'totalNumberOfPayments' in dictionary:
            self.total_number_of_payments = dictionary['totalNumberOfPayments']
        return self
