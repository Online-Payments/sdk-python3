# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.mandate_customer_response import MandateCustomerResponse


class MandateResponse(DataObject):
    """
    | Object containing the created mandate.
    """

    __alias = None
    __customer = None
    __customer_reference = None
    __mandate_pdf = None
    __recurrence_type = None
    __status = None
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
    def customer(self) -> MandateCustomerResponse:
        """
        | Customer object containing customer specific outputs.

        Type: :class:`onlinepayments.sdk.domain.mandate_customer_response.MandateCustomerResponse`
        """
        return self.__customer

    @customer.setter
    def customer(self, value: MandateCustomerResponse):
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
    def mandate_pdf(self) -> str:
        """
        | The mandate PDF in base64 encoded string

        Type: str
        """
        return self.__mandate_pdf

    @mandate_pdf.setter
    def mandate_pdf(self, value: str):
        self.__mandate_pdf = value

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
    def status(self) -> str:
        """
        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: str):
        self.__status = value

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
        dictionary = super(MandateResponse, self).to_dictionary()
        if self.alias is not None:
            dictionary['alias'] = self.alias
        if self.customer is not None:
            dictionary['customer'] = self.customer.to_dictionary()
        if self.customer_reference is not None:
            dictionary['customerReference'] = self.customer_reference
        if self.mandate_pdf is not None:
            dictionary['mandatePdf'] = self.mandate_pdf
        if self.recurrence_type is not None:
            dictionary['recurrenceType'] = self.recurrence_type
        if self.status is not None:
            dictionary['status'] = self.status
        if self.unique_mandate_reference is not None:
            dictionary['uniqueMandateReference'] = self.unique_mandate_reference
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandateResponse, self).from_dictionary(dictionary)
        if 'alias' in dictionary:
            self.alias = dictionary['alias']
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = MandateCustomerResponse()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'customerReference' in dictionary:
            self.customer_reference = dictionary['customerReference']
        if 'mandatePdf' in dictionary:
            self.mandate_pdf = dictionary['mandatePdf']
        if 'recurrenceType' in dictionary:
            self.recurrence_type = dictionary['recurrenceType']
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'uniqueMandateReference' in dictionary:
            self.unique_mandate_reference = dictionary['uniqueMandateReference']
        return self
