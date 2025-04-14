# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .mandate_redirect_data import MandateRedirectData


class MandateMerchantAction(DataObject):

    __action_type: Optional[str] = None
    __redirect_data: Optional[MandateRedirectData] = None

    @property
    def action_type(self) -> Optional[str]:
        """
        | Action merchants needs to take in the online mandate process. Possible values are:
        
        * REDIRECT - The customer needs to be redirected using the details found in redirectData

        Type: str
        """
        return self.__action_type

    @action_type.setter
    def action_type(self, value: Optional[str]) -> None:
        self.__action_type = value

    @property
    def redirect_data(self) -> Optional[MandateRedirectData]:
        """
        | Object containing all data needed to redirect the customer

        Type: :class:`onlinepayments.sdk.domain.mandate_redirect_data.MandateRedirectData`
        """
        return self.__redirect_data

    @redirect_data.setter
    def redirect_data(self, value: Optional[MandateRedirectData]) -> None:
        self.__redirect_data = value

    def to_dictionary(self) -> dict:
        dictionary = super(MandateMerchantAction, self).to_dictionary()
        if self.action_type is not None:
            dictionary['actionType'] = self.action_type
        if self.redirect_data is not None:
            dictionary['redirectData'] = self.redirect_data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MandateMerchantAction':
        super(MandateMerchantAction, self).from_dictionary(dictionary)
        if 'actionType' in dictionary:
            self.action_type = dictionary['actionType']
        if 'redirectData' in dictionary:
            if not isinstance(dictionary['redirectData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectData']))
            value = MandateRedirectData()
            self.redirect_data = value.from_dictionary(dictionary['redirectData'])
        return self
