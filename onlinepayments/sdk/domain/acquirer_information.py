# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class AcquirerInformation(DataObject):
    """
    | Information about the acquirer used to process the transaction
    """

    __name = None

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
        if self.name is not None:
            dictionary['name'] = self.name
        return dictionary

    def from_dictionary(self, dictionary):
        super(AcquirerInformation, self).from_dictionary(dictionary)
        if 'name' in dictionary:
            self.name = dictionary['name']
        return self
