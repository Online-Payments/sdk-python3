#
# This file was automatically generated.
#
from .data_object import DataObject


class CardWithoutCvv(DataObject):

    __slots__ = (
        "__card_number",
        "__cardholder_name",
        "__expiry_date",
    )

    __card_number: str | None
    __cardholder_name: str | None
    __expiry_date: str | None

    def __init__(
        self,
        *,
        card_number: str | None = None,
        cardholder_name: str | None = None,
        expiry_date: str | None = None,
    ) -> None:
        self.card_number = card_number
        self.cardholder_name = cardholder_name
        self.expiry_date = expiry_date

    @property
    def card_number(self) -> str | None:
        """
        | The obfuscated card number

        Type: str
        """
        return self.__card_number

    @card_number.setter
    def card_number(self, value: str | None) -> None:
        self.__card_number = value

    @property
    def cardholder_name(self) -> str | None:
        """
        | The card holder's name on the card.

        Type: str
        """
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value: str | None) -> None:
        self.__cardholder_name = value

    @property
    def expiry_date(self) -> str | None:
        """
        | Expiry date of the card Format: MMYY

        Type: str
        """
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value: str | None) -> None:
        self.__expiry_date = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.card_number is not None:
            dictionary['cardNumber'] = self.card_number
        if self.cardholder_name is not None:
            dictionary['cardholderName'] = self.cardholder_name
        if self.expiry_date is not None:
            dictionary['expiryDate'] = self.expiry_date
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardWithoutCvv':
        super().from_dictionary(dictionary)
        if 'cardNumber' in dictionary:
            self.card_number = dictionary['cardNumber']
        if 'cardholderName' in dictionary:
            self.cardholder_name = dictionary['cardholderName']
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        return self
