#
# This file was automatically generated.
#
from .data_object import DataObject
from .payment_product_field_form_element import PaymentProductFieldFormElement
from .payment_product_field_tooltip import PaymentProductFieldTooltip


class PaymentProductFieldDisplayHints(DataObject):

    __slots__ = (
        "__always_show",
        "__display_order",
        "__form_element",
        "__label",
        "__link",
        "__mask",
        "__obfuscate",
        "__placeholder_label",
        "__preferred_input_type",
        "__tooltip",
    )

    __always_show: bool | None
    __display_order: int | None
    __form_element: PaymentProductFieldFormElement | None
    __label: str | None
    __link: str | None
    __mask: str | None
    __obfuscate: bool | None
    __placeholder_label: str | None
    __preferred_input_type: str | None
    __tooltip: PaymentProductFieldTooltip | None

    def __init__(
        self,
        *,
        always_show: bool | None = None,
        display_order: int | None = None,
        form_element: PaymentProductFieldFormElement | None = None,
        label: str | None = None,
        link: str | None = None,
        mask: str | None = None,
        obfuscate: bool | None = None,
        placeholder_label: str | None = None,
        preferred_input_type: str | None = None,
        tooltip: PaymentProductFieldTooltip | None = None,
    ) -> None:
        self.always_show = always_show
        self.display_order = display_order
        self.form_element = form_element
        self.label = label
        self.link = link
        self.mask = mask
        self.obfuscate = obfuscate
        self.placeholder_label = placeholder_label
        self.preferred_input_type = preferred_input_type
        self.tooltip = tooltip

    @property
    def always_show(self) -> bool | None:
        """
        * true - Indicates that this field is advised to be captured to increase the success rates even-though it isn't marked as required. Please note that making the field required could hurt the success rates negatively. This boolean only indicates our advise to always show this field to the customer.
        * false - Indicates that this field is not to be shown unless it is a required field.

        Type: bool
        """
        return self.__always_show

    @always_show.setter
    def always_show(self, value: bool | None) -> None:
        self.__always_show = value

    @property
    def display_order(self) -> int | None:
        """
        | The order in which the fields should be shown (ascending)

        Type: int
        """
        return self.__display_order

    @display_order.setter
    def display_order(self, value: int | None) -> None:
        self.__display_order = value

    @property
    def form_element(self) -> PaymentProductFieldFormElement | None:
        """
        | Object detailing the type of form element that should be used to present the field

        Type: :class:`onlinepayments.sdk.domain.payment_product_field_form_element.PaymentProductFieldFormElement`
        """
        return self.__form_element

    @form_element.setter
    def form_element(self, value: PaymentProductFieldFormElement | None) -> None:
        self.__form_element = value

    @property
    def label(self) -> str | None:
        """
        | Label/Name of the field to be used in the user interface

        Type: str
        """
        return self.__label

    @label.setter
    def label(self, value: str | None) -> None:
        self.__label = value

    @property
    def link(self) -> str | None:
        """
        | Deprecated: This field is not used by any payment product Link that should be used to replace the '{link}' variable in the label.

        Type: str

        Deprecated; Deprecated
        """
        return self.__link

    @link.setter
    def link(self, value: str | None) -> None:
        self.__link = value

    @property
    def mask(self) -> str | None:
        """
        | A mask that can be used in the input field. You can use it to inject additional characters to provide a better user experience and to restrict the accepted character set (illegal characters will be ignored during typing).
        
        * is used for wildcards (and also chars) 9 is used for numbers Everything outside {{ and }} is used as-is.

        Type: str
        """
        return self.__mask

    @mask.setter
    def mask(self, value: str | None) -> None:
        self.__mask = value

    @property
    def obfuscate(self) -> bool | None:
        """
        * true - The data in this field should be obfuscated as it is entered, just like a password field
        * false - The data in this field does not need to be obfuscated

        Type: bool
        """
        return self.__obfuscate

    @obfuscate.setter
    def obfuscate(self, value: bool | None) -> None:
        self.__obfuscate = value

    @property
    def placeholder_label(self) -> str | None:
        """
        | A placeholder value for the form element

        Type: str
        """
        return self.__placeholder_label

    @placeholder_label.setter
    def placeholder_label(self, value: str | None) -> None:
        self.__placeholder_label = value

    @property
    def preferred_input_type(self) -> str | None:
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
    def preferred_input_type(self, value: str | None) -> None:
        self.__preferred_input_type = value

    @property
    def tooltip(self) -> PaymentProductFieldTooltip | None:
        """
        | Object that contains an optional tooltip to assist the customer

        Type: :class:`onlinepayments.sdk.domain.payment_product_field_tooltip.PaymentProductFieldTooltip`
        """
        return self.__tooltip

    @tooltip.setter
    def tooltip(self, value: PaymentProductFieldTooltip | None) -> None:
        self.__tooltip = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
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
        super().from_dictionary(dictionary)
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
