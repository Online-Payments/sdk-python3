#
# This file was automatically generated.
#
from .card_without_cvv import CardWithoutCvv
from .data_object import DataObject


class CompletePaymentCardPaymentMethodSpecificInput(DataObject):

    __slots__ = (
        "__card",
    )

    __card: CardWithoutCvv | None

    def __init__(
        self,
        *,
        card: CardWithoutCvv | None = None,
    ) -> None:
        self.card = card

    @property
    def card(self) -> CardWithoutCvv | None:
        """
        Type: :class:`onlinepayments.sdk.domain.card_without_cvv.CardWithoutCvv`
        """
        return self.__card

    @card.setter
    def card(self, value: CardWithoutCvv | None) -> None:
        self.__card = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CompletePaymentCardPaymentMethodSpecificInput':
        super().from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardWithoutCvv()
            self.card = value.from_dictionary(dictionary['card'])
        return self
