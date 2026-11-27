#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProduct771SpecificOutput(DataObject):

    __slots__ = (
        "__mandate_reference",
    )

    __mandate_reference: str | None

    def __init__(
        self,
        *,
        mandate_reference: str | None = None,
    ) -> None:
        self.mandate_reference = mandate_reference

    @property
    def mandate_reference(self) -> str | None:
        """
        | Unique reference to a Mandate

        Type: str
        """
        return self.__mandate_reference

    @mandate_reference.setter
    def mandate_reference(self, value: str | None) -> None:
        self.__mandate_reference = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.mandate_reference is not None:
            dictionary['mandateReference'] = self.mandate_reference
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct771SpecificOutput':
        super().from_dictionary(dictionary)
        if 'mandateReference' in dictionary:
            self.mandate_reference = dictionary['mandateReference']
        return self
