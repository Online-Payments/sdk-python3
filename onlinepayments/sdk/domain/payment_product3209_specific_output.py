#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProduct3209SpecificOutput(DataObject):

    __slots__ = (
        "__buyer_compliant_bank_message",
    )

    __buyer_compliant_bank_message: str | None

    def __init__(
        self,
        *,
        buyer_compliant_bank_message: str | None = None,
    ) -> None:
        self.buyer_compliant_bank_message = buyer_compliant_bank_message

    @property
    def buyer_compliant_bank_message(self) -> str | None:
        """
        | This field indicates the text that must be returned and shown to the buyer to be compliant with the law regulating this payment product.

        Type: str
        """
        return self.__buyer_compliant_bank_message

    @buyer_compliant_bank_message.setter
    def buyer_compliant_bank_message(self, value: str | None) -> None:
        self.__buyer_compliant_bank_message = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.buyer_compliant_bank_message is not None:
            dictionary['buyerCompliantBankMessage'] = self.buyer_compliant_bank_message
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct3209SpecificOutput':
        super().from_dictionary(dictionary)
        if 'buyerCompliantBankMessage' in dictionary:
            self.buyer_compliant_bank_message = dictionary['buyerCompliantBankMessage']
        return self
