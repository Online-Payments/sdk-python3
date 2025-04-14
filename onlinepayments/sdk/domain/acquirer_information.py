# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .acquirer_selection_information import AcquirerSelectionInformation
from .data_object import DataObject


class AcquirerInformation(DataObject):

    __acquirer_selection_information: Optional[AcquirerSelectionInformation] = None
    __name: Optional[str] = None

    @property
    def acquirer_selection_information(self) -> Optional[AcquirerSelectionInformation]:
        """
        | Information about the acquirer selection

        Type: :class:`onlinepayments.sdk.domain.acquirer_selection_information.AcquirerSelectionInformation`
        """
        return self.__acquirer_selection_information

    @acquirer_selection_information.setter
    def acquirer_selection_information(self, value: Optional[AcquirerSelectionInformation]) -> None:
        self.__acquirer_selection_information = value

    @property
    def name(self) -> Optional[str]:
        """
        | Name of the acquirer used to process the transaction

        Type: str
        """
        return self.__name

    @name.setter
    def name(self, value: Optional[str]) -> None:
        self.__name = value

    def to_dictionary(self) -> dict:
        dictionary = super(AcquirerInformation, self).to_dictionary()
        if self.acquirer_selection_information is not None:
            dictionary['acquirerSelectionInformation'] = self.acquirer_selection_information.to_dictionary()
        if self.name is not None:
            dictionary['name'] = self.name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AcquirerInformation':
        super(AcquirerInformation, self).from_dictionary(dictionary)
        if 'acquirerSelectionInformation' in dictionary:
            if not isinstance(dictionary['acquirerSelectionInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['acquirerSelectionInformation']))
            value = AcquirerSelectionInformation()
            self.acquirer_selection_information = value.from_dictionary(dictionary['acquirerSelectionInformation'])
        if 'name' in dictionary:
            self.name = dictionary['name']
        return self
