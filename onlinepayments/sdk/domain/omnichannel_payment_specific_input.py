# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class OmnichannelPaymentSpecificInput(DataObject):

    __operator_id: Optional[str] = None

    @property
    def operator_id(self) -> Optional[str]:
        """
        | Merchants may optionally include a user identifier to indicate which person within their organization initiated this request, enabling detailed audit trails and transaction accountability. If not provided, the field defaults to the merchant ID.

        Type: str
        """
        return self.__operator_id

    @operator_id.setter
    def operator_id(self, value: Optional[str]) -> None:
        self.__operator_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(OmnichannelPaymentSpecificInput, self).to_dictionary()
        if self.operator_id is not None:
            dictionary['operatorId'] = self.operator_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OmnichannelPaymentSpecificInput':
        super(OmnichannelPaymentSpecificInput, self).from_dictionary(dictionary)
        if 'operatorId' in dictionary:
            self.operator_id = dictionary['operatorId']
        return self
