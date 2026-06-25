from onlinepayments.sdk.domain.create_mandate_request import CreateMandateRequest
from onlinepayments.sdk.domain.mandate_customer import MandateCustomer
from onlinepayments.sdk.domain.bank_account_iban import BankAccountIban
from onlinepayments.sdk.domain.mandate_contact_details import MandateContactDetails
from onlinepayments.sdk.domain.mandate_address import MandateAddress
from onlinepayments.sdk.domain.mandate_personal_information import MandatePersonalInformation
from onlinepayments.sdk.domain.mandate_personal_name import MandatePersonalName


class CreateMandateRequestBuilder:

    def __init__(self):
        self._alias = "Test Mandate"
        self._customer_iban = "BE45000253450589"
        self._company_name = "BEL Labs"
        self._email_address = "wile.e.coyote@acmelabs.com"
        self._city = "Brussels"
        self._country_code = "BE"
        self._house_number = "3"
        self._street = "Da Vincilaan"
        self._zip = "1930"
        self._first_name = "Jane"
        self._surname = "Doe"
        self._title = "Mrs"
        self._customer_reference = "CUST123"
        self._recurrence_type = "UNIQUE"
        self._signature_type = "UNSIGNED"
        self._return_url = "https://example-mandate-signing-url.com"
        self._unique_mandate_reference = "MANDATE123"

    def with_alias(self, alias):
        self._alias = alias
        return self

    def with_customer_iban(self, customer_iban):
        self._customer_iban = customer_iban
        return self

    def with_company_name(self, company_name):
        self._company_name = company_name
        return self

    def with_email_address(self, email_address):
        self._email_address = email_address
        return self

    def with_city(self, city):
        self._city = city
        return self

    def with_country_code(self, country_code):
        self._country_code = country_code
        return self

    def with_house_number(self, house_number):
        self._house_number = house_number
        return self

    def with_street(self, street):
        self._street = street
        return self

    def with_zip(self, zip_code):
        self._zip = zip_code
        return self

    def with_first_name(self, first_name):
        self._first_name = first_name
        return self

    def with_surname(self, surname):
        self._surname = surname
        return self

    def with_title(self, title):
        self._title = title
        return self

    def with_customer_reference(self, customer_reference):
        self._customer_reference = customer_reference
        return self

    def with_recurrence_type(self, recurrence_type):
        self._recurrence_type = recurrence_type
        return self

    def with_signature_type(self, signature_type):
        self._signature_type = signature_type
        return self

    def with_return_url(self, return_url):
        self._return_url = return_url
        return self

    def with_unique_mandate_reference(self, unique_mandate_reference):
        self._unique_mandate_reference = unique_mandate_reference
        return self

    def build(self):
        bank_account = BankAccountIban()
        bank_account.iban = self._customer_iban

        contact_details = MandateContactDetails()
        contact_details.email_address = self._email_address

        address = MandateAddress()
        address.city = self._city
        address.country_code = self._country_code
        address.house_number = self._house_number
        address.street = self._street
        address.zip = self._zip

        name = MandatePersonalName()
        name.first_name = self._first_name
        name.surname = self._surname

        personal_info = MandatePersonalInformation()
        personal_info.name = name
        personal_info.title = self._title

        customer = MandateCustomer()
        customer.bank_account_iban = bank_account
        customer.company_name = self._company_name
        customer.contact_details = contact_details
        customer.mandate_address = address
        customer.personal_information = personal_info

        request = CreateMandateRequest()
        request.alias = self._alias
        request.customer = customer
        request.customer_reference = self._customer_reference
        request.recurrence_type = self._recurrence_type
        request.signature_type = self._signature_type
        request.return_url = self._return_url
        request.unique_mandate_reference = self._unique_mandate_reference

        return request
