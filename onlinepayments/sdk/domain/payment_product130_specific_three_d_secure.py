# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PaymentProduct130SpecificThreeDSecure(DataObject):
    """
    | Object containing specific data regarding 3-D Secure
    """

    __acquirer_exemption = None
    __merchant_score = None
    __number_of_items = None
    __usecase = None

    @property
    def acquirer_exemption(self) -> bool:
        """
        | Indicates the Acquirer TRA exemption

        Type: bool
        """
        return self.__acquirer_exemption

    @acquirer_exemption.setter
    def acquirer_exemption(self, value: bool):
        self.__acquirer_exemption = value

    @property
    def merchant_score(self) -> str:
        """
        | Score calculated by the 3DS Requestor and provided to CB Scoring service only.

        Type: str
        """
        return self.__merchant_score

    @merchant_score.setter
    def merchant_score(self, value: str):
        self.__merchant_score = value

    @property
    def number_of_items(self) -> int:
        """
        | Number of purchased items or services. 99 if more than 99 items

        Type: int
        """
        return self.__number_of_items

    @number_of_items.setter
    def number_of_items(self, value: int):
        self.__number_of_items = value

    @property
    def usecase(self) -> str:
        """
        | Indicates the type of payment for which an authentication is requested

        Type: str
        """
        return self.__usecase

    @usecase.setter
    def usecase(self, value: str):
        self.__usecase = value

    def to_dictionary(self):
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

    def from_dictionary(self, dictionary):
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
