#
# This file was automatically generated.
#
from .acceptance import Acceptance
from .card_essentials import CardEssentials
from .data_object import DataObject


class PayoutCardPaymentMethodSpecificOutput(DataObject):

    __slots__ = (
        "__acceptance",
        "__authorisation_code",
        "__card",
        "__payment_product_id",
    )

    __acceptance: Acceptance | None
    __authorisation_code: str | None
    __card: CardEssentials | None
    __payment_product_id: int | None

    def __init__(
        self,
        *,
        acceptance: Acceptance | None = None,
        authorisation_code: str | None = None,
        card: CardEssentials | None = None,
        payment_product_id: int | None = None,
    ) -> None:
        self.acceptance = acceptance
        self.authorisation_code = authorisation_code
        self.card = card
        self.payment_product_id = payment_product_id

    @property
    def acceptance(self) -> Acceptance | None:
        """
        | This object contains the acceptance information for the card payment authorization.

        Type: :class:`onlinepayments.sdk.domain.acceptance.Acceptance`
        """
        return self.__acceptance

    @acceptance.setter
    def acceptance(self, value: Acceptance | None) -> None:
        self.__acceptance = value

    @property
    def authorisation_code(self) -> str | None:
        """
        | Card Authorization code as returned by the acquirer

        Type: str
        """
        return self.__authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, value: str | None) -> None:
        self.__authorisation_code = value

    @property
    def card(self) -> CardEssentials | None:
        """
        | Object containing card details

        Type: :class:`onlinepayments.sdk.domain.card_essentials.CardEssentials`
        """
        return self.__card

    @card.setter
    def card(self, value: CardEssentials | None) -> None:
        self.__card = value

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

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.acceptance is not None:
            dictionary['acceptance'] = self.acceptance.to_dictionary()
        if self.authorisation_code is not None:
            dictionary['authorisationCode'] = self.authorisation_code
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PayoutCardPaymentMethodSpecificOutput':
        super().from_dictionary(dictionary)
        if 'acceptance' in dictionary:
            if not isinstance(dictionary['acceptance'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['acceptance']))
            value = Acceptance()
            self.acceptance = value.from_dictionary(dictionary['acceptance'])
        if 'authorisationCode' in dictionary:
            self.authorisation_code = dictionary['authorisationCode']
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardEssentials()
            self.card = value.from_dictionary(dictionary['card'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
