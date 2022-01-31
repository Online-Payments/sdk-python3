# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.create_mandate_with_return_url import CreateMandateWithReturnUrl


class SepaDirectDebitPaymentProduct771SpecificInput(DataObject):
    """
    | Object containing information specific to SEPA Direct Debit
    """

    __existing_unique_mandate_reference = None
    __mandate = None

    @property
    def existing_unique_mandate_reference(self) -> str:
        """
        | The unique reference of the existing mandate to use in this payment.

        Type: str
        """
        return self.__existing_unique_mandate_reference

    @existing_unique_mandate_reference.setter
    def existing_unique_mandate_reference(self, value: str):
        self.__existing_unique_mandate_reference = value

    @property
    def mandate(self) -> CreateMandateWithReturnUrl:
        """
        | Object containing information to create a SEPA Direct Debit mandate.

        Type: :class:`onlinepayments.sdk.domain.create_mandate_with_return_url.CreateMandateWithReturnUrl`
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value: CreateMandateWithReturnUrl):
        self.__mandate = value

    def to_dictionary(self):
        dictionary = super(SepaDirectDebitPaymentProduct771SpecificInput, self).to_dictionary()
        if self.existing_unique_mandate_reference is not None:
            dictionary['existingUniqueMandateReference'] = self.existing_unique_mandate_reference
        if self.mandate is not None:
            dictionary['mandate'] = self.mandate.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(SepaDirectDebitPaymentProduct771SpecificInput, self).from_dictionary(dictionary)
        if 'existingUniqueMandateReference' in dictionary:
            self.existing_unique_mandate_reference = dictionary['existingUniqueMandateReference']
        if 'mandate' in dictionary:
            if not isinstance(dictionary['mandate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandate']))
            value = CreateMandateWithReturnUrl()
            self.mandate = value.from_dictionary(dictionary['mandate'])
        return self
