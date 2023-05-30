# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PaymentProduct3209SpecificOutput(DataObject):
    """
    | OneyDuplo Alcampo specific details
    """

    __buyer_compliant_bank_message = None

    @property
    def buyer_compliant_bank_message(self) -> str:
        """
        | This field indicates the text that must be returned and shown to the buyer to be compliant with the law regulating this payment product.

        Type: str
        """
        return self.__buyer_compliant_bank_message

    @buyer_compliant_bank_message.setter
    def buyer_compliant_bank_message(self, value: str):
        self.__buyer_compliant_bank_message = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct3209SpecificOutput, self).to_dictionary()
        if self.buyer_compliant_bank_message is not None:
            dictionary['buyerCompliantBankMessage'] = self.buyer_compliant_bank_message
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct3209SpecificOutput, self).from_dictionary(dictionary)
        if 'buyerCompliantBankMessage' in dictionary:
            self.buyer_compliant_bank_message = dictionary['buyerCompliantBankMessage']
        return self
