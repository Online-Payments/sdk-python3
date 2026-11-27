#
# This file was automatically generated.
#
from .data_object import DataObject


class ReattemptInstructionsConditions(DataObject):

    __slots__ = (
        "__max_attempts",
        "__max_delay",
    )

    __max_attempts: int | None
    __max_delay: int | None

    def __init__(
        self,
        *,
        max_attempts: int | None = None,
        max_delay: int | None = None,
    ) -> None:
        self.max_attempts = max_attempts
        self.max_delay = max_delay

    @property
    def max_attempts(self) -> int | None:
        """
        | Max number of reattempts permitted.

        Type: int
        """
        return self.__max_attempts

    @max_attempts.setter
    def max_attempts(self, value: int | None) -> None:
        self.__max_attempts = value

    @property
    def max_delay(self) -> int | None:
        """
        | Max hours during which reattempt can be made.

        Type: int
        """
        return self.__max_delay

    @max_delay.setter
    def max_delay(self, value: int | None) -> None:
        self.__max_delay = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.max_attempts is not None:
            dictionary['maxAttempts'] = self.max_attempts
        if self.max_delay is not None:
            dictionary['maxDelay'] = self.max_delay
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ReattemptInstructionsConditions':
        super().from_dictionary(dictionary)
        if 'maxAttempts' in dictionary:
            self.max_attempts = dictionary['maxAttempts']
        if 'maxDelay' in dictionary:
            self.max_delay = dictionary['maxDelay']
        return self
