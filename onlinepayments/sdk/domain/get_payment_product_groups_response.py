# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payment_product_group import PaymentProductGroup


class GetPaymentProductGroupsResponse(DataObject):
    """
    | The response contains an array of payment product groups that match the filters supplied in the request.
    """

    __payment_product_groups = None

    @property
    def payment_product_groups(self) -> List[PaymentProductGroup]:
        """
        | Array containing payment product groups and their characteristics

        Type: list[:class:`onlinepayments.sdk.domain.payment_product_group.PaymentProductGroup`]
        """
        return self.__payment_product_groups

    @payment_product_groups.setter
    def payment_product_groups(self, value: List[PaymentProductGroup]):
        self.__payment_product_groups = value

    def to_dictionary(self):
        dictionary = super(GetPaymentProductGroupsResponse, self).to_dictionary()
        if self.payment_product_groups is not None:
            dictionary['paymentProductGroups'] = []
            for element in self.payment_product_groups:
                if element is not None:
                    dictionary['paymentProductGroups'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary):
        super(GetPaymentProductGroupsResponse, self).from_dictionary(dictionary)
        if 'paymentProductGroups' in dictionary:
            if not isinstance(dictionary['paymentProductGroups'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['paymentProductGroups']))
            self.payment_product_groups = []
            for element in dictionary['paymentProductGroups']:
                value = PaymentProductGroup()
                self.payment_product_groups.append(value.from_dictionary(element))
        return self
