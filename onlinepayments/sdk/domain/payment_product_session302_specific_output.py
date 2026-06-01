# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProductSession302SpecificOutput(DataObject):

    __session: Optional[str] = None

    @property
    def session(self) -> Optional[str]:
        """
        | The payment session object that must be passed to the Apple Pay API on the client side to initialize the Apple Pay payment sheet.

        Type: str
        """
        return self.__session

    @session.setter
    def session(self, value: Optional[str]) -> None:
        self.__session = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProductSession302SpecificOutput, self).to_dictionary()
        if self.session is not None:
            dictionary['session'] = self.session
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductSession302SpecificOutput':
        super(PaymentProductSession302SpecificOutput, self).from_dictionary(dictionary)
        if 'session' in dictionary:
            self.session = dictionary['session']
        return self
