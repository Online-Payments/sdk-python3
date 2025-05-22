# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject


class Feedbacks(DataObject):

    __webhook_url: Optional[str] = None
    __webhooks_urls: Optional[List[str]] = None

    @property
    def webhook_url(self) -> Optional[str]:
        """
        | The URL where the webhook will be dispatched for all status change events related to this payment.

        Type: str

        Deprecated; The URL where the webhook will be dispatched for all status change events related to this payment.
        """
        return self.__webhook_url

    @webhook_url.setter
    def webhook_url(self, value: Optional[str]) -> None:
        self.__webhook_url = value

    @property
    def webhooks_urls(self) -> Optional[List[str]]:
        """
        | The list of the URLs where the webhook will be dispatched for all status change events related to this payment.

        Type: list[str]
        """
        return self.__webhooks_urls

    @webhooks_urls.setter
    def webhooks_urls(self, value: Optional[List[str]]) -> None:
        self.__webhooks_urls = value

    def to_dictionary(self) -> dict:
        dictionary = super(Feedbacks, self).to_dictionary()
        if self.webhook_url is not None:
            dictionary['webhookUrl'] = self.webhook_url
        if self.webhooks_urls is not None:
            dictionary['webhooksUrls'] = []
            for element in self.webhooks_urls:
                if element is not None:
                    dictionary['webhooksUrls'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Feedbacks':
        super(Feedbacks, self).from_dictionary(dictionary)
        if 'webhookUrl' in dictionary:
            self.webhook_url = dictionary['webhookUrl']
        if 'webhooksUrls' in dictionary:
            if not isinstance(dictionary['webhooksUrls'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['webhooksUrls']))
            self.webhooks_urls = []
            for element in dictionary['webhooksUrls']:
                self.webhooks_urls.append(element)
        return self
