#
# This file was automatically generated.
#
from .data_object import DataObject
from .split_payment_product_filter import SplitPaymentProductFilter


class SplitPaymentProductFiltersHostedCheckout(DataObject):

    __slots__ = (
        "__exclude",
        "__restrict_to",
    )

    __exclude: SplitPaymentProductFilter | None
    __restrict_to: SplitPaymentProductFilter | None

    def __init__(
        self,
        *,
        exclude: SplitPaymentProductFilter | None = None,
        restrict_to: SplitPaymentProductFilter | None = None,
    ) -> None:
        self.exclude = exclude
        self.restrict_to = restrict_to

    @property
    def exclude(self) -> SplitPaymentProductFilter | None:
        """
        | The payment product IDs to be excluded or restricted for the payment products available for the following payments in a split payment. Note that you can add exclusions on top of the 'restrictTo' filter.

        Type: :class:`onlinepayments.sdk.domain.split_payment_product_filter.SplitPaymentProductFilter`
        """
        return self.__exclude

    @exclude.setter
    def exclude(self, value: SplitPaymentProductFilter | None) -> None:
        self.__exclude = value

    @property
    def restrict_to(self) -> SplitPaymentProductFilter | None:
        """
        | The payment product IDs to be excluded or restricted for the payment products available for the following payments in a split payment. Note that you can add exclusions on top of the 'restrictTo' filter.

        Type: :class:`onlinepayments.sdk.domain.split_payment_product_filter.SplitPaymentProductFilter`
        """
        return self.__restrict_to

    @restrict_to.setter
    def restrict_to(self, value: SplitPaymentProductFilter | None) -> None:
        self.__restrict_to = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.exclude is not None:
            dictionary['exclude'] = self.exclude.to_dictionary()
        if self.restrict_to is not None:
            dictionary['restrictTo'] = self.restrict_to.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SplitPaymentProductFiltersHostedCheckout':
        super().from_dictionary(dictionary)
        if 'exclude' in dictionary:
            if not isinstance(dictionary['exclude'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['exclude']))
            value = SplitPaymentProductFilter()
            self.exclude = value.from_dictionary(dictionary['exclude'])
        if 'restrictTo' in dictionary:
            if not isinstance(dictionary['restrictTo'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['restrictTo']))
            value = SplitPaymentProductFilter()
            self.restrict_to = value.from_dictionary(dictionary['restrictTo'])
        return self
