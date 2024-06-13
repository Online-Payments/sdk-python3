# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payment_product_filter import PaymentProductFilter


class PaymentProductFiltersHostedCheckout(DataObject):
    """
    | Contains the payment product ids and payment product groups that will be used for manipulating the payment products available for the payment to the customer.
    """

    __exclude = None
    __restrict_to = None

    @property
    def exclude(self) -> PaymentProductFilter:
        """
        | The payment product ids to be be excluded or restricted to from the payment products available for the payment. Note that you can add exclusions on top of the 'restrictTo' filter.

        Type: :class:`onlinepayments.sdk.domain.payment_product_filter.PaymentProductFilter`
        """
        return self.__exclude

    @exclude.setter
    def exclude(self, value: PaymentProductFilter):
        self.__exclude = value

    @property
    def restrict_to(self) -> PaymentProductFilter:
        """
        | The payment product ids to be be excluded or restricted to from the payment products available for the payment. Note that you can add exclusions on top of the 'restrictTo' filter.

        Type: :class:`onlinepayments.sdk.domain.payment_product_filter.PaymentProductFilter`
        """
        return self.__restrict_to

    @restrict_to.setter
    def restrict_to(self, value: PaymentProductFilter):
        self.__restrict_to = value

    def to_dictionary(self):
        dictionary = super(PaymentProductFiltersHostedCheckout, self).to_dictionary()
        if self.exclude is not None:
            dictionary['exclude'] = self.exclude.to_dictionary()
        if self.restrict_to is not None:
            dictionary['restrictTo'] = self.restrict_to.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFiltersHostedCheckout, self).from_dictionary(dictionary)
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
