# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class MobilePaymentData(DataObject):
    """
    | Object containing payment details
    """

    __dpan = None
    __expiry_date = None

    @property
    def dpan(self) -> str:
        """
        | The obfuscated DPAN. Only the last four digits are visible.

        Type: str
        """
        return self.__dpan

    @dpan.setter
    def dpan(self, value: str):
        self.__dpan = value

    @property
    def expiry_date(self) -> str:
        """
        | Expiry date of the tokenized card. Format: MMYY

        Type: str
        """
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value: str):
        self.__expiry_date = value

    def to_dictionary(self):
        dictionary = super(MobilePaymentData, self).to_dictionary()
        if self.dpan is not None:
            dictionary['dpan'] = self.dpan
        if self.expiry_date is not None:
            dictionary['expiryDate'] = self.expiry_date
        return dictionary

    def from_dictionary(self, dictionary):
        super(MobilePaymentData, self).from_dictionary(dictionary)
        if 'dpan' in dictionary:
            self.dpan = dictionary['dpan']
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        return self
