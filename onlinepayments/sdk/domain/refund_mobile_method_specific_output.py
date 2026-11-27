#
# This file was automatically generated.
#
from .data_object import DataObject


class RefundMobileMethodSpecificOutput(DataObject):

    __slots__ = (
        "__network",
        "__total_amount_paid",
        "__total_amount_refunded",
    )

    __network: str | None
    __total_amount_paid: int | None
    __total_amount_refunded: int | None

    def __init__(
        self,
        *,
        network: str | None = None,
        total_amount_paid: int | None = None,
        total_amount_refunded: int | None = None,
    ) -> None:
        self.network = network
        self.total_amount_paid = total_amount_paid
        self.total_amount_refunded = total_amount_refunded

    @property
    def network(self) -> str | None:
        """
        | The card network that was used for a mobile payment method operation

        Type: str
        """
        return self.__network

    @network.setter
    def network(self, value: str | None) -> None:
        self.__network = value

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
        if self.network is not None:
            dictionary['network'] = self.network
        if self.total_amount_paid is not None:
            dictionary['totalAmountPaid'] = self.total_amount_paid
        if self.total_amount_refunded is not None:
            dictionary['totalAmountRefunded'] = self.total_amount_refunded
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundMobileMethodSpecificOutput':
        super().from_dictionary(dictionary)
        if 'network' in dictionary:
            self.network = dictionary['network']
        if 'totalAmountPaid' in dictionary:
            self.total_amount_paid = dictionary['totalAmountPaid']
        if 'totalAmountRefunded' in dictionary:
            self.total_amount_refunded = dictionary['totalAmountRefunded']
        return self
