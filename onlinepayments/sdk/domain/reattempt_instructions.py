#
# This file was automatically generated.
#
from .data_object import DataObject
from .reattempt_instructions_conditions import ReattemptInstructionsConditions


class ReattemptInstructions(DataObject):

    __slots__ = (
        "__conditions",
        "__frozen_period",
        "__indicator",
    )

    __conditions: ReattemptInstructionsConditions | None
    __frozen_period: int | None
    __indicator: str | None

    def __init__(
        self,
        *,
        conditions: ReattemptInstructionsConditions | None = None,
        frozen_period: int | None = None,
        indicator: str | None = None,
    ) -> None:
        self.conditions = conditions
        self.frozen_period = frozen_period
        self.indicator = indicator

    @property
    def conditions(self) -> ReattemptInstructionsConditions | None:
        """
        | Additional conditions to be met for reattempt. If the data is not provided by the acquirer, these fields are omitted from the response.

        Type: :class:`onlinepayments.sdk.domain.reattempt_instructions_conditions.ReattemptInstructionsConditions`
        """
        return self.__conditions

    @conditions.setter
    def conditions(self, value: ReattemptInstructionsConditions | None) -> None:
        self.__conditions = value

    @property
    def frozen_period(self) -> int | None:
        """
        | Hours to wait before next reattempt.

        Type: int
        """
        return self.__frozen_period

    @frozen_period.setter
    def frozen_period(self, value: int | None) -> None:
        self.__frozen_period = value

    @property
    def indicator(self) -> str | None:
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
    def indicator(self, value: str | None) -> None:
        self.__indicator = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.conditions is not None:
            dictionary['conditions'] = self.conditions.to_dictionary()
        if self.frozen_period is not None:
            dictionary['frozenPeriod'] = self.frozen_period
        if self.indicator is not None:
            dictionary['indicator'] = self.indicator
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ReattemptInstructions':
        super().from_dictionary(dictionary)
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
