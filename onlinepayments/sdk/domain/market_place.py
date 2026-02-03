# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class MarketPlace(DataObject):

    __retailer_country: Optional[str] = None
    __retailer_name: Optional[str] = None

    @property
    def retailer_country(self) -> Optional[str]:
        """
        | ISO 3166-1 alpha-2 country code of the retailer.

        Type: str
        """
        return self.__retailer_country

    @retailer_country.setter
    def retailer_country(self, value: Optional[str]) -> None:
        self.__retailer_country = value

    @property
    def retailer_name(self) -> Optional[str]:
        """
        | This field is required if the transaction is performed by a merchant using the marketplace. This field must contain the name of the end merchant.

        Type: str
        """
        return self.__retailer_name

    @retailer_name.setter
    def retailer_name(self, value: Optional[str]) -> None:
        self.__retailer_name = value

    def to_dictionary(self) -> dict:
        dictionary = super(MarketPlace, self).to_dictionary()
        if self.retailer_country is not None:
            dictionary['retailerCountry'] = self.retailer_country
        if self.retailer_name is not None:
            dictionary['retailerName'] = self.retailer_name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MarketPlace':
        super(MarketPlace, self).from_dictionary(dictionary)
        if 'retailerCountry' in dictionary:
            self.retailer_country = dictionary['retailerCountry']
        if 'retailerName' in dictionary:
            self.retailer_name = dictionary['retailerName']
        return self
