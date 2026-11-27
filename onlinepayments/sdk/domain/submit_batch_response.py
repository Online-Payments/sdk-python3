#
# This file was automatically generated.
#
from .data_object import DataObject


class SubmitBatchResponse(DataObject):

    __slots__ = (
        "__merchant_batch_reference",
        "__total_count",
    )

    __merchant_batch_reference: str | None
    __total_count: int | None

    def __init__(
        self,
        *,
        merchant_batch_reference: str | None = None,
        total_count: int | None = None,
    ) -> None:
        self.merchant_batch_reference = merchant_batch_reference
        self.total_count = total_count

    @property
    def merchant_batch_reference(self) -> str | None:
        """
        | Unique batch reference submitted by the merchant.

        Type: str
        """
        return self.__merchant_batch_reference

    @merchant_batch_reference.setter
    def merchant_batch_reference(self, value: str | None) -> None:
        self.__merchant_batch_reference = value

    @property
    def total_count(self) -> int | None:
        """
        | The total number of batch items that were included in the submitted batch.

        Type: int
        """
        return self.__total_count

    @total_count.setter
    def total_count(self, value: int | None) -> None:
        self.__total_count = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.merchant_batch_reference is not None:
            dictionary['merchantBatchReference'] = self.merchant_batch_reference
        if self.total_count is not None:
            dictionary['totalCount'] = self.total_count
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SubmitBatchResponse':
        super().from_dictionary(dictionary)
        if 'merchantBatchReference' in dictionary:
            self.merchant_batch_reference = dictionary['merchantBatchReference']
        if 'totalCount' in dictionary:
            self.total_count = dictionary['totalCount']
        return self
