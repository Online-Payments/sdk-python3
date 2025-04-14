# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .mandate_customer_response import MandateCustomerResponse


class MandateResponse(DataObject):

    __alias: Optional[str] = None
    __customer: Optional[MandateCustomerResponse] = None
    __customer_reference: Optional[str] = None
    __mandate_pdf: Optional[str] = None
    __recurrence_type: Optional[str] = None
    __status: Optional[str] = None
    __unique_mandate_reference: Optional[str] = None

    @property
    def alias(self) -> Optional[str]:
        """
        | An alias for the mandate. This can be used to visually represent the mandate. Do not include any unmasked sensitive data in the alias. If this field is not provided the masked IBAN of the customer is used.

        Type: str
        """
        return self.__alias

    @alias.setter
    def alias(self, value: Optional[str]) -> None:
        self.__alias = value

    @property
    def customer(self) -> Optional[MandateCustomerResponse]:
        """
        | Customer object containing customer specific outputs.

        Type: :class:`onlinepayments.sdk.domain.mandate_customer_response.MandateCustomerResponse`
        """
        return self.__customer

    @customer.setter
    def customer(self, value: Optional[MandateCustomerResponse]) -> None:
        self.__customer = value

    @property
    def customer_reference(self) -> Optional[str]:
        """
        | The unique identifier of a customer

        Type: str
        """
        return self.__customer_reference

    @customer_reference.setter
    def customer_reference(self, value: Optional[str]) -> None:
        self.__customer_reference = value

    @property
    def mandate_pdf(self) -> Optional[str]:
        """
        | The mandate PDF in base64 encoded string

        Type: str
        """
        return self.__mandate_pdf

    @mandate_pdf.setter
    def mandate_pdf(self, value: Optional[str]) -> None:
        self.__mandate_pdf = value

    @property
    def recurrence_type(self) -> Optional[str]:
        """
        | Specifies whether the mandate is for one-off or recurring payments. Possible values are:
        
        * UNIQUE
        * RECURRING

        Type: str
        """
        return self.__recurrence_type

    @recurrence_type.setter
    def recurrence_type(self, value: Optional[str]) -> None:
        self.__recurrence_type = value

    @property
    def status(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: Optional[str]) -> None:
        self.__status = value

    @property
    def unique_mandate_reference(self) -> Optional[str]:
        """
        | The unique identifier of the mandate

        Type: str
        """
        return self.__unique_mandate_reference

    @unique_mandate_reference.setter
    def unique_mandate_reference(self, value: Optional[str]) -> None:
        self.__unique_mandate_reference = value

    def to_dictionary(self) -> dict:
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

    def from_dictionary(self, dictionary: dict) -> 'MandateResponse':
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
