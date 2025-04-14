# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RedirectPaymentProduct840SpecificInput(DataObject):

    __java_script_sdk_flow: Optional[bool] = None
    __address_selection_at_pay_pal: Optional[bool] = None
    __custom: Optional[str] = None
    __pay_later: Optional[bool] = None

    @property
    def java_script_sdk_flow(self) -> Optional[bool]:
        """
        | To be enabled when Javascript SDK integration is implemented on S2S flow
        
        * false = When this flag is disabled the field RedirectionURL is returned by CreatePayment call and should be used in merchant implementation to redirect buyer to PayPal.
        * true = When this flag is enabled the field orderID is returned by CreatePayment call and should be utilized in case merchant has integrated JS SDK button on their S2S implementation Default value is false.

        Type: bool
        """
        return self.__java_script_sdk_flow

    @java_script_sdk_flow.setter
    def java_script_sdk_flow(self, value: Optional[bool]) -> None:
        self.__java_script_sdk_flow = value

    @property
    def address_selection_at_pay_pal(self) -> Optional[bool]:
        """
        | Indicates whether to use PayPal Express Checkout Shortcut.
        
        * true = When shortcut is enabled, the consumer can select a shipping address during PayPal checkout.
        * false = When shortcut is disabled, the consumer cannot change the shipping address. Default value is false. Please note that this field is ignored when order.additionalInput.typeInformation.purchaseType is set to "digital"

        Type: bool
        """
        return self.__address_selection_at_pay_pal

    @address_selection_at_pay_pal.setter
    def address_selection_at_pay_pal(self, value: Optional[bool]) -> None:
        self.__address_selection_at_pay_pal = value

    @property
    def custom(self) -> Optional[str]:
        """
        | Free text field that you can use to support reconciliation flow.

        Type: str
        """
        return self.__custom

    @custom.setter
    def custom(self, value: Optional[str]) -> None:
        self.__custom = value

    @property
    def pay_later(self) -> Optional[bool]:
        """
        | Indicates whether to allow PayPal Pay Later option.
        
        * true = When option is enabled, the consumer can select the PayPal PayLater button given that the merchant meets the eligibility criteria from PayPal.
        * false = When option is disabled, the consumer cannot select the PayPal PayLater button. Default value is true.

        Type: bool
        """
        return self.__pay_later

    @pay_later.setter
    def pay_later(self, value: Optional[bool]) -> None:
        self.__pay_later = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct840SpecificInput, self).to_dictionary()
        if self.java_script_sdk_flow is not None:
            dictionary['JavaScriptSdkFlow'] = self.java_script_sdk_flow
        if self.address_selection_at_pay_pal is not None:
            dictionary['addressSelectionAtPayPal'] = self.address_selection_at_pay_pal
        if self.custom is not None:
            dictionary['custom'] = self.custom
        if self.pay_later is not None:
            dictionary['payLater'] = self.pay_later
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct840SpecificInput':
        super(RedirectPaymentProduct840SpecificInput, self).from_dictionary(dictionary)
        if 'JavaScriptSdkFlow' in dictionary:
            self.java_script_sdk_flow = dictionary['JavaScriptSdkFlow']
        if 'addressSelectionAtPayPal' in dictionary:
            self.address_selection_at_pay_pal = dictionary['addressSelectionAtPayPal']
        if 'custom' in dictionary:
            self.custom = dictionary['custom']
        if 'payLater' in dictionary:
            self.pay_later = dictionary['payLater']
        return self
