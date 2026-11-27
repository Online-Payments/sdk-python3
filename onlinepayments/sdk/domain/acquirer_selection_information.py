#
# This file was automatically generated.
#
from .data_object import DataObject


class AcquirerSelectionInformation(DataObject):

    __slots__ = (
        "__fallback_level",
        "__result",
        "__rule_name",
    )

    __fallback_level: int | None
    __result: str | None
    __rule_name: str | None

    def __init__(
        self,
        *,
        fallback_level: int | None = None,
        result: str | None = None,
        rule_name: str | None = None,
    ) -> None:
        self.fallback_level = fallback_level
        self.result = result
        self.rule_name = rule_name

    @property
    def fallback_level(self) -> int | None:
        """
        | Specifies whether a fallback occurred from the primary choice of the acquirer selection service.

        Type: int
        """
        return self.__fallback_level

    @fallback_level.setter
    def fallback_level(self, value: int | None) -> None:
        self.__fallback_level = value

    @property
    def result(self) -> str | None:
        """
        | Result of the acquirer selection operation

        Type: str
        """
        return self.__result

    @result.setter
    def result(self, value: str | None) -> None:
        self.__result = value

    @property
    def rule_name(self) -> str | None:
        """
        | Name of the rule used to select the acquirer

        Type: str
        """
        return self.__rule_name

    @rule_name.setter
    def rule_name(self, value: str | None) -> None:
        self.__rule_name = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.fallback_level is not None:
            dictionary['fallbackLevel'] = self.fallback_level
        if self.result is not None:
            dictionary['result'] = self.result
        if self.rule_name is not None:
            dictionary['ruleName'] = self.rule_name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AcquirerSelectionInformation':
        super().from_dictionary(dictionary)
        if 'fallbackLevel' in dictionary:
            self.fallback_level = dictionary['fallbackLevel']
        if 'result' in dictionary:
            self.result = dictionary['result']
        if 'ruleName' in dictionary:
            self.rule_name = dictionary['ruleName']
        return self
