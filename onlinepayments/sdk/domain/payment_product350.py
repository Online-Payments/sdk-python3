# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct350(DataObject):

    __app_switch_link: Optional[str] = None
    __payment_request_token: Optional[str] = None

    @property
    def app_switch_link(self) -> Optional[str]:
        """
        | Contains an application switch URL for opening the Swish application on a mobile device (intended to be used by a device with the Swish app installed)

        Type: str
        """
        return self.__app_switch_link

    @app_switch_link.setter
    def app_switch_link(self, value: Optional[str]) -> None:
        self.__app_switch_link = value

    @property
    def payment_request_token(self) -> Optional[str]:
        """
        | Contains the token that identifies the payment on the Swish side. This can be used to generate a QR code (either manually or by calling the public QR Code API of Swish) to be scanned by the Swish app.

        Type: str
        """
        return self.__payment_request_token

    @payment_request_token.setter
    def payment_request_token(self, value: Optional[str]) -> None:
        self.__payment_request_token = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct350, self).to_dictionary()
        if self.app_switch_link is not None:
            dictionary['appSwitchLink'] = self.app_switch_link
        if self.payment_request_token is not None:
            dictionary['paymentRequestToken'] = self.payment_request_token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct350':
        super(PaymentProduct350, self).from_dictionary(dictionary)
        if 'appSwitchLink' in dictionary:
            self.app_switch_link = dictionary['appSwitchLink']
        if 'paymentRequestToken' in dictionary:
            self.payment_request_token = dictionary['paymentRequestToken']
        return self
