# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RedirectPaymentProduct3302SpecificInput(DataObject):

    __organization_entity_type: Optional[str] = None
    __organization_registration_id: Optional[str] = None
    __vat_id: Optional[str] = None

    @property
    def organization_entity_type(self) -> Optional[str]:
        """
        | This parameter defines the legal form of a business  and is mandatory in B2B transactions,  Accurate classification ensures compliance and optimized payment handling.

        Type: str
        """
        return self.__organization_entity_type

    @organization_entity_type.setter
    def organization_entity_type(self, value: Optional[str]) -> None:
        self.__organization_entity_type = value

    @property
    def organization_registration_id(self) -> Optional[str]:
        """
        | Unique identifier given by relevant authority verifying a business's legal registration. Mandatory in B2B transactions

        Type: str
        """
        return self.__organization_registration_id

    @organization_registration_id.setter
    def organization_registration_id(self, value: Optional[str]) -> None:
        self.__organization_registration_id = value

    @property
    def vat_id(self) -> Optional[str]:
        """
        | Tax identification number used to validate a business's VAT compliance. Mandatory in B2B transactions

        Type: str
        """
        return self.__vat_id

    @vat_id.setter
    def vat_id(self, value: Optional[str]) -> None:
        self.__vat_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct3302SpecificInput, self).to_dictionary()
        if self.organization_entity_type is not None:
            dictionary['organizationEntityType'] = self.organization_entity_type
        if self.organization_registration_id is not None:
            dictionary['organizationRegistrationId'] = self.organization_registration_id
        if self.vat_id is not None:
            dictionary['vatId'] = self.vat_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct3302SpecificInput':
        super(RedirectPaymentProduct3302SpecificInput, self).from_dictionary(dictionary)
        if 'organizationEntityType' in dictionary:
            self.organization_entity_type = dictionary['organizationEntityType']
        if 'organizationRegistrationId' in dictionary:
            self.organization_registration_id = dictionary['organizationRegistrationId']
        if 'vatId' in dictionary:
            self.vat_id = dictionary['vatId']
        return self
