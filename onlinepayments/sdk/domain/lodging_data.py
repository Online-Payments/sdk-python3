#
# This file was automatically generated.
#
from .data_object import DataObject


class LodgingData(DataObject):

    __slots__ = (
        "__check_in_date",
    )

    __check_in_date: str | None

    def __init__(
        self,
        *,
        check_in_date: str | None = None,
    ) -> None:
        self.check_in_date = check_in_date

    @property
    def check_in_date(self) -> str | None:
        """
        | The date the guest checks into (or plans to check in to) the facility. Format YYYYMMDD

        Type: str
        """
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value: str | None) -> None:
        self.__check_in_date = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.check_in_date is not None:
            dictionary['checkInDate'] = self.check_in_date
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'LodgingData':
        super().from_dictionary(dictionary)
        if 'checkInDate' in dictionary:
            self.check_in_date = dictionary['checkInDate']
        return self
