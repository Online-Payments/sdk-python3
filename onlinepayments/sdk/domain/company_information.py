#
# This file was automatically generated.
#
from .data_object import DataObject


class CompanyInformation(DataObject):

    __slots__ = (
        "__name",
    )

    __name: str | None

    def __init__(
        self,
        *,
        name: str | None = None,
    ) -> None:
        self.name = name

    @property
    def name(self) -> str | None:
        """
        | Name of company, as a customer. For Klarna payment method, company name should be provided to trigger a B2B session. If nothing is provided, a B2C session will be the default.

        Type: str
        """
        return self.__name

    @name.setter
    def name(self, value: str | None) -> None:
        self.__name = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.name is not None:
            dictionary['name'] = self.name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CompanyInformation':
        super().from_dictionary(dictionary)
        if 'name' in dictionary:
            self.name = dictionary['name']
        return self
