# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.order_status_output import OrderStatusOutput
from onlinepayments.sdk.domain.refund_output import RefundOutput


class RefundResponse(DataObject):
    """
    | This object has the numeric representation of the current refund status, timestamp of last status change and performable action on the current refund resource. In case of a rejected refund, detailed error information is listed.
    """

    __id = None
    __refund_output = None
    __status = None
    __status_output = None

    @property
    def id(self) -> str:
        """
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value

    @property
    def refund_output(self) -> RefundOutput:
        """
        | Object containing refund details

        Type: :class:`onlinepayments.sdk.domain.refund_output.RefundOutput`
        """
        return self.__refund_output

    @refund_output.setter
    def refund_output(self, value: RefundOutput):
        self.__refund_output = value

    @property
    def status(self) -> str:
        """
        | Current high-level status of the payment in a human-readable form.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: str):
        self.__status = value

    @property
    def status_output(self) -> OrderStatusOutput:
        """
        Type: :class:`onlinepayments.sdk.domain.order_status_output.OrderStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value: OrderStatusOutput):
        self.__status_output = value

    def to_dictionary(self):
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

    def from_dictionary(self, dictionary):
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
