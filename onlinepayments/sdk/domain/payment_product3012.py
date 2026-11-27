#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProduct3012(DataObject):

    __slots__ = (
        "__qr_code",
        "__url_intent",
    )

    __qr_code: str | None
    __url_intent: str | None

    def __init__(
        self,
        *,
        qr_code: str | None = None,
        url_intent: str | None = None,
    ) -> None:
        self.qr_code = qr_code
        self.url_intent = url_intent

    @property
    def qr_code(self) -> str | None:
        """
        | Contains a value which can be used to build a QR code (intended to be scanned by a device with the Bancontact app)

        Type: str
        """
        return self.__qr_code

    @qr_code.setter
    def qr_code(self, value: str | None) -> None:
        self.__qr_code = value

    @property
    def url_intent(self) -> str | None:
        """
        | Contains URL intent that can be used as the link of an "open the app" button on a device

        Type: str
        """
        return self.__url_intent

    @url_intent.setter
    def url_intent(self, value: str | None) -> None:
        self.__url_intent = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.qr_code is not None:
            dictionary['qrCode'] = self.qr_code
        if self.url_intent is not None:
            dictionary['urlIntent'] = self.url_intent
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct3012':
        super().from_dictionary(dictionary)
        if 'qrCode' in dictionary:
            self.qr_code = dictionary['qrCode']
        if 'urlIntent' in dictionary:
            self.url_intent = dictionary['urlIntent']
        return self
