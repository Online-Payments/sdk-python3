# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CreateHostedFieldsSessionRequest(DataObject):

    __locale: Optional[str] = None

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

    def to_dictionary(self) -> dict:
        dictionary = super(CreateHostedFieldsSessionRequest, self).to_dictionary()
        if self.locale is not None:
            dictionary['locale'] = self.locale
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreateHostedFieldsSessionRequest':
        super(CreateHostedFieldsSessionRequest, self).from_dictionary(dictionary)
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        return self
