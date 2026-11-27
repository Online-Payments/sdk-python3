#
# This file was automatically generated.
#
from .data_object import DataObject


class MobilePaymentData(DataObject):

    __slots__ = (
        "__dpan",
        "__expiry_date",
    )

    __dpan: str | None
    __expiry_date: str | None

    def __init__(
        self,
        *,
        dpan: str | None = None,
        expiry_date: str | None = None,
    ) -> None:
        self.dpan = dpan
        self.expiry_date = expiry_date

    @property
    def dpan(self) -> str | None:
        """
        | The obfuscated DPAN. Only the last four digits are visible.

        Type: str
        """
        return self.__dpan

    @dpan.setter
    def dpan(self, value: str | None) -> None:
        self.__dpan = value

    @property
    def expiry_date(self) -> str | None:
        """
        | Expiry date of the tokenized card. Format: MMYY

        Type: str
        """
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value: str | None) -> None:
        self.__expiry_date = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.dpan is not None:
            dictionary['dpan'] = self.dpan
        if self.expiry_date is not None:
            dictionary['expiryDate'] = self.expiry_date
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MobilePaymentData':
        super().from_dictionary(dictionary)
        if 'dpan' in dictionary:
            self.dpan = dictionary['dpan']
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        return self
