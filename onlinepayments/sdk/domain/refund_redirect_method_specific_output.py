# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RefundRedirectMethodSpecificOutput(DataObject):

    __total_amount_paid: Optional[int] = None
    __total_amount_refunded: Optional[int] = None

    @property
    def total_amount_paid(self) -> Optional[int]:
        """
        Type: int
        """
        return self.__total_amount_paid

    @total_amount_paid.setter
    def total_amount_paid(self, value: Optional[int]) -> None:
        self.__total_amount_paid = value

    @property
    def total_amount_refunded(self) -> Optional[int]:
        """
        Type: int
        """
        return self.__total_amount_refunded

    @total_amount_refunded.setter
    def total_amount_refunded(self, value: Optional[int]) -> None:
        self.__total_amount_refunded = value

    def to_dictionary(self) -> dict:
        dictionary = super(RefundRedirectMethodSpecificOutput, self).to_dictionary()
        if self.total_amount_paid is not None:
            dictionary['totalAmountPaid'] = self.total_amount_paid
        if self.total_amount_refunded is not None:
            dictionary['totalAmountRefunded'] = self.total_amount_refunded
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundRedirectMethodSpecificOutput':
        super(RefundRedirectMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'totalAmountPaid' in dictionary:
            self.total_amount_paid = dictionary['totalAmountPaid']
        if 'totalAmountRefunded' in dictionary:
            self.total_amount_refunded = dictionary['totalAmountRefunded']
        return self
