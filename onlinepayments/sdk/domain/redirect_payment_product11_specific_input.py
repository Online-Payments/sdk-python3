# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RedirectPaymentProduct11SpecificInput(DataObject):

    __skip_email_validation: Optional[bool] = None

    @property
    def skip_email_validation(self) -> Optional[bool]:
        """
        | Indicates whether to skip the email validation for the payment. When set to true, the email validation will be skipped.

        Type: bool
        """
        return self.__skip_email_validation

    @skip_email_validation.setter
    def skip_email_validation(self, value: Optional[bool]) -> None:
        self.__skip_email_validation = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct11SpecificInput, self).to_dictionary()
        if self.skip_email_validation is not None:
            dictionary['skipEmailValidation'] = self.skip_email_validation
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct11SpecificInput':
        super(RedirectPaymentProduct11SpecificInput, self).from_dictionary(dictionary)
        if 'skipEmailValidation' in dictionary:
            self.skip_email_validation = dictionary['skipEmailValidation']
        return self
