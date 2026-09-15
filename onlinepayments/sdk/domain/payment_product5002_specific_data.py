# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .api_parameters import ApiParameters
from .data_object import DataObject


class PaymentProduct5002SpecificData(DataObject):

    __api_parameters: Optional[ApiParameters] = None

    @property
    def api_parameters(self) -> Optional[ApiParameters]:
        """
        | Collection of parameters and their respective values to pass to the Click to Pay frontend SDK/API to intialize a payment.

        Type: :class:`onlinepayments.sdk.domain.api_parameters.ApiParameters`
        """
        return self.__api_parameters

    @api_parameters.setter
    def api_parameters(self, value: Optional[ApiParameters]) -> None:
        self.__api_parameters = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct5002SpecificData, self).to_dictionary()
        if self.api_parameters is not None:
            dictionary['apiParameters'] = self.api_parameters.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct5002SpecificData':
        super(PaymentProduct5002SpecificData, self).from_dictionary(dictionary)
        if 'apiParameters' in dictionary:
            if not isinstance(dictionary['apiParameters'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['apiParameters']))
            value = ApiParameters()
            self.api_parameters = value.from_dictionary(dictionary['apiParameters'])
        return self
