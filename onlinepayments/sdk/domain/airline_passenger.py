#
# This file was automatically generated.
#
from .data_object import DataObject


class AirlinePassenger(DataObject):

    __slots__ = (
        "__airline_loyalty_status",
        "__country_code",
        "__date_of_birth",
        "__first_name",
        "__passenger_type",
        "__surname",
        "__surname_prefix",
        "__title",
    )

    __airline_loyalty_status: str | None
    __country_code: str | None
    __date_of_birth: str | None
    __first_name: str | None
    __passenger_type: str | None
    __surname: str | None
    __surname_prefix: str | None
    __title: str | None

    def __init__(
        self,
        *,
        airline_loyalty_status: str | None = None,
        country_code: str | None = None,
        date_of_birth: str | None = None,
        first_name: str | None = None,
        passenger_type: str | None = None,
        surname: str | None = None,
        surname_prefix: str | None = None,
        title: str | None = None,
    ) -> None:
        self.airline_loyalty_status = airline_loyalty_status
        self.country_code = country_code
        self.date_of_birth = date_of_birth
        self.first_name = first_name
        self.passenger_type = passenger_type
        self.surname = surname
        self.surname_prefix = surname_prefix
        self.title = title

    @property
    def airline_loyalty_status(self) -> str | None:
        """
        | Airline loyalty program level for the passenger on the itinerary.

        Type: str
        """
        return self.__airline_loyalty_status

    @airline_loyalty_status.setter
    def airline_loyalty_status(self, value: str | None) -> None:
        self.__airline_loyalty_status = value

    @property
    def country_code(self) -> str | None:
        """
        | Passenger's residence country defined in ISO 3166-1 alpha-2.

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: str | None) -> None:
        self.__country_code = value

    @property
    def date_of_birth(self) -> str | None:
        """
        | The date of birth of the passenger. Format YYYYMMDD

        Type: str
        """
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value: str | None) -> None:
        self.__date_of_birth = value

    @property
    def first_name(self) -> str | None:
        """
        | First name of the passenger This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str | None) -> None:
        self.__first_name = value

    @property
    def passenger_type(self) -> str | None:
        """
        | Type of passenger on the itinerary.

        Type: str
        """
        return self.__passenger_type

    @passenger_type.setter
    def passenger_type(self, value: str | None) -> None:
        self.__passenger_type = value

    @property
    def surname(self) -> str | None:
        """
        | Surname of the passenger This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__surname

    @surname.setter
    def surname(self, value: str | None) -> None:
        self.__surname = value

    @property
    def surname_prefix(self) -> str | None:
        """
        | Surname prefix or middle name of the passenger This field is used by the following payment products: 840

        Type: str
        """
        return self.__surname_prefix

    @surname_prefix.setter
    def surname_prefix(self, value: str | None) -> None:
        self.__surname_prefix = value

    @property
    def title(self) -> str | None:
        """
        | Deprecated: This field is not used by any payment product Title of the passenger (this property is used for fraud screening on the payment platform)

        Type: str

        Deprecated; This field is not used by any payment product Title of the passenger (this property is used for fraud screening on the payment platform)
        """
        return self.__title

    @title.setter
    def title(self, value: str | None) -> None:
        self.__title = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.airline_loyalty_status is not None:
            dictionary['airlineLoyaltyStatus'] = self.airline_loyalty_status
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.date_of_birth is not None:
            dictionary['dateOfBirth'] = self.date_of_birth
        if self.first_name is not None:
            dictionary['firstName'] = self.first_name
        if self.passenger_type is not None:
            dictionary['passengerType'] = self.passenger_type
        if self.surname is not None:
            dictionary['surname'] = self.surname
        if self.surname_prefix is not None:
            dictionary['surnamePrefix'] = self.surname_prefix
        if self.title is not None:
            dictionary['title'] = self.title
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AirlinePassenger':
        super().from_dictionary(dictionary)
        if 'airlineLoyaltyStatus' in dictionary:
            self.airline_loyalty_status = dictionary['airlineLoyaltyStatus']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'dateOfBirth' in dictionary:
            self.date_of_birth = dictionary['dateOfBirth']
        if 'firstName' in dictionary:
            self.first_name = dictionary['firstName']
        if 'passengerType' in dictionary:
            self.passenger_type = dictionary['passengerType']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        if 'surnamePrefix' in dictionary:
            self.surname_prefix = dictionary['surnamePrefix']
        if 'title' in dictionary:
            self.title = dictionary['title']
        return self
