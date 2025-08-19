# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentReferences(DataObject):

    __merchant_parameters: Optional[str] = None
    __merchant_reference: Optional[str] = None
    __operation_group_reference: Optional[str] = None

    @property
    def merchant_parameters(self) -> Optional[str]:
        """
        | It allows you to store additional parameters for the transaction in the format you prefer (e.g.-> key-value query string, JSON, etc.) These parameters are then echoed back to you in API GET calls and Webhook notifications. This field must not contain any personal data.

        Type: str
        """
        return self.__merchant_parameters

    @merchant_parameters.setter
    def merchant_parameters(self, value: Optional[str]) -> None:
        self.__merchant_parameters = value

    @property
    def merchant_reference(self) -> Optional[str]:
        """
        | Your unique reference of the transaction that is also returned in our report files. This is almost always used for your reconciliation of our report files. It is highly recommended to provide a single MerchantReference per unique order on your side

        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value: Optional[str]) -> None:
        self.__merchant_reference = value

    @property
    def operation_group_reference(self) -> Optional[str]:
        """
        | An identifier for a group of transactions. This reference helps to link multiple related transactions together, facilitating easier reconciliation and tracking.

        Type: str
        """
        return self.__operation_group_reference

    @operation_group_reference.setter
    def operation_group_reference(self, value: Optional[str]) -> None:
        self.__operation_group_reference = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentReferences, self).to_dictionary()
        if self.merchant_parameters is not None:
            dictionary['merchantParameters'] = self.merchant_parameters
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
        if self.operation_group_reference is not None:
            dictionary['operationGroupReference'] = self.operation_group_reference
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentReferences':
        super(PaymentReferences, self).from_dictionary(dictionary)
        if 'merchantParameters' in dictionary:
            self.merchant_parameters = dictionary['merchantParameters']
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        if 'operationGroupReference' in dictionary:
            self.operation_group_reference = dictionary['operationGroupReference']
        return self
