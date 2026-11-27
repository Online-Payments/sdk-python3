#
# This file was automatically generated.
#
from .data_object import DataObject


class CursorPaginationInfo(DataObject):

    __slots__ = (
        "__has_more",
        "__next_cursor",
    )

    __has_more: bool | None
    __next_cursor: str | None

    def __init__(
        self,
        *,
        has_more: bool | None = None,
        next_cursor: str | None = None,
    ) -> None:
        self.has_more = has_more
        self.next_cursor = next_cursor

    @property
    def has_more(self) -> bool | None:
        """
        | Indicates whether more results are available

        Type: bool
        """
        return self.__has_more

    @has_more.setter
    def has_more(self, value: bool | None) -> None:
        self.__has_more = value

    @property
    def next_cursor(self) -> str | None:
        """
        | Opaque cursor for retrieving the next page. Null if no more results available.

        Type: str
        """
        return self.__next_cursor

    @next_cursor.setter
    def next_cursor(self, value: str | None) -> None:
        self.__next_cursor = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.has_more is not None:
            dictionary['hasMore'] = self.has_more
        if self.next_cursor is not None:
            dictionary['nextCursor'] = self.next_cursor
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CursorPaginationInfo':
        super().from_dictionary(dictionary)
        if 'hasMore' in dictionary:
            self.has_more = dictionary['hasMore']
        if 'nextCursor' in dictionary:
            self.next_cursor = dictionary['nextCursor']
        return self
