# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct771SpecificOutput(DataObject):

    __mandate_reference: Optional[str] = None

    @property
    def mandate_reference(self) -> Optional[str]:
        """
        | Unique reference to a Mandate

        Type: str
        """
        return self.__mandate_reference

    @mandate_reference.setter
    def mandate_reference(self, value: Optional[str]) -> None:
        self.__mandate_reference = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct771SpecificOutput, self).to_dictionary()
        if self.mandate_reference is not None:
            dictionary['mandateReference'] = self.mandate_reference
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct771SpecificOutput':
        super(PaymentProduct771SpecificOutput, self).from_dictionary(dictionary)
        if 'mandateReference' in dictionary:
            self.mandate_reference = dictionary['mandateReference']
        return self
