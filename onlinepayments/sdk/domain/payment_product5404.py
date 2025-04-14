# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct5404(DataObject):

    __app_switch_link: Optional[str] = None
    __qr_code_url: Optional[str] = None

    @property
    def app_switch_link(self) -> Optional[str]:
        """
        | Contains a application switch url that should open WeChat Pay application in mobile device (intended to be used by a device with the WeChat Pay app)

        Type: str
        """
        return self.__app_switch_link

    @app_switch_link.setter
    def app_switch_link(self, value: Optional[str]) -> None:
        self.__app_switch_link = value

    @property
    def qr_code_url(self) -> Optional[str]:
        """
        | Contains a QR code url that can be used to build a QR code (intended to be scanned by a device with the WeChat Pay app)

        Type: str
        """
        return self.__qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value: Optional[str]) -> None:
        self.__qr_code_url = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct5404, self).to_dictionary()
        if self.app_switch_link is not None:
            dictionary['appSwitchLink'] = self.app_switch_link
        if self.qr_code_url is not None:
            dictionary['qrCodeUrl'] = self.qr_code_url
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct5404':
        super(PaymentProduct5404, self).from_dictionary(dictionary)
        if 'appSwitchLink' in dictionary:
            self.app_switch_link = dictionary['appSwitchLink']
        if 'qrCodeUrl' in dictionary:
            self.qr_code_url = dictionary['qrCodeUrl']
        return self
