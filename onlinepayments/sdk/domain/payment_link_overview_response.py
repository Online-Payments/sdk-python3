#
# This file was automatically generated.
#
from .data_object import DataObject
from .pagination import Pagination
from .payment_link_overview_entry import PaymentLinkOverviewEntry


class PaymentLinkOverviewResponse(DataObject):

    __slots__ = (
        "__pagination",
        "__payment_link_overview_entries",
        "__total",
    )

    __pagination: Pagination | None
    __payment_link_overview_entries: list[PaymentLinkOverviewEntry] | None
    __total: int | None

    def __init__(
        self,
        *,
        pagination: Pagination | None = None,
        payment_link_overview_entries: list[PaymentLinkOverviewEntry] | None = None,
        total: int | None = None,
    ) -> None:
        self.pagination = pagination
        self.payment_link_overview_entries = payment_link_overview_entries
        self.total = total

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
    def payment_link_overview_entries(self) -> list[PaymentLinkOverviewEntry] | None:
        """
        | Array of payment link overview entries matching the specified filters.

        Type: list[:class:`onlinepayments.sdk.domain.payment_link_overview_entry.PaymentLinkOverviewEntry`]
        """
        return self.__payment_link_overview_entries

    @payment_link_overview_entries.setter
    def payment_link_overview_entries(self, value: list[PaymentLinkOverviewEntry] | None) -> None:
        self.__payment_link_overview_entries = value

    @property
    def total(self) -> int | None:
        """
        | Total number of payment links matching the request filters across all pages.

        Type: int
        """
        return self.__total

    @total.setter
    def total(self, value: int | None) -> None:
        self.__total = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
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
        super().from_dictionary(dictionary)
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
