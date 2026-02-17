# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CsrRequest(DataObject):

    __csr: Optional[str] = None

    @property
    def csr(self) -> Optional[str]:
        """
        | A Certificate Signing Request (CSR) string that contains the encoded information necessary for generating a digital certificate, including the public key and identity details of the requester.

        Type: str
        """
        return self.__csr

    @csr.setter
    def csr(self, value: Optional[str]) -> None:
        self.__csr = value

    def to_dictionary(self) -> dict:
        dictionary = super(CsrRequest, self).to_dictionary()
        if self.csr is not None:
            dictionary['csr'] = self.csr
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CsrRequest':
        super(CsrRequest, self).from_dictionary(dictionary)
        if 'csr' in dictionary:
            self.csr = dictionary['csr']
        return self
