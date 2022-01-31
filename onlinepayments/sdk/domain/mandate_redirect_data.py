# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class MandateRedirectData(DataObject):
    """
    | Object containing all data needed to redirect the customer
    """

    __returnmac = None
    __redirect_url = None

    @property
    def returnmac(self) -> str:
        """
        | A Message Authentication Code (MAC) is used to authenticate the redirection back to merchant after the payment.

        Type: str
        """
        return self.__returnmac

    @returnmac.setter
    def returnmac(self, value: str):
        self.__returnmac = value

    @property
    def redirect_url(self) -> str:
        """
        | The URL that the customer should be redirected to. Be sure to redirect using the GET method.

        Type: str
        """
        return self.__redirect_url

    @redirect_url.setter
    def redirect_url(self, value: str):
        self.__redirect_url = value

    def to_dictionary(self):
        dictionary = super(MandateRedirectData, self).to_dictionary()
        if self.returnmac is not None:
            dictionary['RETURNMAC'] = self.returnmac
        if self.redirect_url is not None:
            dictionary['redirectURL'] = self.redirect_url
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateRedirectData, self).from_dictionary(dictionary)
        if 'RETURNMAC' in dictionary:
            self.returnmac = dictionary['RETURNMAC']
        if 'redirectURL' in dictionary:
            self.redirect_url = dictionary['redirectURL']
        return self
