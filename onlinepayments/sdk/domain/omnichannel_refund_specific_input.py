# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class OmnichannelRefundSpecificInput(DataObject):

    __operator_id: Optional[str] = None

    @property
    def operator_id(self) -> Optional[str]:
        """
        | While calling Direct, the merchant can indicate which human user of their enterprise requested the action for reporting and auditing purposes. Note that it is up to the merchant to make up a code to identify the employee, for instance, the user ID of the employee logged on to the cash register. When not used, the field defaults to the merchant ID.

        Type: str
        """
        return self.__operator_id

    @operator_id.setter
    def operator_id(self, value: Optional[str]) -> None:
        self.__operator_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(OmnichannelRefundSpecificInput, self).to_dictionary()
        if self.operator_id is not None:
            dictionary['operatorId'] = self.operator_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OmnichannelRefundSpecificInput':
        super(OmnichannelRefundSpecificInput, self).from_dictionary(dictionary)
        if 'operatorId' in dictionary:
            self.operator_id = dictionary['operatorId']
        return self
