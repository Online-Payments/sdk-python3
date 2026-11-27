#
# This file was automatically generated.
#
from .data_object import DataObject


class ShowInstructionsData(DataObject):

    __slots__ = (
        "__show_data",
    )

    __show_data: str | None

    def __init__(
        self,
        *,
        show_data: str | None = None,
    ) -> None:
        self.show_data = show_data

    @property
    def show_data(self) -> str | None:
        """
        | The data that should be shown to the customer that can be used to render the instructions in your own application or website.

        Type: str
        """
        return self.__show_data

    @show_data.setter
    def show_data(self, value: str | None) -> None:
        self.__show_data = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.show_data is not None:
            dictionary['showData'] = self.show_data
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ShowInstructionsData':
        super().from_dictionary(dictionary)
        if 'showData' in dictionary:
            self.show_data = dictionary['showData']
        return self
