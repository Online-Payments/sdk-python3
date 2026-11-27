#
# This file was automatically generated.
#
from .data_object import DataObject


class ValidateCredentialsResponse(DataObject):

    __slots__ = (
        "__result",
    )

    __result: str | None

    def __init__(
        self,
        *,
        result: str | None = None,
    ) -> None:
        self.result = result

    @property
    def result(self) -> str | None:
        """
        | The webhooks validation was OK (Valid) or not OK (Invalid).

        Type: str
        """
        return self.__result

    @result.setter
    def result(self, value: str | None) -> None:
        self.__result = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.result is not None:
            dictionary['result'] = self.result
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ValidateCredentialsResponse':
        super().from_dictionary(dictionary)
        if 'result' in dictionary:
            self.result = dictionary['result']
        return self
