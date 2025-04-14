# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject
from .directory_entry import DirectoryEntry


class ProductDirectory(DataObject):

    __entries: Optional[List[DirectoryEntry]] = None

    @property
    def entries(self) -> Optional[List[DirectoryEntry]]:
        """
        | List of entries in the directory

        Type: list[:class:`onlinepayments.sdk.domain.directory_entry.DirectoryEntry`]
        """
        return self.__entries

    @entries.setter
    def entries(self, value: Optional[List[DirectoryEntry]]) -> None:
        self.__entries = value

    def to_dictionary(self) -> dict:
        dictionary = super(ProductDirectory, self).to_dictionary()
        if self.entries is not None:
            dictionary['entries'] = []
            for element in self.entries:
                if element is not None:
                    dictionary['entries'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ProductDirectory':
        super(ProductDirectory, self).from_dictionary(dictionary)
        if 'entries' in dictionary:
            if not isinstance(dictionary['entries'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['entries']))
            self.entries = []
            for element in dictionary['entries']:
                value = DirectoryEntry()
                self.entries.append(value.from_dictionary(element))
        return self
