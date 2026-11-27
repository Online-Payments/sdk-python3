#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProductFiltersHostedFields(DataObject):

    __slots__ = (
        "__exclude",
        "__restrict_to",
    )

    __exclude: list[int] | None
    __restrict_to: list[int] | None

    def __init__(
        self,
        *,
        exclude: list[int] | None = None,
        restrict_to: list[int] | None = None,
    ) -> None:
        self.exclude = exclude
        self.restrict_to = restrict_to

    @property
    def exclude(self) -> list[int] | None:
        """
        | List containing all payment product ids that should either be restricted to in or excluded from the payment context.

        Type: list[int]
        """
        return self.__exclude

    @exclude.setter
    def exclude(self, value: list[int] | None) -> None:
        self.__exclude = value

    @property
    def restrict_to(self) -> list[int] | None:
        """
        | List containing all payment product ids that should either be restricted to in or excluded from the payment context.

        Type: list[int]
        """
        return self.__restrict_to

    @restrict_to.setter
    def restrict_to(self, value: list[int] | None) -> None:
        self.__restrict_to = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.exclude is not None:
            dictionary['exclude'] = []
            for element in self.exclude:
                if element is not None:
                    dictionary['exclude'].append(element)
        if self.restrict_to is not None:
            dictionary['restrictTo'] = []
            for element in self.restrict_to:
                if element is not None:
                    dictionary['restrictTo'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductFiltersHostedFields':
        super().from_dictionary(dictionary)
        if 'exclude' in dictionary:
            if not isinstance(dictionary['exclude'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['exclude']))
            self.exclude = []
            for element in dictionary['exclude']:
                self.exclude.append(element)
        if 'restrictTo' in dictionary:
            if not isinstance(dictionary['restrictTo'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['restrictTo']))
            self.restrict_to = []
            for element in dictionary['restrictTo']:
                self.restrict_to.append(element)
        return self
