# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RevokeMandateRequest(DataObject):

    __revocation_reason: Optional[str] = None

    @property
    def revocation_reason(self) -> Optional[str]:
        """
        | The reason for revoking the mandate. Possible values are:
        
        * receivedFinal
        * userAction
        * obsolescence
        * refused
        * revocationAskedByDebitor
        * revocationAskedByCreditor
        * deletionAskedByDebitor
        * deletionAskedByCreditor

        Type: str
        """
        return self.__revocation_reason

    @revocation_reason.setter
    def revocation_reason(self, value: Optional[str]) -> None:
        self.__revocation_reason = value

    def to_dictionary(self) -> dict:
        dictionary = super(RevokeMandateRequest, self).to_dictionary()
        if self.revocation_reason is not None:
            dictionary['revocationReason'] = self.revocation_reason
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RevokeMandateRequest':
        super(RevokeMandateRequest, self).from_dictionary(dictionary)
        if 'revocationReason' in dictionary:
            self.revocation_reason = dictionary['revocationReason']
        return self
