# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class GetBatchStatusResponse(DataObject):

    __item_count: Optional[int] = None
    __merchant_batch_reference: Optional[str] = None
    __operation_type: Optional[str] = None
    __status: Optional[str] = None

    @property
    def item_count(self) -> Optional[int]:
        """
        | The total number of items included in the batch submission.

        Type: int
        """
        return self.__item_count

    @item_count.setter
    def item_count(self, value: Optional[int]) -> None:
        self.__item_count = value

    @property
    def merchant_batch_reference(self) -> Optional[str]:
        """
        | Unique batch reference submitted by the merchant.

        Type: str
        """
        return self.__merchant_batch_reference

    @merchant_batch_reference.setter
    def merchant_batch_reference(self, value: Optional[str]) -> None:
        self.__merchant_batch_reference = value

    @property
    def operation_type(self) -> Optional[str]:
        """
        | The specific operation type being requested for the batch.

        Type: str
        """
        return self.__operation_type

    @operation_type.setter
    def operation_type(self, value: Optional[str]) -> None:
        self.__operation_type = value

    @property
    def status(self) -> Optional[str]:
        """
        | The status of the batch.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: Optional[str]) -> None:
        self.__status = value

    def to_dictionary(self) -> dict:
        dictionary = super(GetBatchStatusResponse, self).to_dictionary()
        if self.item_count is not None:
            dictionary['itemCount'] = self.item_count
        if self.merchant_batch_reference is not None:
            dictionary['merchantBatchReference'] = self.merchant_batch_reference
        if self.operation_type is not None:
            dictionary['operationType'] = self.operation_type
        if self.status is not None:
            dictionary['status'] = self.status
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetBatchStatusResponse':
        super(GetBatchStatusResponse, self).from_dictionary(dictionary)
        if 'itemCount' in dictionary:
            self.item_count = dictionary['itemCount']
        if 'merchantBatchReference' in dictionary:
            self.merchant_batch_reference = dictionary['merchantBatchReference']
        if 'operationType' in dictionary:
            self.operation_type = dictionary['operationType']
        if 'status' in dictionary:
            self.status = dictionary['status']
        return self
