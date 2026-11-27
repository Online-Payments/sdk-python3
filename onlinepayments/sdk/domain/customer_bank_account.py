#
# This file was automatically generated.
#
from .data_object import DataObject


class CustomerBankAccount(DataObject):

    __slots__ = (
        "__account_holder_name",
        "__bic",
        "__iban",
    )

    __account_holder_name: str | None
    __bic: str | None
    __iban: str | None

    def __init__(
        self,
        *,
        account_holder_name: str | None = None,
        bic: str | None = None,
        iban: str | None = None,
    ) -> None:
        self.account_holder_name = account_holder_name
        self.bic = bic
        self.iban = iban

    @property
    def account_holder_name(self) -> str | None:
        """
        | Name of account holder

        Type: str
        """
        return self.__account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, value: str | None) -> None:
        self.__account_holder_name = value

    @property
    def bic(self) -> str | None:
        """
        | Bank Identification Code

        Type: str
        """
        return self.__bic

    @bic.setter
    def bic(self, value: str | None) -> None:
        self.__bic = value

    @property
    def iban(self) -> str | None:
        """
        | The IBAN is the International Bank Account Number. It is an internationally agreed format for the BBAN and includes the ISO country code and two check digits.

        Type: str
        """
        return self.__iban

    @iban.setter
    def iban(self, value: str | None) -> None:
        self.__iban = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.account_holder_name is not None:
            dictionary['accountHolderName'] = self.account_holder_name
        if self.bic is not None:
            dictionary['bic'] = self.bic
        if self.iban is not None:
            dictionary['iban'] = self.iban
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CustomerBankAccount':
        super().from_dictionary(dictionary)
        if 'accountHolderName' in dictionary:
            self.account_holder_name = dictionary['accountHolderName']
        if 'bic' in dictionary:
            self.bic = dictionary['bic']
        if 'iban' in dictionary:
            self.iban = dictionary['iban']
        return self
