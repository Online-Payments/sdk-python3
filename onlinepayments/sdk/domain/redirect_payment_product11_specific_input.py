#
# This file was automatically generated.
#
from .data_object import DataObject


class RedirectPaymentProduct11SpecificInput(DataObject):

    __slots__ = (
        "__skip_email_validation",
    )

    __skip_email_validation: bool | None

    def __init__(
        self,
        *,
        skip_email_validation: bool | None = None,
    ) -> None:
        self.skip_email_validation = skip_email_validation

    @property
    def skip_email_validation(self) -> bool | None:
        """
        | Indicates whether to skip the email validation for the payment. When set to true, the email validation will be skipped.

        Type: bool
        """
        return self.__skip_email_validation

    @skip_email_validation.setter
    def skip_email_validation(self, value: bool | None) -> None:
        self.__skip_email_validation = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.skip_email_validation is not None:
            dictionary['skipEmailValidation'] = self.skip_email_validation
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct11SpecificInput':
        super().from_dictionary(dictionary)
        if 'skipEmailValidation' in dictionary:
            self.skip_email_validation = dictionary['skipEmailValidation']
        return self
