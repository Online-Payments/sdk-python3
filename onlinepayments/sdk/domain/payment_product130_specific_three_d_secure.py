# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct130SpecificThreeDSecure(DataObject):

    __acquirer_exemption: Optional[bool] = None
    __merchant_score: Optional[str] = None
    __number_of_items: Optional[int] = None
    __usecase: Optional[str] = None

    @property
    def acquirer_exemption(self) -> Optional[bool]:
        """
        | Indicates the Acquirer TRA exemption

        Type: bool
        """
        return self.__acquirer_exemption

    @acquirer_exemption.setter
    def acquirer_exemption(self, value: Optional[bool]) -> None:
        self.__acquirer_exemption = value

    @property
    def merchant_score(self) -> Optional[str]:
        """
        | Score calculated by the 3DS Requestor and provided to CB Scoring service only.

        Type: str
        """
        return self.__merchant_score

    @merchant_score.setter
    def merchant_score(self, value: Optional[str]) -> None:
        self.__merchant_score = value

    @property
    def number_of_items(self) -> Optional[int]:
        """
        | Number of purchased items or services. 99 if more than 99 items

        Type: int
        """
        return self.__number_of_items

    @number_of_items.setter
    def number_of_items(self, value: Optional[int]) -> None:
        self.__number_of_items = value

    @property
    def usecase(self) -> Optional[str]:
        """
        | Indicates the type of payment for which an authentication is requested

        Type: str
        """
        return self.__usecase

    @usecase.setter
    def usecase(self, value: Optional[str]) -> None:
        self.__usecase = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct130SpecificThreeDSecure, self).to_dictionary()
        if self.acquirer_exemption is not None:
            dictionary['acquirerExemption'] = self.acquirer_exemption
        if self.merchant_score is not None:
            dictionary['merchantScore'] = self.merchant_score
        if self.number_of_items is not None:
            dictionary['numberOfItems'] = self.number_of_items
        if self.usecase is not None:
            dictionary['usecase'] = self.usecase
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct130SpecificThreeDSecure':
        super(PaymentProduct130SpecificThreeDSecure, self).from_dictionary(dictionary)
        if 'acquirerExemption' in dictionary:
            self.acquirer_exemption = dictionary['acquirerExemption']
        if 'merchantScore' in dictionary:
            self.merchant_score = dictionary['merchantScore']
        if 'numberOfItems' in dictionary:
            self.number_of_items = dictionary['numberOfItems']
        if 'usecase' in dictionary:
            self.usecase = dictionary['usecase']
        return self
