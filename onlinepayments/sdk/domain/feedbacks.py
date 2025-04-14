# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class Feedbacks(DataObject):

    __webhook_url: Optional[str] = None

    @property
    def webhook_url(self) -> Optional[str]:
        """
        | The URL where the webhook will be dispatched for all status change events related to this payment.

        Type: str
        """
        return self.__webhook_url

    @webhook_url.setter
    def webhook_url(self, value: Optional[str]) -> None:
        self.__webhook_url = value

    def to_dictionary(self) -> dict:
        dictionary = super(Feedbacks, self).to_dictionary()
        if self.webhook_url is not None:
            dictionary['webhookUrl'] = self.webhook_url
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Feedbacks':
        super(Feedbacks, self).from_dictionary(dictionary)
        if 'webhookUrl' in dictionary:
            self.webhook_url = dictionary['webhookUrl']
        return self
