# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class ExternalTokenLinked(DataObject):

    __computed_token: Optional[str] = None
    __gts_computed_token: Optional[str] = None
    __generated_token: Optional[str] = None

    @property
    def computed_token(self) -> Optional[str]:
        """
        | The computed token

        Type: str
        """
        return self.__computed_token

    @computed_token.setter
    def computed_token(self, value: Optional[str]) -> None:
        self.__computed_token = value

    @property
    def gts_computed_token(self) -> Optional[str]:
        """
        | Deprecated: Use the field ComputedToken instead.

        Type: str

        Deprecated; Use the field ComputedToken instead.
        """
        return self.__gts_computed_token

    @gts_computed_token.setter
    def gts_computed_token(self, value: Optional[str]) -> None:
        self.__gts_computed_token = value

    @property
    def generated_token(self) -> Optional[str]:
        """
        | The generated token

        Type: str
        """
        return self.__generated_token

    @generated_token.setter
    def generated_token(self, value: Optional[str]) -> None:
        self.__generated_token = value

    def to_dictionary(self) -> dict:
        dictionary = super(ExternalTokenLinked, self).to_dictionary()
        if self.computed_token is not None:
            dictionary['ComputedToken'] = self.computed_token
        if self.gts_computed_token is not None:
            dictionary['GTSComputedToken'] = self.gts_computed_token
        if self.generated_token is not None:
            dictionary['GeneratedToken'] = self.generated_token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ExternalTokenLinked':
        super(ExternalTokenLinked, self).from_dictionary(dictionary)
        if 'ComputedToken' in dictionary:
            self.computed_token = dictionary['ComputedToken']
        if 'GTSComputedToken' in dictionary:
            self.gts_computed_token = dictionary['GTSComputedToken']
        if 'GeneratedToken' in dictionary:
            self.generated_token = dictionary['GeneratedToken']
        return self
