# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .payment_product_field_data_restrictions import PaymentProductFieldDataRestrictions
from .payment_product_field_display_hints import PaymentProductFieldDisplayHints


class PaymentProductField(DataObject):

    __data_restrictions: Optional[PaymentProductFieldDataRestrictions] = None
    __display_hints: Optional[PaymentProductFieldDisplayHints] = None
    __id: Optional[str] = None
    __type: Optional[str] = None

    @property
    def data_restrictions(self) -> Optional[PaymentProductFieldDataRestrictions]:
        """
        | Object containing data restrictions that apply to this field, like minimum and/or maximum length

        Type: :class:`onlinepayments.sdk.domain.payment_product_field_data_restrictions.PaymentProductFieldDataRestrictions`
        """
        return self.__data_restrictions

    @data_restrictions.setter
    def data_restrictions(self, value: Optional[PaymentProductFieldDataRestrictions]) -> None:
        self.__data_restrictions = value

    @property
    def display_hints(self) -> Optional[PaymentProductFieldDisplayHints]:
        """
        | Object containing display hints for this field, like the order, mask, preferred keyboard

        Type: :class:`onlinepayments.sdk.domain.payment_product_field_display_hints.PaymentProductFieldDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value: Optional[PaymentProductFieldDisplayHints]) -> None:
        self.__display_hints = value

    @property
    def id(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: Optional[str]) -> None:
        self.__id = value

    @property
    def type(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: Optional[str]) -> None:
        self.__type = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProductField, self).to_dictionary()
        if self.data_restrictions is not None:
            dictionary['dataRestrictions'] = self.data_restrictions.to_dictionary()
        if self.display_hints is not None:
            dictionary['displayHints'] = self.display_hints.to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.type is not None:
            dictionary['type'] = self.type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductField':
        super(PaymentProductField, self).from_dictionary(dictionary)
        if 'dataRestrictions' in dictionary:
            if not isinstance(dictionary['dataRestrictions'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['dataRestrictions']))
            value = PaymentProductFieldDataRestrictions()
            self.data_restrictions = value.from_dictionary(dictionary['dataRestrictions'])
        if 'displayHints' in dictionary:
            if not isinstance(dictionary['displayHints'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['displayHints']))
            value = PaymentProductFieldDisplayHints()
            self.display_hints = value.from_dictionary(dictionary['displayHints'])
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self
