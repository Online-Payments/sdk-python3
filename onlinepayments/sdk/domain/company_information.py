# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CompanyInformation(DataObject):

    __name: Optional[str] = None

    @property
    def name(self) -> Optional[str]:
        """
        | Name of company, as a customer. For Klarna payment method, company name should be provided to trigger a B2B session. If nothing is provided, a B2C session will be the default.

        Type: str
        """
        return self.__name

    @name.setter
    def name(self, value: Optional[str]) -> None:
        self.__name = value

    def to_dictionary(self) -> dict:
        dictionary = super(CompanyInformation, self).to_dictionary()
        if self.name is not None:
            dictionary['name'] = self.name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CompanyInformation':
        super(CompanyInformation, self).from_dictionary(dictionary)
        if 'name' in dictionary:
            self.name = dictionary['name']
        return self
