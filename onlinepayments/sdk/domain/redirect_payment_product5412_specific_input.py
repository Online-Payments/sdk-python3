# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RedirectPaymentProduct5412SpecificInput(DataObject):

    __adjustable_amount: Optional[bool] = None
    __beneficiary_id: Optional[str] = None

    @property
    def adjustable_amount(self) -> Optional[bool]:
        """
        | If true, the customer can adjust the portion of the total amount paid using this payment method in the ANCV app at authentication time.

        Type: bool
        """
        return self.__adjustable_amount

    @adjustable_amount.setter
    def adjustable_amount(self, value: Optional[bool]) -> None:
        self.__adjustable_amount = value

    @property
    def beneficiary_id(self) -> Optional[str]:
        """
        | The 11 digits CV Connect ID of the customer. If this ID is not provided, the customer's e-mail address will be used, if available. The customer will be able to confirm their ID before proceeding with payment.

        Type: str
        """
        return self.__beneficiary_id

    @beneficiary_id.setter
    def beneficiary_id(self, value: Optional[str]) -> None:
        self.__beneficiary_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct5412SpecificInput, self).to_dictionary()
        if self.adjustable_amount is not None:
            dictionary['adjustableAmount'] = self.adjustable_amount
        if self.beneficiary_id is not None:
            dictionary['beneficiaryId'] = self.beneficiary_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5412SpecificInput':
        super(RedirectPaymentProduct5412SpecificInput, self).from_dictionary(dictionary)
        if 'adjustableAmount' in dictionary:
            self.adjustable_amount = dictionary['adjustableAmount']
        if 'beneficiaryId' in dictionary:
            self.beneficiary_id = dictionary['beneficiaryId']
        return self
