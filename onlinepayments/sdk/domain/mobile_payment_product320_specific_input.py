# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.g_pay_three_d_secure import GPayThreeDSecure


class MobilePaymentProduct320SpecificInput(DataObject):
    """
    | Object containing information specific to Google Pay. Required for payments with product 320.
    """

    __three_d_secure = None

    @property
    def three_d_secure(self) -> GPayThreeDSecure:
        """
        | Object containing specific data regarding 3-D Secure

        Type: :class:`onlinepayments.sdk.domain.g_pay_three_d_secure.GPayThreeDSecure`
        """
        return self.__three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, value: GPayThreeDSecure):
        self.__three_d_secure = value

    def to_dictionary(self):
        dictionary = super(MobilePaymentProduct320SpecificInput, self).to_dictionary()
        if self.three_d_secure is not None:
            dictionary['threeDSecure'] = self.three_d_secure.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(MobilePaymentProduct320SpecificInput, self).from_dictionary(dictionary)
        if 'threeDSecure' in dictionary:
            if not isinstance(dictionary['threeDSecure'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecure']))
            value = GPayThreeDSecure()
            self.three_d_secure = value.from_dictionary(dictionary['threeDSecure'])
        return self
