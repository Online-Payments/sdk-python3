# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .mandate_response import MandateResponse


class GetMandateResponse(DataObject):

    __mandate: Optional[MandateResponse] = None

    @property
    def mandate(self) -> Optional[MandateResponse]:
        """
        | Object containing the created mandate.

        Type: :class:`onlinepayments.sdk.domain.mandate_response.MandateResponse`
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value: Optional[MandateResponse]) -> None:
        self.__mandate = value

    def to_dictionary(self) -> dict:
        dictionary = super(GetMandateResponse, self).to_dictionary()
        if self.mandate is not None:
            dictionary['mandate'] = self.mandate.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetMandateResponse':
        super(GetMandateResponse, self).from_dictionary(dictionary)
        if 'mandate' in dictionary:
            if not isinstance(dictionary['mandate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandate']))
            value = MandateResponse()
            self.mandate = value.from_dictionary(dictionary['mandate'])
        return self
