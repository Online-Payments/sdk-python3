#
# This file was automatically generated.
#
from .data_object import DataObject


class ExternalTokenLinked(DataObject):

    __slots__ = (
        "__computed_token",
        "__gts_computed_token",
        "__generated_token",
    )

    __computed_token: str | None
    __gts_computed_token: str | None
    __generated_token: str | None

    def __init__(
        self,
        *,
        computed_token: str | None = None,
        gts_computed_token: str | None = None,
        generated_token: str | None = None,
    ) -> None:
        self.computed_token = computed_token
        self.gts_computed_token = gts_computed_token
        self.generated_token = generated_token

    @property
    def computed_token(self) -> str | None:
        """
        | The computed token

        Type: str
        """
        return self.__computed_token

    @computed_token.setter
    def computed_token(self, value: str | None) -> None:
        self.__computed_token = value

    @property
    def gts_computed_token(self) -> str | None:
        """
        | Deprecated: Use the field ComputedToken instead.

        Type: str

        Deprecated; Use the field ComputedToken instead.
        """
        return self.__gts_computed_token

    @gts_computed_token.setter
    def gts_computed_token(self, value: str | None) -> None:
        self.__gts_computed_token = value

    @property
    def generated_token(self) -> str | None:
        """
        | The generated token

        Type: str
        """
        return self.__generated_token

    @generated_token.setter
    def generated_token(self, value: str | None) -> None:
        self.__generated_token = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.computed_token is not None:
            dictionary['ComputedToken'] = self.computed_token
        if self.gts_computed_token is not None:
            dictionary['GTSComputedToken'] = self.gts_computed_token
        if self.generated_token is not None:
            dictionary['GeneratedToken'] = self.generated_token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ExternalTokenLinked':
        super().from_dictionary(dictionary)
        if 'ComputedToken' in dictionary:
            self.computed_token = dictionary['ComputedToken']
        if 'GTSComputedToken' in dictionary:
            self.gts_computed_token = dictionary['GTSComputedToken']
        if 'GeneratedToken' in dictionary:
            self.generated_token = dictionary['GeneratedToken']
        return self
