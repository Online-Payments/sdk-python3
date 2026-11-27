#
# This file was automatically generated.
#
from .data_object import DataObject
from .surcharge_calculation_card import SurchargeCalculationCard


class CardSource(DataObject):

    __slots__ = (
        "__card",
        "__encrypted_customer_input",
        "__hosted_tokenization_id",
        "__token",
    )

    __card: SurchargeCalculationCard | None
    __encrypted_customer_input: str | None
    __hosted_tokenization_id: str | None
    __token: str | None

    def __init__(
        self,
        *,
        card: SurchargeCalculationCard | None = None,
        encrypted_customer_input: str | None = None,
        hosted_tokenization_id: str | None = None,
        token: str | None = None,
    ) -> None:
        self.card = card
        self.encrypted_customer_input = encrypted_customer_input
        self.hosted_tokenization_id = hosted_tokenization_id
        self.token = token

    @property
    def card(self) -> SurchargeCalculationCard | None:
        """
        | An object containing card number and payment product id, which is used to determine surcharge product type

        Type: :class:`onlinepayments.sdk.domain.surcharge_calculation_card.SurchargeCalculationCard`
        """
        return self.__card

    @card.setter
    def card(self, value: SurchargeCalculationCard | None) -> None:
        self.__card = value

    @property
    def encrypted_customer_input(self) -> str | None:
        """
        | Data that was encrypted client side containing all customer entered data elements like card data. Note: Because this data can only be submitted once to our system and contains encrypted card data you should not store it. As the data was captured within the context of a client session you also need to submit it to us before the session has expired.

        Type: str
        """
        return self.__encrypted_customer_input

    @encrypted_customer_input.setter
    def encrypted_customer_input(self, value: str | None) -> None:
        self.__encrypted_customer_input = value

    @property
    def hosted_tokenization_id(self) -> str | None:
        """
        | An Id of a hosted tokenization session

        Type: str
        """
        return self.__hosted_tokenization_id

    @hosted_tokenization_id.setter
    def hosted_tokenization_id(self, value: str | None) -> None:
        self.__hosted_tokenization_id = value

    @property
    def token(self) -> str | None:
        """
        | An identifier that represents card details that have been previously stored

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: str | None) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.encrypted_customer_input is not None:
            dictionary['encryptedCustomerInput'] = self.encrypted_customer_input
        if self.hosted_tokenization_id is not None:
            dictionary['hostedTokenizationId'] = self.hosted_tokenization_id
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardSource':
        super().from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = SurchargeCalculationCard()
            self.card = value.from_dictionary(dictionary['card'])
        if 'encryptedCustomerInput' in dictionary:
            self.encrypted_customer_input = dictionary['encryptedCustomerInput']
        if 'hostedTokenizationId' in dictionary:
            self.hosted_tokenization_id = dictionary['hostedTokenizationId']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
