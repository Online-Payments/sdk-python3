#
# This file was automatically generated.
#
from .data_object import DataObject
from .mandate_customer import MandateCustomer


class CreateMandateRequest(DataObject):

    __slots__ = (
        "__alias",
        "__customer",
        "__customer_reference",
        "__language",
        "__recurrence_type",
        "__return_url",
        "__signature_type",
        "__unique_mandate_reference",
    )

    __alias: str | None
    __customer: MandateCustomer | None
    __customer_reference: str | None
    __language: str | None
    __recurrence_type: str | None
    __return_url: str | None
    __signature_type: str | None
    __unique_mandate_reference: str | None

    def __init__(
        self,
        *,
        alias: str | None = None,
        customer: MandateCustomer | None = None,
        customer_reference: str | None = None,
        language: str | None = None,
        recurrence_type: str | None = None,
        return_url: str | None = None,
        signature_type: str | None = None,
        unique_mandate_reference: str | None = None,
    ) -> None:
        self.alias = alias
        self.customer = customer
        self.customer_reference = customer_reference
        self.language = language
        self.recurrence_type = recurrence_type
        self.return_url = return_url
        self.signature_type = signature_type
        self.unique_mandate_reference = unique_mandate_reference

    @property
    def alias(self) -> str | None:
        """
        | An alias for the mandate. This can be used to visually represent the mandate. Do not include any unmasked sensitive data in the alias. If this field is not provided the masked IBAN of the customer is used.

        Type: str
        """
        return self.__alias

    @alias.setter
    def alias(self, value: str | None) -> None:
        self.__alias = value

    @property
    def customer(self) -> MandateCustomer | None:
        """
        | Customer object containing customer specific inputs. Required for Create mandate and Create payment calls.

        Type: :class:`onlinepayments.sdk.domain.mandate_customer.MandateCustomer`
        """
        return self.__customer

    @customer.setter
    def customer(self, value: MandateCustomer | None) -> None:
        self.__customer = value

    @property
    def customer_reference(self) -> str | None:
        """
        | The unique identifier of a customer

        Type: str
        """
        return self.__customer_reference

    @customer_reference.setter
    def customer_reference(self, value: str | None) -> None:
        self.__customer_reference = value

    @property
    def language(self) -> str | None:
        """
        | The language code of the customer. ISO 639-1, possible values are:
        
        * de
        * en
        * es
        * fr
        * it
        * nl
        * si
        * sk
        * sv

        Type: str
        """
        return self.__language

    @language.setter
    def language(self, value: str | None) -> None:
        self.__language = value

    @property
    def recurrence_type(self) -> str | None:
        """
        | Specifies whether the mandate is for one-off or recurring payments. Possible values are:
        
        * UNIQUE
        * RECURRING

        Type: str
        """
        return self.__recurrence_type

    @recurrence_type.setter
    def recurrence_type(self, value: str | None) -> None:
        self.__recurrence_type = value

    @property
    def return_url(self) -> str | None:
        """
        | Return URL to use if the mandate signing requires redirection. Required for S2S Create Payment if and only if the signatureType is "SMS" or "AIS".

        Type: str
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value: str | None) -> None:
        self.__return_url = value

    @property
    def signature_type(self) -> str | None:
        """
        | Specifies whether the mandate is unsigned, signed by SMS or tick box. Possible values are:
        
        * UNSIGNED
        * SMS
        * TICK_BOX
        * AIS
        
        | Not all signature types are applicable to all merchants. Please visit the support page to determine the applicable signature types.

        Type: str
        """
        return self.__signature_type

    @signature_type.setter
    def signature_type(self, value: str | None) -> None:
        self.__signature_type = value

    @property
    def unique_mandate_reference(self) -> str | None:
        """
        | The unique identifier of the mandate

        Type: str
        """
        return self.__unique_mandate_reference

    @unique_mandate_reference.setter
    def unique_mandate_reference(self, value: str | None) -> None:
        self.__unique_mandate_reference = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.alias is not None:
            dictionary['alias'] = self.alias
        if self.customer is not None:
            dictionary['customer'] = self.customer.to_dictionary()
        if self.customer_reference is not None:
            dictionary['customerReference'] = self.customer_reference
        if self.language is not None:
            dictionary['language'] = self.language
        if self.recurrence_type is not None:
            dictionary['recurrenceType'] = self.recurrence_type
        if self.return_url is not None:
            dictionary['returnUrl'] = self.return_url
        if self.signature_type is not None:
            dictionary['signatureType'] = self.signature_type
        if self.unique_mandate_reference is not None:
            dictionary['uniqueMandateReference'] = self.unique_mandate_reference
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreateMandateRequest':
        super().from_dictionary(dictionary)
        if 'alias' in dictionary:
            self.alias = dictionary['alias']
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = MandateCustomer()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'customerReference' in dictionary:
            self.customer_reference = dictionary['customerReference']
        if 'language' in dictionary:
            self.language = dictionary['language']
        if 'recurrenceType' in dictionary:
            self.recurrence_type = dictionary['recurrenceType']
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        if 'signatureType' in dictionary:
            self.signature_type = dictionary['signatureType']
        if 'uniqueMandateReference' in dictionary:
            self.unique_mandate_reference = dictionary['uniqueMandateReference']
        return self
