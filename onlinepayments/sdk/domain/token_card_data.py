#
# This file was automatically generated.
#
from .card_bin_details import CardBinDetails
from .card_without_cvv import CardWithoutCvv
from .data_object import DataObject


class TokenCardData(DataObject):

    __slots__ = (
        "__card_bin_details",
        "__card_without_cvv",
        "__cobrand_selection_indicator",
    )

    __card_bin_details: CardBinDetails | None
    __card_without_cvv: CardWithoutCvv | None
    __cobrand_selection_indicator: str | None

    def __init__(
        self,
        *,
        card_bin_details: CardBinDetails | None = None,
        card_without_cvv: CardWithoutCvv | None = None,
        cobrand_selection_indicator: str | None = None,
    ) -> None:
        self.card_bin_details = card_bin_details
        self.card_without_cvv = card_without_cvv
        self.cobrand_selection_indicator = cobrand_selection_indicator

    @property
    def card_bin_details(self) -> CardBinDetails | None:
        """
        | Card BIN details

        Type: :class:`onlinepayments.sdk.domain.card_bin_details.CardBinDetails`
        """
        return self.__card_bin_details

    @card_bin_details.setter
    def card_bin_details(self, value: CardBinDetails | None) -> None:
        self.__card_bin_details = value

    @property
    def card_without_cvv(self) -> CardWithoutCvv | None:
        """
        Type: :class:`onlinepayments.sdk.domain.card_without_cvv.CardWithoutCvv`
        """
        return self.__card_without_cvv

    @card_without_cvv.setter
    def card_without_cvv(self, value: CardWithoutCvv | None) -> None:
        self.__card_without_cvv = value

    @property
    def cobrand_selection_indicator(self) -> str | None:
        """
        | For cobranded cards, this field indicates the brand selection method:
        
        * default - The holder implicitly accepted the default brand.
        * alternative - The holder explicitly selected an alternative brand.
        * notApplicable - The card is not cobranded.

        Type: str
        """
        return self.__cobrand_selection_indicator

    @cobrand_selection_indicator.setter
    def cobrand_selection_indicator(self, value: str | None) -> None:
        self.__cobrand_selection_indicator = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.card_bin_details is not None:
            dictionary['cardBinDetails'] = self.card_bin_details.to_dictionary()
        if self.card_without_cvv is not None:
            dictionary['cardWithoutCvv'] = self.card_without_cvv.to_dictionary()
        if self.cobrand_selection_indicator is not None:
            dictionary['cobrandSelectionIndicator'] = self.cobrand_selection_indicator
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'TokenCardData':
        super().from_dictionary(dictionary)
        if 'cardBinDetails' in dictionary:
            if not isinstance(dictionary['cardBinDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardBinDetails']))
            value = CardBinDetails()
            self.card_bin_details = value.from_dictionary(dictionary['cardBinDetails'])
        if 'cardWithoutCvv' in dictionary:
            if not isinstance(dictionary['cardWithoutCvv'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardWithoutCvv']))
            value = CardWithoutCvv()
            self.card_without_cvv = value.from_dictionary(dictionary['cardWithoutCvv'])
        if 'cobrandSelectionIndicator' in dictionary:
            self.cobrand_selection_indicator = dictionary['cobrandSelectionIndicator']
        return self
