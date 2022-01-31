# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class RefundMobileMethodSpecificOutput(DataObject):
    __network = None
    __total_amount_paid = None
    __total_amount_refunded = None

    @property
    def network(self) -> str:
        """
        Type: str
        """
        return self.__network

    @network.setter
    def network(self, value: str):
        self.__network = value

    @property
    def total_amount_paid(self) -> int:
        """
        Type: int
        """
        return self.__total_amount_paid

    @total_amount_paid.setter
    def total_amount_paid(self, value: int):
        self.__total_amount_paid = value

    @property
    def total_amount_refunded(self) -> int:
        """
        Type: int
        """
        return self.__total_amount_refunded

    @total_amount_refunded.setter
    def total_amount_refunded(self, value: int):
        self.__total_amount_refunded = value

    def to_dictionary(self):
        dictionary = super(RefundMobileMethodSpecificOutput, self).to_dictionary()
        if self.network is not None:
            dictionary['network'] = self.network
        if self.total_amount_paid is not None:
            dictionary['totalAmountPaid'] = self.total_amount_paid
        if self.total_amount_refunded is not None:
            dictionary['totalAmountRefunded'] = self.total_amount_refunded
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundMobileMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'network' in dictionary:
            self.network = dictionary['network']
        if 'totalAmountPaid' in dictionary:
            self.total_amount_paid = dictionary['totalAmountPaid']
        if 'totalAmountRefunded' in dictionary:
            self.total_amount_refunded = dictionary['totalAmountRefunded']
        return self
