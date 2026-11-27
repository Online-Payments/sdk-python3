#
# This file was automatically generated.
#
from .data_object import DataObject
from .refund_response import RefundResponse


class RefundsResponse(DataObject):

    __slots__ = (
        "__refunds",
    )

    __refunds: list[RefundResponse] | None

    def __init__(
        self,
        *,
        refunds: list[RefundResponse] | None = None,
    ) -> None:
        self.refunds = refunds

    @property
    def refunds(self) -> list[RefundResponse] | None:
        """
        | The list of all refunds performed on the requested payment.

        Type: list[:class:`onlinepayments.sdk.domain.refund_response.RefundResponse`]
        """
        return self.__refunds

    @refunds.setter
    def refunds(self, value: list[RefundResponse] | None) -> None:
        self.__refunds = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.refunds is not None:
            dictionary['refunds'] = []
            for element in self.refunds:
                if element is not None:
                    dictionary['refunds'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundsResponse':
        super().from_dictionary(dictionary)
        if 'refunds' in dictionary:
            if not isinstance(dictionary['refunds'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['refunds']))
            self.refunds = []
            for element in dictionary['refunds']:
                value = RefundResponse()
                self.refunds.append(value.from_dictionary(element))
        return self
