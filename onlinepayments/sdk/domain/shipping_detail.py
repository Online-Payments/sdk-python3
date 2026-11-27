#
# This file was automatically generated.
#
from .data_object import DataObject


class ShippingDetail(DataObject):

    __slots__ = (
        "__shipping_cost",
        "__shipping_cost_tax",
    )

    __shipping_cost: int | None
    __shipping_cost_tax: int | None

    def __init__(
        self,
        *,
        shipping_cost: int | None = None,
        shipping_cost_tax: int | None = None,
    ) -> None:
        self.shipping_cost = shipping_cost
        self.shipping_cost_tax = shipping_cost_tax

    @property
    def shipping_cost(self) -> int | None:
        """
        | Amount in the smallest currency unit, i.e.:
        
        * EUR is a 2-decimals currency, the value 1234 will result in EUR 12.34
        * KWD is a 3-decimals currency, the value 1234 will result in KWD 1.234
        * JPY is a zero-decimal currency, the value 1234 will result in JPY 1234

        Type: int
        """
        return self.__shipping_cost

    @shipping_cost.setter
    def shipping_cost(self, value: int | None) -> None:
        self.__shipping_cost = value

    @property
    def shipping_cost_tax(self) -> int | None:
        """
        | Amount in the smallest currency unit, i.e.:
        
        * EUR is a 2-decimals currency, the value 1234 will result in EUR 12.34
        * KWD is a 3-decimals currency, the value 1234 will result in KWD 1.234
        * JPY is a zero-decimal currency, the value 1234 will result in JPY 1234

        Type: int
        """
        return self.__shipping_cost_tax

    @shipping_cost_tax.setter
    def shipping_cost_tax(self, value: int | None) -> None:
        self.__shipping_cost_tax = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.shipping_cost is not None:
            dictionary['shippingCost'] = self.shipping_cost
        if self.shipping_cost_tax is not None:
            dictionary['shippingCostTax'] = self.shipping_cost_tax
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ShippingDetail':
        super().from_dictionary(dictionary)
        if 'shippingCost' in dictionary:
            self.shipping_cost = dictionary['shippingCost']
        if 'shippingCostTax' in dictionary:
            self.shipping_cost_tax = dictionary['shippingCostTax']
        return self
