#
# This file was automatically generated.
#
from .data_object import DataObject


class NetworkTokenData(DataObject):

    __slots__ = (
        "__cardholder_name",
        "__cryptogram",
        "__eci",
        "__network_token",
        "__scheme_token_requestor_id",
        "__token_expiry_date",
    )

    __cardholder_name: str | None
    __cryptogram: str | None
    __eci: int | None
    __network_token: str | None
    __scheme_token_requestor_id: str | None
    __token_expiry_date: str | None

    def __init__(
        self,
        *,
        cardholder_name: str | None = None,
        cryptogram: str | None = None,
        eci: int | None = None,
        network_token: str | None = None,
        scheme_token_requestor_id: str | None = None,
        token_expiry_date: str | None = None,
    ) -> None:
        self.cardholder_name = cardholder_name
        self.cryptogram = cryptogram
        self.eci = eci
        self.network_token = network_token
        self.scheme_token_requestor_id = scheme_token_requestor_id
        self.token_expiry_date = token_expiry_date

    @property
    def cardholder_name(self) -> str | None:
        """
        | The card holder's name on the card associated with the Network Token.

        Type: str
        """
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value: str | None) -> None:
        self.__cardholder_name = value

    @property
    def cryptogram(self) -> str | None:
        """
        | The Token Cryptogram is a dynamic one-time use value that is used to verify the authenticity of the transaction and the integrity of the data used in the generation of the Token Cryptogram. Visa calls this the Token Authentication Verification Value (TAVV) cryptogram.

        Type: str
        """
        return self.__cryptogram

    @cryptogram.setter
    def cryptogram(self, value: str | None) -> None:
        self.__cryptogram = value

    @property
    def eci(self) -> int | None:
        """
        | The Electronic Commerce Indicator linked to the Token Cryptogram that is provided by the token service provider during the generation of the Token Cryptogram.

        Type: int
        """
        return self.__eci

    @eci.setter
    def eci(self, value: int | None) -> None:
        self.__eci = value

    @property
    def network_token(self) -> str | None:
        """
        | Payment Token associated with the Card used for the purchase. Note: This is called Payment Token in the EMVCo documentation.

        Type: str
        """
        return self.__network_token

    @network_token.setter
    def network_token(self, value: str | None) -> None:
        self.__network_token = value

    @property
    def scheme_token_requestor_id(self) -> str | None:
        """
        | Token Requestor Identifier used with the token service provider during the creation of the Network Token. Depending on the acquirer, this data might be required in the authorization request. We advise you to provide it for all Network Token initiated transactions.

        Type: str
        """
        return self.__scheme_token_requestor_id

    @scheme_token_requestor_id.setter
    def scheme_token_requestor_id(self, value: str | None) -> None:
        self.__scheme_token_requestor_id = value

    @property
    def token_expiry_date(self) -> str | None:
        """
        | The expiry date of the network token. Format: MMYY

        Type: str
        """
        return self.__token_expiry_date

    @token_expiry_date.setter
    def token_expiry_date(self, value: str | None) -> None:
        self.__token_expiry_date = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.cardholder_name is not None:
            dictionary['cardholderName'] = self.cardholder_name
        if self.cryptogram is not None:
            dictionary['cryptogram'] = self.cryptogram
        if self.eci is not None:
            dictionary['eci'] = self.eci
        if self.network_token is not None:
            dictionary['networkToken'] = self.network_token
        if self.scheme_token_requestor_id is not None:
            dictionary['schemeTokenRequestorId'] = self.scheme_token_requestor_id
        if self.token_expiry_date is not None:
            dictionary['tokenExpiryDate'] = self.token_expiry_date
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'NetworkTokenData':
        super().from_dictionary(dictionary)
        if 'cardholderName' in dictionary:
            self.cardholder_name = dictionary['cardholderName']
        if 'cryptogram' in dictionary:
            self.cryptogram = dictionary['cryptogram']
        if 'eci' in dictionary:
            self.eci = dictionary['eci']
        if 'networkToken' in dictionary:
            self.network_token = dictionary['networkToken']
        if 'schemeTokenRequestorId' in dictionary:
            self.scheme_token_requestor_id = dictionary['schemeTokenRequestorId']
        if 'tokenExpiryDate' in dictionary:
            self.token_expiry_date = dictionary['tokenExpiryDate']
        return self
