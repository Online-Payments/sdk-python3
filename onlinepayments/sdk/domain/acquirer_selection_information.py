# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class AcquirerSelectionInformation(DataObject):

    __fallback_level: Optional[int] = None
    __result: Optional[str] = None
    __rule_name: Optional[str] = None

    @property
    def fallback_level(self) -> Optional[int]:
        """
        | Specifies whether a fallback occurred from the primary choice of the acquirer selection service.

        Type: int
        """
        return self.__fallback_level

    @fallback_level.setter
    def fallback_level(self, value: Optional[int]) -> None:
        self.__fallback_level = value

    @property
    def result(self) -> Optional[str]:
        """
        | Result of the acquirer selection operation

        Type: str
        """
        return self.__result

    @result.setter
    def result(self, value: Optional[str]) -> None:
        self.__result = value

    @property
    def rule_name(self) -> Optional[str]:
        """
        | Name of the rule used to select the acquirer

        Type: str
        """
        return self.__rule_name

    @rule_name.setter
    def rule_name(self, value: Optional[str]) -> None:
        self.__rule_name = value

    def to_dictionary(self) -> dict:
        dictionary = super(AcquirerSelectionInformation, self).to_dictionary()
        if self.fallback_level is not None:
            dictionary['fallbackLevel'] = self.fallback_level
        if self.result is not None:
            dictionary['result'] = self.result
        if self.rule_name is not None:
            dictionary['ruleName'] = self.rule_name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AcquirerSelectionInformation':
        super(AcquirerSelectionInformation, self).from_dictionary(dictionary)
        if 'fallbackLevel' in dictionary:
            self.fallback_level = dictionary['fallbackLevel']
        if 'result' in dictionary:
            self.result = dictionary['result']
        if 'ruleName' in dictionary:
            self.rule_name = dictionary['ruleName']
        return self
