#
# This file was automatically generated.
#
from .data_object import DataObject


class MandatePersonalNameResponse(DataObject):

    __slots__ = (
        "__first_name",
        "__surname",
    )

    __first_name: str | None
    __surname: str | None

    def __init__(
        self,
        *,
        first_name: str | None = None,
        surname: str | None = None,
    ) -> None:
        self.first_name = first_name
        self.surname = surname

    @property
    def first_name(self) -> str | None:
        """
        | Given name(s) or first name(s) of the customer.

        Type: str
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str | None) -> None:
        self.__first_name = value

    @property
    def surname(self) -> str | None:
        """
        | Surname(s) or last name(s) of the customer.

        Type: str
        """
        return self.__surname

    @surname.setter
    def surname(self, value: str | None) -> None:
        self.__surname = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.first_name is not None:
            dictionary['firstName'] = self.first_name
        if self.surname is not None:
            dictionary['surname'] = self.surname
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MandatePersonalNameResponse':
        super().from_dictionary(dictionary)
        if 'firstName' in dictionary:
            self.first_name = dictionary['firstName']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        return self
