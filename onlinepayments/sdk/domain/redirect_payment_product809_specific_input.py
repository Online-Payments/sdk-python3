#
# This file was automatically generated.
#
from .data_object import DataObject


class RedirectPaymentProduct809SpecificInput(DataObject):
    """
    Deprecated; Deprecated, this is no longer used.
    """

    __slots__ = (
        "__issuer_id",
    )

    __issuer_id: str | None

    def __init__(
        self,
        *,
        issuer_id: str | None = None,
    ) -> None:
        self.issuer_id = issuer_id

    @property
    def issuer_id(self) -> str | None:
        """
        | Deprecated. Unique ID of the issuing bank of the customer

        Type: str
        """
        return self.__issuer_id

    @issuer_id.setter
    def issuer_id(self, value: str | None) -> None:
        self.__issuer_id = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.issuer_id is not None:
            dictionary['issuerId'] = self.issuer_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct809SpecificInput':
        super().from_dictionary(dictionary)
        if 'issuerId' in dictionary:
            self.issuer_id = dictionary['issuerId']
        return self
