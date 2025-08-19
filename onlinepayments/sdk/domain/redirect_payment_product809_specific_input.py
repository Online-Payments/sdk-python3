# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RedirectPaymentProduct809SpecificInput(DataObject):
    """
    Deprecated; Deprecated, this is no longer used.
    """

    __issuer_id: Optional[str] = None

    @property
    def issuer_id(self) -> Optional[str]:
        """
        | Deprecated. Unique ID of the issuing bank of the customer

        Type: str
        """
        return self.__issuer_id

    @issuer_id.setter
    def issuer_id(self, value: Optional[str]) -> None:
        self.__issuer_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct809SpecificInput, self).to_dictionary()
        if self.issuer_id is not None:
            dictionary['issuerId'] = self.issuer_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct809SpecificInput':
        super(RedirectPaymentProduct809SpecificInput, self).from_dictionary(dictionary)
        if 'issuerId' in dictionary:
            self.issuer_id = dictionary['issuerId']
        return self
