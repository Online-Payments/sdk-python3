#
# This file was automatically generated.
#
from .data_object import DataObject
from .personal_name import PersonalName


class PersonalInformation(DataObject):

    __slots__ = (
        "__date_of_birth",
        "__gender",
        "__name",
    )

    __date_of_birth: str | None
    __gender: str | None
    __name: PersonalName | None

    def __init__(
        self,
        *,
        date_of_birth: str | None = None,
        gender: str | None = None,
        name: PersonalName | None = None,
    ) -> None:
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.name = name

    @property
    def date_of_birth(self) -> str | None:
        """
        | The date of birth of the customer of the recipient of the loan. Format YYYYMMDD

        Type: str
        """
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value: str | None) -> None:
        self.__date_of_birth = value

    @property
    def gender(self) -> str | None:
        """
        | The gender of the customer. All values are possible as long as it does not exceed the maximum length of 50 characters.

        Type: str
        """
        return self.__gender

    @gender.setter
    def gender(self, value: str | None) -> None:
        self.__gender = value

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

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.date_of_birth is not None:
            dictionary['dateOfBirth'] = self.date_of_birth
        if self.gender is not None:
            dictionary['gender'] = self.gender
        if self.name is not None:
            dictionary['name'] = self.name.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PersonalInformation':
        super().from_dictionary(dictionary)
        if 'dateOfBirth' in dictionary:
            self.date_of_birth = dictionary['dateOfBirth']
        if 'gender' in dictionary:
            self.gender = dictionary['gender']
        if 'name' in dictionary:
            if not isinstance(dictionary['name'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['name']))
            value = PersonalName()
            self.name = value.from_dictionary(dictionary['name'])
        return self
