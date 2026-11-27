#
# This file was automatically generated.
#
from .data_object import DataObject


class PersonalName(DataObject):

    __slots__ = (
        "__first_name",
        "__surname",
        "__title",
    )

    __first_name: str | None
    __surname: str | None
    __title: str | None

    def __init__(
        self,
        *,
        first_name: str | None = None,
        surname: str | None = None,
        title: str | None = None,
    ) -> None:
        self.first_name = first_name
        self.surname = surname
        self.title = title

    @property
    def first_name(self) -> str | None:
        """
        | Given name(s) or first name(s) of the customer

        Type: str
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str | None) -> None:
        self.__first_name = value

    @property
    def surname(self) -> str | None:
        """
        | Surname(s) or last name(s) of the customer

        Type: str
        """
        return self.__surname

    @surname.setter
    def surname(self, value: str | None) -> None:
        self.__surname = value

    @property
    def title(self) -> str | None:
        """
        | Title of customer

        Type: str
        """
        return self.__title

    @title.setter
    def title(self, value: str | None) -> None:
        self.__title = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.first_name is not None:
            dictionary['firstName'] = self.first_name
        if self.surname is not None:
            dictionary['surname'] = self.surname
        if self.title is not None:
            dictionary['title'] = self.title
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PersonalName':
        super().from_dictionary(dictionary)
        if 'firstName' in dictionary:
            self.first_name = dictionary['firstName']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        if 'title' in dictionary:
            self.title = dictionary['title']
        return self
