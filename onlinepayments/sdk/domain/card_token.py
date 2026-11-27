#
# This file was automatically generated.
#
from .data_object import DataObject


class CardToken(DataObject):

    __slots__ = (
        "__cardholder_name",
        "__expiry_date",
        "__logo_url",
        "__masked_pan",
        "__payment_product_id",
        "__product_name",
        "__token",
    )

    __cardholder_name: str | None
    __expiry_date: str | None
    __logo_url: str | None
    __masked_pan: str | None
    __payment_product_id: int | None
    __product_name: str | None
    __token: str | None

    def __init__(
        self,
        *,
        cardholder_name: str | None = None,
        expiry_date: str | None = None,
        logo_url: str | None = None,
        masked_pan: str | None = None,
        payment_product_id: int | None = None,
        product_name: str | None = None,
        token: str | None = None,
    ) -> None:
        self.cardholder_name = cardholder_name
        self.expiry_date = expiry_date
        self.logo_url = logo_url
        self.masked_pan = masked_pan
        self.payment_product_id = payment_product_id
        self.product_name = product_name
        self.token = token

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

    @property
    def logo_url(self) -> str | None:
        """
        | URL to the card product logo.

        Type: str
        """
        return self.__logo_url

    @logo_url.setter
    def logo_url(self, value: str | None) -> None:
        self.__logo_url = value

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
    def payment_product_id(self) -> int | None:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: int | None) -> None:
        self.__payment_product_id = value

    @property
    def product_name(self) -> str | None:
        """
        | Product name of the card

        Type: str
        """
        return self.__product_name

    @product_name.setter
    def product_name(self, value: str | None) -> None:
        self.__product_name = value

    @property
    def token(self) -> str | None:
        """
        | This is a validated card token available for later use.

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: str | None) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.cardholder_name is not None:
            dictionary['cardholderName'] = self.cardholder_name
        if self.expiry_date is not None:
            dictionary['expiryDate'] = self.expiry_date
        if self.logo_url is not None:
            dictionary['logoUrl'] = self.logo_url
        if self.masked_pan is not None:
            dictionary['maskedPan'] = self.masked_pan
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.product_name is not None:
            dictionary['productName'] = self.product_name
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardToken':
        super().from_dictionary(dictionary)
        if 'cardholderName' in dictionary:
            self.cardholder_name = dictionary['cardholderName']
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        if 'logoUrl' in dictionary:
            self.logo_url = dictionary['logoUrl']
        if 'maskedPan' in dictionary:
            self.masked_pan = dictionary['maskedPan']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'productName' in dictionary:
            self.product_name = dictionary['productName']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
