# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CursorPaginationInfo(DataObject):

    __has_more: Optional[bool] = None
    __next_cursor: Optional[str] = None

    @property
    def has_more(self) -> Optional[bool]:
        """
        | Indicates whether more results are available

        Type: bool
        """
        return self.__has_more

    @has_more.setter
    def has_more(self, value: Optional[bool]) -> None:
        self.__has_more = value

    @property
    def next_cursor(self) -> Optional[str]:
        """
        | Opaque cursor for retrieving the next page. Null if no more results available.

        Type: str
        """
        return self.__next_cursor

    @next_cursor.setter
    def next_cursor(self, value: Optional[str]) -> None:
        self.__next_cursor = value

    def to_dictionary(self) -> dict:
        dictionary = super(CursorPaginationInfo, self).to_dictionary()
        if self.has_more is not None:
            dictionary['hasMore'] = self.has_more
        if self.next_cursor is not None:
            dictionary['nextCursor'] = self.next_cursor
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CursorPaginationInfo':
        super(CursorPaginationInfo, self).from_dictionary(dictionary)
        if 'hasMore' in dictionary:
            self.has_more = dictionary['hasMore']
        if 'nextCursor' in dictionary:
            self.next_cursor = dictionary['nextCursor']
        return self
