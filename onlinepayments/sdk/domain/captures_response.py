# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .capture import Capture
from .data_object import DataObject


class CapturesResponse(DataObject):

    __captures: Optional[List[Capture]] = None

    @property
    def captures(self) -> Optional[List[Capture]]:
        """
        | The list of all captures performed on the requested payment.

        Type: list[:class:`onlinepayments.sdk.domain.capture.Capture`]
        """
        return self.__captures

    @captures.setter
    def captures(self, value: Optional[List[Capture]]) -> None:
        self.__captures = value

    def to_dictionary(self) -> dict:
        dictionary = super(CapturesResponse, self).to_dictionary()
        if self.captures is not None:
            dictionary['captures'] = []
            for element in self.captures:
                if element is not None:
                    dictionary['captures'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CapturesResponse':
        super(CapturesResponse, self).from_dictionary(dictionary)
        if 'captures' in dictionary:
            if not isinstance(dictionary['captures'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['captures']))
            self.captures = []
            for element in dictionary['captures']:
                value = Capture()
                self.captures.append(value.from_dictionary(element))
        return self
