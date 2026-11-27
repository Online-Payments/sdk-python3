#
# This file was automatically generated.
#
from .data_object import DataObject


class RevokeMandateRequest(DataObject):

    __slots__ = (
        "__revocation_reason",
    )

    __revocation_reason: str | None

    def __init__(
        self,
        *,
        revocation_reason: str | None = None,
    ) -> None:
        self.revocation_reason = revocation_reason

    @property
    def revocation_reason(self) -> str | None:
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
        
        | Refer to the support page to determine if the property is applicable.

        Type: str
        """
        return self.__revocation_reason

    @revocation_reason.setter
    def revocation_reason(self, value: str | None) -> None:
        self.__revocation_reason = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.revocation_reason is not None:
            dictionary['revocationReason'] = self.revocation_reason
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RevokeMandateRequest':
        super().from_dictionary(dictionary)
        if 'revocationReason' in dictionary:
            self.revocation_reason = dictionary['revocationReason']
        return self
