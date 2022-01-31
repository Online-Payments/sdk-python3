# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.mandate_personal_name import MandatePersonalName


class MandatePersonalInformation(DataObject):
    """
    | Object containing personal information of the customer.
    | Required for Create mandate and Create payment calls.
    """

    __name = None
    __title = None

    @property
    def name(self) -> MandatePersonalName:
        """
        | Object containing the name details of the customer.
        | Required for Create mandate and Create payment calls.

        Type: :class:`onlinepayments.sdk.domain.mandate_personal_name.MandatePersonalName`
        """
        return self.__name

    @name.setter
    def name(self, value: MandatePersonalName):
        self.__name = value

    @property
    def title(self) -> str:
        """
        | Object containing the title of the customer (Mr, Miss or Mrs).
        | Required for Create mandate and Create payment calls.

        Type: str
        """
        return self.__title

    @title.setter
    def title(self, value: str):
        self.__title = value

    def to_dictionary(self):
        dictionary = super(MandatePersonalInformation, self).to_dictionary()
        if self.name is not None:
            dictionary['name'] = self.name.to_dictionary()
        if self.title is not None:
            dictionary['title'] = self.title
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandatePersonalInformation, self).from_dictionary(dictionary)
        if 'name' in dictionary:
            if not isinstance(dictionary['name'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['name']))
            value = MandatePersonalName()
            self.name = value.from_dictionary(dictionary['name'])
        if 'title' in dictionary:
            self.title = dictionary['title']
        return self
