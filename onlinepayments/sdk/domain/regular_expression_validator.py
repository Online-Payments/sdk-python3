#
# This file was automatically generated.
#
from .data_object import DataObject


class RegularExpressionValidator(DataObject):

    __slots__ = (
        "__regular_expression",
    )

    __regular_expression: str | None

    def __init__(
        self,
        *,
        regular_expression: str | None = None,
    ) -> None:
        self.regular_expression = regular_expression

    @property
    def regular_expression(self) -> str | None:
        """
        Type: str
        """
        return self.__regular_expression

    @regular_expression.setter
    def regular_expression(self, value: str | None) -> None:
        self.__regular_expression = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.regular_expression is not None:
            dictionary['regularExpression'] = self.regular_expression
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RegularExpressionValidator':
        super().from_dictionary(dictionary)
        if 'regularExpression' in dictionary:
            self.regular_expression = dictionary['regularExpression']
        return self
