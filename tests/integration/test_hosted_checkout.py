import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.hostedcheckout.create_hosted_checkout_request_builder import CreateHostedCheckoutRequestBuilder
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.reference_exception import ReferenceException

INVALID_HOSTED_CHECKOUT_ID = "9999999999"


class HostedCheckoutIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test create hosted checkout"""

    def test_create_hosted_checkout_with_card_returns_hosted_checkout_id(self):
        request = CreateHostedCheckoutRequestBuilder() \
            .with_first_name("John") \
            .with_surname("Doe") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_checkout_id)
        self.assertIsNotNone(response.redirect_url)
        self.assertGreater(len(response.redirect_url), 0)

    def test_create_hosted_checkout_with_customer_details_returns_hosted_checkout_id(self):
        request = CreateHostedCheckoutRequestBuilder() \
            .with_amount(5000) \
            .with_currency("EUR") \
            .with_country_code("DE") \
            .with_locale("en_GB") \
            .with_first_name("Jane") \
            .with_surname("Smith") \
            .with_email_address("jane@example.com") \
            .with_phone_number("+441234567890") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_checkout_id)
        self.assertIsNotNone(response.redirect_url)
        self.assertGreater(len(response.redirect_url), 0)

    def test_create_hosted_checkout_with_filters_returns_hosted_checkout_id(self):
        request = CreateHostedCheckoutRequestBuilder() \
            .with_first_name("Bob") \
            .with_surname("Johnson") \
            .with_amount(2500) \
            .with_currency("EUR") \
            .with_country_code("DE") \
            .with_locale("de_DE") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_checkout_id)
        self.assertIsNotNone(response.redirect_url)
        self.assertGreater(len(response.redirect_url), 0)

    def test_create_hosted_checkout_with_session_timeout_returns_hosted_checkout_id(self):
        request = CreateHostedCheckoutRequestBuilder() \
            .with_session_timeout(300) \
            .with_first_name("Alex") \
            .with_surname("Williams") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_checkout_id)
        self.assertIsNotNone(response.redirect_url)
        self.assertGreater(len(response.redirect_url), 0)

    def test_create_hosted_checkout_with_different_locales_returns_hosted_checkout_id(self):
        locales = ["en_US", "de_DE", "fr_FR", "es_ES", "it_IT", "nl_NL"]

        for locale in locales:
            request = CreateHostedCheckoutRequestBuilder() \
                .with_locale(locale) \
                .with_first_name("Test") \
                .with_surname("User") \
                .build()

            response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

            self.assertIsNotNone(response)
            self.assertIsNotNone(response.hosted_checkout_id)
            self.assertIsNotNone(response.redirect_url)
            self.assertGreater(len(response.redirect_url), 0)

    def test_create_hosted_checkout_with_custom_amount_returns_hosted_checkout_id(self):
        request = CreateHostedCheckoutRequestBuilder() \
            .with_amount(9999) \
            .with_currency("EUR") \
            .with_first_name("Rich") \
            .with_surname("Customer") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_checkout_id)
        self.assertIsNotNone(response.redirect_url)
        self.assertGreater(len(response.redirect_url), 0)

    def test_create_hosted_checkout_with_billing_address_returns_hosted_checkout_id(self):
        request = CreateHostedCheckoutRequestBuilder() \
            .with_first_name("John") \
            .with_surname("Resident") \
            .with_country_code("US") \
            .with_city("San Francisco") \
            .with_street("Main Street") \
            .with_house_number("123") \
            .with_state("CA") \
            .with_zip("94102") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_checkout_id)
        self.assertIsNotNone(response.redirect_url)
        self.assertGreater(len(response.redirect_url), 0)

    def test_create_hosted_checkout_with_click_to_pay_returns_hosted_checkout_id(self):
        request = CreateHostedCheckoutRequestBuilder() \
            .with_card_click_to_pay(True) \
            .with_first_name("ClickToPay") \
            .with_surname("Customer") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_checkout_id)
        self.assertIsNotNone(response.redirect_url)
        self.assertGreater(len(response.redirect_url), 0)

    def test_create_hosted_checkout_with_group_cards_returns_hosted_checkout_id(self):
        request = CreateHostedCheckoutRequestBuilder() \
            .with_card_group_cards(True) \
            .with_first_name("GroupCards") \
            .with_surname("Customer") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_checkout_id)
        self.assertIsNotNone(response.redirect_url)
        self.assertGreater(len(response.redirect_url), 0)

    def test_create_hosted_checkout_with_call_context_returns_hosted_checkout_id(self):
        request = CreateHostedCheckoutRequestBuilder() \
            .with_first_name("CallContext") \
            .with_surname("Test") \
            .build()

        context = CallContext(idempotence_key="test-hosted-checkout-" + str(uuid.uuid4()))
        response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_checkout_id)
        self.assertIsNotNone(response.redirect_url)
        self.assertGreater(len(response.redirect_url), 0)

    """Test get hosted checkout"""

    def test_get_hosted_checkout_returns_status(self):
        create_request = CreateHostedCheckoutRequestBuilder() \
            .with_first_name("Status") \
            .with_surname("Check") \
            .build()

        create_response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(create_request)
        hosted_checkout_id = create_response.hosted_checkout_id
        self.assertIsNotNone(hosted_checkout_id)

        get_response = self.client.merchant(MERCHANT_ID).hosted_checkout().get_hosted_checkout(hosted_checkout_id)

        self.assertIsNotNone(get_response)
        self.assertIsNotNone(get_response.status)

    def test_get_hosted_checkout_returns_created_payment_output(self):
        create_request = CreateHostedCheckoutRequestBuilder() \
            .with_amount(7500) \
            .with_currency("EUR") \
            .with_country_code("DE") \
            .with_locale("en_GB") \
            .with_first_name("Retrieve") \
            .with_surname("Payment") \
            .build()

        create_response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(create_request)
        hosted_checkout_id = create_response.hosted_checkout_id
        self.assertIsNotNone(hosted_checkout_id)

        get_response = self.client.merchant(MERCHANT_ID).hosted_checkout().get_hosted_checkout(hosted_checkout_id)

        self.assertIsNotNone(get_response)
        self.assertIsNotNone(get_response.created_payment_output)

    def test_get_hosted_checkout_invalid_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException) as raised:
            self.client.merchant(MERCHANT_ID).hosted_checkout().get_hosted_checkout(INVALID_HOSTED_CHECKOUT_ID)

        self.assertEqual(404, raised.exception.status_code)

    """Test show result page"""

    def test_create_hosted_checkout_with_result_page_hidden_returns_hosted_checkout_id(self):
        request = CreateHostedCheckoutRequestBuilder() \
            .with_show_result_page(False) \
            .with_first_name("Silent") \
            .with_surname("Payment") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_checkout_id)
        self.assertIsNotNone(response.redirect_url)
        self.assertGreater(len(response.redirect_url), 0)

    def test_create_hosted_checkout_with_result_page_shown_returns_hosted_checkout_id(self):
        request = CreateHostedCheckoutRequestBuilder() \
            .with_show_result_page(True) \
            .with_first_name("Visible") \
            .with_surname("Result") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_checkout_id)
        self.assertIsNotNone(response.redirect_url)
        self.assertGreater(len(response.redirect_url), 0)

    """Test recurring payments"""

    def test_create_recurring_hosted_checkout_returns_hosted_checkout_id(self):
        request = CreateHostedCheckoutRequestBuilder() \
            .with_is_recurring(True) \
            .with_first_name("Recurring") \
            .with_surname("Customer") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_checkout_id)
        self.assertIsNotNone(response.redirect_url)
        self.assertGreater(len(response.redirect_url), 0)

    def test_create_one_off_hosted_checkout_returns_hosted_checkout_id(self):
        request = CreateHostedCheckoutRequestBuilder() \
            .with_is_recurring(False) \
            .with_first_name("OneOff") \
            .with_surname("Payment") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_checkout_id)
        self.assertIsNotNone(response.redirect_url)
        self.assertGreater(len(response.redirect_url), 0)

    """Test tokenization"""

    def test_create_hosted_checkout_with_new_unscheduled_card_on_file_returns_hosted_checkout_id(self):
        request = CreateHostedCheckoutRequestBuilder() \
            .with_is_new_unscheduled_card_on_file_series(True) \
            .with_first_name("Card") \
            .with_surname("OnFile") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_checkout_id)
        self.assertIsNotNone(response.redirect_url)
        self.assertGreater(len(response.redirect_url), 0)

    def test_create_hosted_checkout_without_tokenization_returns_hosted_checkout_id(self):
        request = CreateHostedCheckoutRequestBuilder() \
            .with_is_new_unscheduled_card_on_file_series(False) \
            .with_first_name("No") \
            .with_surname("Token") \
            .build()

        response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.hosted_checkout_id)
        self.assertIsNotNone(response.redirect_url)
        self.assertGreater(len(response.redirect_url), 0)

    """Test multiple checkouts"""

    def test_create_multiple_hosted_checkouts_returns_hosted_checkout_ids(self):
        for i in range(3):
            request = CreateHostedCheckoutRequestBuilder() \
                .with_first_name("Batch") \
                .with_surname("Customer" + str(i)) \
                .build()

            response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

            self.assertIsNotNone(response)
            self.assertIsNotNone(response.hosted_checkout_id)
            self.assertIsNotNone(response.redirect_url)
            self.assertGreater(len(response.redirect_url), 0)

    def test_create_hosted_checkouts_with_different_amounts_returns_hosted_checkout_ids(self):
        amounts = [1000, 2500, 5000, 10000]

        for amount in amounts:
            request = CreateHostedCheckoutRequestBuilder() \
                .with_amount(amount) \
                .with_currency("EUR") \
                .with_first_name("Amount") \
                .with_surname("Test") \
                .build()

            response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

            self.assertIsNotNone(response)
            self.assertIsNotNone(response.hosted_checkout_id)
            self.assertIsNotNone(response.redirect_url)
            self.assertGreater(len(response.redirect_url), 0)

    def test_create_hosted_checkouts_with_different_currencies_returns_hosted_checkout_ids(self):
        currencies = ["EUR", "GBP", "USD", "CHF", "SEK"]

        for currency in currencies:
            request = CreateHostedCheckoutRequestBuilder() \
                .with_amount(2000) \
                .with_currency(currency) \
                .with_first_name("Currency") \
                .with_surname("Test") \
                .build()

            response = self.client.merchant(MERCHANT_ID).hosted_checkout().create_hosted_checkout(request)

            self.assertIsNotNone(response)
            self.assertIsNotNone(response.hosted_checkout_id)
            self.assertIsNotNone(response.redirect_url)
            self.assertGreater(len(response.redirect_url), 0)


if __name__ == "__main__":
    unittest.main()