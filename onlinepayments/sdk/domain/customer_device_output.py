#
# This file was automatically generated.
#
from .data_object import DataObject


class CustomerDeviceOutput(DataObject):

    __slots__ = (
        "__ip_address_country_code",
    )

    __ip_address_country_code: str | None

    def __init__(
        self,
        *,
        ip_address_country_code: str | None = None,
    ) -> None:
        self.ip_address_country_code = ip_address_country_code

    @property
    def ip_address_country_code(self) -> str | None:
        """
        | ISO 3166-1 alpha-2 country code

        Type: str
        """
        return self.__ip_address_country_code

    @ip_address_country_code.setter
    def ip_address_country_code(self, value: str | None) -> None:
        self.__ip_address_country_code = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.ip_address_country_code is not None:
            dictionary['ipAddressCountryCode'] = self.ip_address_country_code
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CustomerDeviceOutput':
        super().from_dictionary(dictionary)
        if 'ipAddressCountryCode' in dictionary:
            self.ip_address_country_code = dictionary['ipAddressCountryCode']
        return self
