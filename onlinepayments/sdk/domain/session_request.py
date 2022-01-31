# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject


class SessionRequest(DataObject):
    __tokens = None

    @property
    def tokens(self) -> List[str]:
        """
        | List of previously stored tokens linked to the customer that wants to checkout.

        Type: list[str]
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value: List[str]):
        self.__tokens = value

    def to_dictionary(self):
        dictionary = super(SessionRequest, self).to_dictionary()
        if self.tokens is not None:
            dictionary['tokens'] = []
            for element in self.tokens:
                if element is not None:
                    dictionary['tokens'].append(element)
        return dictionary

    def from_dictionary(self, dictionary):
        super(SessionRequest, self).from_dictionary(dictionary)
        if 'tokens' in dictionary:
            if not isinstance(dictionary['tokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['tokens']))
            self.tokens = []
            for element in dictionary['tokens']:
                self.tokens.append(element)
        return self
