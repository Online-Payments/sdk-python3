# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject


class PaymentProduct320SpecificData(DataObject):

    __gateway: Optional[str] = None
    __networks: Optional[List[str]] = None

    @property
    def gateway(self) -> Optional[str]:
        """
        | The gateway identifier. You should use this when creating a `tokenization specification <https://developers.google.com/pay/api/android/reference/request-objects#Gateway>`_ .

        Type: str
        """
        return self.__gateway

    @gateway.setter
    def gateway(self, value: Optional[str]) -> None:
        self.__gateway = value

    @property
    def networks(self) -> Optional[List[str]]:
        """
        | The networks that can be used in the current payment context. The strings that represent the networks in the array are identical to the strings that GooglePay uses in their documentation. For instance "Visa".

        Type: list[str]
        """
        return self.__networks

    @networks.setter
    def networks(self, value: Optional[List[str]]) -> None:
        self.__networks = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct320SpecificData, self).to_dictionary()
        if self.gateway is not None:
            dictionary['gateway'] = self.gateway
        if self.networks is not None:
            dictionary['networks'] = []
            for element in self.networks:
                if element is not None:
                    dictionary['networks'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct320SpecificData':
        super(PaymentProduct320SpecificData, self).from_dictionary(dictionary)
        if 'gateway' in dictionary:
            self.gateway = dictionary['gateway']
        if 'networks' in dictionary:
            if not isinstance(dictionary['networks'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['networks']))
            self.networks = []
            for element in dictionary['networks']:
                self.networks.append(element)
        return self
