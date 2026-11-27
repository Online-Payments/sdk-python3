#
# This file was automatically generated.
#
from .api_error import APIError
from .data_object import DataObject


class ErrorResponse(DataObject):

    __slots__ = (
        "__error_id",
        "__errors",
    )

    __error_id: str | None
    __errors: list[APIError] | None

    def __init__(
        self,
        *,
        error_id: str | None = None,
        errors: list[APIError] | None = None,
    ) -> None:
        self.error_id = error_id
        self.errors = errors

    @property
    def error_id(self) -> str | None:
        """
        | Unique reference, for debugging purposes, of this error response

        Type: str
        """
        return self.__error_id

    @error_id.setter
    def error_id(self, value: str | None) -> None:
        self.__error_id = value

    @property
    def errors(self) -> list[APIError] | None:
        """
        | List of one or more errors

        Type: list[:class:`onlinepayments.sdk.domain.api_error.APIError`]
        """
        return self.__errors

    @errors.setter
    def errors(self, value: list[APIError] | None) -> None:
        self.__errors = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.error_id is not None:
            dictionary['errorId'] = self.error_id
        if self.errors is not None:
            dictionary['errors'] = []
            for element in self.errors:
                if element is not None:
                    dictionary['errors'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ErrorResponse':
        super().from_dictionary(dictionary)
        if 'errorId' in dictionary:
            self.error_id = dictionary['errorId']
        if 'errors' in dictionary:
            if not isinstance(dictionary['errors'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['errors']))
            self.errors = []
            for element in dictionary['errors']:
                value = APIError()
                self.errors.append(value.from_dictionary(element))
        return self
