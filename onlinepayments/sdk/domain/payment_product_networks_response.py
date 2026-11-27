#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProductNetworksResponse(DataObject):

    __slots__ = (
        "__networks",
    )

    __networks: list[str] | None

    def __init__(
        self,
        *,
        networks: list[str] | None = None,
    ) -> None:
        self.networks = networks

    @property
    def networks(self) -> list[str] | None:
        """
        | Array containing network entries for a payment product. The strings that represent the networks in the array are identical to the strings that the payment product vendors use in their documentation. For instance: "Visa" for Apple Pay, and "VISA" for Google Pay.

        Type: list[str]
        """
        return self.__networks

    @networks.setter
    def networks(self, value: list[str] | None) -> None:
        self.__networks = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.networks is not None:
            dictionary['networks'] = []
            for element in self.networks:
                if element is not None:
                    dictionary['networks'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductNetworksResponse':
        super().from_dictionary(dictionary)
        if 'networks' in dictionary:
            if not isinstance(dictionary['networks'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['networks']))
            self.networks = []
            for element in dictionary['networks']:
                self.networks.append(element)
        return self
