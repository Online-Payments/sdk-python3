#
# This file was automatically generated.
#
from .data_object import DataObject


class MandateRedirectData(DataObject):

    __slots__ = (
        "__returnmac",
        "__redirect_url",
    )

    __returnmac: str | None
    __redirect_url: str | None

    def __init__(
        self,
        *,
        returnmac: str | None = None,
        redirect_url: str | None = None,
    ) -> None:
        self.returnmac = returnmac
        self.redirect_url = redirect_url

    @property
    def returnmac(self) -> str | None:
        """
        | A Message Authentication Code (MAC) is used to authenticate the redirection back to merchant after the payment.

        Type: str
        """
        return self.__returnmac

    @returnmac.setter
    def returnmac(self, value: str | None) -> None:
        self.__returnmac = value

    @property
    def redirect_url(self) -> str | None:
        """
        | The URL that the customer should be redirected to. Be sure to redirect using the GET method.

        Type: str
        """
        return self.__redirect_url

    @redirect_url.setter
    def redirect_url(self, value: str | None) -> None:
        self.__redirect_url = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.returnmac is not None:
            dictionary['RETURNMAC'] = self.returnmac
        if self.redirect_url is not None:
            dictionary['redirectURL'] = self.redirect_url
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MandateRedirectData':
        super().from_dictionary(dictionary)
        if 'RETURNMAC' in dictionary:
            self.returnmac = dictionary['RETURNMAC']
        if 'redirectURL' in dictionary:
            self.redirect_url = dictionary['redirectURL']
        return self
