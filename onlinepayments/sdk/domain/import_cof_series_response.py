#
# This file was automatically generated.
#
from .data_object import DataObject


class ImportCofSeriesResponse(DataObject):

    __slots__ = (
        "__payment_id",
    )

    __payment_id: str | None

    def __init__(
        self,
        *,
        payment_id: str | None = None,
    ) -> None:
        self.payment_id = payment_id

    @property
    def payment_id(self) -> str | None:
        """
        | This is our unique payment transaction identifier.

        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: str | None) -> None:
        self.__payment_id = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ImportCofSeriesResponse':
        super().from_dictionary(dictionary)
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        return self
