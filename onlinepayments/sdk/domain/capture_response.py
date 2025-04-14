# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .capture_output import CaptureOutput
from .capture_status_output import CaptureStatusOutput
from .data_object import DataObject


class CaptureResponse(DataObject):

    __capture_output: Optional[CaptureOutput] = None
    __id: Optional[str] = None
    __status: Optional[str] = None
    __status_output: Optional[CaptureStatusOutput] = None

    @property
    def capture_output(self) -> Optional[CaptureOutput]:
        """
        | Object containing capture details

        Type: :class:`onlinepayments.sdk.domain.capture_output.CaptureOutput`
        """
        return self.__capture_output

    @capture_output.setter
    def capture_output(self, value: Optional[CaptureOutput]) -> None:
        self.__capture_output = value

    @property
    def id(self) -> Optional[str]:
        """
        | Our unique payment transaction identifier

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: Optional[str]) -> None:
        self.__id = value

    @property
    def status(self) -> Optional[str]:
        """
        | Current high-level status of the payment in a human-readable form.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: Optional[str]) -> None:
        self.__status = value

    @property
    def status_output(self) -> Optional[CaptureStatusOutput]:
        """
        | This object has the numeric representation of the current capture status, timestamp of last status change and performable action on the current payment resource. In case of failed payments and negative scenarios, detailed error information is listed.

        Type: :class:`onlinepayments.sdk.domain.capture_status_output.CaptureStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value: Optional[CaptureStatusOutput]) -> None:
        self.__status_output = value

    def to_dictionary(self) -> dict:
        dictionary = super(CaptureResponse, self).to_dictionary()
        if self.capture_output is not None:
            dictionary['captureOutput'] = self.capture_output.to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.status is not None:
            dictionary['status'] = self.status
        if self.status_output is not None:
            dictionary['statusOutput'] = self.status_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CaptureResponse':
        super(CaptureResponse, self).from_dictionary(dictionary)
        if 'captureOutput' in dictionary:
            if not isinstance(dictionary['captureOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['captureOutput']))
            value = CaptureOutput()
            self.capture_output = value.from_dictionary(dictionary['captureOutput'])
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = CaptureStatusOutput()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self
