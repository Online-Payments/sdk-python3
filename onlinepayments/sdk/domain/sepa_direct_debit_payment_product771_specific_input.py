#
# This file was automatically generated.
#
from .create_mandate_with_return_url import CreateMandateWithReturnUrl
from .data_object import DataObject


class SepaDirectDebitPaymentProduct771SpecificInput(DataObject):

    __slots__ = (
        "__existing_unique_mandate_reference",
        "__mandate",
    )

    __existing_unique_mandate_reference: str | None
    __mandate: CreateMandateWithReturnUrl | None

    def __init__(
        self,
        *,
        existing_unique_mandate_reference: str | None = None,
        mandate: CreateMandateWithReturnUrl | None = None,
    ) -> None:
        self.existing_unique_mandate_reference = existing_unique_mandate_reference
        self.mandate = mandate

    @property
    def existing_unique_mandate_reference(self) -> str | None:
        """
        | The unique reference of the existing mandate to use in this payment.

        Type: str
        """
        return self.__existing_unique_mandate_reference

    @existing_unique_mandate_reference.setter
    def existing_unique_mandate_reference(self, value: str | None) -> None:
        self.__existing_unique_mandate_reference = value

    @property
    def mandate(self) -> CreateMandateWithReturnUrl | None:
        """
        | Object containing information to create a SEPA Direct Debit mandate.

        Type: :class:`onlinepayments.sdk.domain.create_mandate_with_return_url.CreateMandateWithReturnUrl`
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value: CreateMandateWithReturnUrl | None) -> None:
        self.__mandate = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.existing_unique_mandate_reference is not None:
            dictionary['existingUniqueMandateReference'] = self.existing_unique_mandate_reference
        if self.mandate is not None:
            dictionary['mandate'] = self.mandate.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SepaDirectDebitPaymentProduct771SpecificInput':
        super().from_dictionary(dictionary)
        if 'existingUniqueMandateReference' in dictionary:
            self.existing_unique_mandate_reference = dictionary['existingUniqueMandateReference']
        if 'mandate' in dictionary:
            if not isinstance(dictionary['mandate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandate']))
            value = CreateMandateWithReturnUrl()
            self.mandate = value.from_dictionary(dictionary['mandate'])
        return self
