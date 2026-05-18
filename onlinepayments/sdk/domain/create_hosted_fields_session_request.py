# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject


class CreateHostedFieldsSessionRequest(DataObject):

    __locale: Optional[str] = None
    __tokens: Optional[List[str]] = None

    @property
    def locale(self) -> Optional[str]:
        """
        | Locale used in the GUI towards the consumer.

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: Optional[str]) -> None:
        self.__locale = value

    @property
    def tokens(self) -> Optional[List[str]]:
        """
        Type: list[str]
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value: Optional[List[str]]) -> None:
        self.__tokens = value

    def to_dictionary(self) -> dict:
        dictionary = super(CreateHostedFieldsSessionRequest, self).to_dictionary()
        if self.locale is not None:
            dictionary['locale'] = self.locale
        if self.tokens is not None:
            dictionary['tokens'] = []
            for element in self.tokens:
                if element is not None:
                    dictionary['tokens'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreateHostedFieldsSessionRequest':
        super(CreateHostedFieldsSessionRequest, self).from_dictionary(dictionary)
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'tokens' in dictionary:
            if not isinstance(dictionary['tokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['tokens']))
            self.tokens = []
            for element in dictionary['tokens']:
                self.tokens.append(element)
        return self
