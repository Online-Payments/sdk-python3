#
# This file was automatically generated.
#
from .data_object import DataObject


class TokenInfo(DataObject):

    __slots__ = (
        "__expiry_date",
        "__is_temporary",
        "__masked_pan",
        "__token_id",
    )

    __expiry_date: str | None
    __is_temporary: bool | None
    __masked_pan: str | None
    __token_id: str | None

    def __init__(
        self,
        *,
        expiry_date: str | None = None,
        is_temporary: bool | None = None,
        masked_pan: str | None = None,
        token_id: str | None = None,
    ) -> None:
        self.expiry_date = expiry_date
        self.is_temporary = is_temporary
        self.masked_pan = masked_pan
        self.token_id = token_id

    @property
    def expiry_date(self) -> str | None:
        """
        | The expiry date of the network token.

        Type: str
        """
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value: str | None) -> None:
        self.__expiry_date = value

    @property
    def is_temporary(self) -> bool | None:
        """
        | Temporary tokens have a lifespan of two hours and can only be used once.

        Type: bool
        """
        return self.__is_temporary

    @is_temporary.setter
    def is_temporary(self, value: bool | None) -> None:
        self.__is_temporary = value

    @property
    def masked_pan(self) -> str | None:
        """
        | The masked Primary Account Number (PAN).

        Type: str
        """
        return self.__masked_pan

    @masked_pan.setter
    def masked_pan(self, value: str | None) -> None:
        self.__masked_pan = value

    @property
    def token_id(self) -> str | None:
        """
        | ID of the token

        Type: str
        """
        return self.__token_id

    @token_id.setter
    def token_id(self, value: str | None) -> None:
        self.__token_id = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.expiry_date is not None:
            dictionary['expiryDate'] = self.expiry_date
        if self.is_temporary is not None:
            dictionary['isTemporary'] = self.is_temporary
        if self.masked_pan is not None:
            dictionary['maskedPan'] = self.masked_pan
        if self.token_id is not None:
            dictionary['tokenId'] = self.token_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'TokenInfo':
        super().from_dictionary(dictionary)
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        if 'isTemporary' in dictionary:
            self.is_temporary = dictionary['isTemporary']
        if 'maskedPan' in dictionary:
            self.masked_pan = dictionary['maskedPan']
        if 'tokenId' in dictionary:
            self.token_id = dictionary['tokenId']
        return self
