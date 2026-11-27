#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentLinkEvent(DataObject):

    __slots__ = (
        "__date_time",
        "__details",
        "__type",
    )

    __date_time: str | None
    __details: str | None
    __type: str | None

    def __init__(
        self,
        *,
        date_time: str | None = None,
        details: str | None = None,
        type: str | None = None,
    ) -> None:
        self.date_time = date_time
        self.details = details
        self.type = type

    @property
    def date_time(self) -> str | None:
        """
        | The date and time the change occurred. The date will contain the UTC offset.

        Type: str
        """
        return self.__date_time

    @date_time.setter
    def date_time(self, value: str | None) -> None:
        self.__date_time = value

    @property
    def details(self) -> str | None:
        """
        | Details of the events. Ex.: email address or phone number of the recipient.

        Type: str
        """
        return self.__details

    @details.setter
    def details(self, value: str | None) -> None:
        self.__details = value

    @property
    def type(self) -> str | None:
        """
        | The type of event that occurred.

        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: str | None) -> None:
        self.__type = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.date_time is not None:
            dictionary['dateTime'] = self.date_time
        if self.details is not None:
            dictionary['details'] = self.details
        if self.type is not None:
            dictionary['type'] = self.type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentLinkEvent':
        super().from_dictionary(dictionary)
        if 'dateTime' in dictionary:
            self.date_time = dictionary['dateTime']
        if 'details' in dictionary:
            self.details = dictionary['details']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self
