#
# This file was automatically generated.
#
from .data_object import DataObject
from .label_template_element import LabelTemplateElement


class AccountOnFileDisplayHints(DataObject):

    __slots__ = (
        "__label_template",
        "__logo",
    )

    __label_template: list[LabelTemplateElement] | None
    __logo: str | None

    def __init__(
        self,
        *,
        label_template: list[LabelTemplateElement] | None = None,
        logo: str | None = None,
    ) -> None:
        self.label_template = label_template
        self.logo = logo

    @property
    def label_template(self) -> list[LabelTemplateElement] | None:
        """
        | Array of attribute keys and their mask

        Type: list[:class:`onlinepayments.sdk.domain.label_template_element.LabelTemplateElement`]
        """
        return self.__label_template

    @label_template.setter
    def label_template(self, value: list[LabelTemplateElement] | None) -> None:
        self.__label_template = value

    @property
    def logo(self) -> str | None:
        """
        | Partial URL that you can reference for the image of this payment product. You can use our server-side resize functionality by appending '?size={{width}}x{{height}}' to the full URL, where width and height are specified in pixels. The resized image will always keep its correct aspect ratio.

        Type: str
        """
        return self.__logo

    @logo.setter
    def logo(self, value: str | None) -> None:
        self.__logo = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.label_template is not None:
            dictionary['labelTemplate'] = []
            for element in self.label_template:
                if element is not None:
                    dictionary['labelTemplate'].append(element.to_dictionary())
        if self.logo is not None:
            dictionary['logo'] = self.logo
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AccountOnFileDisplayHints':
        super().from_dictionary(dictionary)
        if 'labelTemplate' in dictionary:
            if not isinstance(dictionary['labelTemplate'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['labelTemplate']))
            self.label_template = []
            for element in dictionary['labelTemplate']:
                value = LabelTemplateElement()
                self.label_template.append(value.from_dictionary(element))
        if 'logo' in dictionary:
            self.logo = dictionary['logo']
        return self
