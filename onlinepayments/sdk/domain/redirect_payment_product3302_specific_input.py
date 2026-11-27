#
# This file was automatically generated.
#
from .data_object import DataObject


class RedirectPaymentProduct3302SpecificInput(DataObject):

    __slots__ = (
        "__organization_entity_type",
        "__organization_registration_id",
        "__vat_id",
    )

    __organization_entity_type: str | None
    __organization_registration_id: str | None
    __vat_id: str | None

    def __init__(
        self,
        *,
        organization_entity_type: str | None = None,
        organization_registration_id: str | None = None,
        vat_id: str | None = None,
    ) -> None:
        self.organization_entity_type = organization_entity_type
        self.organization_registration_id = organization_registration_id
        self.vat_id = vat_id

    @property
    def organization_entity_type(self) -> str | None:
        """
        | This parameter defines the legal form of a business  and is mandatory in B2B transactions,  Accurate classification ensures compliance and optimized payment handling.

        Type: str
        """
        return self.__organization_entity_type

    @organization_entity_type.setter
    def organization_entity_type(self, value: str | None) -> None:
        self.__organization_entity_type = value

    @property
    def organization_registration_id(self) -> str | None:
        """
        | Unique identifier given by relevant authority verifying a business's legal registration. Mandatory in B2B transactions

        Type: str
        """
        return self.__organization_registration_id

    @organization_registration_id.setter
    def organization_registration_id(self, value: str | None) -> None:
        self.__organization_registration_id = value

    @property
    def vat_id(self) -> str | None:
        """
        | Tax identification number used to validate a business's VAT compliance. Mandatory in B2B transactions

        Type: str
        """
        return self.__vat_id

    @vat_id.setter
    def vat_id(self, value: str | None) -> None:
        self.__vat_id = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.organization_entity_type is not None:
            dictionary['organizationEntityType'] = self.organization_entity_type
        if self.organization_registration_id is not None:
            dictionary['organizationRegistrationId'] = self.organization_registration_id
        if self.vat_id is not None:
            dictionary['vatId'] = self.vat_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct3302SpecificInput':
        super().from_dictionary(dictionary)
        if 'organizationEntityType' in dictionary:
            self.organization_entity_type = dictionary['organizationEntityType']
        if 'organizationRegistrationId' in dictionary:
            self.organization_registration_id = dictionary['organizationRegistrationId']
        if 'vatId' in dictionary:
            self.vat_id = dictionary['vatId']
        return self
