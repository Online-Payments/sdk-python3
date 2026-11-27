#
# This file was automatically generated.
#
from .data_object import DataObject


class LabelTemplateElement(DataObject):

    __slots__ = (
        "__attribute_key",
        "__mask",
    )

    __attribute_key: str | None
    __mask: str | None

    def __init__(
        self,
        *,
        attribute_key: str | None = None,
        mask: str | None = None,
    ) -> None:
        self.attribute_key = attribute_key
        self.mask = mask

    @property
    def attribute_key(self) -> str | None:
        """
        | Name of the attribute that is shown to the customer on selection pages or screens

        Type: str
        """
        return self.__attribute_key

    @attribute_key.setter
    def attribute_key(self, value: str | None) -> None:
        self.__attribute_key = value

    @property
    def mask(self) -> str | None:
        """
        | Regular mask for the attributeKey Note: The mask is optional as not every field has a mask

        Type: str
        """
        return self.__mask

    @mask.setter
    def mask(self, value: str | None) -> None:
        self.__mask = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.attribute_key is not None:
            dictionary['attributeKey'] = self.attribute_key
        if self.mask is not None:
            dictionary['mask'] = self.mask
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'LabelTemplateElement':
        super().from_dictionary(dictionary)
        if 'attributeKey' in dictionary:
            self.attribute_key = dictionary['attributeKey']
        if 'mask' in dictionary:
            self.mask = dictionary['mask']
        return self
