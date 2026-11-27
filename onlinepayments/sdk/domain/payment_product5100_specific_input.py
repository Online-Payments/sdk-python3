#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProduct5100SpecificInput(DataObject):

    __slots__ = (
        "__brand",
    )

    __brand: str | None

    def __init__(
        self,
        *,
        brand: str | None = None,
    ) -> None:
        self.brand = brand

    @property
    def brand(self) -> str | None:
        """
        | Indicate whether to use a specific Cpay brand. Brands are configurable at the payment method level. See BackOffice Cpay configuration for allowed values.

        Type: str
        """
        return self.__brand

    @brand.setter
    def brand(self, value: str | None) -> None:
        self.__brand = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.brand is not None:
            dictionary['brand'] = self.brand
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct5100SpecificInput':
        super().from_dictionary(dictionary)
        if 'brand' in dictionary:
            self.brand = dictionary['brand']
        return self
