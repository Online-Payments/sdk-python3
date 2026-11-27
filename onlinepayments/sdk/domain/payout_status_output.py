#
# This file was automatically generated.
#
from .data_object import DataObject


class PayoutStatusOutput(DataObject):

    __slots__ = (
        "__is_cancellable",
        "__status_category",
        "__status_code",
    )

    __is_cancellable: bool | None
    __status_category: str | None
    __status_code: int | None

    def __init__(
        self,
        *,
        is_cancellable: bool | None = None,
        status_category: str | None = None,
        status_code: int | None = None,
    ) -> None:
        self.is_cancellable = is_cancellable
        self.status_category = status_category
        self.status_code = status_code

    @property
    def is_cancellable(self) -> bool | None:
        """
        | Flag indicating if the payout can be cancelled
        
        * true
        * false

        Type: bool
        """
        return self.__is_cancellable

    @is_cancellable.setter
    def is_cancellable(self, value: bool | None) -> None:
        self.__is_cancellable = value

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

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.is_cancellable is not None:
            dictionary['isCancellable'] = self.is_cancellable
        if self.status_category is not None:
            dictionary['statusCategory'] = self.status_category
        if self.status_code is not None:
            dictionary['statusCode'] = self.status_code
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PayoutStatusOutput':
        super().from_dictionary(dictionary)
        if 'isCancellable' in dictionary:
            self.is_cancellable = dictionary['isCancellable']
        if 'statusCategory' in dictionary:
            self.status_category = dictionary['statusCategory']
        if 'statusCode' in dictionary:
            self.status_code = dictionary['statusCode']
        return self
