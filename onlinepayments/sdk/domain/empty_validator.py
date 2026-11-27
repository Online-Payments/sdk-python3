#
# This file was automatically generated.
#
from .data_object import DataObject


class EmptyValidator(DataObject):

    __slots__ = ()

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'EmptyValidator':
        super().from_dictionary(dictionary)
        return self
