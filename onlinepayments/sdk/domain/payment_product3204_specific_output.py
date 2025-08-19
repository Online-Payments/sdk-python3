# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct3204SpecificOutput(DataObject):

    __banking_app_label: Optional[str] = None

    @property
    def banking_app_label(self) -> Optional[str]:
        """
        | The name given by the bank (the publisher of the mobile application) to identify the mobile account where the User will confirm the payment

        Type: str
        """
        return self.__banking_app_label

    @banking_app_label.setter
    def banking_app_label(self, value: Optional[str]) -> None:
        self.__banking_app_label = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct3204SpecificOutput, self).to_dictionary()
        if self.banking_app_label is not None:
            dictionary['bankingAppLabel'] = self.banking_app_label
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct3204SpecificOutput':
        super(PaymentProduct3204SpecificOutput, self).from_dictionary(dictionary)
        if 'bankingAppLabel' in dictionary:
            self.banking_app_label = dictionary['bankingAppLabel']
        return self
