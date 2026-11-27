#
# This file was automatically generated.
#
from .data_object import DataObject


class ProblemDetailsResponse(DataObject):

    __slots__ = (
        "__detail",
        "__instance",
        "__status",
        "__title",
        "__type",
    )

    __detail: str | None
    __instance: str | None
    __status: int | None
    __title: str | None
    __type: str | None

    def __init__(
        self,
        *,
        detail: str | None = None,
        instance: str | None = None,
        status: int | None = None,
        title: str | None = None,
        type: str | None = None,
    ) -> None:
        self.detail = detail
        self.instance = instance
        self.status = status
        self.title = title
        self.type = type

    @property
    def detail(self) -> str | None:
        """
        | A human-readable explanation specific to this occurrence of the problem.

        Type: str
        """
        return self.__detail

    @detail.setter
    def detail(self, value: str | None) -> None:
        self.__detail = value

    @property
    def instance(self) -> str | None:
        """
        | A URI reference that identifies the specific occurrence of the problem.

        Type: str
        """
        return self.__instance

    @instance.setter
    def instance(self, value: str | None) -> None:
        self.__instance = value

    @property
    def status(self) -> int | None:
        """
        | The HTTP status code.

        Type: int
        """
        return self.__status

    @status.setter
    def status(self, value: int | None) -> None:
        self.__status = value

    @property
    def title(self) -> str | None:
        """
        | A short, human-readable summary of the problem type.

        Type: str
        """
        return self.__title

    @title.setter
    def title(self, value: str | None) -> None:
        self.__title = value

    @property
    def type(self) -> str | None:
        """
        | A URI reference that identifies the problem type.

        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: str | None) -> None:
        self.__type = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.detail is not None:
            dictionary['detail'] = self.detail
        if self.instance is not None:
            dictionary['instance'] = self.instance
        if self.status is not None:
            dictionary['status'] = self.status
        if self.title is not None:
            dictionary['title'] = self.title
        if self.type is not None:
            dictionary['type'] = self.type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ProblemDetailsResponse':
        super().from_dictionary(dictionary)
        if 'detail' in dictionary:
            self.detail = dictionary['detail']
        if 'instance' in dictionary:
            self.instance = dictionary['instance']
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'title' in dictionary:
            self.title = dictionary['title']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self
