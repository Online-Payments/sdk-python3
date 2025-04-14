# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CaptureStatusOutput(DataObject):

    __status_code: Optional[int] = None

    @property
    def status_code(self) -> Optional[int]:
        """
        | Numeric status code of the legacy API. The value can also be found in the BackOffice and in report files.

        Type: int
        """
        return self.__status_code

    @status_code.setter
    def status_code(self, value: Optional[int]) -> None:
        self.__status_code = value

    def to_dictionary(self) -> dict:
        dictionary = super(CaptureStatusOutput, self).to_dictionary()
        if self.status_code is not None:
            dictionary['statusCode'] = self.status_code
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CaptureStatusOutput':
        super(CaptureStatusOutput, self).from_dictionary(dictionary)
        if 'statusCode' in dictionary:
            self.status_code = dictionary['statusCode']
        return self
