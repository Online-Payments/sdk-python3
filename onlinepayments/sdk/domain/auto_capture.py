# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class AutoCapture(DataObject):

    __delay_in_minutes: Optional[int] = None

    @property
    def delay_in_minutes(self) -> Optional[int]:
        """
        | Delay in minutes between authorization and automatic capture for this request. Minimum value is 0 minutes, maximum value is 43200 minutes (30 days).

        Type: int
        """
        return self.__delay_in_minutes

    @delay_in_minutes.setter
    def delay_in_minutes(self, value: Optional[int]) -> None:
        self.__delay_in_minutes = value

    def to_dictionary(self) -> dict:
        dictionary = super(AutoCapture, self).to_dictionary()
        if self.delay_in_minutes is not None:
            dictionary['delayInMinutes'] = self.delay_in_minutes
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AutoCapture':
        super(AutoCapture, self).from_dictionary(dictionary)
        if 'delayInMinutes' in dictionary:
            self.delay_in_minutes = dictionary['delayInMinutes']
        return self
