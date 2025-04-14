# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_of_money import AmountOfMoney
from .data_object import DataObject
from .line_item_invoice_data import LineItemInvoiceData
from .order_line_details import OrderLineDetails
from .other_details import OtherDetails


class LineItem(DataObject):

    __amount_of_money: Optional[AmountOfMoney] = None
    __invoice_data: Optional[LineItemInvoiceData] = None
    __order_line_details: Optional[OrderLineDetails] = None
    __other_details: Optional[OtherDetails] = None

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
    def invoice_data(self) -> Optional[LineItemInvoiceData]:
        """
        | Object containing the line items of the invoice or shopping cart

        Type: :class:`onlinepayments.sdk.domain.line_item_invoice_data.LineItemInvoiceData`
        """
        return self.__invoice_data

    @invoice_data.setter
    def invoice_data(self, value: Optional[LineItemInvoiceData]) -> None:
        self.__invoice_data = value

    @property
    def order_line_details(self) -> Optional[OrderLineDetails]:
        """
        | Object containing additional information that when supplied can have a beneficial effect on the discountrates

        Type: :class:`onlinepayments.sdk.domain.order_line_details.OrderLineDetails`
        """
        return self.__order_line_details

    @order_line_details.setter
    def order_line_details(self, value: Optional[OrderLineDetails]) -> None:
        self.__order_line_details = value

    @property
    def other_details(self) -> Optional[OtherDetails]:
        """
        | Other information for specific payment methods.

        Type: :class:`onlinepayments.sdk.domain.other_details.OtherDetails`
        """
        return self.__other_details

    @other_details.setter
    def other_details(self, value: Optional[OtherDetails]) -> None:
        self.__other_details = value

    def to_dictionary(self) -> dict:
        dictionary = super(LineItem, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.invoice_data is not None:
            dictionary['invoiceData'] = self.invoice_data.to_dictionary()
        if self.order_line_details is not None:
            dictionary['orderLineDetails'] = self.order_line_details.to_dictionary()
        if self.other_details is not None:
            dictionary['otherDetails'] = self.other_details.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'LineItem':
        super(LineItem, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'invoiceData' in dictionary:
            if not isinstance(dictionary['invoiceData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['invoiceData']))
            value = LineItemInvoiceData()
            self.invoice_data = value.from_dictionary(dictionary['invoiceData'])
        if 'orderLineDetails' in dictionary:
            if not isinstance(dictionary['orderLineDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['orderLineDetails']))
            value = OrderLineDetails()
            self.order_line_details = value.from_dictionary(dictionary['orderLineDetails'])
        if 'otherDetails' in dictionary:
            if not isinstance(dictionary['otherDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['otherDetails']))
            value = OtherDetails()
            self.other_details = value.from_dictionary(dictionary['otherDetails'])
        return self
