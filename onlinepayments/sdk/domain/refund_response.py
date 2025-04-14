# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .order_status_output import OrderStatusOutput
from .refund_output import RefundOutput


class RefundResponse(DataObject):

    __id: Optional[str] = None
    __refund_output: Optional[RefundOutput] = None
    __status: Optional[str] = None
    __status_output: Optional[OrderStatusOutput] = None

    @property
    def id(self) -> Optional[str]:
        """
        | Our unique payment transaction identifier

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: Optional[str]) -> None:
        self.__id = value

    @property
    def refund_output(self) -> Optional[RefundOutput]:
        """
        | Object containing refund details

        Type: :class:`onlinepayments.sdk.domain.refund_output.RefundOutput`
        """
        return self.__refund_output

    @refund_output.setter
    def refund_output(self, value: Optional[RefundOutput]) -> None:
        self.__refund_output = value

    @property
    def status(self) -> Optional[str]:
        """
        | Current high-level status of the payment in a human-readable form.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: Optional[str]) -> None:
        self.__status = value

    @property
    def status_output(self) -> Optional[OrderStatusOutput]:
        """
        Type: :class:`onlinepayments.sdk.domain.order_status_output.OrderStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value: Optional[OrderStatusOutput]) -> None:
        self.__status_output = value

    def to_dictionary(self) -> dict:
        dictionary = super(RefundResponse, self).to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.refund_output is not None:
            dictionary['refundOutput'] = self.refund_output.to_dictionary()
        if self.status is not None:
            dictionary['status'] = self.status
        if self.status_output is not None:
            dictionary['statusOutput'] = self.status_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundResponse':
        super(RefundResponse, self).from_dictionary(dictionary)
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'refundOutput' in dictionary:
            if not isinstance(dictionary['refundOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['refundOutput']))
            value = RefundOutput()
            self.refund_output = value.from_dictionary(dictionary['refundOutput'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = OrderStatusOutput()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self
