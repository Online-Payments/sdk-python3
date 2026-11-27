#
# This file was automatically generated.
#
from .data_object import DataObject


class CsrRequest(DataObject):

    __slots__ = (
        "__csr",
    )

    __csr: str | None

    def __init__(
        self,
        *,
        csr: str | None = None,
    ) -> None:
        self.csr = csr

    @property
    def csr(self) -> str | None:
        """
        | A Certificate Signing Request (CSR) string that contains the encoded information necessary for generating a digital certificate, including the public key and identity details of the requester.

        Type: str
        """
        return self.__csr

    @csr.setter
    def csr(self, value: str | None) -> None:
        self.__csr = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.csr is not None:
            dictionary['csr'] = self.csr
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CsrRequest':
        super().from_dictionary(dictionary)
        if 'csr' in dictionary:
            self.csr = dictionary['csr']
        return self
