# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class OrderLineDetails(DataObject):

    __discount_amount: Optional[int] = None
    __product_brand: Optional[str] = None
    __product_code: Optional[str] = None
    __product_name: Optional[str] = None
    __product_price: Optional[int] = None
    __product_type: Optional[str] = None
    __quantity: Optional[int] = None
    __tax_amount: Optional[int] = None
    __unit: Optional[str] = None

    @property
    def discount_amount(self) -> Optional[int]:
        """
        | Discount on the line item, with the last two digits implied as decimal places

        Type: int
        """
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, value: Optional[int]) -> None:
        self.__discount_amount = value

    @property
    def product_brand(self) -> Optional[str]:
        """
        | The brand of the product.

        Type: str
        """
        return self.__product_brand

    @product_brand.setter
    def product_brand(self, value: Optional[str]) -> None:
        self.__product_brand = value

    @property
    def product_code(self) -> Optional[str]:
        """
        | Product or UPC Code

        Type: str
        """
        return self.__product_code

    @product_code.setter
    def product_code(self, value: Optional[str]) -> None:
        self.__product_code = value

    @property
    def product_name(self) -> Optional[str]:
        """
        | The name of the product.

        Type: str
        """
        return self.__product_name

    @product_name.setter
    def product_name(self, value: Optional[str]) -> None:
        self.__product_name = value

    @property
    def product_price(self) -> Optional[int]:
        """
        | The price of one unit of the product, the value should be zero or greater

        Type: int
        """
        return self.__product_price

    @product_price.setter
    def product_price(self, value: Optional[int]) -> None:
        self.__product_price = value

    @property
    def product_type(self) -> Optional[str]:
        """
        | Code used to classify items that are purchased

        Type: str
        """
        return self.__product_type

    @product_type.setter
    def product_type(self, value: Optional[str]) -> None:
        self.__product_type = value

    @property
    def quantity(self) -> Optional[int]:
        """
        | Quantity of the units being purchased, should be greater than zero Note: Must not be all spaces or all zeros

        Type: int
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value: Optional[int]) -> None:
        self.__quantity = value

    @property
    def tax_amount(self) -> Optional[int]:
        """
        | Tax on the line item, with the last two digits implied as decimal places

        Type: int
        """
        return self.__tax_amount

    @tax_amount.setter
    def tax_amount(self, value: Optional[int]) -> None:
        self.__tax_amount = value

    @property
    def unit(self) -> Optional[str]:
        """
        | Indicates the line item unit of measure; for example: each, kit, pair, gallon, month, etc.

        Type: str
        """
        return self.__unit

    @unit.setter
    def unit(self, value: Optional[str]) -> None:
        self.__unit = value

    def to_dictionary(self) -> dict:
        dictionary = super(OrderLineDetails, self).to_dictionary()
        if self.discount_amount is not None:
            dictionary['discountAmount'] = self.discount_amount
        if self.product_brand is not None:
            dictionary['productBrand'] = self.product_brand
        if self.product_code is not None:
            dictionary['productCode'] = self.product_code
        if self.product_name is not None:
            dictionary['productName'] = self.product_name
        if self.product_price is not None:
            dictionary['productPrice'] = self.product_price
        if self.product_type is not None:
            dictionary['productType'] = self.product_type
        if self.quantity is not None:
            dictionary['quantity'] = self.quantity
        if self.tax_amount is not None:
            dictionary['taxAmount'] = self.tax_amount
        if self.unit is not None:
            dictionary['unit'] = self.unit
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OrderLineDetails':
        super(OrderLineDetails, self).from_dictionary(dictionary)
        if 'discountAmount' in dictionary:
            self.discount_amount = dictionary['discountAmount']
        if 'productBrand' in dictionary:
            self.product_brand = dictionary['productBrand']
        if 'productCode' in dictionary:
            self.product_code = dictionary['productCode']
        if 'productName' in dictionary:
            self.product_name = dictionary['productName']
        if 'productPrice' in dictionary:
            self.product_price = dictionary['productPrice']
        if 'productType' in dictionary:
            self.product_type = dictionary['productType']
        if 'quantity' in dictionary:
            self.quantity = dictionary['quantity']
        if 'taxAmount' in dictionary:
            self.tax_amount = dictionary['taxAmount']
        if 'unit' in dictionary:
            self.unit = dictionary['unit']
        return self
