#
# This file was automatically generated.
#
from .data_object import DataObject


class RangeValidator(DataObject):

    __slots__ = (
        "__max_value",
        "__min_value",
    )

    __max_value: int | None
    __min_value: int | None

    def __init__(
        self,
        *,
        max_value: int | None = None,
        min_value: int | None = None,
    ) -> None:
        self.max_value = max_value
        self.min_value = min_value

    @property
    def max_value(self) -> int | None:
        """
        Type: int
        """
        return self.__max_value

    @max_value.setter
    def max_value(self, value: int | None) -> None:
        self.__max_value = value

    @property
    def min_value(self) -> int | None:
        """
        Type: int
        """
        return self.__min_value

    @min_value.setter
    def min_value(self, value: int | None) -> None:
        self.__min_value = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.max_value is not None:
            dictionary['maxValue'] = self.max_value
        if self.min_value is not None:
            dictionary['minValue'] = self.min_value
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RangeValidator':
        super().from_dictionary(dictionary)
        if 'maxValue' in dictionary:
            self.max_value = dictionary['maxValue']
        if 'minValue' in dictionary:
            self.min_value = dictionary['minValue']
        return self
