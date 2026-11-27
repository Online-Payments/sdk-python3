#
# This file was automatically generated.
#
from .data_object import DataObject


class DpaData(DataObject):

    __slots__ = (
        "__dpa_name",
    )

    __dpa_name: str | None

    def __init__(
        self,
        *,
        dpa_name: str | None = None,
    ) -> None:
        self.dpa_name = dpa_name

    @property
    def dpa_name(self) -> str | None:
        """
        | Legal name of registered DPA.

        Type: str
        """
        return self.__dpa_name

    @dpa_name.setter
    def dpa_name(self, value: str | None) -> None:
        self.__dpa_name = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.dpa_name is not None:
            dictionary['dpaName'] = self.dpa_name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DpaData':
        super().from_dictionary(dictionary)
        if 'dpaName' in dictionary:
            self.dpa_name = dictionary['dpaName']
        return self
