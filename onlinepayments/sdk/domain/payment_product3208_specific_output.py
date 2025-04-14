# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct3208SpecificOutput(DataObject):

    __buyer_compliant_bank_message: Optional[str] = None

    @property
    def buyer_compliant_bank_message(self) -> Optional[str]:
        """
        | This field indicates the text that must be returned and shown to the buyer to be compliant with the law regulating this payment product.

        Type: str
        """
        return self.__buyer_compliant_bank_message

    @buyer_compliant_bank_message.setter
    def buyer_compliant_bank_message(self, value: Optional[str]) -> None:
        self.__buyer_compliant_bank_message = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct3208SpecificOutput, self).to_dictionary()
        if self.buyer_compliant_bank_message is not None:
            dictionary['buyerCompliantBankMessage'] = self.buyer_compliant_bank_message
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct3208SpecificOutput':
        super(PaymentProduct3208SpecificOutput, self).from_dictionary(dictionary)
        if 'buyerCompliantBankMessage' in dictionary:
            self.buyer_compliant_bank_message = dictionary['buyerCompliantBankMessage']
        return self
