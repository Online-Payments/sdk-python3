#
# This file was automatically generated.
#
from .data_object import DataObject
from .directory_entry import DirectoryEntry


class ProductDirectory(DataObject):

    __slots__ = (
        "__entries",
    )

    __entries: list[DirectoryEntry] | None

    def __init__(
        self,
        *,
        entries: list[DirectoryEntry] | None = None,
    ) -> None:
        self.entries = entries

    @property
    def entries(self) -> list[DirectoryEntry] | None:
        """
        | List of entries in the directory

        Type: list[:class:`onlinepayments.sdk.domain.directory_entry.DirectoryEntry`]
        """
        return self.__entries

    @entries.setter
    def entries(self, value: list[DirectoryEntry] | None) -> None:
        self.__entries = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.entries is not None:
            dictionary['entries'] = []
            for element in self.entries:
                if element is not None:
                    dictionary['entries'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ProductDirectory':
        super().from_dictionary(dictionary)
        if 'entries' in dictionary:
            if not isinstance(dictionary['entries'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['entries']))
            self.entries = []
            for element in dictionary['entries']:
                value = DirectoryEntry()
                self.entries.append(value.from_dictionary(element))
        return self
