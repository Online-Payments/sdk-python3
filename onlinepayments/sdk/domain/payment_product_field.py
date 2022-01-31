# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payment_product_field_data_restrictions import PaymentProductFieldDataRestrictions
from onlinepayments.sdk.domain.payment_product_field_display_hints import PaymentProductFieldDisplayHints


class PaymentProductField(DataObject):
    __data_restrictions = None
    __display_hints = None
    __id = None
    __type = None

    @property
    def data_restrictions(self) -> PaymentProductFieldDataRestrictions:
        """
        | Object containing data restrictions that apply to this field, like minimum and/or maximum length

        Type: :class:`onlinepayments.sdk.domain.payment_product_field_data_restrictions.PaymentProductFieldDataRestrictions`
        """
        return self.__data_restrictions

    @data_restrictions.setter
    def data_restrictions(self, value: PaymentProductFieldDataRestrictions):
        self.__data_restrictions = value

    @property
    def display_hints(self) -> PaymentProductFieldDisplayHints:
        """
        | Object containing display hints for this field, like the order, mask, preferred keyboard

        Type: :class:`onlinepayments.sdk.domain.payment_product_field_display_hints.PaymentProductFieldDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value: PaymentProductFieldDisplayHints):
        self.__display_hints = value

    @property
    def id(self) -> str:
        """
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value

    @property
    def type(self) -> str:
        """
        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: str):
        self.__type = value

    def to_dictionary(self):
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

    def from_dictionary(self, dictionary):
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
