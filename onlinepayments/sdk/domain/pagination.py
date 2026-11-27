#
# This file was automatically generated.
#
from .data_object import DataObject


class Pagination(DataObject):

    __slots__ = (
        "__page",
        "__page_size",
    )

    __page: int | None
    __page_size: int | None

    def __init__(
        self,
        *,
        page: int | None = None,
        page_size: int | None = None,
    ) -> None:
        self.page = page
        self.page_size = page_size

    @property
    def page(self) -> int | None:
        """
        | The page number to retrieve (1-based). Default is 1.

        Type: int
        """
        return self.__page

    @page.setter
    def page(self, value: int | None) -> None:
        self.__page = value

    @property
    def page_size(self) -> int | None:
        """
        | Number of results per page. Default is 50, maximum is 1000.

        Type: int
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value: int | None) -> None:
        self.__page_size = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.page is not None:
            dictionary['page'] = self.page
        if self.page_size is not None:
            dictionary['pageSize'] = self.page_size
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Pagination':
        super().from_dictionary(dictionary)
        if 'page' in dictionary:
            self.page = dictionary['page']
        if 'pageSize' in dictionary:
            self.page_size = dictionary['pageSize']
        return self
