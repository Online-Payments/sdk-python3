#
# This file was automatically generated.
#
from .data_object import DataObject


class LoanRecipient(DataObject):

    __slots__ = (
        "__account_number",
        "__date_of_birth",
        "__partial_pan",
        "__surname",
        "__zip",
    )

    __account_number: str | None
    __date_of_birth: str | None
    __partial_pan: str | None
    __surname: str | None
    __zip: str | None

    def __init__(
        self,
        *,
        account_number: str | None = None,
        date_of_birth: str | None = None,
        partial_pan: str | None = None,
        surname: str | None = None,
        zip: str | None = None,
    ) -> None:
        self.account_number = account_number
        self.date_of_birth = date_of_birth
        self.partial_pan = partial_pan
        self.surname = surname
        self.zip = zip

    @property
    def account_number(self) -> str | None:
        """
        | Should be filled with the last 10 digits of the bank account number of the recipient of the loan.

        Type: str
        """
        return self.__account_number

    @account_number.setter
    def account_number(self, value: str | None) -> None:
        self.__account_number = value

    @property
    def date_of_birth(self) -> str | None:
        """
        | The date of birth of the customer of the recipient of the loan. Format YYYYMMDD

        Type: str
        """
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value: str | None) -> None:
        self.__date_of_birth = value

    @property
    def partial_pan(self) -> str | None:
        """
        | Should be filled with the first 6 and last 4 digits of the PAN number of the recipient of the loan.

        Type: str
        """
        return self.__partial_pan

    @partial_pan.setter
    def partial_pan(self, value: str | None) -> None:
        self.__partial_pan = value

    @property
    def surname(self) -> str | None:
        """
        | Surname of the recipient of the loan.

        Type: str
        """
        return self.__surname

    @surname.setter
    def surname(self, value: str | None) -> None:
        self.__surname = value

    @property
    def zip(self) -> str | None:
        """
        | Zip code of the recipient of the loan

        Type: str
        """
        return self.__zip

    @zip.setter
    def zip(self, value: str | None) -> None:
        self.__zip = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.account_number is not None:
            dictionary['accountNumber'] = self.account_number
        if self.date_of_birth is not None:
            dictionary['dateOfBirth'] = self.date_of_birth
        if self.partial_pan is not None:
            dictionary['partialPan'] = self.partial_pan
        if self.surname is not None:
            dictionary['surname'] = self.surname
        if self.zip is not None:
            dictionary['zip'] = self.zip
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'LoanRecipient':
        super().from_dictionary(dictionary)
        if 'accountNumber' in dictionary:
            self.account_number = dictionary['accountNumber']
        if 'dateOfBirth' in dictionary:
            self.date_of_birth = dictionary['dateOfBirth']
        if 'partialPan' in dictionary:
            self.partial_pan = dictionary['partialPan']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        if 'zip' in dictionary:
            self.zip = dictionary['zip']
        return self
