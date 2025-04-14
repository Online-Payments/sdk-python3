# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class IINDetail(DataObject):

    __card_type: Optional[str] = None
    __is_allowed_in_context: Optional[bool] = None
    __payment_product_id: Optional[int] = None

    @property
    def card_type(self) -> Optional[str]:
        """
        | The card's type as categorised by the payment method. Possible values are:
        
        * Credit
        * Debit
        * Prepaid

        Type: str
        """
        return self.__card_type

    @card_type.setter
    def card_type(self, value: Optional[str]) -> None:
        self.__card_type = value

    @property
    def is_allowed_in_context(self) -> Optional[bool]:
        """
        | Populated only if you submitted a payment context.
        
        * true - The payment product is allowed in the submitted context.
        * false - The payment product is not allowed in the submitted context. Note that in this case, none of the brands of the card will be allowed in the submitted context.

        Type: bool
        """
        return self.__is_allowed_in_context

    @is_allowed_in_context.setter
    def is_allowed_in_context(self, value: Optional[bool]) -> None:
        self.__is_allowed_in_context = value

    @property
    def payment_product_id(self) -> Optional[int]:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: Optional[int]) -> None:
        self.__payment_product_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(IINDetail, self).to_dictionary()
        if self.card_type is not None:
            dictionary['cardType'] = self.card_type
        if self.is_allowed_in_context is not None:
            dictionary['isAllowedInContext'] = self.is_allowed_in_context
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'IINDetail':
        super(IINDetail, self).from_dictionary(dictionary)
        if 'cardType' in dictionary:
            self.card_type = dictionary['cardType']
        if 'isAllowedInContext' in dictionary:
            self.is_allowed_in_context = dictionary['isAllowedInContext']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
