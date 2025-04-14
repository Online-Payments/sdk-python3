# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RedirectionData(DataObject):

    __return_url: Optional[str] = None

    @property
    def return_url(self) -> Optional[str]:
        """
        | The URL that the customer is redirected to after the payment flow has finished. You can add any number of key value pairs in the query string that, for instance help you to identify the customer when they return to your site. Please note that we will also append some additional key value pairs that will also help you with this identification process. Note: The provided URL should be absolute and contain the protocol to use, e.g. http:// or https://. For use on mobile devices a custom protocol can be used in the form of protocol://. This protocol must be registered on the device first. URLs without a protocol will be rejected.

        Type: str
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value: Optional[str]) -> None:
        self.__return_url = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectionData, self).to_dictionary()
        if self.return_url is not None:
            dictionary['returnUrl'] = self.return_url
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectionData':
        super(RedirectionData, self).from_dictionary(dictionary)
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        return self
