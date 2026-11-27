#
# This file was automatically generated.
#
from .data_object import DataObject
from .personal_name import PersonalName


class AddressPersonal(DataObject):

    __slots__ = (
        "__additional_info",
        "__city",
        "__company_name",
        "__country_code",
        "__house_number",
        "__name",
        "__state",
        "__street",
        "__zip",
    )

    __additional_info: str | None
    __city: str | None
    __company_name: str | None
    __country_code: str | None
    __house_number: str | None
    __name: PersonalName | None
    __state: str | None
    __street: str | None
    __zip: str | None

    def __init__(
        self,
        *,
        additional_info: str | None = None,
        city: str | None = None,
        company_name: str | None = None,
        country_code: str | None = None,
        house_number: str | None = None,
        name: PersonalName | None = None,
        state: str | None = None,
        street: str | None = None,
        zip: str | None = None,
    ) -> None:
        self.additional_info = additional_info
        self.city = city
        self.company_name = company_name
        self.country_code = country_code
        self.house_number = house_number
        self.name = name
        self.state = state
        self.street = street
        self.zip = zip

    @property
    def additional_info(self) -> str | None:
        """
        | Second line of street or additional address information

        Type: str
        """
        return self.__additional_info

    @additional_info.setter
    def additional_info(self, value: str | None) -> None:
        self.__additional_info = value

    @property
    def city(self) -> str | None:
        """
        | City

        Type: str
        """
        return self.__city

    @city.setter
    def city(self, value: str | None) -> None:
        self.__city = value

    @property
    def company_name(self) -> str | None:
        """
        | Company Name

        Type: str
        """
        return self.__company_name

    @company_name.setter
    def company_name(self, value: str | None) -> None:
        self.__company_name = value

    @property
    def country_code(self) -> str | None:
        """
        | ISO 3166-1 alpha-2 country code

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: str | None) -> None:
        self.__country_code = value

    @property
    def house_number(self) -> str | None:
        """
        | House number

        Type: str
        """
        return self.__house_number

    @house_number.setter
    def house_number(self, value: str | None) -> None:
        self.__house_number = value

    @property
    def name(self) -> PersonalName | None:
        """
        | Object containing the name details of the customer

        Type: :class:`onlinepayments.sdk.domain.personal_name.PersonalName`
        """
        return self.__name

    @name.setter
    def name(self, value: PersonalName | None) -> None:
        self.__name = value

    @property
    def state(self) -> str | None:
        """
        | ISO 3166-2 country subdivision code

        Type: str
        """
        return self.__state

    @state.setter
    def state(self, value: str | None) -> None:
        self.__state = value

    @property
    def street(self) -> str | None:
        """
        | Street name

        Type: str
        """
        return self.__street

    @street.setter
    def street(self, value: str | None) -> None:
        self.__street = value

    @property
    def zip(self) -> str | None:
        """
        | Zip code

        Type: str
        """
        return self.__zip

    @zip.setter
    def zip(self, value: str | None) -> None:
        self.__zip = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.additional_info is not None:
            dictionary['additionalInfo'] = self.additional_info
        if self.city is not None:
            dictionary['city'] = self.city
        if self.company_name is not None:
            dictionary['companyName'] = self.company_name
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.house_number is not None:
            dictionary['houseNumber'] = self.house_number
        if self.name is not None:
            dictionary['name'] = self.name.to_dictionary()
        if self.state is not None:
            dictionary['state'] = self.state
        if self.street is not None:
            dictionary['street'] = self.street
        if self.zip is not None:
            dictionary['zip'] = self.zip
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AddressPersonal':
        super().from_dictionary(dictionary)
        if 'additionalInfo' in dictionary:
            self.additional_info = dictionary['additionalInfo']
        if 'city' in dictionary:
            self.city = dictionary['city']
        if 'companyName' in dictionary:
            self.company_name = dictionary['companyName']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'houseNumber' in dictionary:
            self.house_number = dictionary['houseNumber']
        if 'name' in dictionary:
            if not isinstance(dictionary['name'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['name']))
            value = PersonalName()
            self.name = value.from_dictionary(dictionary['name'])
        if 'state' in dictionary:
            self.state = dictionary['state']
        if 'street' in dictionary:
            self.street = dictionary['street']
        if 'zip' in dictionary:
            self.zip = dictionary['zip']
        return self
