# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .split_payment_product_filter import SplitPaymentProductFilter


class SplitPaymentProductFiltersHostedCheckout(DataObject):

    __exclude: Optional[SplitPaymentProductFilter] = None
    __restrict_to: Optional[SplitPaymentProductFilter] = None

    @property
    def exclude(self) -> Optional[SplitPaymentProductFilter]:
        """
        | The payment product IDs to be excluded or restricted for the payment products available for the following payments in a split payment. Note that you can add exclusions on top of the 'restrictTo' filter.

        Type: :class:`onlinepayments.sdk.domain.split_payment_product_filter.SplitPaymentProductFilter`
        """
        return self.__exclude

    @exclude.setter
    def exclude(self, value: Optional[SplitPaymentProductFilter]) -> None:
        self.__exclude = value

    @property
    def restrict_to(self) -> Optional[SplitPaymentProductFilter]:
        """
        | The payment product IDs to be excluded or restricted for the payment products available for the following payments in a split payment. Note that you can add exclusions on top of the 'restrictTo' filter.

        Type: :class:`onlinepayments.sdk.domain.split_payment_product_filter.SplitPaymentProductFilter`
        """
        return self.__restrict_to

    @restrict_to.setter
    def restrict_to(self, value: Optional[SplitPaymentProductFilter]) -> None:
        self.__restrict_to = value

    def to_dictionary(self) -> dict:
        dictionary = super(SplitPaymentProductFiltersHostedCheckout, self).to_dictionary()
        if self.exclude is not None:
            dictionary['exclude'] = self.exclude.to_dictionary()
        if self.restrict_to is not None:
            dictionary['restrictTo'] = self.restrict_to.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SplitPaymentProductFiltersHostedCheckout':
        super(SplitPaymentProductFiltersHostedCheckout, self).from_dictionary(dictionary)
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
