# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .three_ds_input_data import ThreeDsInputData


class DpaTransactionOptions(DataObject):

    __three_ds_input_data: Optional[ThreeDsInputData] = None

    @property
    def three_ds_input_data(self) -> Optional[ThreeDsInputData]:
        """
        | Merchant’s 3DS input data. Conditionality: Must be supplied if 3DS is to be performed by SRC System.

        Type: :class:`onlinepayments.sdk.domain.three_ds_input_data.ThreeDsInputData`
        """
        return self.__three_ds_input_data

    @three_ds_input_data.setter
    def three_ds_input_data(self, value: Optional[ThreeDsInputData]) -> None:
        self.__three_ds_input_data = value

    def to_dictionary(self) -> dict:
        dictionary = super(DpaTransactionOptions, self).to_dictionary()
        if self.three_ds_input_data is not None:
            dictionary['threeDsInputData'] = self.three_ds_input_data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DpaTransactionOptions':
        super(DpaTransactionOptions, self).from_dictionary(dictionary)
        if 'threeDsInputData' in dictionary:
            if not isinstance(dictionary['threeDsInputData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDsInputData']))
            value = ThreeDsInputData()
            self.three_ds_input_data = value.from_dictionary(dictionary['threeDsInputData'])
        return self
