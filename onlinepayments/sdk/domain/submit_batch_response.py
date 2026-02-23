# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class SubmitBatchResponse(DataObject):

    __merchant_batch_reference: Optional[str] = None
    __total_count: Optional[int] = None

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
    def total_count(self) -> Optional[int]:
        """
        | The total number of batch items that were included in the submitted batch.

        Type: int
        """
        return self.__total_count

    @total_count.setter
    def total_count(self, value: Optional[int]) -> None:
        self.__total_count = value

    def to_dictionary(self) -> dict:
        dictionary = super(SubmitBatchResponse, self).to_dictionary()
        if self.merchant_batch_reference is not None:
            dictionary['merchantBatchReference'] = self.merchant_batch_reference
        if self.total_count is not None:
            dictionary['totalCount'] = self.total_count
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SubmitBatchResponse':
        super(SubmitBatchResponse, self).from_dictionary(dictionary)
        if 'merchantBatchReference' in dictionary:
            self.merchant_batch_reference = dictionary['merchantBatchReference']
        if 'totalCount' in dictionary:
            self.total_count = dictionary['totalCount']
        return self
