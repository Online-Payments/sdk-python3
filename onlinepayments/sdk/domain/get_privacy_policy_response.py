# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class GetPrivacyPolicyResponse(DataObject):
    """
    | Object containing the privacy policy.
    """

    __html_content = None

    @property
    def html_content(self) -> str:
        """
        | HTML content to be displayed to the user.

        Type: str
        """
        return self.__html_content

    @html_content.setter
    def html_content(self, value: str):
        self.__html_content = value

    def to_dictionary(self):
        dictionary = super(GetPrivacyPolicyResponse, self).to_dictionary()
        if self.html_content is not None:
            dictionary['htmlContent'] = self.html_content
        return dictionary

    def from_dictionary(self, dictionary):
        super(GetPrivacyPolicyResponse, self).from_dictionary(dictionary)
        if 'htmlContent' in dictionary:
            self.html_content = dictionary['htmlContent']
        return self
