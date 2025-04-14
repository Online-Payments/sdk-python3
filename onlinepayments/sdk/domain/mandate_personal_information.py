# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .mandate_personal_name import MandatePersonalName


class MandatePersonalInformation(DataObject):

    __name: Optional[MandatePersonalName] = None
    __title: Optional[str] = None

    @property
    def name(self) -> Optional[MandatePersonalName]:
        """
        | Object containing the name details of the customer. Required for Create mandate and Create payment calls.

        Type: :class:`onlinepayments.sdk.domain.mandate_personal_name.MandatePersonalName`
        """
        return self.__name

    @name.setter
    def name(self, value: Optional[MandatePersonalName]) -> None:
        self.__name = value

    @property
    def title(self) -> Optional[str]:
        """
        | Object containing the title of the customer (Mr, Miss or Mrs)

        Type: str
        """
        return self.__title

    @title.setter
    def title(self, value: Optional[str]) -> None:
        self.__title = value

    def to_dictionary(self) -> dict:
        dictionary = super(MandatePersonalInformation, self).to_dictionary()
        if self.name is not None:
            dictionary['name'] = self.name.to_dictionary()
        if self.title is not None:
            dictionary['title'] = self.title
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MandatePersonalInformation':
        super(MandatePersonalInformation, self).from_dictionary(dictionary)
        if 'name' in dictionary:
            if not isinstance(dictionary['name'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['name']))
            value = MandatePersonalName()
            self.name = value.from_dictionary(dictionary['name'])
        if 'title' in dictionary:
            self.title = dictionary['title']
        return self
