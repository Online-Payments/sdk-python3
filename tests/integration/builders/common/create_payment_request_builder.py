import uuid

from onlinepayments.sdk.domain.address import Address
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.auto_capture import AutoCapture
from onlinepayments.sdk.domain.browser_data import BrowserData
from onlinepayments.sdk.domain.card import Card
from onlinepayments.sdk.domain.card_payment_method_specific_input import CardPaymentMethodSpecificInput
from onlinepayments.sdk.domain.company_information import CompanyInformation
from onlinepayments.sdk.domain.contact_details import ContactDetails
from onlinepayments.sdk.domain.create_payment_request import CreatePaymentRequest
from onlinepayments.sdk.domain.customer import Customer
from onlinepayments.sdk.domain.customer_account import CustomerAccount
from onlinepayments.sdk.domain.customer_account_authentication import CustomerAccountAuthentication
from onlinepayments.sdk.domain.customer_device import CustomerDevice
from onlinepayments.sdk.domain.customer_payment_activity import CustomerPaymentActivity
from onlinepayments.sdk.domain.order import Order
from onlinepayments.sdk.domain.order_references import OrderReferences
from onlinepayments.sdk.domain.payment_account_on_file import PaymentAccountOnFile
from onlinepayments.sdk.domain.personal_information import PersonalInformation
from onlinepayments.sdk.domain.personal_name import PersonalName
from onlinepayments.sdk.domain.redirect_payment_method_specific_input import RedirectPaymentMethodSpecificInput


class CreatePaymentRequestBuilder:

    CARD = "CARD"
    PAYPAL_REDIRECT = "PAYPAL_REDIRECT"

    def __init__(self):
        self._card_number = "4012000033330026"
        self._cvv = "123"
        self._expiry_date = "0530"
        self._cardholder_name = "Wile E. Coyote"
        self._amount = 1000
        self._currency = "EUR"
        self._merchant_reference = "Ref-" + str(uuid.uuid4())
        self._merchant_customer_id = "CUST-000001"
        self._token = None
        self._payment_method_type = self.CARD
        self._auto_capture = False

    def with_card_number(self, card_number):
        self._card_number = card_number
        return self

    def with_cvv(self, cvv):
        self._cvv = cvv
        return self

    def with_expiry_date(self, expiry_date):
        self._expiry_date = expiry_date
        return self

    def with_cardholder_name(self, cardholder_name):
        self._cardholder_name = cardholder_name
        return self

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

    def with_token(self, token):
        self._token = token
        return self

    def with_card_payment_method(self):
        self._payment_method_type = self.CARD
        return self

    def with_pay_pal_redirect_payment_method(self):
        self._payment_method_type = self.PAYPAL_REDIRECT
        return self

    def with_auto_capture(self, auto_capture):
        self._auto_capture = auto_capture
        return self

    def build(self):
        request = CreatePaymentRequest()

        if self._payment_method_type == self.CARD:
            if self._token is not None:
                request.card_payment_method_specific_input = self._build_card_payment_input_with_token()
            else:
                request.card_payment_method_specific_input = self._build_card_payment_input_with_card()
            request.order = self._build_card_order()
        else:
            request.redirect_payment_method_specific_input = self._build_redirect_payment_input()
            request.order = self._build_pay_pal_order()

        return request

    def _build_card_payment_input_with_token(self):
        card_input = self._build_card_payment_input()
        card_input.token = self._token

        return card_input

    def _build_card_payment_input_with_card(self):
        card_input = self._build_card_payment_input()
        card_input.card = self._build_card()

        return card_input

    def _build_card_payment_input(self):
        card_input = CardPaymentMethodSpecificInput()
        card_input.payment_product_id = 1
        card_input.authorization_mode = "FINAL_AUTHORIZATION"
        card_input.transaction_channel = "ECOMMERCE"
        card_input.return_url = "https://example.com/return"
        if self._auto_capture:
            auto_capture = AutoCapture()
            auto_capture.delay_in_minutes = 10
            card_input.auto_capture = auto_capture

        return card_input

    def _build_redirect_payment_input(self):
        redirect_input = RedirectPaymentMethodSpecificInput()
        redirect_input.payment_product_id = 840

        return redirect_input

    def _build_card(self):
        card = Card()
        card.card_number = self._card_number
        card.cardholder_name = self._cardholder_name
        card.cvv = self._cvv
        card.expiry_date = self._expiry_date

        return card

    def _build_card_order(self):
        order = Order()
        order.amount_of_money = self._build_amount_of_money()
        order.customer = self._build_customer()
        order.references = self._build_order_references()

        return order

    def _build_pay_pal_order(self):
        references = self._build_order_references()
        references.descriptor = "Applefruitcompany"
        references.merchant_parameters = "SessionID=126548354&ShopperID=73541312"

        order = Order()
        order.amount_of_money = self._build_amount_of_money()
        order.references = references

        return order

    def _build_amount_of_money(self):
        amount_of_money = AmountOfMoney()
        amount_of_money.amount = self._amount
        amount_of_money.currency_code = self._currency

        return amount_of_money

    def _build_order_references(self):
        references = OrderReferences()
        references.merchant_reference = self._merchant_reference

        return references

    def _build_customer(self):
        customer = Customer()
        customer.company_information = self._build_company_information()
        customer.merchant_customer_id = self._merchant_customer_id
        customer.account = self._build_customer_account()
        customer.account_type = "existing"
        customer.billing_address = self._build_billing_address()
        customer.contact_details = self._build_contact_details()
        customer.device = self._build_customer_device()
        customer.personal_information = self._build_personal_information()

        return customer

    def _build_company_information(self):
        company_information = CompanyInformation()
        company_information.name = "CUST-000001"

        return company_information

    def _build_customer_account(self):
        authentication = CustomerAccountAuthentication()
        authentication.method = "guest"
        authentication.utc_timestamp = "202309261631"

        payment_account_on_file = PaymentAccountOnFile()
        payment_account_on_file.create_date = "20100101"
        payment_account_on_file.number_of_card_on_file_creation_attempts_last24_hours = 1

        payment_activity = CustomerPaymentActivity()
        payment_activity.number_of_payment_attempts_last24_hours = 1
        payment_activity.number_of_payment_attempts_last_year = 0
        payment_activity.number_of_purchases_last6_months = 0

        account = CustomerAccount()
        account.authentication = authentication
        account.change_date = "20200101"
        account.changed_during_checkout = True
        account.create_date = "20100101"
        account.had_suspicious_activity = False
        account.password_change_date = "20200101"
        account.password_changed_during_checkout = False
        account.payment_account_on_file = payment_account_on_file
        account.payment_activity = payment_activity

        return account

    def _build_billing_address(self):
        billing_address = Address()
        billing_address.country_code = "BE"
        billing_address.city = "Brussels"
        billing_address.house_number = "3"
        billing_address.state = "Flemish Brabant"
        billing_address.street = "Da Vincilaan"
        billing_address.zip = "1930"
        billing_address.additional_info = "floor 9"

        return billing_address

    def _build_contact_details(self):
        contact_details = ContactDetails()
        contact_details.email_address = "wile.e.coyote@acmelabs.com"
        contact_details.phone_number = "+321234567890"

        return contact_details

    def _build_customer_device(self):
        browser_data = BrowserData()
        browser_data.color_depth = 99
        browser_data.java_enabled = True
        browser_data.java_script_enabled = True
        browser_data.screen_height = "768"
        browser_data.screen_width = "1024"

        device = CustomerDevice()
        device.accept_header = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
        device.browser_data = browser_data
        device.ip_address = "123.123.123.123"
        device.locale = "en_GB"
        device.user_agent = "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/75.0.3770.142Safari/537.36"
        device.timezone_offset_utc_minutes = "-180"

        return device

    def _build_personal_information(self):
        personal_name = PersonalName()
        personal_name.title = "M."
        personal_name.first_name = "Wile"
        personal_name.surname = "Coyote"

        personal_information = PersonalInformation()
        personal_information.name = personal_name
        personal_information.gender = "male"
        personal_information.date_of_birth = "19500101"

        return personal_information
