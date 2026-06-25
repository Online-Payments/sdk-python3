import uuid

from onlinepayments.sdk.domain.address import Address
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.card_payment_method_specific_input_for_hosted_checkout import CardPaymentMethodSpecificInputForHostedCheckout
from onlinepayments.sdk.domain.contact_details import ContactDetails
from onlinepayments.sdk.domain.create_hosted_checkout_request import CreateHostedCheckoutRequest
from onlinepayments.sdk.domain.customer import Customer
from onlinepayments.sdk.domain.hosted_checkout_specific_input import HostedCheckoutSpecificInput
from onlinepayments.sdk.domain.mobile_payment_method_hosted_checkout_specific_input import MobilePaymentMethodHostedCheckoutSpecificInput
from onlinepayments.sdk.domain.order import Order
from onlinepayments.sdk.domain.order_references import OrderReferences
from onlinepayments.sdk.domain.personal_information import PersonalInformation
from onlinepayments.sdk.domain.personal_name import PersonalName
from onlinepayments.sdk.domain.redirect_payment_method_specific_input import RedirectPaymentMethodSpecificInput
from onlinepayments.sdk.domain.sepa_direct_debit_payment_method_specific_input_base import SepaDirectDebitPaymentMethodSpecificInputBase


class CreateHostedCheckoutRequestBuilder:

    def __init__(self):
        self._amount = 1000
        self._currency = "EUR"
        self._merchant_reference = "Ord-" + str(uuid.uuid4())
        self._merchant_customer_id = "CUST-000001"
        self._locale = "en_US"
        self._return_url = "https://example.com/return"
        self._show_result_page = True
        self._session_timeout = 600
        self._allowed_number_of_payment_attempts = 10
        self._is_recurring = False
        self._is_new_unscheduled_card_on_file_series = False
        self._variant = None
        self._tokens = None
        self._country_code = "US"
        self._first_name = "Test"
        self._surname = "User"
        self._title = None
        self._email_address = None
        self._phone_number = None
        self._city = None
        self._street = None
        self._house_number = None
        self._additional_info = None
        self._state = None
        self._zip = None
        self._payment_product_filters = None
        self._split_payment_product_filters = None
        self._feedbacks = None
        self._fraud_fields = None
        self._card_click_to_pay = False
        self._card_group_cards = False
        self._redirect_payment_product_id = 3
        self._sepa_payment_product_id = 771
        self._mobile_payment_product_id = None
        self._use_redirect_payment = False
        self._use_sepa_payment = False
        self._use_mobile_payment = False

    def with_amount(self, amount):
        self._amount = amount
        return self

    def with_currency(self, currency):
        self._currency = currency
        return self

    def with_merchant_reference(self, merchant_reference):
        self._merchant_reference = merchant_reference
        return self

    def with_merchant_customer_id(self, merchant_customer_id):
        self._merchant_customer_id = merchant_customer_id
        return self

    def with_locale(self, locale):
        self._locale = locale
        return self

    def with_return_url(self, return_url):
        self._return_url = return_url
        return self

    def with_show_result_page(self, show_result_page):
        self._show_result_page = show_result_page
        return self

    def with_session_timeout(self, session_timeout):
        self._session_timeout = session_timeout
        return self

    def with_allowed_number_of_payment_attempts(self, allowed_number_of_payment_attempts):
        self._allowed_number_of_payment_attempts = allowed_number_of_payment_attempts
        return self

    def with_is_recurring(self, is_recurring):
        self._is_recurring = is_recurring
        return self

    def with_is_new_unscheduled_card_on_file_series(self, is_new_unscheduled_card_on_file_series):
        self._is_new_unscheduled_card_on_file_series = is_new_unscheduled_card_on_file_series
        return self

    def with_variant(self, variant):
        self._variant = variant
        return self

    def with_tokens(self, tokens):
        self._tokens = tokens
        return self

    def with_country_code(self, country_code):
        self._country_code = country_code
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

    def with_email_address(self, email_address):
        self._email_address = email_address
        return self

    def with_phone_number(self, phone_number):
        self._phone_number = phone_number
        return self

    def with_city(self, city):
        self._city = city
        return self

    def with_street(self, street):
        self._street = street
        return self

    def with_house_number(self, house_number):
        self._house_number = house_number
        return self

    def with_additional_info(self, additional_info):
        self._additional_info = additional_info
        return self

    def with_state(self, state):
        self._state = state
        return self

    def with_zip(self, zip_code):
        self._zip = zip_code
        return self

    def with_payment_product_filters(self, payment_product_filters):
        self._payment_product_filters = payment_product_filters
        return self

    def with_split_payment_product_filters(self, split_payment_product_filters):
        self._split_payment_product_filters = split_payment_product_filters
        return self

    def with_feedbacks(self, feedbacks):
        self._feedbacks = feedbacks
        return self

    def with_fraud_fields(self, fraud_fields):
        self._fraud_fields = fraud_fields
        return self

    def with_card_click_to_pay(self, card_click_to_pay):
        self._card_click_to_pay = card_click_to_pay
        return self

    def with_card_group_cards(self, card_group_cards):
        self._card_group_cards = card_group_cards
        return self

    def build(self):
        request = CreateHostedCheckoutRequest()
        request.hosted_checkout_specific_input = self._build_hosted_checkout_specific_input()
        request.order = self._build_order()

        if self._use_redirect_payment:
            request.redirect_payment_method_specific_input = self._build_redirect_payment_input()
        elif self._use_sepa_payment:
            request.sepa_direct_debit_payment_method_specific_input = self._build_sepa_payment_input()
        elif self._use_mobile_payment:
            request.mobile_payment_method_specific_input = self._build_mobile_payment_input()

        if self._feedbacks is not None:
            request.feedbacks = self._feedbacks

        if self._fraud_fields is not None:
            request.fraud_fields = self._fraud_fields

        return request

    def _build_hosted_checkout_specific_input(self):
        input_ = HostedCheckoutSpecificInput()
        input_.locale = self._locale
        input_.return_url = self._return_url
        input_.show_result_page = self._show_result_page
        input_.session_timeout = self._session_timeout
        input_.allowed_number_of_payment_attempts = self._allowed_number_of_payment_attempts
        input_.is_recurring = self._is_recurring
        input_.is_new_unscheduled_card_on_file_series = self._is_new_unscheduled_card_on_file_series

        if self._variant is not None:
            input_.variant = self._variant

        if self._tokens is not None:
            input_.tokens = self._tokens

        if not self._use_redirect_payment and not self._use_sepa_payment and not self._use_mobile_payment:
            input_.card_payment_method_specific_input = self._build_card_payment_input()

        if self._payment_product_filters is not None:
            input_.payment_product_filters = self._payment_product_filters

        if self._split_payment_product_filters is not None:
            input_.split_payment_product_filters = self._split_payment_product_filters

        return input_

    def _build_card_payment_input(self):
        card_input = CardPaymentMethodSpecificInputForHostedCheckout()
        card_input.click_to_pay = self._card_click_to_pay
        card_input.group_cards = self._card_group_cards

        return card_input

    def _build_redirect_payment_input(self):
        redirect_input = RedirectPaymentMethodSpecificInput()
        redirect_input.payment_product_id = self._redirect_payment_product_id

        return redirect_input

    def _build_sepa_payment_input(self):
        sepa_input = SepaDirectDebitPaymentMethodSpecificInputBase()
        sepa_input.payment_product_id = self._sepa_payment_product_id

        return sepa_input

    def _build_mobile_payment_input(self):
        mobile_input = MobilePaymentMethodHostedCheckoutSpecificInput()
        mobile_input.payment_product_id = self._mobile_payment_product_id

        return mobile_input

    def _build_order(self):
        order = Order()
        order.amount_of_money = self._build_amount_of_money()
        order.customer = self._build_customer()
        order.references = self._build_order_references()

        return order

    def _build_amount_of_money(self):
        amount = AmountOfMoney()
        amount.amount = self._amount
        amount.currency_code = self._currency

        return amount

    def _build_order_references(self):
        references = OrderReferences()
        references.merchant_reference = self._merchant_reference

        return references

    def _build_customer(self):
        customer = Customer()
        customer.merchant_customer_id = self._merchant_customer_id
        customer.billing_address = self._build_billing_address()

        if self._first_name is not None or self._surname is not None:
            customer.personal_information = self._build_personal_information()

        if self._email_address is not None or self._phone_number is not None:
            customer.contact_details = self._build_contact_details()

        return customer

    def _build_billing_address(self):
        address = Address()
        address.country_code = self._country_code

        if self._city is not None:
            address.city = self._city

        if self._street is not None:
            address.street = self._street

        if self._house_number is not None:
            address.house_number = self._house_number

        if self._additional_info is not None:
            address.additional_info = self._additional_info

        if self._state is not None:
            address.state = self._state

        if self._zip is not None:
            address.zip = self._zip

        return address

    def _build_personal_information(self):
        personal_info = PersonalInformation()
        personal_info.name = self._build_personal_name()

        return personal_info

    def _build_personal_name(self):
        name = PersonalName()
        name.first_name = self._first_name
        name.surname = self._surname

        if self._title is not None:
            name.title = self._title

        return name

    def _build_contact_details(self):
        details = ContactDetails()

        if self._email_address is not None:
            details.email_address = self._email_address

        if self._phone_number is not None:
            details.phone_number = self._phone_number

        return details
