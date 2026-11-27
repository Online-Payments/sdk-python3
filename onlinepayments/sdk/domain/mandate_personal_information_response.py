#
# This file was automatically generated.
#
from .data_object import DataObject
from .mandate_personal_name_response import MandatePersonalNameResponse


class MandatePersonalInformationResponse(DataObject):

    __slots__ = (
        "__name",
        "__title",
    )

    __name: MandatePersonalNameResponse | None
    __title: str | None

    def __init__(
        self,
        *,
        name: MandatePersonalNameResponse | None = None,
        title: str | None = None,
    ) -> None:
        self.name = name
        self.title = title

    @property
    def name(self) -> MandatePersonalNameResponse | None:
        """
        | Object containing the name details of the customer.

        Type: :class:`onlinepayments.sdk.domain.mandate_personal_name_response.MandatePersonalNameResponse`
        """
        return self.__name

    @name.setter
    def name(self, value: MandatePersonalNameResponse | None) -> None:
        self.__name = value

    @property
    def title(self) -> str | None:
        """
        | Object containing the title of the customer (Mr, Miss or Mrs)

        Type: str
        """
        return self.__title

    @title.setter
    def title(self, value: str | None) -> None:
        self.__title = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.name is not None:
            dictionary['name'] = self.name.to_dictionary()
        if self.title is not None:
            dictionary['title'] = self.title
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MandatePersonalInformationResponse':
        super().from_dictionary(dictionary)
        if 'name' in dictionary:
            if not isinstance(dictionary['name'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['name']))
            value = MandatePersonalNameResponse()
            self.name = value.from_dictionary(dictionary['name'])
        if 'title' in dictionary:
            self.title = dictionary['title']
        return self
