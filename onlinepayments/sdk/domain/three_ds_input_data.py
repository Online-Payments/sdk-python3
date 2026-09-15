# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class ThreeDsInputData(DataObject):

    __acquirer_id: Optional[str] = None
    __acquirer_mid: Optional[str] = None
    __requestor_id: Optional[str] = None

    @property
    def acquirer_id(self) -> Optional[str]:
        """
        | Merchant’s Acquirer ID.

        Type: str
        """
        return self.__acquirer_id

    @acquirer_id.setter
    def acquirer_id(self, value: Optional[str]) -> None:
        self.__acquirer_id = value

    @property
    def acquirer_mid(self) -> Optional[str]:
        """
        | Acquirer’s Merchant ID.

        Type: str
        """
        return self.__acquirer_mid

    @acquirer_mid.setter
    def acquirer_mid(self, value: Optional[str]) -> None:
        self.__acquirer_mid = value

    @property
    def requestor_id(self) -> Optional[str]:
        """
        | The ID assigned to the merchant for authentication request to initiate 3DS with MPI.

        Type: str
        """
        return self.__requestor_id

    @requestor_id.setter
    def requestor_id(self, value: Optional[str]) -> None:
        self.__requestor_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(ThreeDsInputData, self).to_dictionary()
        if self.acquirer_id is not None:
            dictionary['acquirerId'] = self.acquirer_id
        if self.acquirer_mid is not None:
            dictionary['acquirerMid'] = self.acquirer_mid
        if self.requestor_id is not None:
            dictionary['requestorId'] = self.requestor_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ThreeDsInputData':
        super(ThreeDsInputData, self).from_dictionary(dictionary)
        if 'acquirerId' in dictionary:
            self.acquirer_id = dictionary['acquirerId']
        if 'acquirerMid' in dictionary:
            self.acquirer_mid = dictionary['acquirerMid']
        if 'requestorId' in dictionary:
            self.requestor_id = dictionary['requestorId']
        return self
