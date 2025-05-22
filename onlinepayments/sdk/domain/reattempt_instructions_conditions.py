# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class ReattemptInstructionsConditions(DataObject):

    __max_attempts: Optional[int] = None
    __max_delay: Optional[int] = None

    @property
    def max_attempts(self) -> Optional[int]:
        """
        | Max number of reattempts permitted.

        Type: int
        """
        return self.__max_attempts

    @max_attempts.setter
    def max_attempts(self, value: Optional[int]) -> None:
        self.__max_attempts = value

    @property
    def max_delay(self) -> Optional[int]:
        """
        | Max hours during which reattempt can be made.

        Type: int
        """
        return self.__max_delay

    @max_delay.setter
    def max_delay(self, value: Optional[int]) -> None:
        self.__max_delay = value

    def to_dictionary(self) -> dict:
        dictionary = super(ReattemptInstructionsConditions, self).to_dictionary()
        if self.max_attempts is not None:
            dictionary['maxAttempts'] = self.max_attempts
        if self.max_delay is not None:
            dictionary['maxDelay'] = self.max_delay
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ReattemptInstructionsConditions':
        super(ReattemptInstructionsConditions, self).from_dictionary(dictionary)
        if 'maxAttempts' in dictionary:
            self.max_attempts = dictionary['maxAttempts']
        if 'maxDelay' in dictionary:
            self.max_delay = dictionary['maxDelay']
        return self
