# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CurrencyConversionInput(DataObject):

    __accepted_by_user: Optional[bool] = None
    __dcc_session_id: Optional[str] = None

    @property
    def accepted_by_user(self) -> Optional[bool]:
        """
        | Dynamic Currency Conversion(DCC) Proposal accepted by user

        Type: bool
        """
        return self.__accepted_by_user

    @accepted_by_user.setter
    def accepted_by_user(self, value: Optional[bool]) -> None:
        self.__accepted_by_user = value

    @property
    def dcc_session_id(self) -> Optional[str]:
        """
        | Dynamic Currency Conversion(DCC) Session Id that was previously returned by rate enquiry (/dccrate).

        Type: str
        """
        return self.__dcc_session_id

    @dcc_session_id.setter
    def dcc_session_id(self, value: Optional[str]) -> None:
        self.__dcc_session_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(CurrencyConversionInput, self).to_dictionary()
        if self.accepted_by_user is not None:
            dictionary['acceptedByUser'] = self.accepted_by_user
        if self.dcc_session_id is not None:
            dictionary['dccSessionId'] = self.dcc_session_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CurrencyConversionInput':
        super(CurrencyConversionInput, self).from_dictionary(dictionary)
        if 'acceptedByUser' in dictionary:
            self.accepted_by_user = dictionary['acceptedByUser']
        if 'dccSessionId' in dictionary:
            self.dcc_session_id = dictionary['dccSessionId']
        return self
