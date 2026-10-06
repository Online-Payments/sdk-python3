# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .pagination import Pagination
from .payment_link_overview_filtering import PaymentLinkOverviewFiltering
from .payment_link_overview_sorting import PaymentLinkOverviewSorting


class GetPaymentLinksByMerchantGroupRequest(DataObject):

    __filtering: Optional[PaymentLinkOverviewFiltering] = None
    __pagination: Optional[Pagination] = None
    __sorting: Optional[PaymentLinkOverviewSorting] = None

    @property
    def filtering(self) -> Optional[PaymentLinkOverviewFiltering]:
        """
        | Object containing the filter criteria for retrieving payment links.

        Type: :class:`onlinepayments.sdk.domain.payment_link_overview_filtering.PaymentLinkOverviewFiltering`
        """
        return self.__filtering

    @filtering.setter
    def filtering(self, value: Optional[PaymentLinkOverviewFiltering]) -> None:
        self.__filtering = value

    @property
    def pagination(self) -> Optional[Pagination]:
        """
        | Object containing pagination parameters.

        Type: :class:`onlinepayments.sdk.domain.pagination.Pagination`
        """
        return self.__pagination

    @pagination.setter
    def pagination(self, value: Optional[Pagination]) -> None:
        self.__pagination = value

    @property
    def sorting(self) -> Optional[PaymentLinkOverviewSorting]:
        """
        | Object containing sorting parameters.

        Type: :class:`onlinepayments.sdk.domain.payment_link_overview_sorting.PaymentLinkOverviewSorting`
        """
        return self.__sorting

    @sorting.setter
    def sorting(self, value: Optional[PaymentLinkOverviewSorting]) -> None:
        self.__sorting = value

    def to_dictionary(self) -> dict:
        dictionary = super(GetPaymentLinksByMerchantGroupRequest, self).to_dictionary()
        if self.filtering is not None:
            dictionary['filtering'] = self.filtering.to_dictionary()
        if self.pagination is not None:
            dictionary['pagination'] = self.pagination.to_dictionary()
        if self.sorting is not None:
            dictionary['sorting'] = self.sorting.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetPaymentLinksByMerchantGroupRequest':
        super(GetPaymentLinksByMerchantGroupRequest, self).from_dictionary(dictionary)
        if 'filtering' in dictionary:
            if not isinstance(dictionary['filtering'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['filtering']))
            value = PaymentLinkOverviewFiltering()
            self.filtering = value.from_dictionary(dictionary['filtering'])
        if 'pagination' in dictionary:
            if not isinstance(dictionary['pagination'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['pagination']))
            value = Pagination()
            self.pagination = value.from_dictionary(dictionary['pagination'])
        if 'sorting' in dictionary:
            if not isinstance(dictionary['sorting'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['sorting']))
            value = PaymentLinkOverviewSorting()
            self.sorting = value.from_dictionary(dictionary['sorting'])
        return self
