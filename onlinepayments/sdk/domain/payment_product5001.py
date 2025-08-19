# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct5001(DataObject):

    __message: Optional[str] = None
    __polling_url: Optional[str] = None

    @property
    def message(self) -> Optional[str]:
        """
        | A text string intended to be displayed to the consumer

        Type: str
        """
        return self.__message

    @message.setter
    def message(self, value: Optional[str]) -> None:
        self.__message = value

    @property
    def polling_url(self) -> Optional[str]:
        """
        | A URL that must be polled using JavaScript; it responds with either true or false to say if transaction is still pending or not. As long as the response status is 'true', the message should be shown and polling should continue. Once the status changes to 'false', you should verify the payment outcome and redirect the customer to your status page accordingly. Remember, a pending status 'false' indicates that the Bizum process has concluded, but it does not necessarily confirm a successful payment. And if you end the polling after a few minutes without receiving the status 'false', it means that the transaction can't be ended as accepted or refused yet. NB - If you try to call the polling endpoint with invalid data, you will receive an http 204.

        Type: str
        """
        return self.__polling_url

    @polling_url.setter
    def polling_url(self, value: Optional[str]) -> None:
        self.__polling_url = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct5001, self).to_dictionary()
        if self.message is not None:
            dictionary['message'] = self.message
        if self.polling_url is not None:
            dictionary['pollingUrl'] = self.polling_url
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct5001':
        super(PaymentProduct5001, self).from_dictionary(dictionary)
        if 'message' in dictionary:
            self.message = dictionary['message']
        if 'pollingUrl' in dictionary:
            self.polling_url = dictionary['pollingUrl']
        return self
