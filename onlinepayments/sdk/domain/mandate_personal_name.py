# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class MandatePersonalName(DataObject):

    __first_name: Optional[str] = None
    __surname: Optional[str] = None

    @property
    def first_name(self) -> Optional[str]:
        """
        | Given name(s) or first name(s) of the customer. Required for Create mandate and Create payment calls.

        Type: str
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value: Optional[str]) -> None:
        self.__first_name = value

    @property
    def surname(self) -> Optional[str]:
        """
        | Surname(s) or last name(s) of the customer. Required for Create mandate and Create payment calls.

        Type: str
        """
        return self.__surname

    @surname.setter
    def surname(self, value: Optional[str]) -> None:
        self.__surname = value

    def to_dictionary(self) -> dict:
        dictionary = super(MandatePersonalName, self).to_dictionary()
        if self.first_name is not None:
            dictionary['firstName'] = self.first_name
        if self.surname is not None:
            dictionary['surname'] = self.surname
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MandatePersonalName':
        super(MandatePersonalName, self).from_dictionary(dictionary)
        if 'firstName' in dictionary:
            self.first_name = dictionary['firstName']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        return self
