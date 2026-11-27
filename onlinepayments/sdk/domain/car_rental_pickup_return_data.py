#
# This file was automatically generated.
#
from .data_object import DataObject


class CarRentalPickupReturnData(DataObject):

    __slots__ = (
        "__address",
        "__city",
        "__country",
        "__date",
        "__location",
        "__postcode",
        "__state",
    )

    __address: str | None
    __city: str | None
    __country: int | None
    __date: str | None
    __location: str | None
    __postcode: str | None
    __state: str | None

    def __init__(
        self,
        *,
        address: str | None = None,
        city: str | None = None,
        country: int | None = None,
        date: str | None = None,
        location: str | None = None,
        postcode: str | None = None,
        state: str | None = None,
    ) -> None:
        self.address = address
        self.city = city
        self.country = country
        self.date = date
        self.location = location
        self.postcode = postcode
        self.state = state

    @property
    def address(self) -> str | None:
        """
        | Address of the pickup/return location

        Type: str
        """
        return self.__address

    @address.setter
    def address(self, value: str | None) -> None:
        self.__address = value

    @property
    def city(self) -> str | None:
        """
        | City of the pickup/return location

        Type: str
        """
        return self.__city

    @city.setter
    def city(self, value: str | None) -> None:
        self.__city = value

    @property
    def country(self) -> int | None:
        """
        | Country of the pickup/return location ISO 3166-1 numeric

        Type: int
        """
        return self.__country

    @country.setter
    def country(self, value: int | None) -> None:
        self.__country = value

    @property
    def date(self) -> str | None:
        """
        | UTC Time at which the vehicle was rented/picked up or returned.

        Type: str
        """
        return self.__date

    @date.setter
    def date(self, value: str | None) -> None:
        self.__date = value

    @property
    def location(self) -> str | None:
        """
        | This field contains data that uniquely identifies the location where the car was picked up or returned (e.g., DBA name, hotel, airport, etc.).

        Type: str
        """
        return self.__location

    @location.setter
    def location(self, value: str | None) -> None:
        self.__location = value

    @property
    def postcode(self) -> str | None:
        """
        | Postal code of the pickup/return location

        Type: str
        """
        return self.__postcode

    @postcode.setter
    def postcode(self, value: str | None) -> None:
        self.__postcode = value

    @property
    def state(self) -> str | None:
        """
        | State/region of the pickup/return location

        Type: str
        """
        return self.__state

    @state.setter
    def state(self, value: str | None) -> None:
        self.__state = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.address is not None:
            dictionary['address'] = self.address
        if self.city is not None:
            dictionary['city'] = self.city
        if self.country is not None:
            dictionary['country'] = self.country
        if self.date is not None:
            dictionary['date'] = self.date
        if self.location is not None:
            dictionary['location'] = self.location
        if self.postcode is not None:
            dictionary['postcode'] = self.postcode
        if self.state is not None:
            dictionary['state'] = self.state
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CarRentalPickupReturnData':
        super().from_dictionary(dictionary)
        if 'address' in dictionary:
            self.address = dictionary['address']
        if 'city' in dictionary:
            self.city = dictionary['city']
        if 'country' in dictionary:
            self.country = dictionary['country']
        if 'date' in dictionary:
            self.date = dictionary['date']
        if 'location' in dictionary:
            self.location = dictionary['location']
        if 'postcode' in dictionary:
            self.postcode = dictionary['postcode']
        if 'state' in dictionary:
            self.state = dictionary['state']
        return self
