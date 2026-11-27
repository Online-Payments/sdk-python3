#
# This file was automatically generated.
#
from .data_object import DataObject


class Product302Recurring(DataObject):

    __slots__ = (
        "__recurring_payment_sequence_indicator",
    )

    __recurring_payment_sequence_indicator: str | None

    def __init__(
        self,
        *,
        recurring_payment_sequence_indicator: str | None = None,
    ) -> None:
        self.recurring_payment_sequence_indicator = recurring_payment_sequence_indicator

    @property
    def recurring_payment_sequence_indicator(self) -> str | None:
        """
        * first = This transaction is the first of a series of recurring transactions

        Type: str
        """
        return self.__recurring_payment_sequence_indicator

    @recurring_payment_sequence_indicator.setter
    def recurring_payment_sequence_indicator(self, value: str | None) -> None:
        self.__recurring_payment_sequence_indicator = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.recurring_payment_sequence_indicator is not None:
            dictionary['recurringPaymentSequenceIndicator'] = self.recurring_payment_sequence_indicator
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Product302Recurring':
        super().from_dictionary(dictionary)
        if 'recurringPaymentSequenceIndicator' in dictionary:
            self.recurring_payment_sequence_indicator = dictionary['recurringPaymentSequenceIndicator']
        return self
