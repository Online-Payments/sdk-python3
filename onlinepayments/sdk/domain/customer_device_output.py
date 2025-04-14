# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CustomerDeviceOutput(DataObject):

    __ip_address_country_code: Optional[str] = None

    @property
    def ip_address_country_code(self) -> Optional[str]:
        """
        | ISO 3166-1 alpha-2 country code

        Type: str
        """
        return self.__ip_address_country_code

    @ip_address_country_code.setter
    def ip_address_country_code(self, value: Optional[str]) -> None:
        self.__ip_address_country_code = value

    def to_dictionary(self) -> dict:
        dictionary = super(CustomerDeviceOutput, self).to_dictionary()
        if self.ip_address_country_code is not None:
            dictionary['ipAddressCountryCode'] = self.ip_address_country_code
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CustomerDeviceOutput':
        super(CustomerDeviceOutput, self).from_dictionary(dictionary)
        if 'ipAddressCountryCode' in dictionary:
            self.ip_address_country_code = dictionary['ipAddressCountryCode']
        return self
