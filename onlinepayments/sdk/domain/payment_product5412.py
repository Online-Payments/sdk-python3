# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct5412(DataObject):

    __app_url: Optional[str] = None
    __polling_url: Optional[str] = None
    __qr_code: Optional[str] = None

    @property
    def app_url(self) -> Optional[str]:
        """
        | A URL intended for mobile devices that is to be linked to the QR code so that mobile users can tap it, to open the Chèque-Vacances app.

        Type: str
        """
        return self.__app_url

    @app_url.setter
    def app_url(self, value: Optional[str]) -> None:
        self.__app_url = value

    @property
    def polling_url(self) -> Optional[str]:
        """
        | A URL that must be polled using JavaScript; it responds with one of the following:
        
        * PRETRANSACTION, which indicates that the user has not yet consummed the QR code. At this step, the user can still be allowed to enter their beneficiary ID (or an e-mail known by ANCV) to initiate a CV Connect payment. As long as the response status is 'PRETRANSACTION', the input form should be shown and polling should continue.
        * TRANSACTION, which indicates that the buyer has used the QR code to open the Chèque-Vacances app, but has not yet confirmed the payment in the app. In this case, you should show a message asking the user to confirm the payment in their Chèque-Vacances app and continue polling. The user should no longer be allowed to enter their beneficiary ID. As long as the response status is not 'FINALIZED', the message should be shown and polling should continue.
        * FINALIZED, which indicates that the CV Connect process has concluded, but it does not necessarily confirm a successful payment. In this case, you should verify the payment outcome and redirect the customer to your status page accordingly. If polling ends after a few minutes without receiving the status 'FINALIZED', it means the transaction cannot yet be ended as accepted or refused. Once the status changes to 'FINALIZED', you should verify the payment outcome and redirect the customer to your status page accordingly. Remember, a 'FINALIZED' status indicates that the CV Connect process has concluded, but it does not necessarily confirm a successful payment. If you end the polling after a few minutes without receiving the status 'FINALIZED', it means the transaction cannot yet be ended as accepted or refused. NB — If you try to call the polling endpoint with invalid data, you will receive an HTTP 204.

        Type: str
        """
        return self.__polling_url

    @polling_url.setter
    def polling_url(self, value: Optional[str]) -> None:
        self.__polling_url = value

    @property
    def qr_code(self) -> Optional[str]:
        """
        | Contains a base64 encoded PNG image. By prepending data:image/png;base64, this value can be used as the source of an HTML inline image on a desktop or tablet (intended to be scanned by a device with the Chèque-Vacances app)

        Type: str
        """
        return self.__qr_code

    @qr_code.setter
    def qr_code(self, value: Optional[str]) -> None:
        self.__qr_code = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct5412, self).to_dictionary()
        if self.app_url is not None:
            dictionary['appUrl'] = self.app_url
        if self.polling_url is not None:
            dictionary['pollingUrl'] = self.polling_url
        if self.qr_code is not None:
            dictionary['qrCode'] = self.qr_code
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct5412':
        super(PaymentProduct5412, self).from_dictionary(dictionary)
        if 'appUrl' in dictionary:
            self.app_url = dictionary['appUrl']
        if 'pollingUrl' in dictionary:
            self.polling_url = dictionary['pollingUrl']
        if 'qrCode' in dictionary:
            self.qr_code = dictionary['qrCode']
        return self
