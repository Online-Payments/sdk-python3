#
# This file was automatically generated.
#
from .address_personal import AddressPersonal
from .data_object import DataObject
from .shipping_method import ShippingMethod


class Shipping(DataObject):

    __slots__ = (
        "__address",
        "__address_indicator",
        "__email_address",
        "__first_usage_date",
        "__is_first_usage",
        "__method",
        "__shipping_cost",
        "__shipping_cost_tax",
        "__type",
    )

    __address: AddressPersonal | None
    __address_indicator: str | None
    __email_address: str | None
    __first_usage_date: str | None
    __is_first_usage: bool | None
    __method: ShippingMethod | None
    __shipping_cost: int | None
    __shipping_cost_tax: int | None
    __type: str | None

    def __init__(
        self,
        *,
        address: AddressPersonal | None = None,
        address_indicator: str | None = None,
        email_address: str | None = None,
        first_usage_date: str | None = None,
        is_first_usage: bool | None = None,
        method: ShippingMethod | None = None,
        shipping_cost: int | None = None,
        shipping_cost_tax: int | None = None,
        type: str | None = None,
    ) -> None:
        self.address = address
        self.address_indicator = address_indicator
        self.email_address = email_address
        self.first_usage_date = first_usage_date
        self.is_first_usage = is_first_usage
        self.method = method
        self.shipping_cost = shipping_cost
        self.shipping_cost_tax = shipping_cost_tax
        self.type = type

    @property
    def address(self) -> AddressPersonal | None:
        """
        | Object containing address information

        Type: :class:`onlinepayments.sdk.domain.address_personal.AddressPersonal`
        """
        return self.__address

    @address.setter
    def address(self, value: AddressPersonal | None) -> None:
        self.__address = value

    @property
    def address_indicator(self) -> str | None:
        """
        | Indicates shipping method chosen for the transaction. Possible values:
        
        * same-as-billing = the shipping address is the same as the billing address
        * another-verified-address-on-file-with-merchant = the address used for shipping is another verified address of the customer that is on file with you
        * different-than-billing = shipping address is different from the billing address
        * ship-to-store = goods are shipped to a store (shipping address = store address)
        * digital-goods = electronic delivery of digital goods
        * travel-and-event-tickets-not-shipped = travel and/or event tickets that are not shipped
        * other = other means of delivery

        Type: str
        """
        return self.__address_indicator

    @address_indicator.setter
    def address_indicator(self, value: str | None) -> None:
        self.__address_indicator = value

    @property
    def email_address(self) -> str | None:
        """
        | Email address linked to the shipping

        Type: str
        """
        return self.__email_address

    @email_address.setter
    def email_address(self, value: str | None) -> None:
        self.__email_address = value

    @property
    def first_usage_date(self) -> str | None:
        """
        | Date (YYYYMMDD) when the shipping details for this transaction were first used.

        Type: str
        """
        return self.__first_usage_date

    @first_usage_date.setter
    def first_usage_date(self, value: str | None) -> None:
        self.__first_usage_date = value

    @property
    def is_first_usage(self) -> bool | None:
        """
        | Indicator if this shipping address is used for the first time to ship an order
        |
        | true = the shipping details are used for the first time with this transaction
        |
        | false = the shipping details have been used for other transactions in the past

        Type: bool
        """
        return self.__is_first_usage

    @is_first_usage.setter
    def is_first_usage(self, value: bool | None) -> None:
        self.__is_first_usage = value

    @property
    def method(self) -> ShippingMethod | None:
        """
        | Object containing information regarding shipping method

        Type: :class:`onlinepayments.sdk.domain.shipping_method.ShippingMethod`
        """
        return self.__method

    @method.setter
    def method(self, value: ShippingMethod | None) -> None:
        self.__method = value

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

    @property
    def type(self) -> str | None:
        """
        | Indicates the merchandise delivery timeframe. Possible values:
        
        * electronic = For electronic delivery (services or digital goods)
        * same-day = For same day deliveries
        * overnight = For overnight deliveries
        * 2-day-or-more = For two day or more delivery time

        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: str | None) -> None:
        self.__type = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.address is not None:
            dictionary['address'] = self.address.to_dictionary()
        if self.address_indicator is not None:
            dictionary['addressIndicator'] = self.address_indicator
        if self.email_address is not None:
            dictionary['emailAddress'] = self.email_address
        if self.first_usage_date is not None:
            dictionary['firstUsageDate'] = self.first_usage_date
        if self.is_first_usage is not None:
            dictionary['isFirstUsage'] = self.is_first_usage
        if self.method is not None:
            dictionary['method'] = self.method.to_dictionary()
        if self.shipping_cost is not None:
            dictionary['shippingCost'] = self.shipping_cost
        if self.shipping_cost_tax is not None:
            dictionary['shippingCostTax'] = self.shipping_cost_tax
        if self.type is not None:
            dictionary['type'] = self.type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Shipping':
        super().from_dictionary(dictionary)
        if 'address' in dictionary:
            if not isinstance(dictionary['address'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['address']))
            value = AddressPersonal()
            self.address = value.from_dictionary(dictionary['address'])
        if 'addressIndicator' in dictionary:
            self.address_indicator = dictionary['addressIndicator']
        if 'emailAddress' in dictionary:
            self.email_address = dictionary['emailAddress']
        if 'firstUsageDate' in dictionary:
            self.first_usage_date = dictionary['firstUsageDate']
        if 'isFirstUsage' in dictionary:
            self.is_first_usage = dictionary['isFirstUsage']
        if 'method' in dictionary:
            if not isinstance(dictionary['method'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['method']))
            value = ShippingMethod()
            self.method = value.from_dictionary(dictionary['method'])
        if 'shippingCost' in dictionary:
            self.shipping_cost = dictionary['shippingCost']
        if 'shippingCostTax' in dictionary:
            self.shipping_cost_tax = dictionary['shippingCostTax']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self
