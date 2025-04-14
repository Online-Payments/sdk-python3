# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct5500SpecificOutput(DataObject):

    __entity_id: Optional[str] = None
    __payment_end_date: Optional[str] = None
    __payment_reference: Optional[str] = None
    __payment_start_date: Optional[str] = None

    @property
    def entity_id(self) -> Optional[str]:
        """
        | The reference to be used during Multibanco payment for reconciliation matter

        Type: str
        """
        return self.__entity_id

    @entity_id.setter
    def entity_id(self, value: Optional[str]) -> None:
        self.__entity_id = value

    @property
    def payment_end_date(self) -> Optional[str]:
        """
        | The end date of the payment validity

        Type: str
        """
        return self.__payment_end_date

    @payment_end_date.setter
    def payment_end_date(self, value: Optional[str]) -> None:
        self.__payment_end_date = value

    @property
    def payment_reference(self) -> Optional[str]:
        """
        | The reference to be used within the Multibanco network to confirm the payment

        Type: str
        """
        return self.__payment_reference

    @payment_reference.setter
    def payment_reference(self, value: Optional[str]) -> None:
        self.__payment_reference = value

    @property
    def payment_start_date(self) -> Optional[str]:
        """
        | The start date of the payment validity

        Type: str
        """
        return self.__payment_start_date

    @payment_start_date.setter
    def payment_start_date(self, value: Optional[str]) -> None:
        self.__payment_start_date = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct5500SpecificOutput, self).to_dictionary()
        if self.entity_id is not None:
            dictionary['entityId'] = self.entity_id
        if self.payment_end_date is not None:
            dictionary['paymentEndDate'] = self.payment_end_date
        if self.payment_reference is not None:
            dictionary['paymentReference'] = self.payment_reference
        if self.payment_start_date is not None:
            dictionary['paymentStartDate'] = self.payment_start_date
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct5500SpecificOutput':
        super(PaymentProduct5500SpecificOutput, self).from_dictionary(dictionary)
        if 'entityId' in dictionary:
            self.entity_id = dictionary['entityId']
        if 'paymentEndDate' in dictionary:
            self.payment_end_date = dictionary['paymentEndDate']
        if 'paymentReference' in dictionary:
            self.payment_reference = dictionary['paymentReference']
        if 'paymentStartDate' in dictionary:
            self.payment_start_date = dictionary['paymentStartDate']
        return self
