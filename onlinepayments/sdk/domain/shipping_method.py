#
# This file was automatically generated.
#
from .data_object import DataObject


class ShippingMethod(DataObject):

    __slots__ = (
        "__details",
        "__name",
        "__speed",
        "__type",
    )

    __details: str | None
    __name: str | None
    __speed: int | None
    __type: str | None

    def __init__(
        self,
        *,
        details: str | None = None,
        name: str | None = None,
        speed: int | None = None,
        type: str | None = None,
    ) -> None:
        self.details = details
        self.name = name
        self.speed = speed
        self.type = type

    @property
    def details(self) -> str | None:
        """
        | Details about the shipping method

        Type: str
        """
        return self.__details

    @details.setter
    def details(self, value: str | None) -> None:
        self.__details = value

    @property
    def name(self) -> str | None:
        """
        | Name of the shipping method

        Type: str
        """
        return self.__name

    @name.setter
    def name(self, value: str | None) -> None:
        self.__name = value

    @property
    def speed(self) -> int | None:
        """
        | Number of hours to delivery

        Type: int
        """
        return self.__speed

    @speed.setter
    def speed(self, value: int | None) -> None:
        self.__speed = value

    @property
    def type(self) -> str | None:
        """
        | Shipping method type

        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: str | None) -> None:
        self.__type = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.details is not None:
            dictionary['details'] = self.details
        if self.name is not None:
            dictionary['name'] = self.name
        if self.speed is not None:
            dictionary['speed'] = self.speed
        if self.type is not None:
            dictionary['type'] = self.type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ShippingMethod':
        super().from_dictionary(dictionary)
        if 'details' in dictionary:
            self.details = dictionary['details']
        if 'name' in dictionary:
            self.name = dictionary['name']
        if 'speed' in dictionary:
            self.speed = dictionary['speed']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self
