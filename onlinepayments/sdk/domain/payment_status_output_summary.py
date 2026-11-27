#
# This file was automatically generated.
#
from .api_error import APIError
from .data_object import DataObject


class PaymentStatusOutputSummary(DataObject):

    __slots__ = (
        "__errors",
        "__status_category",
        "__status_code",
        "__status_code_change_date_time",
    )

    __errors: list[APIError] | None
    __status_category: str | None
    __status_code: int | None
    __status_code_change_date_time: str | None

    def __init__(
        self,
        *,
        errors: list[APIError] | None = None,
        status_category: str | None = None,
        status_code: int | None = None,
        status_code_change_date_time: str | None = None,
    ) -> None:
        self.errors = errors
        self.status_category = status_category
        self.status_code = status_code
        self.status_code_change_date_time = status_code_change_date_time

    @property
    def errors(self) -> list[APIError] | None:
        """
        | This field contains the set of errors encountered during the process.

        Type: list[:class:`onlinepayments.sdk.domain.api_error.APIError`]
        """
        return self.__errors

    @errors.setter
    def errors(self, value: list[APIError] | None) -> None:
        self.__errors = value

    @property
    def status_category(self) -> str | None:
        """
        | Highlevel status of the payment, payout or refund.

        Type: str
        """
        return self.__status_category

    @status_category.setter
    def status_category(self, value: str | None) -> None:
        self.__status_category = value

    @property
    def status_code(self) -> int | None:
        """
        | Numeric status code of the legacy API. The value can also be found in the BackOffice and in report files.

        Type: int
        """
        return self.__status_code

    @status_code.setter
    def status_code(self, value: int | None) -> None:
        self.__status_code = value

    @property
    def status_code_change_date_time(self) -> str | None:
        """
        | Timestamp of the latest status change

        Type: str
        """
        return self.__status_code_change_date_time

    @status_code_change_date_time.setter
    def status_code_change_date_time(self, value: str | None) -> None:
        self.__status_code_change_date_time = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.errors is not None:
            dictionary['errors'] = []
            for element in self.errors:
                if element is not None:
                    dictionary['errors'].append(element.to_dictionary())
        if self.status_category is not None:
            dictionary['statusCategory'] = self.status_category
        if self.status_code is not None:
            dictionary['statusCode'] = self.status_code
        if self.status_code_change_date_time is not None:
            dictionary['statusCodeChangeDateTime'] = self.status_code_change_date_time
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentStatusOutputSummary':
        super().from_dictionary(dictionary)
        if 'errors' in dictionary:
            if not isinstance(dictionary['errors'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['errors']))
            self.errors = []
            for element in dictionary['errors']:
                value = APIError()
                self.errors.append(value.from_dictionary(element))
        if 'statusCategory' in dictionary:
            self.status_category = dictionary['statusCategory']
        if 'statusCode' in dictionary:
            self.status_code = dictionary['statusCode']
        if 'statusCodeChangeDateTime' in dictionary:
            self.status_code_change_date_time = dictionary['statusCodeChangeDateTime']
        return self
