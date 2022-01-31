# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class ThreeDSecureResults(DataObject):
    """
    | 3D Secure results object
    """

    __eci = None
    __xid = None

    @property
    def eci(self) -> str:
        """
        | Indicates Authentication validation results returned after AuthenticationValidation

        Type: str
        """
        return self.__eci

    @eci.setter
    def eci(self, value: str):
        self.__eci = value

    @property
    def xid(self) -> str:
        """
        | Transaction ID for the Authentication

        Type: str
        """
        return self.__xid

    @xid.setter
    def xid(self, value: str):
        self.__xid = value

    def to_dictionary(self):
        dictionary = super(ThreeDSecureResults, self).to_dictionary()
        if self.eci is not None:
            dictionary['eci'] = self.eci
        if self.xid is not None:
            dictionary['xid'] = self.xid
        return dictionary

    def from_dictionary(self, dictionary):
        super(ThreeDSecureResults, self).from_dictionary(dictionary)
        if 'eci' in dictionary:
            self.eci = dictionary['eci']
        if 'xid' in dictionary:
            self.xid = dictionary['xid']
        return self
