# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class MultiplePaymentInformation(DataObject):
    """
    | Container announcing forecoming subsequent payments. Holds modalities of these subsequent payments.
    """

    __payment_pattern = None
    __total_number_of_payments = None

    @property
    def payment_pattern(self) -> str:
        """
        | Typology of multiple payment. Allowed values:
        |   * PartialShipment

        Type: str
        """
        return self.__payment_pattern

    @payment_pattern.setter
    def payment_pattern(self, value: str):
        self.__payment_pattern = value

    @property
    def total_number_of_payments(self) -> int:
        """
        | Total number of payments. If a payment is implied by this call, it implicitly has ordinal number 1.

        Type: int
        """
        return self.__total_number_of_payments

    @total_number_of_payments.setter
    def total_number_of_payments(self, value: int):
        self.__total_number_of_payments = value

    def to_dictionary(self):
        dictionary = super(MultiplePaymentInformation, self).to_dictionary()
        if self.payment_pattern is not None:
            dictionary['paymentPattern'] = self.payment_pattern
        if self.total_number_of_payments is not None:
            dictionary['totalNumberOfPayments'] = self.total_number_of_payments
        return dictionary

    def from_dictionary(self, dictionary):
        super(MultiplePaymentInformation, self).from_dictionary(dictionary)
        if 'paymentPattern' in dictionary:
            self.payment_pattern = dictionary['paymentPattern']
        if 'totalNumberOfPayments' in dictionary:
            self.total_number_of_payments = dictionary['totalNumberOfPayments']
        return self
