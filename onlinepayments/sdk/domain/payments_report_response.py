#
# This file was automatically generated.
#
from .cursor_pagination_info import CursorPaginationInfo
from .data_object import DataObject
from .payment_summary import PaymentSummary


class PaymentsReportResponse(DataObject):

    __slots__ = (
        "__pagination",
        "__payments",
    )

    __pagination: CursorPaginationInfo | None
    __payments: list[PaymentSummary] | None

    def __init__(
        self,
        *,
        pagination: CursorPaginationInfo | None = None,
        payments: list[PaymentSummary] | None = None,
    ) -> None:
        self.pagination = pagination
        self.payments = payments

    @property
    def pagination(self) -> CursorPaginationInfo | None:
        """
        | Pagination information for cursor-based pagination

        Type: :class:`onlinepayments.sdk.domain.cursor_pagination_info.CursorPaginationInfo`
        """
        return self.__pagination

    @pagination.setter
    def pagination(self, value: CursorPaginationInfo | None) -> None:
        self.__pagination = value

    @property
    def payments(self) -> list[PaymentSummary] | None:
        """
        | List of payment summaries

        Type: list[:class:`onlinepayments.sdk.domain.payment_summary.PaymentSummary`]
        """
        return self.__payments

    @payments.setter
    def payments(self, value: list[PaymentSummary] | None) -> None:
        self.__payments = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.pagination is not None:
            dictionary['pagination'] = self.pagination.to_dictionary()
        if self.payments is not None:
            dictionary['payments'] = []
            for element in self.payments:
                if element is not None:
                    dictionary['payments'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentsReportResponse':
        super().from_dictionary(dictionary)
        if 'pagination' in dictionary:
            if not isinstance(dictionary['pagination'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['pagination']))
            value = CursorPaginationInfo()
            self.pagination = value.from_dictionary(dictionary['pagination'])
        if 'payments' in dictionary:
            if not isinstance(dictionary['payments'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['payments']))
            self.payments = []
            for element in dictionary['payments']:
                value = PaymentSummary()
                self.payments.append(value.from_dictionary(element))
        return self
