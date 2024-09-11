# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.mandate_personal_name_response import MandatePersonalNameResponse


class MandatePersonalInformationResponse(DataObject):
    """
    | Object containing personal information of the customer
    """

    __name = None
    __title = None

    @property
    def name(self) -> MandatePersonalNameResponse:
        """
        | Object containing the name details of the customer.

        Type: :class:`onlinepayments.sdk.domain.mandate_personal_name_response.MandatePersonalNameResponse`
        """
        return self.__name

    @name.setter
    def name(self, value: MandatePersonalNameResponse):
        self.__name = value

    @property
    def title(self) -> str:
        """
        | Object containing the title of the customer (Mr, Miss or Mrs)

        Type: str
        """
        return self.__title

    @title.setter
    def title(self, value: str):
        self.__title = value

    def to_dictionary(self):
        dictionary = super(MandatePersonalInformationResponse, self).to_dictionary()
        if self.name is not None:
            dictionary['name'] = self.name.to_dictionary()
        if self.title is not None:
            dictionary['title'] = self.title
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandatePersonalInformationResponse, self).from_dictionary(dictionary)
        if 'name' in dictionary:
            if not isinstance(dictionary['name'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['name']))
            value = MandatePersonalNameResponse()
            self.name = value.from_dictionary(dictionary['name'])
        if 'title' in dictionary:
            self.title = dictionary['title']
        return self
