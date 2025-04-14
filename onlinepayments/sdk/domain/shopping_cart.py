# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .amount_breakdown import AmountBreakdown
from .data_object import DataObject
from .gift_card_purchase import GiftCardPurchase
from .line_item import LineItem


class ShoppingCart(DataObject):

    __amount_breakdown: Optional[List[AmountBreakdown]] = None
    __gift_card_purchase: Optional[GiftCardPurchase] = None
    __is_pre_order: Optional[bool] = None
    __items: Optional[List[LineItem]] = None
    __pre_order_item_availability_date: Optional[str] = None
    __re_order_indicator: Optional[bool] = None

    @property
    def amount_breakdown(self) -> Optional[List[AmountBreakdown]]:
        """
        | Deprecated: Use order.shipping.shippingCost for shipping cost. Other amounts are not used. Determines how the total amount is split into amount types

        Type: list[:class:`onlinepayments.sdk.domain.amount_breakdown.AmountBreakdown`]

        Deprecated; Use order.shipping.shippingCost for shipping cost. Other amounts are not used. Determines how the total amount is split into amount types
        """
        return self.__amount_breakdown

    @amount_breakdown.setter
    def amount_breakdown(self, value: Optional[List[AmountBreakdown]]) -> None:
        self.__amount_breakdown = value

    @property
    def gift_card_purchase(self) -> Optional[GiftCardPurchase]:
        """
        | Object containing information on purchased gift card(s)

        Type: :class:`onlinepayments.sdk.domain.gift_card_purchase.GiftCardPurchase`
        """
        return self.__gift_card_purchase

    @gift_card_purchase.setter
    def gift_card_purchase(self, value: Optional[GiftCardPurchase]) -> None:
        self.__gift_card_purchase = value

    @property
    def is_pre_order(self) -> Optional[bool]:
        """
        | The customer is pre-ordering one or more items

        Type: bool
        """
        return self.__is_pre_order

    @is_pre_order.setter
    def is_pre_order(self, value: Optional[bool]) -> None:
        self.__is_pre_order = value

    @property
    def items(self) -> Optional[List[LineItem]]:
        """
        | Shopping cart data

        Type: list[:class:`onlinepayments.sdk.domain.line_item.LineItem`]
        """
        return self.__items

    @items.setter
    def items(self, value: Optional[List[LineItem]]) -> None:
        self.__items = value

    @property
    def pre_order_item_availability_date(self) -> Optional[str]:
        """
        | Date (YYYYMMDD) when the preordered item becomes available

        Type: str
        """
        return self.__pre_order_item_availability_date

    @pre_order_item_availability_date.setter
    def pre_order_item_availability_date(self, value: Optional[str]) -> None:
        self.__pre_order_item_availability_date = value

    @property
    def re_order_indicator(self) -> Optional[bool]:
        """
        | Indicates whether the cardholder is reordering previously purchased item(s)
        |
        | true = the customer is re-ordering at least one of the items again
        |
        | false = this is the first time the customer is ordering these items

        Type: bool
        """
        return self.__re_order_indicator

    @re_order_indicator.setter
    def re_order_indicator(self, value: Optional[bool]) -> None:
        self.__re_order_indicator = value

    def to_dictionary(self) -> dict:
        dictionary = super(ShoppingCart, self).to_dictionary()
        if self.amount_breakdown is not None:
            dictionary['amountBreakdown'] = []
            for element in self.amount_breakdown:
                if element is not None:
                    dictionary['amountBreakdown'].append(element.to_dictionary())
        if self.gift_card_purchase is not None:
            dictionary['giftCardPurchase'] = self.gift_card_purchase.to_dictionary()
        if self.is_pre_order is not None:
            dictionary['isPreOrder'] = self.is_pre_order
        if self.items is not None:
            dictionary['items'] = []
            for element in self.items:
                if element is not None:
                    dictionary['items'].append(element.to_dictionary())
        if self.pre_order_item_availability_date is not None:
            dictionary['preOrderItemAvailabilityDate'] = self.pre_order_item_availability_date
        if self.re_order_indicator is not None:
            dictionary['reOrderIndicator'] = self.re_order_indicator
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ShoppingCart':
        super(ShoppingCart, self).from_dictionary(dictionary)
        if 'amountBreakdown' in dictionary:
            if not isinstance(dictionary['amountBreakdown'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['amountBreakdown']))
            self.amount_breakdown = []
            for element in dictionary['amountBreakdown']:
                value = AmountBreakdown()
                self.amount_breakdown.append(value.from_dictionary(element))
        if 'giftCardPurchase' in dictionary:
            if not isinstance(dictionary['giftCardPurchase'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['giftCardPurchase']))
            value = GiftCardPurchase()
            self.gift_card_purchase = value.from_dictionary(dictionary['giftCardPurchase'])
        if 'isPreOrder' in dictionary:
            self.is_pre_order = dictionary['isPreOrder']
        if 'items' in dictionary:
            if not isinstance(dictionary['items'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['items']))
            self.items = []
            for element in dictionary['items']:
                value = LineItem()
                self.items.append(value.from_dictionary(element))
        if 'preOrderItemAvailabilityDate' in dictionary:
            self.pre_order_item_availability_date = dictionary['preOrderItemAvailabilityDate']
        if 'reOrderIndicator' in dictionary:
            self.re_order_indicator = dictionary['reOrderIndicator']
        return self
