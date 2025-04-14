# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RedirectData(DataObject):

    __returnmac: Optional[str] = None
    __redirect_url: Optional[str] = None

    @property
    def returnmac(self) -> Optional[str]:
        """
        | A Message Authentication Code (MAC) is used to authenticate the redirection back to merchant after the payment

        Type: str
        """
        return self.__returnmac

    @returnmac.setter
    def returnmac(self, value: Optional[str]) -> None:
        self.__returnmac = value

    @property
    def redirect_url(self) -> Optional[str]:
        """
        | The URL that the customer should be redirected to. Be sure to redirect using the GET method

        Type: str
        """
        return self.__redirect_url

    @redirect_url.setter
    def redirect_url(self, value: Optional[str]) -> None:
        self.__redirect_url = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectData, self).to_dictionary()
        if self.returnmac is not None:
            dictionary['RETURNMAC'] = self.returnmac
        if self.redirect_url is not None:
            dictionary['redirectURL'] = self.redirect_url
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectData':
        super(RedirectData, self).from_dictionary(dictionary)
        if 'RETURNMAC' in dictionary:
            self.returnmac = dictionary['RETURNMAC']
        if 'redirectURL' in dictionary:
            self.redirect_url = dictionary['redirectURL']
        return self
