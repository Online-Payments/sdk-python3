#
# This file was automatically generated.
#
from .browser_data import BrowserData
from .data_object import DataObject


class CustomerDevice(DataObject):

    __slots__ = (
        "__accept_header",
        "__browser_data",
        "__device_fingerprint",
        "__ip_address",
        "__locale",
        "__timezone_offset_utc_minutes",
        "__user_agent",
    )

    __accept_header: str | None
    __browser_data: BrowserData | None
    __device_fingerprint: str | None
    __ip_address: str | None
    __locale: str | None
    __timezone_offset_utc_minutes: str | None
    __user_agent: str | None

    def __init__(
        self,
        *,
        accept_header: str | None = None,
        browser_data: BrowserData | None = None,
        device_fingerprint: str | None = None,
        ip_address: str | None = None,
        locale: str | None = None,
        timezone_offset_utc_minutes: str | None = None,
        user_agent: str | None = None,
    ) -> None:
        self.accept_header = accept_header
        self.browser_data = browser_data
        self.device_fingerprint = device_fingerprint
        self.ip_address = ip_address
        self.locale = locale
        self.timezone_offset_utc_minutes = timezone_offset_utc_minutes
        self.user_agent = user_agent

    @property
    def accept_header(self) -> str | None:
        """
        | The accept-header of the customer client from the HTTP Headers.

        Type: str
        """
        return self.__accept_header

    @accept_header.setter
    def accept_header(self, value: str | None) -> None:
        self.__accept_header = value

    @property
    def browser_data(self) -> BrowserData | None:
        """
        | Object containing information regarding the browser of the customer

        Type: :class:`onlinepayments.sdk.domain.browser_data.BrowserData`
        """
        return self.__browser_data

    @browser_data.setter
    def browser_data(self, value: BrowserData | None) -> None:
        self.__browser_data = value

    @property
    def device_fingerprint(self) -> str | None:
        """
        | The session ID for the device fingerprint must match the one sent in the device fingerprint script.

        Type: str
        """
        return self.__device_fingerprint

    @device_fingerprint.setter
    def device_fingerprint(self, value: str | None) -> None:
        self.__device_fingerprint = value

    @property
    def ip_address(self) -> str | None:
        """
        | The IP address of the customer client from the HTTP Headers.

        Type: str
        """
        return self.__ip_address

    @ip_address.setter
    def ip_address(self, value: str | None) -> None:
        self.__ip_address = value

    @property
    def locale(self) -> str | None:
        """
        | Locale of the client device/browser. Returned in the browser from the navigator.language property.
        |
        | If you use the latest version of our JavaScript Client SDK, we will collect this data and include it in the encryptedCustomerInput property. We will then automatically populate this data if available.

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: str | None) -> None:
        self.__locale = value

    @property
    def timezone_offset_utc_minutes(self) -> str | None:
        """
        | Offset in minutes of timezone of the client versus the UTC. Value is returned by the JavaScript getTimezoneOffset() Method.
        |
        | If you use the latest version of our JavaScript Client SDK, we will collect this data and include it in the encryptedCustomerInput property. We will then automatically populate this data if available.

        Type: str
        """
        return self.__timezone_offset_utc_minutes

    @timezone_offset_utc_minutes.setter
    def timezone_offset_utc_minutes(self, value: str | None) -> None:
        self.__timezone_offset_utc_minutes = value

    @property
    def user_agent(self) -> str | None:
        """
        | User-Agent of the client device/browser from the HTTP Headers.
        |
        | As a fall-back we will use the userAgent that might be included in the encryptedCustomerInput, but this is captured client side using JavaScript and might be different.

        Type: str
        """
        return self.__user_agent

    @user_agent.setter
    def user_agent(self, value: str | None) -> None:
        self.__user_agent = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
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
        super().from_dictionary(dictionary)
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
