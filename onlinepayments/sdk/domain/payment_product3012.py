# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PaymentProduct3012(DataObject):
    """
    | Contains the third party data for payment product 3012 (Bancontact)
    """

    __qr_code = None
    __url_intent = None

    @property
    def qr_code(self) -> str:
        """
        | Contains a base64 encoded PNG image. By prepending data:image/png;base64, this value can be used as the source of an HTML inline image on a desktop or tablet (intended to be scanned by a device with the Bancontact app)

        Type: str
        """
        return self.__qr_code

    @qr_code.setter
    def qr_code(self, value: str):
        self.__qr_code = value

    @property
    def url_intent(self) -> str:
        """
        | Contains URL intent that can be used as the link of an "open the app" button on a device

        Type: str
        """
        return self.__url_intent

    @url_intent.setter
    def url_intent(self, value: str):
        self.__url_intent = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct3012, self).to_dictionary()
        if self.qr_code is not None:
            dictionary['qrCode'] = self.qr_code
        if self.url_intent is not None:
            dictionary['urlIntent'] = self.url_intent
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct3012, self).from_dictionary(dictionary)
        if 'qrCode' in dictionary:
            self.qr_code = dictionary['qrCode']
        if 'urlIntent' in dictionary:
            self.url_intent = dictionary['urlIntent']
        return self
