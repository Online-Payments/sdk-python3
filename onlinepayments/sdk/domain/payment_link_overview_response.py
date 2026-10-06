# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject
from .pagination import Pagination
from .payment_link_overview_entry import PaymentLinkOverviewEntry


class PaymentLinkOverviewResponse(DataObject):

    __pagination: Optional[Pagination] = None
    __payment_link_overview_entries: Optional[List[PaymentLinkOverviewEntry]] = None
    __total: Optional[int] = None

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
    def payment_link_overview_entries(self) -> Optional[List[PaymentLinkOverviewEntry]]:
        """
        | Array of payment link overview entries matching the specified filters.

        Type: list[:class:`onlinepayments.sdk.domain.payment_link_overview_entry.PaymentLinkOverviewEntry`]
        """
        return self.__payment_link_overview_entries

    @payment_link_overview_entries.setter
    def payment_link_overview_entries(self, value: Optional[List[PaymentLinkOverviewEntry]]) -> None:
        self.__payment_link_overview_entries = value

    @property
    def total(self) -> Optional[int]:
        """
        | Total number of payment links matching the request filters across all pages.

        Type: int
        """
        return self.__total

    @total.setter
    def total(self, value: Optional[int]) -> None:
        self.__total = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentLinkOverviewResponse, self).to_dictionary()
        if self.pagination is not None:
            dictionary['pagination'] = self.pagination.to_dictionary()
        if self.payment_link_overview_entries is not None:
            dictionary['paymentLinkOverviewEntries'] = []
            for element in self.payment_link_overview_entries:
                if element is not None:
                    dictionary['paymentLinkOverviewEntries'].append(element.to_dictionary())
        if self.total is not None:
            dictionary['total'] = self.total
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentLinkOverviewResponse':
        super(PaymentLinkOverviewResponse, self).from_dictionary(dictionary)
        if 'pagination' in dictionary:
            if not isinstance(dictionary['pagination'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['pagination']))
            value = Pagination()
            self.pagination = value.from_dictionary(dictionary['pagination'])
        if 'paymentLinkOverviewEntries' in dictionary:
            if not isinstance(dictionary['paymentLinkOverviewEntries'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['paymentLinkOverviewEntries']))
            self.payment_link_overview_entries = []
            for element in dictionary['paymentLinkOverviewEntries']:
                value = PaymentLinkOverviewEntry()
                self.payment_link_overview_entries.append(value.from_dictionary(element))
        if 'total' in dictionary:
            self.total = dictionary['total']
        return self
