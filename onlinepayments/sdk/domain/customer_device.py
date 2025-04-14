# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .browser_data import BrowserData
from .data_object import DataObject


class CustomerDevice(DataObject):

    __accept_header: Optional[str] = None
    __browser_data: Optional[BrowserData] = None
    __device_fingerprint: Optional[str] = None
    __ip_address: Optional[str] = None
    __locale: Optional[str] = None
    __timezone_offset_utc_minutes: Optional[str] = None
    __user_agent: Optional[str] = None

    @property
    def accept_header(self) -> Optional[str]:
        """
        | The accept-header of the customer client from the HTTP Headers.

        Type: str
        """
        return self.__accept_header

    @accept_header.setter
    def accept_header(self, value: Optional[str]) -> None:
        self.__accept_header = value

    @property
    def browser_data(self) -> Optional[BrowserData]:
        """
        | Object containing information regarding the browser of the customer

        Type: :class:`onlinepayments.sdk.domain.browser_data.BrowserData`
        """
        return self.__browser_data

    @browser_data.setter
    def browser_data(self, value: Optional[BrowserData]) -> None:
        self.__browser_data = value

    @property
    def device_fingerprint(self) -> Optional[str]:
        """
        | The session ID for the device fingerprint must match the one sent in the device fingerprint script.

        Type: str
        """
        return self.__device_fingerprint

    @device_fingerprint.setter
    def device_fingerprint(self, value: Optional[str]) -> None:
        self.__device_fingerprint = value

    @property
    def ip_address(self) -> Optional[str]:
        """
        | The IP address of the customer client from the HTTP Headers.

        Type: str
        """
        return self.__ip_address

    @ip_address.setter
    def ip_address(self, value: Optional[str]) -> None:
        self.__ip_address = value

    @property
    def locale(self) -> Optional[str]:
        """
        | Locale of the client device/browser. Returned in the browser from the navigator.language property.
        |
        | If you use the latest version of our JavaScript Client SDK, we will collect this data and include it in the encryptedCustomerInput property. We will then automatically populate this data if available.

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: Optional[str]) -> None:
        self.__locale = value

    @property
    def timezone_offset_utc_minutes(self) -> Optional[str]:
        """
        | Offset in minutes of timezone of the client versus the UTC. Value is returned by the JavaScript getTimezoneOffset() Method.
        |
        | If you use the latest version of our JavaScript Client SDK, we will collect this data and include it in the encryptedCustomerInput property. We will then automatically populate this data if available.

        Type: str
        """
        return self.__timezone_offset_utc_minutes

    @timezone_offset_utc_minutes.setter
    def timezone_offset_utc_minutes(self, value: Optional[str]) -> None:
        self.__timezone_offset_utc_minutes = value

    @property
    def user_agent(self) -> Optional[str]:
        """
        | User-Agent of the client device/browser from the HTTP Headers.
        |
        | As a fall-back we will use the userAgent that might be included in the encryptedCustomerInput, but this is captured client side using JavaScript and might be different.

        Type: str
        """
        return self.__user_agent

    @user_agent.setter
    def user_agent(self, value: Optional[str]) -> None:
        self.__user_agent = value

    def to_dictionary(self) -> dict:
        dictionary = super(CustomerDevice, self).to_dictionary()
        if self.accept_header is not None:
            dictionary['acceptHeader'] = self.accept_header
        if self.browser_data is not None:
            dictionary['browserData'] = self.browser_data.to_dictionary()
        if self.device_fingerprint is not None:
            dictionary['deviceFingerprint'] = self.device_fingerprint
        if self.ip_address is not None:
            dictionary['ipAddress'] = self.ip_address
        if self.locale is not None:
            dictionary['locale'] = self.locale
        if self.timezone_offset_utc_minutes is not None:
            dictionary['timezoneOffsetUtcMinutes'] = self.timezone_offset_utc_minutes
        if self.user_agent is not None:
            dictionary['userAgent'] = self.user_agent
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CustomerDevice':
        super(CustomerDevice, self).from_dictionary(dictionary)
        if 'acceptHeader' in dictionary:
            self.accept_header = dictionary['acceptHeader']
        if 'browserData' in dictionary:
            if not isinstance(dictionary['browserData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['browserData']))
            value = BrowserData()
            self.browser_data = value.from_dictionary(dictionary['browserData'])
        if 'deviceFingerprint' in dictionary:
            self.device_fingerprint = dictionary['deviceFingerprint']
        if 'ipAddress' in dictionary:
            self.ip_address = dictionary['ipAddress']
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'timezoneOffsetUtcMinutes' in dictionary:
            self.timezone_offset_utc_minutes = dictionary['timezoneOffsetUtcMinutes']
        if 'userAgent' in dictionary:
            self.user_agent = dictionary['userAgent']
        return self
