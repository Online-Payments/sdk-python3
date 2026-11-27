#
# This file was automatically generated.
#
from .data_object import DataObject


class RefundRedirectMethodSpecificOutput(DataObject):

    __slots__ = (
        "__total_amount_paid",
        "__total_amount_refunded",
    )

    __total_amount_paid: int | None
    __total_amount_refunded: int | None

    def __init__(
        self,
        *,
        total_amount_paid: int | None = None,
        total_amount_refunded: int | None = None,
    ) -> None:
        self.total_amount_paid = total_amount_paid
        self.total_amount_refunded = total_amount_refunded

    @property
    def total_amount_paid(self) -> int | None:
        """
        Type: int
        """
        return self.__total_amount_paid

    @total_amount_paid.setter
    def total_amount_paid(self, value: int | None) -> None:
        self.__total_amount_paid = value

    @property
    def total_amount_refunded(self) -> int | None:
        """
        Type: int
        """
        return self.__total_amount_refunded

    @total_amount_refunded.setter
    def total_amount_refunded(self, value: int | None) -> None:
        self.__total_amount_refunded = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.total_amount_paid is not None:
            dictionary['totalAmountPaid'] = self.total_amount_paid
        if self.total_amount_refunded is not None:
            dictionary['totalAmountRefunded'] = self.total_amount_refunded
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundRedirectMethodSpecificOutput':
        super().from_dictionary(dictionary)
        if 'totalAmountPaid' in dictionary:
            self.total_amount_paid = dictionary['totalAmountPaid']
        if 'totalAmountRefunded' in dictionary:
            self.total_amount_refunded = dictionary['totalAmountRefunded']
        return self
