#
# This file was automatically generated.
#
from .data_object import DataObject


class CaptureStatusOutput(DataObject):

    __slots__ = (
        "__status_code",
    )

    __status_code: int | None

    def __init__(
        self,
        *,
        status_code: int | None = None,
    ) -> None:
        self.status_code = status_code

    @property
    def status_code(self) -> int | None:
        """
        | Numeric status code of the legacy API. The value can also be found in the BackOffice and in report files.

        Type: int
        """
        return self.__status_code

    @status_code.setter
    def status_code(self, value: int | None) -> None:
        self.__status_code = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.status_code is not None:
            dictionary['statusCode'] = self.status_code
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CaptureStatusOutput':
        super().from_dictionary(dictionary)
        if 'statusCode' in dictionary:
            self.status_code = dictionary['statusCode']
        return self
