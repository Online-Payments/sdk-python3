# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .create_mandate_with_return_url import CreateMandateWithReturnUrl
from .data_object import DataObject


class SepaDirectDebitPaymentProduct771SpecificInput(DataObject):

    __existing_unique_mandate_reference: Optional[str] = None
    __mandate: Optional[CreateMandateWithReturnUrl] = None

    @property
    def existing_unique_mandate_reference(self) -> Optional[str]:
        """
        | The unique reference of the existing mandate to use in this payment.

        Type: str
        """
        return self.__existing_unique_mandate_reference

    @existing_unique_mandate_reference.setter
    def existing_unique_mandate_reference(self, value: Optional[str]) -> None:
        self.__existing_unique_mandate_reference = value

    @property
    def mandate(self) -> Optional[CreateMandateWithReturnUrl]:
        """
        | Object containing information to create a SEPA Direct Debit mandate.

        Type: :class:`onlinepayments.sdk.domain.create_mandate_with_return_url.CreateMandateWithReturnUrl`
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value: Optional[CreateMandateWithReturnUrl]) -> None:
        self.__mandate = value

    def to_dictionary(self) -> dict:
        dictionary = super(SepaDirectDebitPaymentProduct771SpecificInput, self).to_dictionary()
        if self.existing_unique_mandate_reference is not None:
            dictionary['existingUniqueMandateReference'] = self.existing_unique_mandate_reference
        if self.mandate is not None:
            dictionary['mandate'] = self.mandate.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SepaDirectDebitPaymentProduct771SpecificInput':
        super(SepaDirectDebitPaymentProduct771SpecificInput, self).from_dictionary(dictionary)
        if 'existingUniqueMandateReference' in dictionary:
            self.existing_unique_mandate_reference = dictionary['existingUniqueMandateReference']
        if 'mandate' in dictionary:
            if not isinstance(dictionary['mandate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandate']))
            value = CreateMandateWithReturnUrl()
            self.mandate = value.from_dictionary(dictionary['mandate'])
        return self
