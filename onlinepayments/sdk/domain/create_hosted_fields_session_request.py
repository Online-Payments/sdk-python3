#
# This file was automatically generated.
#
from .data_object import DataObject
from .payment_product_filters_hosted_fields import PaymentProductFiltersHostedFields


class CreateHostedFieldsSessionRequest(DataObject):

    __slots__ = (
        "__locale",
        "__origin",
        "__payment_product_filters",
        "__tokens",
    )

    __locale: str | None
    __origin: str | None
    __payment_product_filters: PaymentProductFiltersHostedFields | None
    __tokens: list[str] | None

    def __init__(
        self,
        *,
        locale: str | None = None,
        origin: str | None = None,
        payment_product_filters: PaymentProductFiltersHostedFields | None = None,
        tokens: list[str] | None = None,
    ) -> None:
        self.locale = locale
        self.origin = origin
        self.payment_product_filters = payment_product_filters
        self.tokens = tokens

    @property
    def locale(self) -> str | None:
        """
        | Locale used in the GUI towards the consumer.

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: str | None) -> None:
        self.__locale = value

    @property
    def origin(self) -> str | None:
        """
        | merchant site's origin.

        Type: str
        """
        return self.__origin

    @origin.setter
    def origin(self, value: str | None) -> None:
        self.__origin = value

    @property
    def payment_product_filters(self) -> PaymentProductFiltersHostedFields | None:
        """
        | Optional object that limits which payment products are allowed in the session.

        Type: :class:`onlinepayments.sdk.domain.payment_product_filters_hosted_fields.PaymentProductFiltersHostedFields`
        """
        return self.__payment_product_filters

    @payment_product_filters.setter
    def payment_product_filters(self, value: PaymentProductFiltersHostedFields | None) -> None:
        self.__payment_product_filters = value

    @property
    def tokens(self) -> list[str] | None:
        """
        | These are your stored tokens that you can reuse during the session.

        Type: list[str]
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value: list[str] | None) -> None:
        self.__tokens = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.locale is not None:
            dictionary['locale'] = self.locale
        if self.origin is not None:
            dictionary['origin'] = self.origin
        if self.payment_product_filters is not None:
            dictionary['paymentProductFilters'] = self.payment_product_filters.to_dictionary()
        if self.tokens is not None:
            dictionary['tokens'] = []
            for element in self.tokens:
                if element is not None:
                    dictionary['tokens'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreateHostedFieldsSessionRequest':
        super().from_dictionary(dictionary)
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'origin' in dictionary:
            self.origin = dictionary['origin']
        if 'paymentProductFilters' in dictionary:
            if not isinstance(dictionary['paymentProductFilters'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProductFilters']))
            value = PaymentProductFiltersHostedFields()
            self.payment_product_filters = value.from_dictionary(dictionary['paymentProductFilters'])
        if 'tokens' in dictionary:
            if not isinstance(dictionary['tokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['tokens']))
            self.tokens = []
            for element in dictionary['tokens']:
                self.tokens.append(element)
        return self
