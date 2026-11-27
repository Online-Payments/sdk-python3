#
# This file was automatically generated.
#
from .data_object import DataObject
from .three_ds_input_data import ThreeDsInputData


class DpaTransactionOptions(DataObject):

    __slots__ = (
        "__three_ds_input_data",
    )

    __three_ds_input_data: ThreeDsInputData | None

    def __init__(
        self,
        *,
        three_ds_input_data: ThreeDsInputData | None = None,
    ) -> None:
        self.three_ds_input_data = three_ds_input_data

    @property
    def three_ds_input_data(self) -> ThreeDsInputData | None:
        """
        | Merchant’s 3DS input data. Conditionality: Must be supplied if 3DS is to be performed by SRC System.

        Type: :class:`onlinepayments.sdk.domain.three_ds_input_data.ThreeDsInputData`
        """
        return self.__three_ds_input_data

    @three_ds_input_data.setter
    def three_ds_input_data(self, value: ThreeDsInputData | None) -> None:
        self.__three_ds_input_data = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.three_ds_input_data is not None:
            dictionary['threeDsInputData'] = self.three_ds_input_data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DpaTransactionOptions':
        super().from_dictionary(dictionary)
        if 'threeDsInputData' in dictionary:
            if not isinstance(dictionary['threeDsInputData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDsInputData']))
            value = ThreeDsInputData()
            self.three_ds_input_data = value.from_dictionary(dictionary['threeDsInputData'])
        return self
