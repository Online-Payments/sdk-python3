#
# This file was automatically generated.
#
from .data_object import DataObject


class BankAccountIban(DataObject):

    __slots__ = (
        "__iban",
    )

    __iban: str | None

    def __init__(
        self,
        *,
        iban: str | None = None,
    ) -> None:
        self.iban = iban

    @property
    def iban(self) -> str | None:
        """
        | The IBAN is the International Bank Account Number. It is an internationally agreed format for the BBAN and includes the ISO country code and two check digits. Required for the creation of a Payout Required for Create and Update token. Required for Create mandate and Create payment with mandate calls. It is optional when the mandate signature type is "AIS"; otherwise, it is mandatory.

        Type: str
        """
        return self.__iban

    @iban.setter
    def iban(self, value: str | None) -> None:
        self.__iban = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.iban is not None:
            dictionary['iban'] = self.iban
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'BankAccountIban':
        super().from_dictionary(dictionary)
        if 'iban' in dictionary:
            self.iban = dictionary['iban']
        return self
