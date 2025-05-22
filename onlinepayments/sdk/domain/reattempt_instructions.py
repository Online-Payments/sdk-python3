# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .reattempt_instructions_conditions import ReattemptInstructionsConditions


class ReattemptInstructions(DataObject):

    __conditions: Optional[ReattemptInstructionsConditions] = None
    __frozen_period: Optional[int] = None
    __indicator: Optional[str] = None

    @property
    def conditions(self) -> Optional[ReattemptInstructionsConditions]:
        """
        | Additional conditions to be met for reattempt. If the data is not provided by the acquirer, these fields are omitted from the response.

        Type: :class:`onlinepayments.sdk.domain.reattempt_instructions_conditions.ReattemptInstructionsConditions`
        """
        return self.__conditions

    @conditions.setter
    def conditions(self, value: Optional[ReattemptInstructionsConditions]) -> None:
        self.__conditions = value

    @property
    def frozen_period(self) -> Optional[int]:
        """
        | Hours to wait before next reattempt.

        Type: int
        """
        return self.__frozen_period

    @frozen_period.setter
    def frozen_period(self, value: Optional[int]) -> None:
        self.__frozen_period = value

    @property
    def indicator(self) -> Optional[str]:
        """
        | High-level use case. ``frozenPeriod`` and ``conditions``, when provided, only apply if indicator is one of:
        
        * ``retryLater``: retry with no change;
        * ``updateBeforeRetry``: retry requires data updates; Otherwise:
        * ``neverRetry``: the current payment authorization cannot be retried;
        * ``dontStorePanCredentials``: no retry and no subsequent payment attempt or payment series using this PAN from credentials on file;

        Type: str
        """
        return self.__indicator

    @indicator.setter
    def indicator(self, value: Optional[str]) -> None:
        self.__indicator = value

    def to_dictionary(self) -> dict:
        dictionary = super(ReattemptInstructions, self).to_dictionary()
        if self.conditions is not None:
            dictionary['conditions'] = self.conditions.to_dictionary()
        if self.frozen_period is not None:
            dictionary['frozenPeriod'] = self.frozen_period
        if self.indicator is not None:
            dictionary['indicator'] = self.indicator
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ReattemptInstructions':
        super(ReattemptInstructions, self).from_dictionary(dictionary)
        if 'conditions' in dictionary:
            if not isinstance(dictionary['conditions'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['conditions']))
            value = ReattemptInstructionsConditions()
            self.conditions = value.from_dictionary(dictionary['conditions'])
        if 'frozenPeriod' in dictionary:
            self.frozen_period = dictionary['frozenPeriod']
        if 'indicator' in dictionary:
            self.indicator = dictionary['indicator']
        return self
