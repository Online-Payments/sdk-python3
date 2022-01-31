# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.api_error import APIError


class PaymentStatusOutput(DataObject):
    """
    | This object has the numeric representation of the current payment status, timestamp of last status change and performable action on the current payment resource. In case of failed payments and negative scenarios, detailed error information is listed.
    """

    __errors = None
    __is_authorized = None
    __is_cancellable = None
    __is_refundable = None
    __status_category = None
    __status_code = None
    __status_code_change_date_time = None

    @property
    def errors(self) -> List[APIError]:
        """
        | Contains the set of errors

        Type: list[:class:`onlinepayments.sdk.domain.api_error.APIError`]
        """
        return self.__errors

    @errors.setter
    def errors(self, value: List[APIError]):
        self.__errors = value

    @property
    def is_authorized(self) -> bool:
        """
        | Indicates if the transaction has been authorized

        Type: bool
        """
        return self.__is_authorized

    @is_authorized.setter
    def is_authorized(self, value: bool):
        self.__is_authorized = value

    @property
    def is_cancellable(self) -> bool:
        """
        | Flag indicating if the payment can be cancelled

        Type: bool
        """
        return self.__is_cancellable

    @is_cancellable.setter
    def is_cancellable(self, value: bool):
        self.__is_cancellable = value

    @property
    def is_refundable(self) -> bool:
        """
        | Flag indicating if the payment can be refunded

        Type: bool
        """
        return self.__is_refundable

    @is_refundable.setter
    def is_refundable(self, value: bool):
        self.__is_refundable = value

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

    @property
    def status_code_change_date_time(self) -> str:
        """
        | Timestamp of the latest status change

        Type: str
        """
        return self.__status_code_change_date_time

    @status_code_change_date_time.setter
    def status_code_change_date_time(self, value: str):
        self.__status_code_change_date_time = value

    def to_dictionary(self):
        dictionary = super(PaymentStatusOutput, self).to_dictionary()
        if self.errors is not None:
            dictionary['errors'] = []
            for element in self.errors:
                if element is not None:
                    dictionary['errors'].append(element.to_dictionary())
        if self.is_authorized is not None:
            dictionary['isAuthorized'] = self.is_authorized
        if self.is_cancellable is not None:
            dictionary['isCancellable'] = self.is_cancellable
        if self.is_refundable is not None:
            dictionary['isRefundable'] = self.is_refundable
        if self.status_category is not None:
            dictionary['statusCategory'] = self.status_category
        if self.status_code is not None:
            dictionary['statusCode'] = self.status_code
        if self.status_code_change_date_time is not None:
            dictionary['statusCodeChangeDateTime'] = self.status_code_change_date_time
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentStatusOutput, self).from_dictionary(dictionary)
        if 'errors' in dictionary:
            if not isinstance(dictionary['errors'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['errors']))
            self.errors = []
            for element in dictionary['errors']:
                value = APIError()
                self.errors.append(value.from_dictionary(element))
        if 'isAuthorized' in dictionary:
            self.is_authorized = dictionary['isAuthorized']
        if 'isCancellable' in dictionary:
            self.is_cancellable = dictionary['isCancellable']
        if 'isRefundable' in dictionary:
            self.is_refundable = dictionary['isRefundable']
        if 'statusCategory' in dictionary:
            self.status_category = dictionary['statusCategory']
        if 'statusCode' in dictionary:
            self.status_code = dictionary['statusCode']
        if 'statusCodeChangeDateTime' in dictionary:
            self.status_code_change_date_time = dictionary['statusCodeChangeDateTime']
        return self
