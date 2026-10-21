import unittest
import uuid

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.payments.cancel_payment_request_builder import CancelPaymentRequestBuilder
from tests.integration.builders.payments.capture_payment_request_builder import CapturePaymentRequestBuilder
from tests.integration.builders.preauthorization.increment_authorization_request_builder import IncrementAuthorizationRequestBuilder
from tests.integration.builders.preauthorization.update_authorization_additional_data_request_builder import UpdateAuthorizationAdditionalDataRequestBuilder
from tests.integration.sdk_test_helper import (
    create_mastercard_payment_and_get_id,
    create_pre_authorized_mastercard_payment_and_get_id,
    create_pre_authorized_payment_and_get_id
)
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.domain.increment_authorization_request import IncrementAuthorizationRequest
from onlinepayments.sdk.domain.update_authorization_additional_data_request import UpdateAuthorizationAdditionalDataRequest
from onlinepayments.sdk.reference_exception import ReferenceException
from onlinepayments.sdk.validation_exception import ValidationException

NON_EXISTING_PAYMENT_ID = "9999999999_0"
CURRENCY_CODE = "EUR"
PAYMENT_AMOUNT = 1000
INCREMENTED_AMOUNT = 1500


class PreAuthorizationIntegrationTest(unittest.TestCase):

    def setUp(self):
        self._client_ctx = init_utils.create_client()
        self.client = self._client_ctx.__enter__()

    def tearDown(self):
        self._client_ctx.__exit__(None, None, None)

    """Test increment authorization"""

    def test_increment_authorization_pre_authorized_payment_returns_incremented_payment(self):
        payment_id = create_pre_authorized_mastercard_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)
        request = IncrementAuthorizationRequestBuilder() \
            .with_amount(INCREMENTED_AMOUNT) \
            .build()

        response = self.client.merchant(MERCHANT_ID).pre_authorization().increment_authorization(payment_id, request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment)
        self.assertIsNotNone(response.payment.id)
        self.assertEqual("PENDING_CAPTURE", response.payment.status)

        payment = self.client.merchant(MERCHANT_ID).payments().get_payment(payment_id)

        self.assertIsNotNone(payment)
        self.assertEqual("PENDING_CAPTURE", payment.status)
        self.assertIsNotNone(payment.payment_output)
        self.assertIsNotNone(payment.payment_output.amount_of_money)
        self.assertEqual(INCREMENTED_AMOUNT, payment.payment_output.amount_of_money.amount)

    def test_increment_authorization_with_call_context_returns_incremented_payment(self):
        payment_id = create_pre_authorized_mastercard_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)
        request = IncrementAuthorizationRequestBuilder() \
            .with_amount(INCREMENTED_AMOUNT) \
            .build()
        context = CallContext(idempotence_key="test-increment-authorization-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).pre_authorization().increment_authorization(payment_id, request, context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment)
        self.assertIsNotNone(response.payment.id)
        self.assertEqual("PENDING_CAPTURE", response.payment.status)

        payment = self.client.merchant(MERCHANT_ID).payments().get_payment(payment_id)

        self.assertIsNotNone(payment)
        self.assertEqual("PENDING_CAPTURE", payment.status)
        self.assertIsNotNone(payment.payment_output)
        self.assertIsNotNone(payment.payment_output.amount_of_money)
        self.assertEqual(INCREMENTED_AMOUNT, payment.payment_output.amount_of_money.amount)

    def test_increment_authorization_twice_returns_cumulative_amount(self):
        payment_id = create_pre_authorized_mastercard_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)

        first_response = self.client.merchant(MERCHANT_ID).pre_authorization().increment_authorization(
            payment_id, IncrementAuthorizationRequestBuilder().with_amount(1300).build()
        )

        self.assertIsNotNone(first_response)
        self.assertIsNotNone(first_response.payment)

        second_response = self.client.merchant(MERCHANT_ID).pre_authorization().increment_authorization(
            payment_id, IncrementAuthorizationRequestBuilder().with_amount(INCREMENTED_AMOUNT).build()
        )

        self.assertIsNotNone(second_response)
        self.assertIsNotNone(second_response.payment)

        payment = self.client.merchant(MERCHANT_ID).payments().get_payment(payment_id)

        self.assertIsNotNone(payment)
        self.assertEqual("PENDING_CAPTURE", payment.status)
        self.assertIsNotNone(payment.payment_output)
        self.assertIsNotNone(payment.payment_output.amount_of_money)
        self.assertEqual(INCREMENTED_AMOUNT, payment.payment_output.amount_of_money.amount)

    def test_increment_authorization_then_capture_incremented_amount_returns_captured_payment(self):
        payment_id = create_pre_authorized_mastercard_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)

        self.client.merchant(MERCHANT_ID).pre_authorization().increment_authorization(
            payment_id, IncrementAuthorizationRequestBuilder().with_amount(INCREMENTED_AMOUNT).build()
        )

        capture_request = CapturePaymentRequestBuilder() \
            .with_amount(INCREMENTED_AMOUNT) \
            .with_is_final(True) \
            .build()

        response = self.client.merchant(MERCHANT_ID).payments().capture_payment(payment_id, capture_request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertEqual("CAPTURE_REQUESTED", response.status)

    def test_increment_authorization_invalid_payment_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException) as raised:
            self.client.merchant(MERCHANT_ID).pre_authorization().increment_authorization(
                NON_EXISTING_PAYMENT_ID, IncrementAuthorizationRequestBuilder().build()
            )

        self.assertEqual(404, raised.exception.status_code)

    def test_increment_authorization_without_amount_of_money_raises_validation_exception(self):
        payment_id = create_pre_authorized_mastercard_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).pre_authorization().increment_authorization(
                payment_id, IncrementAuthorizationRequest()
            )

    def test_increment_authorization_zero_amount_raises_validation_exception(self):
        payment_id = create_pre_authorized_mastercard_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).pre_authorization().increment_authorization(
                payment_id, IncrementAuthorizationRequestBuilder().with_amount(0).build()
            )

    def test_increment_authorization_different_currency_raises_validation_exception(self):
        payment_id = create_pre_authorized_mastercard_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).pre_authorization().increment_authorization(
                payment_id, IncrementAuthorizationRequestBuilder().with_currency("USD").build()
            )

    def test_increment_authorization_final_authorization_payment_raises_validation_exception(self):
        payment_id = create_mastercard_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).pre_authorization().increment_authorization(
                payment_id, IncrementAuthorizationRequestBuilder().build()
            )

    def test_increment_authorization_after_capture_raises_validation_exception(self):
        payment_id = create_pre_authorized_mastercard_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)

        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).pre_authorization().increment_authorization(
                payment_id, IncrementAuthorizationRequestBuilder().build()
            )

    def test_increment_authorization_after_cancel_raises_validation_exception(self):
        payment_id = create_pre_authorized_mastercard_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)

        self.client.merchant(MERCHANT_ID).payments().cancel_payment(
            payment_id, CancelPaymentRequestBuilder().build()
        )

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).pre_authorization().increment_authorization(
                payment_id, IncrementAuthorizationRequestBuilder().build()
            )

    """Test add authorization details"""

    def test_add_authorization_details_full_car_rental_data_returns_payment(self):
        payment_id = create_pre_authorized_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)

        response = self.client.merchant(MERCHANT_ID).pre_authorization().add_authorization_details(
            payment_id, UpdateAuthorizationAdditionalDataRequestBuilder().build()
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment)
        self.assertIsNotNone(response.payment.id)
        self.assertEqual("PENDING_CAPTURE", response.payment.status)

    def test_add_authorization_details_minimal_car_rental_data_returns_payment(self):
        payment_id = create_pre_authorized_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)
        request = UpdateAuthorizationAdditionalDataRequestBuilder() \
            .with_minimal_car_rental_data() \
            .build()

        response = self.client.merchant(MERCHANT_ID).pre_authorization().add_authorization_details(payment_id, request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment)
        self.assertIsNotNone(response.payment.id)
        self.assertEqual("PENDING_CAPTURE", response.payment.status)

    def test_add_authorization_details_with_call_context_returns_payment(self):
        payment_id = create_pre_authorized_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)
        context = CallContext(idempotence_key="test-authorization-details-" + str(uuid.uuid4()))

        response = self.client.merchant(MERCHANT_ID).pre_authorization().add_authorization_details(
            payment_id, UpdateAuthorizationAdditionalDataRequestBuilder().build(), context
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment)
        self.assertIsNotNone(response.payment.id)
        self.assertEqual("PENDING_CAPTURE", response.payment.status)

    def test_add_authorization_details_then_capture_returns_captured_payment(self):
        payment_id = create_pre_authorized_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)

        self.client.merchant(MERCHANT_ID).pre_authorization().add_authorization_details(
            payment_id, UpdateAuthorizationAdditionalDataRequestBuilder().build()
        )

        response = self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertEqual("CAPTURE_REQUESTED", response.status)

    def test_add_authorization_details_invalid_payment_id_raises_reference_exception(self):
        with self.assertRaises(ReferenceException) as raised:
            self.client.merchant(MERCHANT_ID).pre_authorization().add_authorization_details(
                NON_EXISTING_PAYMENT_ID, UpdateAuthorizationAdditionalDataRequestBuilder().build()
            )

        self.assertEqual(404, raised.exception.status_code)

    def test_add_authorization_details_without_car_rental_data_raises_validation_exception(self):
        payment_id = create_pre_authorized_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).pre_authorization().add_authorization_details(
                payment_id, UpdateAuthorizationAdditionalDataRequest()
            )

    def test_add_authorization_details_invalid_car_rental_data_raises_validation_exception(self):
        payment_id = create_pre_authorized_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)
        request = UpdateAuthorizationAdditionalDataRequestBuilder() \
            .with_charges_category("invalid") \
            .build()

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).pre_authorization().add_authorization_details(payment_id, request)

    def test_add_authorization_details_after_capture_raises_validation_exception(self):
        payment_id = create_pre_authorized_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)

        self.client.merchant(MERCHANT_ID).payments().capture_payment(
            payment_id, CapturePaymentRequestBuilder().build()
        )

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).pre_authorization().add_authorization_details(
                payment_id, UpdateAuthorizationAdditionalDataRequestBuilder().build()
            )

    def test_add_authorization_details_after_cancel_raises_validation_exception(self):
        payment_id = create_pre_authorized_payment_and_get_id(self.client, PAYMENT_AMOUNT, CURRENCY_CODE)

        self.client.merchant(MERCHANT_ID).payments().cancel_payment(
            payment_id, CancelPaymentRequestBuilder().build()
        )

        with self.assertRaises(ValidationException):
            self.client.merchant(MERCHANT_ID).pre_authorization().add_authorization_details(
                payment_id, UpdateAuthorizationAdditionalDataRequestBuilder().build()
            )


if __name__ == "__main__":
    unittest.main()
