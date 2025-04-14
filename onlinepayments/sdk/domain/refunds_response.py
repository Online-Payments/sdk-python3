# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject
from .refund_response import RefundResponse


class RefundsResponse(DataObject):

    __refunds: Optional[List[RefundResponse]] = None

    @property
    def refunds(self) -> Optional[List[RefundResponse]]:
        """
        | The list of all refunds performed on the requested payment.

        Type: list[:class:`onlinepayments.sdk.domain.refund_response.RefundResponse`]
        """
        return self.__refunds

    @refunds.setter
    def refunds(self, value: Optional[List[RefundResponse]]) -> None:
        self.__refunds = value

    def to_dictionary(self) -> dict:
        dictionary = super(RefundsResponse, self).to_dictionary()
        if self.refunds is not None:
            dictionary['refunds'] = []
            for element in self.refunds:
                if element is not None:
                    dictionary['refunds'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundsResponse':
        super(RefundsResponse, self).from_dictionary(dictionary)
        if 'refunds' in dictionary:
            if not isinstance(dictionary['refunds'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['refunds']))
            self.refunds = []
            for element in dictionary['refunds']:
                value = RefundResponse()
                self.refunds.append(value.from_dictionary(element))
        return self
