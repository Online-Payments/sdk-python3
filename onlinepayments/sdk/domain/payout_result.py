# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .payout_output import PayoutOutput
from .payout_status_output import PayoutStatusOutput


class PayoutResult(DataObject):

    __id: Optional[str] = None
    __payout_output: Optional[PayoutOutput] = None
    __status: Optional[str] = None
    __status_output: Optional[PayoutStatusOutput] = None

    @property
    def id(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: Optional[str]) -> None:
        self.__id = value

    @property
    def payout_output(self) -> Optional[PayoutOutput]:
        """
        Type: :class:`onlinepayments.sdk.domain.payout_output.PayoutOutput`
        """
        return self.__payout_output

    @payout_output.setter
    def payout_output(self, value: Optional[PayoutOutput]) -> None:
        self.__payout_output = value

    @property
    def status(self) -> Optional[str]:
        """
        | Current high-level status of the payout in a human-readable form.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: Optional[str]) -> None:
        self.__status = value

    @property
    def status_output(self) -> Optional[PayoutStatusOutput]:
        """
        Type: :class:`onlinepayments.sdk.domain.payout_status_output.PayoutStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value: Optional[PayoutStatusOutput]) -> None:
        self.__status_output = value

    def to_dictionary(self) -> dict:
        dictionary = super(PayoutResult, self).to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.payout_output is not None:
            dictionary['payoutOutput'] = self.payout_output.to_dictionary()
        if self.status is not None:
            dictionary['status'] = self.status
        if self.status_output is not None:
            dictionary['statusOutput'] = self.status_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PayoutResult':
        super(PayoutResult, self).from_dictionary(dictionary)
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'payoutOutput' in dictionary:
            if not isinstance(dictionary['payoutOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payoutOutput']))
            value = PayoutOutput()
            self.payout_output = value.from_dictionary(dictionary['payoutOutput'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = PayoutStatusOutput()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self
