# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .address_personal import AddressPersonal
from .data_object import DataObject
from .shipping_method import ShippingMethod


class Shipping(DataObject):

    __address: Optional[AddressPersonal] = None
    __address_indicator: Optional[str] = None
    __email_address: Optional[str] = None
    __first_usage_date: Optional[str] = None
    __is_first_usage: Optional[bool] = None
    __method: Optional[ShippingMethod] = None
    __shipping_cost: Optional[int] = None
    __shipping_cost_tax: Optional[int] = None
    __type: Optional[str] = None

    @property
    def address(self) -> Optional[AddressPersonal]:
        """
        | Object containing address information

        Type: :class:`onlinepayments.sdk.domain.address_personal.AddressPersonal`
        """
        return self.__address

    @address.setter
    def address(self, value: Optional[AddressPersonal]) -> None:
        self.__address = value

    @property
    def address_indicator(self) -> Optional[str]:
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
    def address_indicator(self, value: Optional[str]) -> None:
        self.__address_indicator = value

    @property
    def email_address(self) -> Optional[str]:
        """
        | Email address linked to the shipping

        Type: str
        """
        return self.__email_address

    @email_address.setter
    def email_address(self, value: Optional[str]) -> None:
        self.__email_address = value

    @property
    def first_usage_date(self) -> Optional[str]:
        """
        | Date (YYYYMMDD) when the shipping details for this transaction were first used.

        Type: str
        """
        return self.__first_usage_date

    @first_usage_date.setter
    def first_usage_date(self, value: Optional[str]) -> None:
        self.__first_usage_date = value

    @property
    def is_first_usage(self) -> Optional[bool]:
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
    def is_first_usage(self, value: Optional[bool]) -> None:
        self.__is_first_usage = value

    @property
    def method(self) -> Optional[ShippingMethod]:
        """
        | Object containing information regarding shipping method

        Type: :class:`onlinepayments.sdk.domain.shipping_method.ShippingMethod`
        """
        return self.__method

    @method.setter
    def method(self, value: Optional[ShippingMethod]) -> None:
        self.__method = value

    @property
    def shipping_cost(self) -> Optional[int]:
        """
        | Cost associated with the shipping of the order.

        Type: int
        """
        return self.__shipping_cost

    @shipping_cost.setter
    def shipping_cost(self, value: Optional[int]) -> None:
        self.__shipping_cost = value

    @property
    def shipping_cost_tax(self) -> Optional[int]:
        """
        | Tax amount of the shipping cost.

        Type: int
        """
        return self.__shipping_cost_tax

    @shipping_cost_tax.setter
    def shipping_cost_tax(self, value: Optional[int]) -> None:
        self.__shipping_cost_tax = value

    @property
    def type(self) -> Optional[str]:
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
    def type(self, value: Optional[str]) -> None:
        self.__type = value

    def to_dictionary(self) -> dict:
        dictionary = super(Shipping, self).to_dictionary()
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
        super(Shipping, self).from_dictionary(dictionary)
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
