# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.directory_entry import DirectoryEntry


class ProductDirectory(DataObject):
    __entries = None

    @property
    def entries(self) -> List[DirectoryEntry]:
        """
        | List of entries in the directory

        Type: list[:class:`onlinepayments.sdk.domain.directory_entry.DirectoryEntry`]
        """
        return self.__entries

    @entries.setter
    def entries(self, value: List[DirectoryEntry]):
        self.__entries = value

    def to_dictionary(self):
        dictionary = super(ProductDirectory, self).to_dictionary()
        if self.entries is not None:
            dictionary['entries'] = []
            for element in self.entries:
                if element is not None:
                    dictionary['entries'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary):
        super(ProductDirectory, self).from_dictionary(dictionary)
        if 'entries' in dictionary:
            if not isinstance(dictionary['entries'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['entries']))
            self.entries = []
            for element in dictionary['entries']:
                value = DirectoryEntry()
                self.entries.append(value.from_dictionary(element))
        return self
