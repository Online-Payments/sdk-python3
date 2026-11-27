#
# This file was automatically generated.
#
from .data_object import DataObject


class CardInstallmentDetails(DataObject):

    __slots__ = (
        "__installment_payment_sequence_indicator",
    )

    __installment_payment_sequence_indicator: str | None

    def __init__(
        self,
        *,
        installment_payment_sequence_indicator: str | None = None,
    ) -> None:
        self.installment_payment_sequence_indicator = installment_payment_sequence_indicator

    @property
    def installment_payment_sequence_indicator(self) -> str | None:
        """
        * first = This transaction is the first of a series of installment transactions
        * subsequent = This transaction is a subsequent transaction in a series of installment transactions Note: For any first of an installment the system will automatically create a token as you will need to use a token for any subsequent installment transactions. In case a token already exists this is indicated in the response with a value of False for the isNewToken property in the response.

        Type: str
        """
        return self.__installment_payment_sequence_indicator

    @installment_payment_sequence_indicator.setter
    def installment_payment_sequence_indicator(self, value: str | None) -> None:
        self.__installment_payment_sequence_indicator = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.installment_payment_sequence_indicator is not None:
            dictionary['installmentPaymentSequenceIndicator'] = self.installment_payment_sequence_indicator
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardInstallmentDetails':
        super().from_dictionary(dictionary)
        if 'installmentPaymentSequenceIndicator' in dictionary:
            self.installment_payment_sequence_indicator = dictionary['installmentPaymentSequenceIndicator']
        return self
