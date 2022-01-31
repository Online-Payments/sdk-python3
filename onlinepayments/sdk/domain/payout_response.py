# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payout_output import PayoutOutput
from onlinepayments.sdk.domain.payout_status_output import PayoutStatusOutput


class PayoutResponse(DataObject):
    __id = None
    __payout_output = None
    __status = None
    __status_output = None

    @property
    def id(self) -> str:
        """
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value

    @property
    def payout_output(self) -> PayoutOutput:
        """
        Type: :class:`onlinepayments.sdk.domain.payout_output.PayoutOutput`
        """
        return self.__payout_output

    @payout_output.setter
    def payout_output(self, value: PayoutOutput):
        self.__payout_output = value

    @property
    def status(self) -> str:
        """
        | Current high-level status of the payout in a human-readable form.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: str):
        self.__status = value

    @property
    def status_output(self) -> PayoutStatusOutput:
        """
        Type: :class:`onlinepayments.sdk.domain.payout_status_output.PayoutStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value: PayoutStatusOutput):
        self.__status_output = value

    def to_dictionary(self):
        dictionary = super(PayoutResponse, self).to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.payout_output is not None:
            dictionary['payoutOutput'] = self.payout_output.to_dictionary()
        if self.status is not None:
            dictionary['status'] = self.status
        if self.status_output is not None:
            dictionary['statusOutput'] = self.status_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PayoutResponse, self).from_dictionary(dictionary)
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
