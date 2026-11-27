#
# This file was automatically generated.
#
from .data_object import DataObject


class FraudFields(DataObject):

    __slots__ = (
        "__black_list_data",
        "__customer_ip_address",
        "__product_categories",
    )

    __black_list_data: str | None
    __customer_ip_address: str | None
    __product_categories: list[str] | None

    def __init__(
        self,
        *,
        black_list_data: str | None = None,
        customer_ip_address: str | None = None,
        product_categories: list[str] | None = None,
    ) -> None:
        self.black_list_data = black_list_data
        self.customer_ip_address = customer_ip_address
        self.product_categories = product_categories

    @property
    def black_list_data(self) -> str | None:
        """
        | Additional black list input

        Type: str
        """
        return self.__black_list_data

    @black_list_data.setter
    def black_list_data(self, value: str | None) -> None:
        self.__black_list_data = value

    @property
    def customer_ip_address(self) -> str | None:
        """
        | Deprecated: Use order.customer.device.ipAddress instead.
        |
        | The IP Address of the customer that is making the payment

        Type: str

        Deprecated; Use order.customer.device.ipAddress instead.  The IP Address of the customer that is making the payment
        """
        return self.__customer_ip_address

    @customer_ip_address.setter
    def customer_ip_address(self, value: str | None) -> None:
        self.__customer_ip_address = value

    @property
    def product_categories(self) -> list[str] | None:
        """
        | List of product categories that are being purchased.

        Type: list[str]
        """
        return self.__product_categories

    @product_categories.setter
    def product_categories(self, value: list[str] | None) -> None:
        self.__product_categories = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
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

    def from_dictionary(self, dictionary: dict) -> 'FraudFields':
        super().from_dictionary(dictionary)
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
