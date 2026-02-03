# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RefundRedirectPaymentProduct900SpecificInput(DataObject):

    __refund_reason: Optional[str] = None

    @property
    def refund_reason(self) -> Optional[str]:
        """
        | The reason for the refund, required for Wero payments. This value is sent to the consumer’s bank as part of the Wero refund request and will be shown to the consumer in their banking application. If not provided, the value defaults to "Other".

        Type: str
        """
        return self.__refund_reason

    @refund_reason.setter
    def refund_reason(self, value: Optional[str]) -> None:
        self.__refund_reason = value

    def to_dictionary(self) -> dict:
        dictionary = super(RefundRedirectPaymentProduct900SpecificInput, self).to_dictionary()
        if self.refund_reason is not None:
            dictionary['refundReason'] = self.refund_reason
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundRedirectPaymentProduct900SpecificInput':
        super(RefundRedirectPaymentProduct900SpecificInput, self).from_dictionary(dictionary)
        if 'refundReason' in dictionary:
            self.refund_reason = dictionary['refundReason']
        return self
