# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct3012(DataObject):

    __qr_code: Optional[str] = None
    __url_intent: Optional[str] = None

    @property
    def qr_code(self) -> Optional[str]:
        """
        | Contains a value which can be used to build a QR code (intended to be scanned by a device with the Bancontact app)

        Type: str
        """
        return self.__qr_code

    @qr_code.setter
    def qr_code(self, value: Optional[str]) -> None:
        self.__qr_code = value

    @property
    def url_intent(self) -> Optional[str]:
        """
        | Contains URL intent that can be used as the link of an "open the app" button on a device

        Type: str
        """
        return self.__url_intent

    @url_intent.setter
    def url_intent(self, value: Optional[str]) -> None:
        self.__url_intent = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct3012, self).to_dictionary()
        if self.qr_code is not None:
            dictionary['qrCode'] = self.qr_code
        if self.url_intent is not None:
            dictionary['urlIntent'] = self.url_intent
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct3012':
        super(PaymentProduct3012, self).from_dictionary(dictionary)
        if 'qrCode' in dictionary:
            self.qr_code = dictionary['qrCode']
        if 'urlIntent' in dictionary:
            self.url_intent = dictionary['urlIntent']
        return self
