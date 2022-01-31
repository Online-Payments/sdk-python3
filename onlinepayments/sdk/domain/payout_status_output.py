# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PayoutStatusOutput(DataObject):
    __is_cancellable = None
    __status_category = None
    __status_code = None

    @property
    def is_cancellable(self) -> bool:
        """
        | Flag indicating if the payout can be cancelled 
        |  * true 
        |  * false

        Type: bool
        """
        return self.__is_cancellable

    @is_cancellable.setter
    def is_cancellable(self, value: bool):
        self.__is_cancellable = value

    @property
    def status_category(self) -> str:
        """
        | Highlevel status of the payment, payout or refund.

        Type: str
        """
        return self.__status_category

    @status_category.setter
    def status_category(self, value: str):
        self.__status_category = value

    @property
    def status_code(self) -> int:
        """
        | Numeric status code of the legacy API. It is returned to ease the migration from the legacy APIs. You should not write new business logic based on this property as it will be deprecated in a future version of the API. The value can also be found in the BackOffice and in report files.

        Type: int
        """
        return self.__status_code

    @status_code.setter
    def status_code(self, value: int):
        self.__status_code = value

    def to_dictionary(self):
        dictionary = super(PayoutStatusOutput, self).to_dictionary()
        if self.is_cancellable is not None:
            dictionary['isCancellable'] = self.is_cancellable
        if self.status_category is not None:
            dictionary['statusCategory'] = self.status_category
        if self.status_code is not None:
            dictionary['statusCode'] = self.status_code
        return dictionary

    def from_dictionary(self, dictionary):
        super(PayoutStatusOutput, self).from_dictionary(dictionary)
        if 'isCancellable' in dictionary:
            self.is_cancellable = dictionary['isCancellable']
        if 'statusCategory' in dictionary:
            self.status_category = dictionary['statusCategory']
        if 'statusCode' in dictionary:
            self.status_code = dictionary['statusCode']
        return self
