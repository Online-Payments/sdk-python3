# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.acquirer_selection_information import AcquirerSelectionInformation


class AcquirerInformation(DataObject):
    """
    | Information about the acquirer used to process the transaction
    """

    __acquirer_selection_information = None
    __name = None

    @property
    def acquirer_selection_information(self) -> AcquirerSelectionInformation:
        """
        | Information about the acquirer selection

        Type: :class:`onlinepayments.sdk.domain.acquirer_selection_information.AcquirerSelectionInformation`
        """
        return self.__acquirer_selection_information

    @acquirer_selection_information.setter
    def acquirer_selection_information(self, value: AcquirerSelectionInformation):
        self.__acquirer_selection_information = value

    @property
    def name(self) -> str:
        """
        | Name of the acquirer used to process the transaction

        Type: str
        """
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    def to_dictionary(self):
        dictionary = super(AcquirerInformation, self).to_dictionary()
        if self.acquirer_selection_information is not None:
            dictionary['acquirerSelectionInformation'] = self.acquirer_selection_information.to_dictionary()
        if self.name is not None:
            dictionary['name'] = self.name
        return dictionary

    def from_dictionary(self, dictionary):
        super(AcquirerInformation, self).from_dictionary(dictionary)
        if 'acquirerSelectionInformation' in dictionary:
            if not isinstance(dictionary['acquirerSelectionInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['acquirerSelectionInformation']))
            value = AcquirerSelectionInformation()
            self.acquirer_selection_information = value.from_dictionary(dictionary['acquirerSelectionInformation'])
        if 'name' in dictionary:
            self.name = dictionary['name']
        return self
