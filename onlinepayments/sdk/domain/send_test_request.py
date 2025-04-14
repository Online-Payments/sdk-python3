# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class SendTestRequest(DataObject):

    __url: Optional[str] = None

    @property
    def url(self) -> Optional[str]:
        """
        | Url to which the dummy webhook would be sent. If the parameter is not sent, It will be sent as default to the webhook url configured in the backoffice.

        Type: str
        """
        return self.__url

    @url.setter
    def url(self, value: Optional[str]) -> None:
        self.__url = value

    def to_dictionary(self) -> dict:
        dictionary = super(SendTestRequest, self).to_dictionary()
        if self.url is not None:
            dictionary['url'] = self.url
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SendTestRequest':
        super(SendTestRequest, self).from_dictionary(dictionary)
        if 'url' in dictionary:
            self.url = dictionary['url']
        return self
