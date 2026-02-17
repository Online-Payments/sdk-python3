# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class ImportCofSeriesResponse(DataObject):

    __payment_id: Optional[str] = None

    @property
    def payment_id(self) -> Optional[str]:
        """
        | This is our unique payment transaction identifier.

        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: Optional[str]) -> None:
        self.__payment_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(ImportCofSeriesResponse, self).to_dictionary()
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ImportCofSeriesResponse':
        super(ImportCofSeriesResponse, self).from_dictionary(dictionary)
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        return self
