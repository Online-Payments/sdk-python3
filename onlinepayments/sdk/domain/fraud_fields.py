# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class FraudFields(DataObject):
    """
    | Object containing additional data that will be used to assess the risk of fraud
    """

    __black_list_data = None
    __customer_ip_address = None

    @property
    def black_list_data(self) -> str:
        """
        | Additional black list input

        Type: str
        """
        return self.__black_list_data

    @black_list_data.setter
    def black_list_data(self, value: str):
        self.__black_list_data = value

    @property
    def customer_ip_address(self) -> str:
        """
        | The IP Address of the customer that is making the payment

        Type: str
        """
        return self.__customer_ip_address

    @customer_ip_address.setter
    def customer_ip_address(self, value: str):
        self.__customer_ip_address = value

    def to_dictionary(self):
        dictionary = super(FraudFields, self).to_dictionary()
        if self.black_list_data is not None:
            dictionary['blackListData'] = self.black_list_data
        if self.customer_ip_address is not None:
            dictionary['customerIpAddress'] = self.customer_ip_address
        return dictionary

    def from_dictionary(self, dictionary):
        super(FraudFields, self).from_dictionary(dictionary)
        if 'blackListData' in dictionary:
            self.black_list_data = dictionary['blackListData']
        if 'customerIpAddress' in dictionary:
            self.customer_ip_address = dictionary['customerIpAddress']
        return self
