#
# This file was automatically generated.
#
from .data_object import DataObject


class SurchargeCalculationCard(DataObject):

    __slots__ = (
        "__card_number",
        "__payment_product_id",
    )

    __card_number: str | None
    __payment_product_id: int | None

    def __init__(
        self,
        *,
        card_number: str | None = None,
        payment_product_id: int | None = None,
    ) -> None:
        self.card_number = card_number
        self.payment_product_id = payment_product_id

    @property
    def card_number(self) -> str | None:
        """
        | The complete credit/debit card number (also known as the PAN) is always obfuscated in any of our responses.

        Type: str
        """
        return self.__card_number

    @card_number.setter
    def card_number(self, value: str | None) -> None:
        self.__card_number = value

    @property
    def payment_product_id(self) -> int | None:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: int | None) -> None:
        self.__payment_product_id = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.card_number is not None:
            dictionary['cardNumber'] = self.card_number
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SurchargeCalculationCard':
        super().from_dictionary(dictionary)
        if 'cardNumber' in dictionary:
            self.card_number = dictionary['cardNumber']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
