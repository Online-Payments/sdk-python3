# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class ApplePayLineItem(DataObject):

    __amount: Optional[str] = None
    __label: Optional[str] = None
    __payment_timing: Optional[str] = None
    __recurring_payment_end_date: Optional[str] = None
    __recurring_payment_interval_count: Optional[int] = None
    __recurring_payment_interval_unit: Optional[str] = None
    __recurring_payment_start_date: Optional[str] = None

    @property
    def amount(self) -> Optional[str]:
        """
        | A required value that’s the monetary amount of the line item.

        Type: str
        """
        return self.__amount

    @amount.setter
    def amount(self, value: Optional[str]) -> None:
        self.__amount = value

    @property
    def label(self) -> Optional[str]:
        """
        | A required value that’s a short, localized description of the line item.

        Type: str
        """
        return self.__label

    @label.setter
    def label(self, value: Optional[str]) -> None:
        self.__label = value

    @property
    def payment_timing(self) -> Optional[str]:
        """
        | The time that the payment occurs as part of a successful transaction.

        Type: str
        """
        return self.__payment_timing

    @payment_timing.setter
    def payment_timing(self, value: Optional[str]) -> None:
        self.__payment_timing = value

    @property
    def recurring_payment_end_date(self) -> Optional[str]:
        """
        | The date of the final payment. Example 2022-01-01T00:00:00

        Type: str
        """
        return self.__recurring_payment_end_date

    @recurring_payment_end_date.setter
    def recurring_payment_end_date(self, value: Optional[str]) -> None:
        self.__recurring_payment_end_date = value

    @property
    def recurring_payment_interval_count(self) -> Optional[int]:
        """
        | The number of interval units that make up the total payment interval.

        Type: int
        """
        return self.__recurring_payment_interval_count

    @recurring_payment_interval_count.setter
    def recurring_payment_interval_count(self, value: Optional[int]) -> None:
        self.__recurring_payment_interval_count = value

    @property
    def recurring_payment_interval_unit(self) -> Optional[str]:
        """
        | The amount of time — in calendar units, such as day, month, or year — that represents a fraction of the total payment interval.

        Type: str
        """
        return self.__recurring_payment_interval_unit

    @recurring_payment_interval_unit.setter
    def recurring_payment_interval_unit(self, value: Optional[str]) -> None:
        self.__recurring_payment_interval_unit = value

    @property
    def recurring_payment_start_date(self) -> Optional[str]:
        """
        | The date of the first payment. Example 2022-01-01T00:00:00

        Type: str
        """
        return self.__recurring_payment_start_date

    @recurring_payment_start_date.setter
    def recurring_payment_start_date(self, value: Optional[str]) -> None:
        self.__recurring_payment_start_date = value

    def to_dictionary(self) -> dict:
        dictionary = super(ApplePayLineItem, self).to_dictionary()
        if self.amount is not None:
            dictionary['amount'] = self.amount
        if self.label is not None:
            dictionary['label'] = self.label
        if self.payment_timing is not None:
            dictionary['paymentTiming'] = self.payment_timing
        if self.recurring_payment_end_date is not None:
            dictionary['recurringPaymentEndDate'] = self.recurring_payment_end_date
        if self.recurring_payment_interval_count is not None:
            dictionary['recurringPaymentIntervalCount'] = self.recurring_payment_interval_count
        if self.recurring_payment_interval_unit is not None:
            dictionary['recurringPaymentIntervalUnit'] = self.recurring_payment_interval_unit
        if self.recurring_payment_start_date is not None:
            dictionary['recurringPaymentStartDate'] = self.recurring_payment_start_date
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ApplePayLineItem':
        super(ApplePayLineItem, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            self.amount = dictionary['amount']
        if 'label' in dictionary:
            self.label = dictionary['label']
        if 'paymentTiming' in dictionary:
            self.payment_timing = dictionary['paymentTiming']
        if 'recurringPaymentEndDate' in dictionary:
            self.recurring_payment_end_date = dictionary['recurringPaymentEndDate']
        if 'recurringPaymentIntervalCount' in dictionary:
            self.recurring_payment_interval_count = dictionary['recurringPaymentIntervalCount']
        if 'recurringPaymentIntervalUnit' in dictionary:
            self.recurring_payment_interval_unit = dictionary['recurringPaymentIntervalUnit']
        if 'recurringPaymentStartDate' in dictionary:
            self.recurring_payment_start_date = dictionary['recurringPaymentStartDate']
        return self
