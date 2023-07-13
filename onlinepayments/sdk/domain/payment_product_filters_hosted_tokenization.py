# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payment_product_filter_hosted_tokenization import PaymentProductFilterHostedTokenization


class PaymentProductFiltersHostedTokenization(DataObject):
    """
    | Contains the payment product ids that will be used for manipulating the payment products available for the payment to the customer.
    """

    __exclude = None
    __restrict_to = None

    @property
    def exclude(self) -> PaymentProductFilterHostedTokenization:
        """
        | Contains the payment product ids that should be excluded from the payment products available for the payment. Note that excluding a payment product will ensure exclusion, even if the payment product is also present in the restrictTo filter.

        Type: :class:`onlinepayments.sdk.domain.payment_product_filter_hosted_tokenization.PaymentProductFilterHostedTokenization`
        """
        return self.__exclude

    @exclude.setter
    def exclude(self, value: PaymentProductFilterHostedTokenization):
        self.__exclude = value

    @property
    def restrict_to(self) -> PaymentProductFilterHostedTokenization:
        """
        | Contains the payment product ids that should be excluded from the payment products available for the payment. Note that excluding a payment product will ensure exclusion, even if the payment product is also present in the restrictTo filter.

        Type: :class:`onlinepayments.sdk.domain.payment_product_filter_hosted_tokenization.PaymentProductFilterHostedTokenization`
        """
        return self.__restrict_to

    @restrict_to.setter
    def restrict_to(self, value: PaymentProductFilterHostedTokenization):
        self.__restrict_to = value

    def to_dictionary(self):
        dictionary = super(PaymentProductFiltersHostedTokenization, self).to_dictionary()
        if self.exclude is not None:
            dictionary['exclude'] = self.exclude.to_dictionary()
        if self.restrict_to is not None:
            dictionary['restrictTo'] = self.restrict_to.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFiltersHostedTokenization, self).from_dictionary(dictionary)
        if 'exclude' in dictionary:
            if not isinstance(dictionary['exclude'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['exclude']))
            value = PaymentProductFilterHostedTokenization()
            self.exclude = value.from_dictionary(dictionary['exclude'])
        if 'restrictTo' in dictionary:
            if not isinstance(dictionary['restrictTo'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['restrictTo']))
            value = PaymentProductFilterHostedTokenization()
            self.restrict_to = value.from_dictionary(dictionary['restrictTo'])
        return self
