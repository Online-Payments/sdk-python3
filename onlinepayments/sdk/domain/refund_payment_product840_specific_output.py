# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .refund_payment_product840_customer_account import RefundPaymentProduct840CustomerAccount


class RefundPaymentProduct840SpecificOutput(DataObject):

    __customer_account: Optional[RefundPaymentProduct840CustomerAccount] = None

    @property
    def customer_account(self) -> Optional[RefundPaymentProduct840CustomerAccount]:
        """
        Type: :class:`onlinepayments.sdk.domain.refund_payment_product840_customer_account.RefundPaymentProduct840CustomerAccount`
        """
        return self.__customer_account

    @customer_account.setter
    def customer_account(self, value: Optional[RefundPaymentProduct840CustomerAccount]) -> None:
        self.__customer_account = value

    def to_dictionary(self) -> dict:
        dictionary = super(RefundPaymentProduct840SpecificOutput, self).to_dictionary()
        if self.customer_account is not None:
            dictionary['customerAccount'] = self.customer_account.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundPaymentProduct840SpecificOutput':
        super(RefundPaymentProduct840SpecificOutput, self).from_dictionary(dictionary)
        if 'customerAccount' in dictionary:
            if not isinstance(dictionary['customerAccount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerAccount']))
            value = RefundPaymentProduct840CustomerAccount()
            self.customer_account = value.from_dictionary(dictionary['customerAccount'])
        return self
