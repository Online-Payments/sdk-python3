# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.surcharge import Surcharge


class CalculateSurchargeResponse(DataObject):
    __surcharges = None

    @property
    def surcharges(self) -> List[Surcharge]:
        """
        | List of surcharge calculations matching the bin and paymentProductId if supplied

        Type: list[:class:`onlinepayments.sdk.domain.surcharge.Surcharge`]
        """
        return self.__surcharges

    @surcharges.setter
    def surcharges(self, value: List[Surcharge]):
        self.__surcharges = value

    def to_dictionary(self):
        dictionary = super(CalculateSurchargeResponse, self).to_dictionary()
        if self.surcharges is not None:
            dictionary['surcharges'] = []
            for element in self.surcharges:
                if element is not None:
                    dictionary['surcharges'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary):
        super(CalculateSurchargeResponse, self).from_dictionary(dictionary)
        if 'surcharges' in dictionary:
            if not isinstance(dictionary['surcharges'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['surcharges']))
            self.surcharges = []
            for element in dictionary['surcharges']:
                value = Surcharge()
                self.surcharges.append(value.from_dictionary(element))
        return self
