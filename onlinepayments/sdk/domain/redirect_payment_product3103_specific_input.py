#
# This file was automatically generated.
#
from .data_object import DataObject


class RedirectPaymentProduct3103SpecificInput(DataObject):

    __slots__ = (
        "__complete_remaining_payment_amount",
    )

    __complete_remaining_payment_amount: bool | None

    def __init__(
        self,
        *,
        complete_remaining_payment_amount: bool | None = None,
    ) -> None:
        self.complete_remaining_payment_amount = complete_remaining_payment_amount

    @property
    def complete_remaining_payment_amount(self) -> bool | None:
        """
        | Determines how the remaining payment amount is handled if the initial payment is insufficient.
        
        * ``true``: The payment process will continue on our side, allowing the customer to pay the outstanding amount using a different payment method.
        * ``false``: Merchant must create and process a separate payment for the remaining amount independently.

        Type: bool
        """
        return self.__complete_remaining_payment_amount

    @complete_remaining_payment_amount.setter
    def complete_remaining_payment_amount(self, value: bool | None) -> None:
        self.__complete_remaining_payment_amount = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.complete_remaining_payment_amount is not None:
            dictionary['completeRemainingPaymentAmount'] = self.complete_remaining_payment_amount
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct3103SpecificInput':
        super().from_dictionary(dictionary)
        if 'completeRemainingPaymentAmount' in dictionary:
            self.complete_remaining_payment_amount = dictionary['completeRemainingPaymentAmount']
        return self
