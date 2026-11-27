#
# This file was automatically generated.
#
from .data_object import DataObject


class SessionDetails(DataObject):

    __slots__ = (
        "__id",
        "__type",
    )

    __id: str | None
    __type: str | None

    def __init__(
        self,
        *,
        id: str | None = None,
        type: str | None = None,
    ) -> None:
        self.id = id
        self.type = type

    @property
    def id(self) -> str | None:
        """
        | Session identifier from where this payment originates from. Depends on the session type: ex: For PayByLink: id is the corresponding paymentLinkId.

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: str | None) -> None:
        self.__id = value

    @property
    def type(self) -> str | None:
        """
        | Session type. This denotes the origin of the session. For example PayByLink, HostedTokenization, etc.

        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: str | None) -> None:
        self.__type = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.type is not None:
            dictionary['type'] = self.type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SessionDetails':
        super().from_dictionary(dictionary)
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self
