# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class CustomerDeviceOutput(DataObject):
    """
    | Object containing information on the device and browser of the customer
    """

    __ip_address_country_code = None

    @property
    def ip_address_country_code(self) -> str:
        """
        | ISO 3166-1 alpha-2 country code

        Type: str
        """
        return self.__ip_address_country_code

    @ip_address_country_code.setter
    def ip_address_country_code(self, value: str):
        self.__ip_address_country_code = value

    def to_dictionary(self):
        dictionary = super(CustomerDeviceOutput, self).to_dictionary()
        if self.ip_address_country_code is not None:
            dictionary['ipAddressCountryCode'] = self.ip_address_country_code
        return dictionary

    def from_dictionary(self, dictionary):
        super(CustomerDeviceOutput, self).from_dictionary(dictionary)
        if 'ipAddressCountryCode' in dictionary:
            self.ip_address_country_code = dictionary['ipAddressCountryCode']
        return self
