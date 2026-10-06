# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class Pagination(DataObject):

    __page: Optional[int] = None
    __page_size: Optional[int] = None

    @property
    def page(self) -> Optional[int]:
        """
        | The page number to retrieve (1-based). Default is 1.

        Type: int
        """
        return self.__page

    @page.setter
    def page(self, value: Optional[int]) -> None:
        self.__page = value

    @property
    def page_size(self) -> Optional[int]:
        """
        | Number of results per page. Default is 50, maximum is 1000.

        Type: int
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value: Optional[int]) -> None:
        self.__page_size = value

    def to_dictionary(self) -> dict:
        dictionary = super(Pagination, self).to_dictionary()
        if self.page is not None:
            dictionary['page'] = self.page
        if self.page_size is not None:
            dictionary['pageSize'] = self.page_size
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Pagination':
        super(Pagination, self).from_dictionary(dictionary)
        if 'page' in dictionary:
            self.page = dictionary['page']
        if 'pageSize' in dictionary:
            self.page_size = dictionary['pageSize']
        return self
