# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject


class FraudFields(DataObject):
    """
    | Object containing additional data that will be used to assess the risk of fraud
    """

    __black_list_data = None
    __customer_ip_address = None
    __product_categories = None

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
        | Deprecated: Use order.customer.device.ipAddress instead.
        
        | The IP Address of the customer that is making the payment

        Type: str
        """
        return self.__customer_ip_address

    @customer_ip_address.setter
    def customer_ip_address(self, value: str):
        self.__customer_ip_address = value

    @property
    def product_categories(self) -> List[str]:
        """
        | List of product categories that are being purchased.

        Type: list[str]
        """
        return self.__product_categories

    @product_categories.setter
    def product_categories(self, value: List[str]):
        self.__product_categories = value

    def to_dictionary(self):
        dictionary = super(FraudFields, self).to_dictionary()
        if self.black_list_data is not None:
            dictionary['blackListData'] = self.black_list_data
        if self.customer_ip_address is not None:
            dictionary['customerIpAddress'] = self.customer_ip_address
        if self.product_categories is not None:
            dictionary['productCategories'] = []
            for element in self.product_categories:
                if element is not None:
                    dictionary['productCategories'].append(element)
        return dictionary

    def from_dictionary(self, dictionary):
        super(FraudFields, self).from_dictionary(dictionary)
        if 'blackListData' in dictionary:
            self.black_list_data = dictionary['blackListData']
        if 'customerIpAddress' in dictionary:
            self.customer_ip_address = dictionary['customerIpAddress']
        if 'productCategories' in dictionary:
            if not isinstance(dictionary['productCategories'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['productCategories']))
            self.product_categories = []
            for element in dictionary['productCategories']:
                self.product_categories.append(element)
        return self
