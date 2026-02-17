# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject
from .detokenized_token_response import DetokenizedTokenResponse


class DetokenizationResponse(DataObject):

    __tokens: Optional[List[DetokenizedTokenResponse]] = None

    @property
    def tokens(self) -> Optional[List[DetokenizedTokenResponse]]:
        """
        | The response contains an array of detokenized data for the provided token IDs, which includes card details and expiration dates.

        Type: list[:class:`onlinepayments.sdk.domain.detokenized_token_response.DetokenizedTokenResponse`]
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value: Optional[List[DetokenizedTokenResponse]]) -> None:
        self.__tokens = value

    def to_dictionary(self) -> dict:
        dictionary = super(DetokenizationResponse, self).to_dictionary()
        if self.tokens is not None:
            dictionary['tokens'] = []
            for element in self.tokens:
                if element is not None:
                    dictionary['tokens'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DetokenizationResponse':
        super(DetokenizationResponse, self).from_dictionary(dictionary)
        if 'tokens' in dictionary:
            if not isinstance(dictionary['tokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['tokens']))
            self.tokens = []
            for element in dictionary['tokens']:
                value = DetokenizedTokenResponse()
                self.tokens.append(value.from_dictionary(element))
        return self
