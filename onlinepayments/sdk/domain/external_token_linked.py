# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class ExternalTokenLinked(DataObject):
    __computed_token = None
    __gts_computed_token = None
    __generated_token = None

    @property
    def computed_token(self) -> str:
        """
        | The computed token

        Type: str
        """
        return self.__computed_token

    @computed_token.setter
    def computed_token(self, value: str):
        self.__computed_token = value

    @property
    def gts_computed_token(self) -> str:
        """
        | Deprecated: Use the field ComputedToken instead.

        Type: str
        """
        return self.__gts_computed_token

    @gts_computed_token.setter
    def gts_computed_token(self, value: str):
        self.__gts_computed_token = value

    @property
    def generated_token(self) -> str:
        """
        | The generated token

        Type: str
        """
        return self.__generated_token

    @generated_token.setter
    def generated_token(self, value: str):
        self.__generated_token = value

    def to_dictionary(self):
        dictionary = super(ExternalTokenLinked, self).to_dictionary()
        if self.computed_token is not None:
            dictionary['ComputedToken'] = self.computed_token
        if self.gts_computed_token is not None:
            dictionary['GTSComputedToken'] = self.gts_computed_token
        if self.generated_token is not None:
            dictionary['GeneratedToken'] = self.generated_token
        return dictionary

    def from_dictionary(self, dictionary):
        super(ExternalTokenLinked, self).from_dictionary(dictionary)
        if 'ComputedToken' in dictionary:
            self.computed_token = dictionary['ComputedToken']
        if 'GTSComputedToken' in dictionary:
            self.gts_computed_token = dictionary['GTSComputedToken']
        if 'GeneratedToken' in dictionary:
            self.generated_token = dictionary['GeneratedToken']
        return self
