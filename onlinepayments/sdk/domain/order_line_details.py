#
# This file was automatically generated.
#
from .data_object import DataObject


class OrderLineDetails(DataObject):

    __slots__ = (
        "__discount_amount",
        "__product_brand",
        "__product_code",
        "__product_name",
        "__product_price",
        "__product_type",
        "__quantity",
        "__tax_amount",
        "__tax_percentage",
        "__unit",
    )

    __discount_amount: int | None
    __product_brand: str | None
    __product_code: str | None
    __product_name: str | None
    __product_price: int | None
    __product_type: str | None
    __quantity: int | None
    __tax_amount: int | None
    __tax_percentage: float | None
    __unit: str | None

    def __init__(
        self,
        *,
        discount_amount: int | None = None,
        product_brand: str | None = None,
        product_code: str | None = None,
        product_name: str | None = None,
        product_price: int | None = None,
        product_type: str | None = None,
        quantity: int | None = None,
        tax_amount: int | None = None,
        tax_percentage: float | None = None,
        unit: str | None = None,
    ) -> None:
        self.discount_amount = discount_amount
        self.product_brand = product_brand
        self.product_code = product_code
        self.product_name = product_name
        self.product_price = product_price
        self.product_type = product_type
        self.quantity = quantity
        self.tax_amount = tax_amount
        self.tax_percentage = tax_percentage
        self.unit = unit

    @property
    def discount_amount(self) -> int | None:
        """
        | Amount in the smallest currency unit, i.e.:
        
        * EUR is a 2-decimals currency, the value 1234 will result in EUR 12.34
        * KWD is a 3-decimals currency, the value 1234 will result in KWD 1.234
        * JPY is a zero-decimal currency, the value 1234 will result in JPY 1234

        Type: int
        """
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, value: int | None) -> None:
        self.__discount_amount = value

    @property
    def product_brand(self) -> str | None:
        """
        | The brand of the product.

        Type: str
        """
        return self.__product_brand

    @product_brand.setter
    def product_brand(self, value: str | None) -> None:
        self.__product_brand = value

    @property
    def product_code(self) -> str | None:
        """
        | Product or UPC Code

        Type: str
        """
        return self.__product_code

    @product_code.setter
    def product_code(self, value: str | None) -> None:
        self.__product_code = value

    @property
    def product_name(self) -> str | None:
        """
        | The name of the product.

        Type: str
        """
        return self.__product_name

    @product_name.setter
    def product_name(self, value: str | None) -> None:
        self.__product_name = value

    @property
    def product_price(self) -> int | None:
        """
        | The price of one unit of the product, the value should be zero or greater

        Type: int
        """
        return self.__product_price

    @product_price.setter
    def product_price(self, value: int | None) -> None:
        self.__product_price = value

    @property
    def product_type(self) -> str | None:
        """
        | Code used to classify items that are purchased

        Type: str
        """
        return self.__product_type

    @product_type.setter
    def product_type(self, value: str | None) -> None:
        self.__product_type = value

    @property
    def quantity(self) -> int | None:
        """
        | Quantity of the units being purchased, should be greater than zero Note: Must not be all spaces or all zeros

        Type: int
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int | None) -> None:
        self.__quantity = value

    @property
    def tax_amount(self) -> int | None:
        """
        | Amount in the smallest currency unit, i.e.:
        
        * EUR is a 2-decimals currency, the value 1234 will result in EUR 12.34
        * KWD is a 3-decimals currency, the value 1234 will result in KWD 1.234
        * JPY is a zero-decimal currency, the value 1234 will result in JPY 1234

        Type: int
        """
        return self.__tax_amount

    @tax_amount.setter
    def tax_amount(self, value: int | None) -> None:
        self.__tax_amount = value

    @property
    def tax_percentage(self) -> float | None:
        """
        | tax percentage, in hundredths of a percent. For example, for a tax percentage of 21%, this field should be set to 2100. Omit if not applicable or not known.

        Type: float
        """
        return self.__tax_percentage

    @tax_percentage.setter
    def tax_percentage(self, value: float | None) -> None:
        self.__tax_percentage = value

    @property
    def unit(self) -> str | None:
        """
        | Indicates the line item unit of measure; for example: each, kit, pair, gallon, month, etc.

        Type: str
        """
        return self.__unit

    @unit.setter
    def unit(self, value: str | None) -> None:
        self.__unit = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
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
        if self.tax_percentage is not None:
            dictionary['taxPercentage'] = self.tax_percentage
        if self.unit is not None:
            dictionary['unit'] = self.unit
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OrderLineDetails':
        super().from_dictionary(dictionary)
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
        if 'taxPercentage' in dictionary:
            self.tax_percentage = dictionary['taxPercentage']
        if 'unit' in dictionary:
            self.unit = dictionary['unit']
        return self
