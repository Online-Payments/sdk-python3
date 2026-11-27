#
# This file was automatically generated.
#
from .data_object import DataObject


class LengthValidator(DataObject):

    __slots__ = (
        "__max_length",
        "__min_length",
    )

    __max_length: int | None
    __min_length: int | None

    def __init__(
        self,
        *,
        max_length: int | None = None,
        min_length: int | None = None,
    ) -> None:
        self.max_length = max_length
        self.min_length = min_length

    @property
    def max_length(self) -> int | None:
        """
        Type: int
        """
        return self.__max_length

    @max_length.setter
    def max_length(self, value: int | None) -> None:
        self.__max_length = value

    @property
    def min_length(self) -> int | None:
        """
        Type: int
        """
        return self.__min_length

    @min_length.setter
    def min_length(self, value: int | None) -> None:
        self.__min_length = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.max_length is not None:
            dictionary['maxLength'] = self.max_length
        if self.min_length is not None:
            dictionary['minLength'] = self.min_length
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'LengthValidator':
        super().from_dictionary(dictionary)
        if 'maxLength' in dictionary:
            self.max_length = dictionary['maxLength']
        if 'minLength' in dictionary:
            self.min_length = dictionary['minLength']
        return self
