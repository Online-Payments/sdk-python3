#
# This file was automatically generated.
#
from .api_error import APIError
from .data_object import DataObject
from .refund_response import RefundResponse


class RefundErrorResponse(DataObject):

    __slots__ = (
        "__error_id",
        "__errors",
        "__refund_result",
    )

    __error_id: str | None
    __errors: list[APIError] | None
    __refund_result: RefundResponse | None

    def __init__(
        self,
        *,
        error_id: str | None = None,
        errors: list[APIError] | None = None,
        refund_result: RefundResponse | None = None,
    ) -> None:
        self.error_id = error_id
        self.errors = errors
        self.refund_result = refund_result

    @property
    def error_id(self) -> str | None:
        """
        Type: str
        """
        return self.__error_id

    @error_id.setter
    def error_id(self, value: str | None) -> None:
        self.__error_id = value

    @property
    def errors(self) -> list[APIError] | None:
        """
        Type: list[:class:`onlinepayments.sdk.domain.api_error.APIError`]
        """
        return self.__errors

    @errors.setter
    def errors(self, value: list[APIError] | None) -> None:
        self.__errors = value

    @property
    def refund_result(self) -> RefundResponse | None:
        """
        | Deprecated: This field is not used by any payment product

        Type: :class:`onlinepayments.sdk.domain.refund_response.RefundResponse`
        """
        return self.__refund_result

    @refund_result.setter
    def refund_result(self, value: RefundResponse | None) -> None:
        self.__refund_result = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.error_id is not None:
            dictionary['errorId'] = self.error_id
        if self.errors is not None:
            dictionary['errors'] = []
            for element in self.errors:
                if element is not None:
                    dictionary['errors'].append(element.to_dictionary())
        if self.refund_result is not None:
            dictionary['refundResult'] = self.refund_result.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundErrorResponse':
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
        if 'refundResult' in dictionary:
            if not isinstance(dictionary['refundResult'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['refundResult']))
            value = RefundResponse()
            self.refund_result = value.from_dictionary(dictionary['refundResult'])
        return self
