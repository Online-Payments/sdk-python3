#
# This file was automatically generated.
#
from .bank_account_iban import BankAccountIban
from .data_object import DataObject
from .mandate_address_response import MandateAddressResponse
from .mandate_contact_details import MandateContactDetails
from .mandate_personal_information_response import MandatePersonalInformationResponse


class MandateCustomerResponse(DataObject):

    __slots__ = (
        "__bank_account_iban",
        "__company_name",
        "__contact_details",
        "__mandate_address",
        "__personal_information",
    )

    __bank_account_iban: BankAccountIban | None
    __company_name: str | None
    __contact_details: MandateContactDetails | None
    __mandate_address: MandateAddressResponse | None
    __personal_information: MandatePersonalInformationResponse | None

    def __init__(
        self,
        *,
        bank_account_iban: BankAccountIban | None = None,
        company_name: str | None = None,
        contact_details: MandateContactDetails | None = None,
        mandate_address: MandateAddressResponse | None = None,
        personal_information: MandatePersonalInformationResponse | None = None,
    ) -> None:
        self.bank_account_iban = bank_account_iban
        self.company_name = company_name
        self.contact_details = contact_details
        self.mandate_address = mandate_address
        self.personal_information = personal_information

    @property
    def bank_account_iban(self) -> BankAccountIban | None:
        """
        | Object containing IBAN information

        Type: :class:`onlinepayments.sdk.domain.bank_account_iban.BankAccountIban`
        """
        return self.__bank_account_iban

    @bank_account_iban.setter
    def bank_account_iban(self, value: BankAccountIban | None) -> None:
        self.__bank_account_iban = value

    @property
    def company_name(self) -> str | None:
        """
        | Name of company, as a customer

        Type: str
        """
        return self.__company_name

    @company_name.setter
    def company_name(self, value: str | None) -> None:
        self.__company_name = value

    @property
    def contact_details(self) -> MandateContactDetails | None:
        """
        | Object containing email address

        Type: :class:`onlinepayments.sdk.domain.mandate_contact_details.MandateContactDetails`
        """
        return self.__contact_details

    @contact_details.setter
    def contact_details(self, value: MandateContactDetails | None) -> None:
        self.__contact_details = value

    @property
    def mandate_address(self) -> MandateAddressResponse | None:
        """
        | Object containing consumer address details

        Type: :class:`onlinepayments.sdk.domain.mandate_address_response.MandateAddressResponse`
        """
        return self.__mandate_address

    @mandate_address.setter
    def mandate_address(self, value: MandateAddressResponse | None) -> None:
        self.__mandate_address = value

    @property
    def personal_information(self) -> MandatePersonalInformationResponse | None:
        """
        | Object containing personal information of the customer

        Type: :class:`onlinepayments.sdk.domain.mandate_personal_information_response.MandatePersonalInformationResponse`
        """
        return self.__personal_information

    @personal_information.setter
    def personal_information(self, value: MandatePersonalInformationResponse | None) -> None:
        self.__personal_information = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.bank_account_iban is not None:
            dictionary['bankAccountIban'] = self.bank_account_iban.to_dictionary()
        if self.company_name is not None:
            dictionary['companyName'] = self.company_name
        if self.contact_details is not None:
            dictionary['contactDetails'] = self.contact_details.to_dictionary()
        if self.mandate_address is not None:
            dictionary['mandateAddress'] = self.mandate_address.to_dictionary()
        if self.personal_information is not None:
            dictionary['personalInformation'] = self.personal_information.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MandateCustomerResponse':
        super().from_dictionary(dictionary)
        if 'bankAccountIban' in dictionary:
            if not isinstance(dictionary['bankAccountIban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountIban']))
            value = BankAccountIban()
            self.bank_account_iban = value.from_dictionary(dictionary['bankAccountIban'])
        if 'companyName' in dictionary:
            self.company_name = dictionary['companyName']
        if 'contactDetails' in dictionary:
            if not isinstance(dictionary['contactDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['contactDetails']))
            value = MandateContactDetails()
            self.contact_details = value.from_dictionary(dictionary['contactDetails'])
        if 'mandateAddress' in dictionary:
            if not isinstance(dictionary['mandateAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandateAddress']))
            value = MandateAddressResponse()
            self.mandate_address = value.from_dictionary(dictionary['mandateAddress'])
        if 'personalInformation' in dictionary:
            if not isinstance(dictionary['personalInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['personalInformation']))
            value = MandatePersonalInformationResponse()
            self.personal_information = value.from_dictionary(dictionary['personalInformation'])
        return self
