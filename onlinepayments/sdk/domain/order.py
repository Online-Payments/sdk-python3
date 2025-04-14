# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .additional_order_input import AdditionalOrderInput
from .amount_of_money import AmountOfMoney
from .customer import Customer
from .data_object import DataObject
from .discount import Discount
from .order_references import OrderReferences
from .shipping import Shipping
from .shopping_cart import ShoppingCart
from .surcharge_specific_input import SurchargeSpecificInput


class Order(DataObject):

    __additional_input: Optional[AdditionalOrderInput] = None
    __amount_of_money: Optional[AmountOfMoney] = None
    __customer: Optional[Customer] = None
    __discount: Optional[Discount] = None
    __references: Optional[OrderReferences] = None
    __shipping: Optional[Shipping] = None
    __shopping_cart: Optional[ShoppingCart] = None
    __surcharge_specific_input: Optional[SurchargeSpecificInput] = None

    @property
    def additional_input(self) -> Optional[AdditionalOrderInput]:
        """
        | Object containing additional input on the order

        Type: :class:`onlinepayments.sdk.domain.additional_order_input.AdditionalOrderInput`
        """
        return self.__additional_input

    @additional_input.setter
    def additional_input(self, value: Optional[AdditionalOrderInput]) -> None:
        self.__additional_input = value

    @property
    def amount_of_money(self) -> Optional[AmountOfMoney]:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: Optional[AmountOfMoney]) -> None:
        self.__amount_of_money = value

    @property
    def customer(self) -> Optional[Customer]:
        """
        | Object containing the details of the customer

        Type: :class:`onlinepayments.sdk.domain.customer.Customer`
        """
        return self.__customer

    @customer.setter
    def customer(self, value: Optional[Customer]) -> None:
        self.__customer = value

    @property
    def discount(self) -> Optional[Discount]:
        """
        | Object to apply a discount to the total basket by adding a discount line.

        Type: :class:`onlinepayments.sdk.domain.discount.Discount`
        """
        return self.__discount

    @discount.setter
    def discount(self, value: Optional[Discount]) -> None:
        self.__discount = value

    @property
    def references(self) -> Optional[OrderReferences]:
        """
        | Object that holds all reference properties that are linked to this transaction

        Type: :class:`onlinepayments.sdk.domain.order_references.OrderReferences`
        """
        return self.__references

    @references.setter
    def references(self, value: Optional[OrderReferences]) -> None:
        self.__references = value

    @property
    def shipping(self) -> Optional[Shipping]:
        """
        | Object containing information regarding shipping / delivery

        Type: :class:`onlinepayments.sdk.domain.shipping.Shipping`
        """
        return self.__shipping

    @shipping.setter
    def shipping(self, value: Optional[Shipping]) -> None:
        self.__shipping = value

    @property
    def shopping_cart(self) -> Optional[ShoppingCart]:
        """
        | Shopping cart data, including items and specific amounts.

        Type: :class:`onlinepayments.sdk.domain.shopping_cart.ShoppingCart`
        """
        return self.__shopping_cart

    @shopping_cart.setter
    def shopping_cart(self, value: Optional[ShoppingCart]) -> None:
        self.__shopping_cart = value

    @property
    def surcharge_specific_input(self) -> Optional[SurchargeSpecificInput]:
        """
        | Object containing specific input required to apply surcharging to an order.

        Type: :class:`onlinepayments.sdk.domain.surcharge_specific_input.SurchargeSpecificInput`
        """
        return self.__surcharge_specific_input

    @surcharge_specific_input.setter
    def surcharge_specific_input(self, value: Optional[SurchargeSpecificInput]) -> None:
        self.__surcharge_specific_input = value

    def to_dictionary(self) -> dict:
        dictionary = super(Order, self).to_dictionary()
        if self.additional_input is not None:
            dictionary['additionalInput'] = self.additional_input.to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.customer is not None:
            dictionary['customer'] = self.customer.to_dictionary()
        if self.discount is not None:
            dictionary['discount'] = self.discount.to_dictionary()
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        if self.shipping is not None:
            dictionary['shipping'] = self.shipping.to_dictionary()
        if self.shopping_cart is not None:
            dictionary['shoppingCart'] = self.shopping_cart.to_dictionary()
        if self.surcharge_specific_input is not None:
            dictionary['surchargeSpecificInput'] = self.surcharge_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Order':
        super(Order, self).from_dictionary(dictionary)
        if 'additionalInput' in dictionary:
            if not isinstance(dictionary['additionalInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['additionalInput']))
            value = AdditionalOrderInput()
            self.additional_input = value.from_dictionary(dictionary['additionalInput'])
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = Customer()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'discount' in dictionary:
            if not isinstance(dictionary['discount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['discount']))
            value = Discount()
            self.discount = value.from_dictionary(dictionary['discount'])
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = OrderReferences()
            self.references = value.from_dictionary(dictionary['references'])
        if 'shipping' in dictionary:
            if not isinstance(dictionary['shipping'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['shipping']))
            value = Shipping()
            self.shipping = value.from_dictionary(dictionary['shipping'])
        if 'shoppingCart' in dictionary:
            if not isinstance(dictionary['shoppingCart'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['shoppingCart']))
            value = ShoppingCart()
            self.shopping_cart = value.from_dictionary(dictionary['shoppingCart'])
        if 'surchargeSpecificInput' in dictionary:
            if not isinstance(dictionary['surchargeSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeSpecificInput']))
            value = SurchargeSpecificInput()
            self.surcharge_specific_input = value.from_dictionary(dictionary['surchargeSpecificInput'])
        return self
