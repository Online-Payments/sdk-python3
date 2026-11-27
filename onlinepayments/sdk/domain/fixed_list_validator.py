#
# This file was automatically generated.
#
from .data_object import DataObject


class FixedListValidator(DataObject):

    __slots__ = (
        "__allowed_values",
    )

    __allowed_values: list[str] | None

    def __init__(
        self,
        *,
        allowed_values: list[str] | None = None,
    ) -> None:
        self.allowed_values = allowed_values

    @property
    def allowed_values(self) -> list[str] | None:
        """
        Type: list[str]
        """
        return self.__allowed_values

    @allowed_values.setter
    def allowed_values(self, value: list[str] | None) -> None:
        self.__allowed_values = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.allowed_values is not None:
            dictionary['allowedValues'] = []
            for element in self.allowed_values:
                if element is not None:
                    dictionary['allowedValues'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'FixedListValidator':
        super().from_dictionary(dictionary)
        if 'allowedValues' in dictionary:
            if not isinstance(dictionary['allowedValues'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['allowedValues']))
            self.allowed_values = []
            for element in dictionary['allowedValues']:
                self.allowed_values.append(element)
        return self
