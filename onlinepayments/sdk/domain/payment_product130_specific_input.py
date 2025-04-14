# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .payment_product130_specific_three_d_secure import PaymentProduct130SpecificThreeDSecure


class PaymentProduct130SpecificInput(DataObject):

    __three_d_secure: Optional[PaymentProduct130SpecificThreeDSecure] = None

    @property
    def three_d_secure(self) -> Optional[PaymentProduct130SpecificThreeDSecure]:
        """
        | Object containing specific data regarding 3-D Secure

        Type: :class:`onlinepayments.sdk.domain.payment_product130_specific_three_d_secure.PaymentProduct130SpecificThreeDSecure`
        """
        return self.__three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, value: Optional[PaymentProduct130SpecificThreeDSecure]) -> None:
        self.__three_d_secure = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct130SpecificInput, self).to_dictionary()
        if self.three_d_secure is not None:
            dictionary['threeDSecure'] = self.three_d_secure.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct130SpecificInput':
        super(PaymentProduct130SpecificInput, self).from_dictionary(dictionary)
        if 'threeDSecure' in dictionary:
            if not isinstance(dictionary['threeDSecure'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecure']))
            value = PaymentProduct130SpecificThreeDSecure()
            self.three_d_secure = value.from_dictionary(dictionary['threeDSecure'])
        return self
