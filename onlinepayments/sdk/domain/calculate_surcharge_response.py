# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject
from .surcharge import Surcharge


class CalculateSurchargeResponse(DataObject):

    __surcharges: Optional[List[Surcharge]] = None

    @property
    def surcharges(self) -> Optional[List[Surcharge]]:
        """
        Type: list[:class:`onlinepayments.sdk.domain.surcharge.Surcharge`]
        """
        return self.__surcharges

    @surcharges.setter
    def surcharges(self, value: Optional[List[Surcharge]]) -> None:
        self.__surcharges = value

    def to_dictionary(self) -> dict:
        dictionary = super(CalculateSurchargeResponse, self).to_dictionary()
        if self.surcharges is not None:
            dictionary['surcharges'] = []
            for element in self.surcharges:
                if element is not None:
                    dictionary['surcharges'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CalculateSurchargeResponse':
        super(CalculateSurchargeResponse, self).from_dictionary(dictionary)
        if 'surcharges' in dictionary:
            if not isinstance(dictionary['surcharges'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['surcharges']))
            self.surcharges = []
            for element in dictionary['surcharges']:
                value = Surcharge()
                self.surcharges.append(value.from_dictionary(element))
        return self
