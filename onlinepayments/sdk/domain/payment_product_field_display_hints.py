# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .payment_product_field_form_element import PaymentProductFieldFormElement
from .payment_product_field_tooltip import PaymentProductFieldTooltip


class PaymentProductFieldDisplayHints(DataObject):

    __always_show: Optional[bool] = None
    __display_order: Optional[int] = None
    __form_element: Optional[PaymentProductFieldFormElement] = None
    __label: Optional[str] = None
    __link: Optional[str] = None
    __mask: Optional[str] = None
    __obfuscate: Optional[bool] = None
    __placeholder_label: Optional[str] = None
    __preferred_input_type: Optional[str] = None
    __tooltip: Optional[PaymentProductFieldTooltip] = None

    @property
    def always_show(self) -> Optional[bool]:
        """
        * true - Indicates that this field is advised to be captured to increase the success rates even-though it isn't marked as required. Please note that making the field required could hurt the success rates negatively. This boolean only indicates our advise to always show this field to the customer.
        * false - Indicates that this field is not to be shown unless it is a required field.

        Type: bool
        """
        return self.__always_show

    @always_show.setter
    def always_show(self, value: Optional[bool]) -> None:
        self.__always_show = value

    @property
    def display_order(self) -> Optional[int]:
        """
        | The order in which the fields should be shown (ascending)

        Type: int
        """
        return self.__display_order

    @display_order.setter
    def display_order(self, value: Optional[int]) -> None:
        self.__display_order = value

    @property
    def form_element(self) -> Optional[PaymentProductFieldFormElement]:
        """
        | Object detailing the type of form element that should be used to present the field

        Type: :class:`onlinepayments.sdk.domain.payment_product_field_form_element.PaymentProductFieldFormElement`
        """
        return self.__form_element

    @form_element.setter
    def form_element(self, value: Optional[PaymentProductFieldFormElement]) -> None:
        self.__form_element = value

    @property
    def label(self) -> Optional[str]:
        """
        | Label/Name of the field to be used in the user interface

        Type: str
        """
        return self.__label

    @label.setter
    def label(self, value: Optional[str]) -> None:
        self.__label = value

    @property
    def link(self) -> Optional[str]:
        """
        | Deprecated: This field is not used by any payment product Link that should be used to replace the '{link}' variable in the label.

        Type: str

        Deprecated; Deprecated
        """
        return self.__link

    @link.setter
    def link(self, value: Optional[str]) -> None:
        self.__link = value

    @property
    def mask(self) -> Optional[str]:
        """
        | A mask that can be used in the input field. You can use it to inject additional characters to provide a better user experience and to restrict the accepted character set (illegal characters will be ignored during typing).
        
        * is used for wildcards (and also chars) 9 is used for numbers Everything outside {{ and }} is used as-is.

        Type: str
        """
        return self.__mask

    @mask.setter
    def mask(self, value: Optional[str]) -> None:
        self.__mask = value

    @property
    def obfuscate(self) -> Optional[bool]:
        """
        * true - The data in this field should be obfuscated as it is entered, just like a password field
        * false - The data in this field does not need to be obfuscated

        Type: bool
        """
        return self.__obfuscate

    @obfuscate.setter
    def obfuscate(self, value: Optional[bool]) -> None:
        self.__obfuscate = value

    @property
    def placeholder_label(self) -> Optional[str]:
        """
        | A placeholder value for the form element

        Type: str
        """
        return self.__placeholder_label

    @placeholder_label.setter
    def placeholder_label(self, value: Optional[str]) -> None:
        self.__placeholder_label = value

    @property
    def preferred_input_type(self) -> Optional[str]:
        """
        | The type of keyboard that can best be used to fill out the value of this field. Possible values are:
        
        * PhoneNumberKeyboard - Keyboard that is normally used to enter phone numbers
        * StringKeyboard - Keyboard that is used to enter strings
        * IntegerKeyboard - Keyboard that is used to enter only numerical values
        * EmailAddressKeyboard - Keyboard that allows easier entry of email addresses

        Type: str
        """
        return self.__preferred_input_type

    @preferred_input_type.setter
    def preferred_input_type(self, value: Optional[str]) -> None:
        self.__preferred_input_type = value

    @property
    def tooltip(self) -> Optional[PaymentProductFieldTooltip]:
        """
        | Object that contains an optional tooltip to assist the customer

        Type: :class:`onlinepayments.sdk.domain.payment_product_field_tooltip.PaymentProductFieldTooltip`
        """
        return self.__tooltip

    @tooltip.setter
    def tooltip(self, value: Optional[PaymentProductFieldTooltip]) -> None:
        self.__tooltip = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProductFieldDisplayHints, self).to_dictionary()
        if self.always_show is not None:
            dictionary['alwaysShow'] = self.always_show
        if self.display_order is not None:
            dictionary['displayOrder'] = self.display_order
        if self.form_element is not None:
            dictionary['formElement'] = self.form_element.to_dictionary()
        if self.label is not None:
            dictionary['label'] = self.label
        if self.link is not None:
            dictionary['link'] = self.link
        if self.mask is not None:
            dictionary['mask'] = self.mask
        if self.obfuscate is not None:
            dictionary['obfuscate'] = self.obfuscate
        if self.placeholder_label is not None:
            dictionary['placeholderLabel'] = self.placeholder_label
        if self.preferred_input_type is not None:
            dictionary['preferredInputType'] = self.preferred_input_type
        if self.tooltip is not None:
            dictionary['tooltip'] = self.tooltip.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductFieldDisplayHints':
        super(PaymentProductFieldDisplayHints, self).from_dictionary(dictionary)
        if 'alwaysShow' in dictionary:
            self.always_show = dictionary['alwaysShow']
        if 'displayOrder' in dictionary:
            self.display_order = dictionary['displayOrder']
        if 'formElement' in dictionary:
            if not isinstance(dictionary['formElement'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['formElement']))
            value = PaymentProductFieldFormElement()
            self.form_element = value.from_dictionary(dictionary['formElement'])
        if 'label' in dictionary:
            self.label = dictionary['label']
        if 'link' in dictionary:
            self.link = dictionary['link']
        if 'mask' in dictionary:
            self.mask = dictionary['mask']
        if 'obfuscate' in dictionary:
            self.obfuscate = dictionary['obfuscate']
        if 'placeholderLabel' in dictionary:
            self.placeholder_label = dictionary['placeholderLabel']
        if 'preferredInputType' in dictionary:
            self.preferred_input_type = dictionary['preferredInputType']
        if 'tooltip' in dictionary:
            if not isinstance(dictionary['tooltip'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['tooltip']))
            value = PaymentProductFieldTooltip()
            self.tooltip = value.from_dictionary(dictionary['tooltip'])
        return self
