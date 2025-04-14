# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .g_pay_three_d_secure import GPayThreeDSecure


class MobilePaymentProduct320SpecificInput(DataObject):

    __three_d_secure: Optional[GPayThreeDSecure] = None

    @property
    def three_d_secure(self) -> Optional[GPayThreeDSecure]:
        """
        | Object containing specific data regarding 3-D Secure

        Type: :class:`onlinepayments.sdk.domain.g_pay_three_d_secure.GPayThreeDSecure`
        """
        return self.__three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, value: Optional[GPayThreeDSecure]) -> None:
        self.__three_d_secure = value

    def to_dictionary(self) -> dict:
        dictionary = super(MobilePaymentProduct320SpecificInput, self).to_dictionary()
        if self.three_d_secure is not None:
            dictionary['threeDSecure'] = self.three_d_secure.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MobilePaymentProduct320SpecificInput':
        super(MobilePaymentProduct320SpecificInput, self).from_dictionary(dictionary)
        if 'threeDSecure' in dictionary:
            if not isinstance(dictionary['threeDSecure'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecure']))
            value = GPayThreeDSecure()
            self.three_d_secure = value.from_dictionary(dictionary['threeDSecure'])
        return self
