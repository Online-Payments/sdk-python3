# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class RedirectPaymentProduct840SpecificInput(DataObject):
    """
    | Object containing specific input required for PayPal payments (Payment product ID 840)
    """

    __address_selection_at_pay_pal = None

    @property
    def address_selection_at_pay_pal(self) -> bool:
        """
        | Indicates whether to use PayPal Express Checkout Shortcut.
        |  * true = When shortcut is enabled, the consumer can select a shipping address during PayPal checkout.
        |  * false = When shortcut is disabled, the consumer cannot change the shipping address.
        | Default value is false.
        | Please note that this field is ignored when order.additionalInput.typeInformation.purchaseType is set to "digital"

        Type: bool
        """
        return self.__address_selection_at_pay_pal

    @address_selection_at_pay_pal.setter
    def address_selection_at_pay_pal(self, value: bool):
        self.__address_selection_at_pay_pal = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct840SpecificInput, self).to_dictionary()
        if self.address_selection_at_pay_pal is not None:
            dictionary['addressSelectionAtPayPal'] = self.address_selection_at_pay_pal
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct840SpecificInput, self).from_dictionary(dictionary)
        if 'addressSelectionAtPayPal' in dictionary:
            self.address_selection_at_pay_pal = dictionary['addressSelectionAtPayPal']
        return self
