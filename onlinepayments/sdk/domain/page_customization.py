# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PageCustomization(DataObject):
    __template = None

    @property
    def template(self) -> str:
        """
        | Using the Back-Office it is possible to upload multiple templates of your HostedCheckout payment pages. You can force the use of a template by specifying it in the Template field. This allows you to customize the hostedcheckout pages or the redirection pages. Please note that you need to specify the filename of the template.

        Type: str
        """
        return self.__template

    @template.setter
    def template(self, value: str):
        self.__template = value

    def to_dictionary(self):
        dictionary = super(PageCustomization, self).to_dictionary()
        if self.template is not None:
            dictionary['template'] = self.template
        return dictionary

    def from_dictionary(self, dictionary):
        super(PageCustomization, self).from_dictionary(dictionary)
        if 'template' in dictionary:
            self.template = dictionary['template']
        return self
