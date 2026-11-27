#
# This file was automatically generated.
#
from .data_object import DataObject


class GetPrivacyPolicyResponse(DataObject):

    __slots__ = (
        "__html_content",
    )

    __html_content: str | None

    def __init__(
        self,
        *,
        html_content: str | None = None,
    ) -> None:
        self.html_content = html_content

    @property
    def html_content(self) -> str | None:
        """
        | HTML content to be displayed to the user.

        Type: str
        """
        return self.__html_content

    @html_content.setter
    def html_content(self, value: str | None) -> None:
        self.__html_content = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.html_content is not None:
            dictionary['htmlContent'] = self.html_content
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetPrivacyPolicyResponse':
        super().from_dictionary(dictionary)
        if 'htmlContent' in dictionary:
            self.html_content = dictionary['htmlContent']
        return self
