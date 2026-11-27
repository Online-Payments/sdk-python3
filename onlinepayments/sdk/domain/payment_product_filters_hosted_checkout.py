#
# This file was automatically generated.
#
from .data_object import DataObject
from .payment_product_filter import PaymentProductFilter


class PaymentProductFiltersHostedCheckout(DataObject):

    __slots__ = (
        "__exclude",
        "__restrict_to",
    )

    __exclude: PaymentProductFilter | None
    __restrict_to: PaymentProductFilter | None

    def __init__(
        self,
        *,
        exclude: PaymentProductFilter | None = None,
        restrict_to: PaymentProductFilter | None = None,
    ) -> None:
        self.exclude = exclude
        self.restrict_to = restrict_to

    @property
    def exclude(self) -> PaymentProductFilter | None:
        """
        | The payment product ids to be be excluded or restricted to from the payment products available for the payment. Note that you can add exclusions on top of the 'restrictTo' filter.

        Type: :class:`onlinepayments.sdk.domain.payment_product_filter.PaymentProductFilter`
        """
        return self.__exclude

    @exclude.setter
    def exclude(self, value: PaymentProductFilter | None) -> None:
        self.__exclude = value

    @property
    def restrict_to(self) -> PaymentProductFilter | None:
        """
        | The payment product ids to be be excluded or restricted to from the payment products available for the payment. Note that you can add exclusions on top of the 'restrictTo' filter.

        Type: :class:`onlinepayments.sdk.domain.payment_product_filter.PaymentProductFilter`
        """
        return self.__restrict_to

    @restrict_to.setter
    def restrict_to(self, value: PaymentProductFilter | None) -> None:
        self.__restrict_to = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.exclude is not None:
            dictionary['exclude'] = self.exclude.to_dictionary()
        if self.restrict_to is not None:
            dictionary['restrictTo'] = self.restrict_to.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductFiltersHostedCheckout':
        super().from_dictionary(dictionary)
        if 'exclude' in dictionary:
            if not isinstance(dictionary['exclude'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['exclude']))
            value = PaymentProductFilter()
            self.exclude = value.from_dictionary(dictionary['exclude'])
        if 'restrictTo' in dictionary:
            if not isinstance(dictionary['restrictTo'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['restrictTo']))
            value = PaymentProductFilter()
            self.restrict_to = value.from_dictionary(dictionary['restrictTo'])
        return self
