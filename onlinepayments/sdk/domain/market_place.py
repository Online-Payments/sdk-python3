#
# This file was automatically generated.
#
from .data_object import DataObject


class MarketPlace(DataObject):

    __slots__ = (
        "__retailer_country",
        "__retailer_name",
    )

    __retailer_country: str | None
    __retailer_name: str | None

    def __init__(
        self,
        *,
        retailer_country: str | None = None,
        retailer_name: str | None = None,
    ) -> None:
        self.retailer_country = retailer_country
        self.retailer_name = retailer_name

    @property
    def retailer_country(self) -> str | None:
        """
        | ISO 3166-1 alpha-2 country code of the retailer.

        Type: str
        """
        return self.__retailer_country

    @retailer_country.setter
    def retailer_country(self, value: str | None) -> None:
        self.__retailer_country = value

    @property
    def retailer_name(self) -> str | None:
        """
        | This field is required if the transaction is performed by a merchant using the marketplace. This field must contain the name of the end merchant.

        Type: str
        """
        return self.__retailer_name

    @retailer_name.setter
    def retailer_name(self, value: str | None) -> None:
        self.__retailer_name = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.retailer_country is not None:
            dictionary['retailerCountry'] = self.retailer_country
        if self.retailer_name is not None:
            dictionary['retailerName'] = self.retailer_name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MarketPlace':
        super().from_dictionary(dictionary)
        if 'retailerCountry' in dictionary:
            self.retailer_country = dictionary['retailerCountry']
        if 'retailerName' in dictionary:
            self.retailer_name = dictionary['retailerName']
        return self
