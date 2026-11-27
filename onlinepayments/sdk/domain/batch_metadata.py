#
# This file was automatically generated.
#
from .data_object import DataObject


class BatchMetadata(DataObject):

    __slots__ = (
        "__item_count",
        "__merchant_batch_reference",
        "__operation_type",
    )

    __item_count: int | None
    __merchant_batch_reference: str | None
    __operation_type: str | None

    def __init__(
        self,
        *,
        item_count: int | None = None,
        merchant_batch_reference: str | None = None,
        operation_type: str | None = None,
    ) -> None:
        self.item_count = item_count
        self.merchant_batch_reference = merchant_batch_reference
        self.operation_type = operation_type

    @property
    def item_count(self) -> int | None:
        """
        | The total number of items included in the batch submission.

        Type: int
        """
        return self.__item_count

    @item_count.setter
    def item_count(self, value: int | None) -> None:
        self.__item_count = value

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
    def operation_type(self) -> str | None:
        """
        | The specific operation type being requested for the batch.

        Type: str
        """
        return self.__operation_type

    @operation_type.setter
    def operation_type(self, value: str | None) -> None:
        self.__operation_type = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.item_count is not None:
            dictionary['itemCount'] = self.item_count
        if self.merchant_batch_reference is not None:
            dictionary['merchantBatchReference'] = self.merchant_batch_reference
        if self.operation_type is not None:
            dictionary['operationType'] = self.operation_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'BatchMetadata':
        super().from_dictionary(dictionary)
        if 'itemCount' in dictionary:
            self.item_count = dictionary['itemCount']
        if 'merchantBatchReference' in dictionary:
            self.merchant_batch_reference = dictionary['merchantBatchReference']
        if 'operationType' in dictionary:
            self.operation_type = dictionary['operationType']
        return self
