# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct5407(DataObject):

    __pairing_token: Optional[str] = None
    __qr_code: Optional[str] = None

    @property
    def pairing_token(self) -> Optional[str]:
        """
        | A numeric token, which the user has to copy or type into the TWINT app in order to pair it with the merchant for the payment process.

        Type: str
        """
        return self.__pairing_token

    @pairing_token.setter
    def pairing_token(self, value: Optional[str]) -> None:
        self.__pairing_token = value

    @property
    def qr_code(self) -> Optional[str]:
        """
        | Contains a base64 encoded PNG image. By prepending data:image/png;base64, this value can be used as the source of an HTML inline image on a desktop or tablet (intended to be scanned by a device with the Twint app)

        Type: str
        """
        return self.__qr_code

    @qr_code.setter
    def qr_code(self, value: Optional[str]) -> None:
        self.__qr_code = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct5407, self).to_dictionary()
        if self.pairing_token is not None:
            dictionary['pairingToken'] = self.pairing_token
        if self.qr_code is not None:
            dictionary['qrCode'] = self.qr_code
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct5407':
        super(PaymentProduct5407, self).from_dictionary(dictionary)
        if 'pairingToken' in dictionary:
            self.pairing_token = dictionary['pairingToken']
        if 'qrCode' in dictionary:
            self.qr_code = dictionary['qrCode']
        return self
