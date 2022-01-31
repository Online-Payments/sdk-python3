# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.mandate_customer import MandateCustomer


class CreateMandateRequest(DataObject):
    """
    | Object containing information to create a SEPA Direct Debit mandate.
    """

    __alias = None
    __customer = None
    __customer_reference = None
    __language = None
    __recurrence_type = None
    __return_url = None
    __signature_type = None
    __unique_mandate_reference = None

    @property
    def alias(self) -> str:
        """
        | An alias for the mandate. This can be used to visually represent the mandate. Do not include any unmasked sensitive data in the alias. If this field is not provided the masked IBAN of the customer is used.

        Type: str
        """
        return self.__alias

    @alias.setter
    def alias(self, value: str):
        self.__alias = value

    @property
    def customer(self) -> MandateCustomer:
        """
        | Customer object containing customer specific inputs.
        | Required for Create mandate and Create payment calls.

        Type: :class:`onlinepayments.sdk.domain.mandate_customer.MandateCustomer`
        """
        return self.__customer

    @customer.setter
    def customer(self, value: MandateCustomer):
        self.__customer = value

    @property
    def customer_reference(self) -> str:
        """
        | The unique identifier of a customer

        Type: str
        """
        return self.__customer_reference

    @customer_reference.setter
    def customer_reference(self, value: str):
        self.__customer_reference = value

    @property
    def language(self) -> str:
        """
        | The language code of the customer. ISO 639-1, possible values are:
        | * de
        | * en
        | * es
        | * fr
        | * it
        | * nl
        | * si
        | * sk
        | * sv

        Type: str
        """
        return self.__language

    @language.setter
    def language(self, value: str):
        self.__language = value

    @property
    def recurrence_type(self) -> str:
        """
        | Specifies whether the mandate is for one-off or recurring payments. Possible values are:
        | * UNIQUE
        | * RECURRING

        Type: str
        """
        return self.__recurrence_type

    @recurrence_type.setter
    def recurrence_type(self, value: str):
        self.__recurrence_type = value

    @property
    def return_url(self) -> str:
        """
        | Return URL to use if the mandate signing requires redirection. Required for S2S Create Payment if and only if the signatureType is "SMS".

        Type: str
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value: str):
        self.__return_url = value

    @property
    def signature_type(self) -> str:
        """
        | Specifies whether the mandate is unsigned or signed by SMS. Possible values are:
        | * UNSIGNED
        | * SMS

        Type: str
        """
        return self.__signature_type

    @signature_type.setter
    def signature_type(self, value: str):
        self.__signature_type = value

    @property
    def unique_mandate_reference(self) -> str:
        """
        | The unique identifier of the mandate

        Type: str
        """
        return self.__unique_mandate_reference

    @unique_mandate_reference.setter
    def unique_mandate_reference(self, value: str):
        self.__unique_mandate_reference = value

    def to_dictionary(self):
        dictionary = super(CreateMandateRequest, self).to_dictionary()
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

    def from_dictionary(self, dictionary):
        super(CreateMandateRequest, self).from_dictionary(dictionary)
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
