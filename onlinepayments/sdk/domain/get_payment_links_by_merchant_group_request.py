#
# This file was automatically generated.
#
from .data_object import DataObject
from .pagination import Pagination
from .payment_link_overview_filtering import PaymentLinkOverviewFiltering
from .payment_link_overview_sorting import PaymentLinkOverviewSorting


class GetPaymentLinksByMerchantGroupRequest(DataObject):

    __slots__ = (
        "__filtering",
        "__pagination",
        "__sorting",
    )

    __filtering: PaymentLinkOverviewFiltering | None
    __pagination: Pagination | None
    __sorting: PaymentLinkOverviewSorting | None

    def __init__(
        self,
        *,
        filtering: PaymentLinkOverviewFiltering | None = None,
        pagination: Pagination | None = None,
        sorting: PaymentLinkOverviewSorting | None = None,
    ) -> None:
        self.filtering = filtering
        self.pagination = pagination
        self.sorting = sorting

    @property
    def filtering(self) -> PaymentLinkOverviewFiltering | None:
        """
        | Object containing the filter criteria for retrieving payment links.

        Type: :class:`onlinepayments.sdk.domain.payment_link_overview_filtering.PaymentLinkOverviewFiltering`
        """
        return self.__filtering

    @filtering.setter
    def filtering(self, value: PaymentLinkOverviewFiltering | None) -> None:
        self.__filtering = value

    @property
    def pagination(self) -> Pagination | None:
        """
        | Object containing pagination parameters.

        Type: :class:`onlinepayments.sdk.domain.pagination.Pagination`
        """
        return self.__pagination

    @pagination.setter
    def pagination(self, value: Pagination | None) -> None:
        self.__pagination = value

    @property
    def sorting(self) -> PaymentLinkOverviewSorting | None:
        """
        | Object containing sorting parameters.

        Type: :class:`onlinepayments.sdk.domain.payment_link_overview_sorting.PaymentLinkOverviewSorting`
        """
        return self.__sorting

    @sorting.setter
    def sorting(self, value: PaymentLinkOverviewSorting | None) -> None:
        self.__sorting = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.filtering is not None:
            dictionary['filtering'] = self.filtering.to_dictionary()
        if self.pagination is not None:
            dictionary['pagination'] = self.pagination.to_dictionary()
        if self.sorting is not None:
            dictionary['sorting'] = self.sorting.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetPaymentLinksByMerchantGroupRequest':
        super().from_dictionary(dictionary)
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
