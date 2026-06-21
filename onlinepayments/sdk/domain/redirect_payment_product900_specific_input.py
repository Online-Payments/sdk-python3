# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RedirectPaymentProduct900SpecificInput(DataObject):

    __capture_trigger: Optional[str] = None

    @property
    def capture_trigger(self) -> Optional[str]:
        """
        | Display your customers in the Wero portal when you will capture the transaction. Mandatory only for requests in authorisation mode. Possible values:
        
        * shipping - Upon shipping the order.
        * delivery - Upon delivering the order.
        * availability - As soon as the order is available.
        * serviceFulfilment - Upon fulfilling the service.
        * other - For any other use case.

        Type: str
        """
        return self.__capture_trigger

    @capture_trigger.setter
    def capture_trigger(self, value: Optional[str]) -> None:
        self.__capture_trigger = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct900SpecificInput, self).to_dictionary()
        if self.capture_trigger is not None:
            dictionary['captureTrigger'] = self.capture_trigger
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct900SpecificInput':
        super(RedirectPaymentProduct900SpecificInput, self).from_dictionary(dictionary)
        if 'captureTrigger' in dictionary:
            self.capture_trigger = dictionary['captureTrigger']
        return self
