#
# This file was automatically generated.
#
from .data_object import DataObject


class DetokenizedTokenResponse(DataObject):

    __slots__ = (
        "__card_brand",
        "__card_expiry_date",
        "__card_holder_name",
        "__encrypted_card_number",
        "__payment_id",
        "__scheme_reference_data",
        "__token",
    )

    __card_brand: str | None
    __card_expiry_date: str | None
    __card_holder_name: str | None
    __encrypted_card_number: str | None
    __payment_id: str | None
    __scheme_reference_data: str | None
    __token: str | None

    def __init__(
        self,
        *,
        card_brand: str | None = None,
        card_expiry_date: str | None = None,
        card_holder_name: str | None = None,
        encrypted_card_number: str | None = None,
        payment_id: str | None = None,
        scheme_reference_data: str | None = None,
        token: str | None = None,
    ) -> None:
        self.card_brand = card_brand
        self.card_expiry_date = card_expiry_date
        self.card_holder_name = card_holder_name
        self.encrypted_card_number = encrypted_card_number
        self.payment_id = payment_id
        self.scheme_reference_data = scheme_reference_data
        self.token = token

    @property
    def card_brand(self) -> str | None:
        """
        | The brand of the card (e.g., VISA, MasterCard).

        Type: str
        """
        return self.__card_brand

    @card_brand.setter
    def card_brand(self, value: str | None) -> None:
        self.__card_brand = value

    @property
    def card_expiry_date(self) -> str | None:
        """
        | The expiration date of the card in MMYY format, where MM represents the two-digit month and YY represents the two-digit year. For example, a value of 0529 indicates that the card expires in May 2029.

        Type: str
        """
        return self.__card_expiry_date

    @card_expiry_date.setter
    def card_expiry_date(self, value: str | None) -> None:
        self.__card_expiry_date = value

    @property
    def card_holder_name(self) -> str | None:
        """
        | The full name of the cardholder as it appears on the card.

        Type: str
        """
        return self.__card_holder_name

    @card_holder_name.setter
    def card_holder_name(self, value: str | None) -> None:
        self.__card_holder_name = value

    @property
    def encrypted_card_number(self) -> str | None:
        """
        | The card number, encrypted and Base64 encoded for secure transport.

        Type: str
        """
        return self.__encrypted_card_number

    @encrypted_card_number.setter
    def encrypted_card_number(self, value: str | None) -> None:
        self.__encrypted_card_number = value

    @property
    def payment_id(self) -> str | None:
        """
        | The unique identifier for the payment associated with the token is necessary for tracking.

        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: str | None) -> None:
        self.__payment_id = value

    @property
    def scheme_reference_data(self) -> str | None:
        """
        | Reference data associated with the payment scheme for the credentials on file.

        Type: str
        """
        return self.__scheme_reference_data

    @scheme_reference_data.setter
    def scheme_reference_data(self, value: str | None) -> None:
        self.__scheme_reference_data = value

    @property
    def token(self) -> str | None:
        """
        | The unique identifier for the token is required for processing.

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: str | None) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.card_brand is not None:
            dictionary['cardBrand'] = self.card_brand
        if self.card_expiry_date is not None:
            dictionary['cardExpiryDate'] = self.card_expiry_date
        if self.card_holder_name is not None:
            dictionary['cardHolderName'] = self.card_holder_name
        if self.encrypted_card_number is not None:
            dictionary['encryptedCardNumber'] = self.encrypted_card_number
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        if self.scheme_reference_data is not None:
            dictionary['schemeReferenceData'] = self.scheme_reference_data
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DetokenizedTokenResponse':
        super().from_dictionary(dictionary)
        if 'cardBrand' in dictionary:
            self.card_brand = dictionary['cardBrand']
        if 'cardExpiryDate' in dictionary:
            self.card_expiry_date = dictionary['cardExpiryDate']
        if 'cardHolderName' in dictionary:
            self.card_holder_name = dictionary['cardHolderName']
        if 'encryptedCardNumber' in dictionary:
            self.encrypted_card_number = dictionary['encryptedCardNumber']
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        if 'schemeReferenceData' in dictionary:
            self.scheme_reference_data = dictionary['schemeReferenceData']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
