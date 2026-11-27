#
# This file was automatically generated.
#
from .data_object import DataObject
from .payment_product_field_display_element import PaymentProductFieldDisplayElement


class ValueMappingElement(DataObject):

    __slots__ = (
        "__display_elements",
        "__value",
    )

    __display_elements: list[PaymentProductFieldDisplayElement] | None
    __value: str | None

    def __init__(
        self,
        *,
        display_elements: list[PaymentProductFieldDisplayElement] | None = None,
        value: str | None = None,
    ) -> None:
        self.display_elements = display_elements
        self.value = value

    @property
    def display_elements(self) -> list[PaymentProductFieldDisplayElement] | None:
        """
        Type: list[:class:`onlinepayments.sdk.domain.payment_product_field_display_element.PaymentProductFieldDisplayElement`]
        """
        return self.__display_elements

    @display_elements.setter
    def display_elements(self, value: list[PaymentProductFieldDisplayElement] | None) -> None:
        self.__display_elements = value

    @property
    def value(self) -> str | None:
        """
        | Value corresponding to the key

        Type: str
        """
        return self.__value

    @value.setter
    def value(self, value: str | None) -> None:
        self.__value = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.display_elements is not None:
            dictionary['displayElements'] = []
            for element in self.display_elements:
                if element is not None:
                    dictionary['displayElements'].append(element.to_dictionary())
        if self.value is not None:
            dictionary['value'] = self.value
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ValueMappingElement':
        super().from_dictionary(dictionary)
        if 'displayElements' in dictionary:
            if not isinstance(dictionary['displayElements'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['displayElements']))
            self.display_elements = []
            for element in dictionary['displayElements']:
                value = PaymentProductFieldDisplayElement()
                self.display_elements.append(value.from_dictionary(element))
        if 'value' in dictionary:
            self.value = dictionary['value']
        return self
