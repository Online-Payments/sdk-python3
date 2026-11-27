#
# This file was automatically generated.
#
from .card import Card
from .data_object import DataObject


class CardPayoutMethodSpecificInput(DataObject):

    __slots__ = (
        "__card",
        "__hosted_fields_session_id",
        "__payment_product_id",
        "__payout_reason",
        "__token",
    )

    __card: Card | None
    __hosted_fields_session_id: str | None
    __payment_product_id: int | None
    __payout_reason: str | None
    __token: str | None

    def __init__(
        self,
        *,
        card: Card | None = None,
        hosted_fields_session_id: str | None = None,
        payment_product_id: int | None = None,
        payout_reason: str | None = None,
        token: str | None = None,
    ) -> None:
        self.card = card
        self.hosted_fields_session_id = hosted_fields_session_id
        self.payment_product_id = payment_product_id
        self.payout_reason = payout_reason
        self.token = token

    @property
    def card(self) -> Card | None:
        """
        | Object containing card details

        Type: :class:`onlinepayments.sdk.domain.card.Card`
        """
        return self.__card

    @card.setter
    def card(self, value: Card | None) -> None:
        self.__card = value

    @property
    def hosted_fields_session_id(self) -> str | None:
        """
        | A unique identifier that references a previously created hosted fields session. Use this field to reuse the payment method details securely captured in the referenced hosted fields session.

        Type: str
        """
        return self.__hosted_fields_session_id

    @hosted_fields_session_id.setter
    def hosted_fields_session_id(self, value: str | None) -> None:
        self.__hosted_fields_session_id = value

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
    def payout_reason(self) -> str | None:
        """
        | Allows you to additionally specify the reason for initiating the payout for authorization purposes. If this field is not specified, authorization of the payment will be made according to your merchant profile. Possible values are:
        
        * Gambling
        * Refund
        * Loyalty

        Type: str
        """
        return self.__payout_reason

    @payout_reason.setter
    def payout_reason(self, value: str | None) -> None:
        self.__payout_reason = value

    @property
    def token(self) -> str | None:
        """
        | ID of the token

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
        if self.hosted_fields_session_id is not None:
            dictionary['hostedFieldsSessionId'] = self.hosted_fields_session_id
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.payout_reason is not None:
            dictionary['payoutReason'] = self.payout_reason
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardPayoutMethodSpecificInput':
        super().from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = Card()
            self.card = value.from_dictionary(dictionary['card'])
        if 'hostedFieldsSessionId' in dictionary:
            self.hosted_fields_session_id = dictionary['hostedFieldsSessionId']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'payoutReason' in dictionary:
            self.payout_reason = dictionary['payoutReason']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
