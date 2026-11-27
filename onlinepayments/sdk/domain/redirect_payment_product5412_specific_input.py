#
# This file was automatically generated.
#
from .data_object import DataObject


class RedirectPaymentProduct5412SpecificInput(DataObject):

    __slots__ = (
        "__adjustable_amount",
        "__beneficiary_id",
    )

    __adjustable_amount: bool | None
    __beneficiary_id: str | None

    def __init__(
        self,
        *,
        adjustable_amount: bool | None = None,
        beneficiary_id: str | None = None,
    ) -> None:
        self.adjustable_amount = adjustable_amount
        self.beneficiary_id = beneficiary_id

    @property
    def adjustable_amount(self) -> bool | None:
        """
        | If true, the customer can adjust the portion of the total amount paid using this payment method in the ANCV app at authentication time.

        Type: bool
        """
        return self.__adjustable_amount

    @adjustable_amount.setter
    def adjustable_amount(self, value: bool | None) -> None:
        self.__adjustable_amount = value

    @property
    def beneficiary_id(self) -> str | None:
        """
        | The customer's 11-digit CV Connect ID, or their e-mail address on file with ANCV. The customer will be able to confirm their ID before proceeding with payment.

        Type: str
        """
        return self.__beneficiary_id

    @beneficiary_id.setter
    def beneficiary_id(self, value: str | None) -> None:
        self.__beneficiary_id = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.adjustable_amount is not None:
            dictionary['adjustableAmount'] = self.adjustable_amount
        if self.beneficiary_id is not None:
            dictionary['beneficiaryId'] = self.beneficiary_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5412SpecificInput':
        super().from_dictionary(dictionary)
        if 'adjustableAmount' in dictionary:
            self.adjustable_amount = dictionary['adjustableAmount']
        if 'beneficiaryId' in dictionary:
            self.beneficiary_id = dictionary['beneficiaryId']
        return self
