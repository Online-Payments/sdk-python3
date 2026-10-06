# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class SharePaymentLinkRequest(DataObject):

    __channel: Optional[str] = None
    __locale: Optional[str] = None
    __recipient: Optional[str] = None

    @property
    def channel(self) -> Optional[str]:
        """
        | Specifies the communication channel for sharing the payment link.

        Type: str
        """
        return self.__channel

    @channel.setter
    def channel(self, value: Optional[str]) -> None:
        self.__channel = value

    @property
    def locale(self) -> Optional[str]:
        """
        | The locale code in language-country format following ISO 639-1 and ISO 3166-1 standards (e.g., fr-BE, en-US, de-DE).

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: Optional[str]) -> None:
        self.__locale = value

    @property
    def recipient(self) -> Optional[str]:
        """
        | The email address of the recipient.

        Type: str
        """
        return self.__recipient

    @recipient.setter
    def recipient(self, value: Optional[str]) -> None:
        self.__recipient = value

    def to_dictionary(self) -> dict:
        dictionary = super(SharePaymentLinkRequest, self).to_dictionary()
        if self.channel is not None:
            dictionary['channel'] = self.channel
        if self.locale is not None:
            dictionary['locale'] = self.locale
        if self.recipient is not None:
            dictionary['recipient'] = self.recipient
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SharePaymentLinkRequest':
        super(SharePaymentLinkRequest, self).from_dictionary(dictionary)
        if 'channel' in dictionary:
            self.channel = dictionary['channel']
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'recipient' in dictionary:
            self.recipient = dictionary['recipient']
        return self
