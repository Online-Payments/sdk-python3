# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class CompanyInformation(DataObject):
    """
    | Object containing company information
    """

    __name = None

    @property
    def name(self) -> str:
        """
        | Name of company, as a customer

        Type: str
        """
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    def to_dictionary(self):
        dictionary = super(CompanyInformation, self).to_dictionary()
        if self.name is not None:
            dictionary['name'] = self.name
        return dictionary

    def from_dictionary(self, dictionary):
        super(CompanyInformation, self).from_dictionary(dictionary)
        if 'name' in dictionary:
            self.name = dictionary['name']
        return self
