# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PaymentProduct771SpecificOutput(DataObject):
    """
    | Output that is SEPA Direct Debit specific (i.e. the used mandate)
    """

    __mandate_reference = None

    @property
    def mandate_reference(self) -> str:
        """
        | Unique reference to a Mandate

        Type: str
        """
        return self.__mandate_reference

    @mandate_reference.setter
    def mandate_reference(self, value: str):
        self.__mandate_reference = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct771SpecificOutput, self).to_dictionary()
        if self.mandate_reference is not None:
            dictionary['mandateReference'] = self.mandate_reference
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct771SpecificOutput, self).from_dictionary(dictionary)
        if 'mandateReference' in dictionary:
            self.mandate_reference = dictionary['mandateReference']
        return self
