# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .personal_name_token import PersonalNameToken


class PersonalInformationToken(DataObject):

    __name: Optional[PersonalNameToken] = None

    @property
    def name(self) -> Optional[PersonalNameToken]:
        """
        Type: :class:`onlinepayments.sdk.domain.personal_name_token.PersonalNameToken`
        """
        return self.__name

    @name.setter
    def name(self, value: Optional[PersonalNameToken]) -> None:
        self.__name = value

    def to_dictionary(self) -> dict:
        dictionary = super(PersonalInformationToken, self).to_dictionary()
        if self.name is not None:
            dictionary['name'] = self.name.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PersonalInformationToken':
        super(PersonalInformationToken, self).from_dictionary(dictionary)
        if 'name' in dictionary:
            if not isinstance(dictionary['name'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['name']))
            value = PersonalNameToken()
            self.name = value.from_dictionary(dictionary['name'])
        return self
