#
# This file was automatically generated.
#
from .data_object import DataObject


class SendTestRequest(DataObject):

    __slots__ = (
        "__url",
    )

    __url: str | None

    def __init__(
        self,
        *,
        url: str | None = None,
    ) -> None:
        self.url = url

    @property
    def url(self) -> str | None:
        """
        | Url to which the dummy webhook would be sent. If the parameter is not sent, It will be sent as default to the webhook url configured in the backoffice.

        Type: str
        """
        return self.__url

    @url.setter
    def url(self, value: str | None) -> None:
        self.__url = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.url is not None:
            dictionary['url'] = self.url
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SendTestRequest':
        super().from_dictionary(dictionary)
        if 'url' in dictionary:
            self.url = dictionary['url']
        return self
