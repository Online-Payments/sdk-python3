#
# This file was automatically generated.
#
from .data_object import DataObject


class CardPaymentMethodSpecificOutputSummaryCard(DataObject):

    __slots__ = (
        "__card_number",
    )

    __card_number: str | None

    def __init__(
        self,
        *,
        card_number: str | None = None,
    ) -> None:
        self.card_number = card_number

    @property
    def card_number(self) -> str | None:
        """
        | The masked credit/debit card number

        Type: str
        """
        return self.__card_number

    @card_number.setter
    def card_number(self, value: str | None) -> None:
        self.__card_number = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.card_number is not None:
            dictionary['cardNumber'] = self.card_number
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardPaymentMethodSpecificOutputSummaryCard':
        super().from_dictionary(dictionary)
        if 'cardNumber' in dictionary:
            self.card_number = dictionary['cardNumber']
        return self
