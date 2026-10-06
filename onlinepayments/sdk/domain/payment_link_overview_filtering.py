# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject


class PaymentLinkOverviewFiltering(DataObject):

    __merchant_ids: Optional[List[str]] = None
    __status: Optional[List[str]] = None

    @property
    def merchant_ids(self) -> Optional[List[str]]:
        """
        | List of unique merchant IDs to filter the payment links by.

        Type: list[str]
        """
        return self.__merchant_ids

    @merchant_ids.setter
    def merchant_ids(self, value: Optional[List[str]]) -> None:
        self.__merchant_ids = value

    @property
    def status(self) -> Optional[List[str]]:
        """
        | Filter payment links by their current status. You can provide one or more status values to retrieve only the links matching those statuses. When multiple statuses are provided, the response will include payment links matching ANY of the specified values (OR logic). If this parameter is omitted, payment links with all statuses will be returned. Possible values are:
        
        * ACTIVE - Payment link is ready to be used
        * CANCELLED - Payment link has been manually cancelled
        * PAID - Payment has been successfully completed
        * EXPIRED - Payment link has passed its expiration date

        Type: list[str]
        """
        return self.__status

    @status.setter
    def status(self, value: Optional[List[str]]) -> None:
        self.__status = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentLinkOverviewFiltering, self).to_dictionary()
        if self.merchant_ids is not None:
            dictionary['merchantIds'] = []
            for element in self.merchant_ids:
                if element is not None:
                    dictionary['merchantIds'].append(element)
        if self.status is not None:
            dictionary['status'] = []
            for element in self.status:
                if element is not None:
                    dictionary['status'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentLinkOverviewFiltering':
        super(PaymentLinkOverviewFiltering, self).from_dictionary(dictionary)
        if 'merchantIds' in dictionary:
            if not isinstance(dictionary['merchantIds'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['merchantIds']))
            self.merchant_ids = []
            for element in dictionary['merchantIds']:
                self.merchant_ids.append(element)
        if 'status' in dictionary:
            if not isinstance(dictionary['status'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['status']))
            self.status = []
            for element in dictionary['status']:
                self.status.append(element)
        return self
