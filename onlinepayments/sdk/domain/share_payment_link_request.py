#
# This file was automatically generated.
#
from .data_object import DataObject


class SharePaymentLinkRequest(DataObject):

    __slots__ = (
        "__channel",
        "__locale",
        "__recipient",
    )

    __channel: str | None
    __locale: str | None
    __recipient: str | None

    def __init__(
        self,
        *,
        channel: str | None = None,
        locale: str | None = None,
        recipient: str | None = None,
    ) -> None:
        self.channel = channel
        self.locale = locale
        self.recipient = recipient

    @property
    def channel(self) -> str | None:
        """
        | Specifies the communication channel for sharing the payment link.

        Type: str
        """
        return self.__channel

    @channel.setter
    def channel(self, value: str | None) -> None:
        self.__channel = value

    @property
    def locale(self) -> str | None:
        """
        | The locale code in language-country format following ISO 639-1 and ISO 3166-1 standards (e.g., fr-BE, en-US, de-DE).

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: str | None) -> None:
        self.__locale = value

    @property
    def recipient(self) -> str | None:
        """
        | The email address of the recipient.

        Type: str
        """
        return self.__recipient

    @recipient.setter
    def recipient(self, value: str | None) -> None:
        self.__recipient = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.channel is not None:
            dictionary['channel'] = self.channel
        if self.locale is not None:
            dictionary['locale'] = self.locale
        if self.recipient is not None:
            dictionary['recipient'] = self.recipient
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SharePaymentLinkRequest':
        super().from_dictionary(dictionary)
        if 'channel' in dictionary:
            self.channel = dictionary['channel']
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'recipient' in dictionary:
            self.recipient = dictionary['recipient']
        return self
