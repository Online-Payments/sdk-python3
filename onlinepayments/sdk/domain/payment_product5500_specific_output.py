# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PaymentProduct5500SpecificOutput(DataObject):
    """
    | Multibanco (payment product 5500) specific details
    """

    __payment_end_date = None
    __payment_reference = None
    __payment_start_date = None

    @property
    def payment_end_date(self) -> str:
        """
        | The end date of the payment validity

        Type: str
        """
        return self.__payment_end_date

    @payment_end_date.setter
    def payment_end_date(self, value: str):
        self.__payment_end_date = value

    @property
    def payment_reference(self) -> str:
        """
        | The reference to be used within the Multibanco network to confirm the payment

        Type: str
        """
        return self.__payment_reference

    @payment_reference.setter
    def payment_reference(self, value: str):
        self.__payment_reference = value

    @property
    def payment_start_date(self) -> str:
        """
        | The start date of the payment validity

        Type: str
        """
        return self.__payment_start_date

    @payment_start_date.setter
    def payment_start_date(self, value: str):
        self.__payment_start_date = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct5500SpecificOutput, self).to_dictionary()
        if self.payment_end_date is not None:
            dictionary['paymentEndDate'] = self.payment_end_date
        if self.payment_reference is not None:
            dictionary['paymentReference'] = self.payment_reference
        if self.payment_start_date is not None:
            dictionary['paymentStartDate'] = self.payment_start_date
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct5500SpecificOutput, self).from_dictionary(dictionary)
        if 'paymentEndDate' in dictionary:
            self.payment_end_date = dictionary['paymentEndDate']
        if 'paymentReference' in dictionary:
            self.payment_reference = dictionary['paymentReference']
        if 'paymentStartDate' in dictionary:
            self.payment_start_date = dictionary['paymentStartDate']
        return self
