#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProduct5500SpecificOutput(DataObject):

    __slots__ = (
        "__entity_id",
        "__payment_end_date",
        "__payment_reference",
        "__payment_start_date",
    )

    __entity_id: str | None
    __payment_end_date: str | None
    __payment_reference: str | None
    __payment_start_date: str | None

    def __init__(
        self,
        *,
        entity_id: str | None = None,
        payment_end_date: str | None = None,
        payment_reference: str | None = None,
        payment_start_date: str | None = None,
    ) -> None:
        self.entity_id = entity_id
        self.payment_end_date = payment_end_date
        self.payment_reference = payment_reference
        self.payment_start_date = payment_start_date

    @property
    def entity_id(self) -> str | None:
        """
        | The reference to be used during Multibanco payment for reconciliation matter

        Type: str
        """
        return self.__entity_id

    @entity_id.setter
    def entity_id(self, value: str | None) -> None:
        self.__entity_id = value

    @property
    def payment_end_date(self) -> str | None:
        """
        | The end date of the payment validity

        Type: str
        """
        return self.__payment_end_date

    @payment_end_date.setter
    def payment_end_date(self, value: str | None) -> None:
        self.__payment_end_date = value

    @property
    def payment_reference(self) -> str | None:
        """
        | The reference to be used within the Multibanco network to confirm the payment

        Type: str
        """
        return self.__payment_reference

    @payment_reference.setter
    def payment_reference(self, value: str | None) -> None:
        self.__payment_reference = value

    @property
    def payment_start_date(self) -> str | None:
        """
        | The start date of the payment validity

        Type: str
        """
        return self.__payment_start_date

    @payment_start_date.setter
    def payment_start_date(self, value: str | None) -> None:
        self.__payment_start_date = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.entity_id is not None:
            dictionary['entityId'] = self.entity_id
        if self.payment_end_date is not None:
            dictionary['paymentEndDate'] = self.payment_end_date
        if self.payment_reference is not None:
            dictionary['paymentReference'] = self.payment_reference
        if self.payment_start_date is not None:
            dictionary['paymentStartDate'] = self.payment_start_date
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct5500SpecificOutput':
        super().from_dictionary(dictionary)
        if 'entityId' in dictionary:
            self.entity_id = dictionary['entityId']
        if 'paymentEndDate' in dictionary:
            self.payment_end_date = dictionary['paymentEndDate']
        if 'paymentReference' in dictionary:
            self.payment_reference = dictionary['paymentReference']
        if 'paymentStartDate' in dictionary:
            self.payment_start_date = dictionary['paymentStartDate']
        return self
