#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProductFieldTooltip(DataObject):

    __slots__ = (
        "__image",
        "__label",
    )

    __image: str | None
    __label: str | None

    def __init__(
        self,
        *,
        image: str | None = None,
        label: str | None = None,
    ) -> None:
        self.image = image
        self.label = label

    @property
    def image(self) -> str | None:
        """
        | Deprecated: This field is not used by any payment product Relative URL that can be used to retrieve an image for the tooltip image.

        Type: str

        Deprecated; This field is not used by any payment product Relative URL that can be used to retrieve an image for the tooltip image.
        """
        return self.__image

    @image.setter
    def image(self, value: str | None) -> None:
        self.__image = value

    @property
    def label(self) -> str | None:
        """
        | A text explaining the field in more detail. This is meant to be used for displaying to the customer.

        Type: str
        """
        return self.__label

    @label.setter
    def label(self, value: str | None) -> None:
        self.__label = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.image is not None:
            dictionary['image'] = self.image
        if self.label is not None:
            dictionary['label'] = self.label
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductFieldTooltip':
        super().from_dictionary(dictionary)
        if 'image' in dictionary:
            self.image = dictionary['image']
        if 'label' in dictionary:
            self.label = dictionary['label']
        return self
