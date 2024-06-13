# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class ThreeDSWhitelist(DataObject):
    __source = None
    __status = None

    @property
    def source(self) -> str:
        """
        | Whitelist Status Source. This data element will be populated by the system setting Whitelist Status

        Type: str
        """
        return self.__source

    @source.setter
    def source(self, value: str):
        self.__source = value

    @property
    def status(self) -> str:
        """
        | Whitelist Status. Enables the communication of trusted beneficiary/whitelist status between the ACS, the DS and the 3DS Requestor.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: str):
        self.__status = value

    def to_dictionary(self):
        dictionary = super(ThreeDSWhitelist, self).to_dictionary()
        if self.source is not None:
            dictionary['source'] = self.source
        if self.status is not None:
            dictionary['status'] = self.status
        return dictionary

    def from_dictionary(self, dictionary):
        super(ThreeDSWhitelist, self).from_dictionary(dictionary)
        if 'source' in dictionary:
            self.source = dictionary['source']
        if 'status' in dictionary:
            self.status = dictionary['status']
        return self
