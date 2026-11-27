#
# This file was automatically generated.
#
from .data_object import DataObject


class LineItemInvoiceData(DataObject):

    __slots__ = (
        "__description",
    )

    __description: str | None

    def __init__(
        self,
        *,
        description: str | None = None,
    ) -> None:
        self.description = description

    @property
    def description(self) -> str | None:
        """
        | Shopping cart item description

        Type: str
        """
        return self.__description

    @description.setter
    def description(self, value: str | None) -> None:
        self.__description = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.description is not None:
            dictionary['description'] = self.description
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'LineItemInvoiceData':
        super().from_dictionary(dictionary)
        if 'description' in dictionary:
            self.description = dictionary['description']
        return self
