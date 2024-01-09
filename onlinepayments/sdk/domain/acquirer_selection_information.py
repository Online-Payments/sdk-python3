# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class AcquirerSelectionInformation(DataObject):
    """
    | Information about the acquirer selection
    """

    __fallback_level = None
    __result = None
    __rule_name = None

    @property
    def fallback_level(self) -> int:
        """
        | Specifies whether a fallback occurred from the primary choice of the acquirer selection service.

        Type: int
        """
        return self.__fallback_level

    @fallback_level.setter
    def fallback_level(self, value: int):
        self.__fallback_level = value

    @property
    def result(self) -> str:
        """
        | Result of the acquirer selection operation

        Type: str
        """
        return self.__result

    @result.setter
    def result(self, value: str):
        self.__result = value

    @property
    def rule_name(self) -> str:
        """
        | Name of the rule used to select the acquirer

        Type: str
        """
        return self.__rule_name

    @rule_name.setter
    def rule_name(self, value: str):
        self.__rule_name = value

    def to_dictionary(self):
        dictionary = super(AcquirerSelectionInformation, self).to_dictionary()
        if self.fallback_level is not None:
            dictionary['fallbackLevel'] = self.fallback_level
        if self.result is not None:
            dictionary['result'] = self.result
        if self.rule_name is not None:
            dictionary['ruleName'] = self.rule_name
        return dictionary

    def from_dictionary(self, dictionary):
        super(AcquirerSelectionInformation, self).from_dictionary(dictionary)
        if 'fallbackLevel' in dictionary:
            self.fallback_level = dictionary['fallbackLevel']
        if 'result' in dictionary:
            self.result = dictionary['result']
        if 'ruleName' in dictionary:
            self.rule_name = dictionary['ruleName']
        return self
