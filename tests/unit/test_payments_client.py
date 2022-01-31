import os
import unittest
from unittest.mock import MagicMock, patch

from onlinepayments.sdk.api_exception import ApiException
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.communication_exception import CommunicationException
from onlinepayments.sdk.communicator import Communicator
from onlinepayments.sdk.connection import Connection
from onlinepayments.sdk.declined_payment_exception import DeclinedPaymentException
from onlinepayments.sdk.defaultimpl.default_authenticator import DefaultAuthenticator
from onlinepayments.sdk.domain.address import Address
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.card import Card
from onlinepayments.sdk.domain.card_payment_method_specific_input import CardPaymentMethodSpecificInput
from onlinepayments.sdk.domain.create_payment_request import CreatePaymentRequest
from onlinepayments.sdk.domain.customer import Customer
from onlinepayments.sdk.domain.order import Order
from onlinepayments.sdk.factory import Factory
from onlinepayments.sdk.idempotence_exception import IdempotenceException
from onlinepayments.sdk.meta_data_provider import MetaDataProvider
from onlinepayments.sdk.not_found_exception import NotFoundException
from onlinepayments.sdk.reference_exception import ReferenceException
from onlinepayments.sdk.response_exception import ResponseException
from onlinepayments.sdk.validation_exception import ValidationException
from tests import file_utils


class PaymentsClientTest(unittest.TestCase):
    """Tests that a payment created in a merchant of a client result in appropriate POST requests being created"""

    @patch.multiple(Connection, __abstractmethods__=set())
    def setUp(self):
        self.mock_connection = MagicMock(spec=Connection(), autospec=True)
        self.communicator = Communicator(
            api_endpoint="http://localhost",
            authenticator=DefaultAuthenticator("admin", "admin"),
            meta_data_provider=MetaDataProvider("OnlinePayments"),
            connection=self.mock_connection)

    def test_create_success(self):
        """Tests that a payment can be created and communicated appropriately when responded to with a 201 message"""
        client = Factory.create_client_from_communicator(self.communicator)
        response_body = read_resource("pending_capture.json")
        request_body = create_request()

        def receive_post(uri, request_headers, body):
            def generate_body():
                for start in range(0, len(response_body), 1024):
                    yield response_body[start: start + 1024].encode('utf-8')

            return 201, None, generate_body()

        self.mock_connection.post.side_effect = receive_post

        response = client.merchant("merchantId").payments().create_payment(request_body)

        self.assertEqual("1_1", response.payment.id)
        self.assertEqual("PENDING_CAPTURE", response.payment.status)

    def test_create_rejected(self):
        """Tests that a 400 failure response with a payment result will throw a DeclinedPaymentException"""
        client = Factory.create_client_from_communicator(self.communicator)
        response_body = read_resource("rejected.json")
        request_body = create_request()

        def receive_post(uri, request_headers, body):
            def generate_response():
                for start in range(0, len(response_body), 1024):
                    yield response_body[start: start + 1024].encode('utf-8')

            return 400, None, generate_response()

        self.mock_connection.post.side_effect = receive_post

        with self.assertRaises(DeclinedPaymentException) as context:
            client.merchant("merchantId").payments().create_payment(request_body)
        self.assertIn("payment '1_1'", str(context.exception.args))
        self.assertIn("status 'REJECTED'", str(context.exception))
        self.assertIn(response_body, str(context.exception))
        self.assertIsNotNone(context.exception.create_payment_result)
        self.assertEqual("1_1", context.exception.create_payment_result.payment.id)
        self.assertEqual("REJECTED", context.exception.create_payment_result.payment.status)

    def test_create_invalid_request(self):
        """Tests that a 400 failure response without a payment result will throw a ValidationException"""
        client = Factory.create_client_from_communicator(self.communicator)
        response_body = read_resource("invalid_request.json")
        request_body = create_request()

        def receive_post(uri, request_headers, body):
            def generate_response():
                for start in range(0, len(response_body), 1024):
                    yield response_body[start: start + 1024].encode('utf-8')

            return 400, None, generate_response()

        self.mock_connection.post.side_effect = receive_post

        with self.assertRaises(ValidationException) as exception:
            client.merchant("merchantId").payments().create_payment(request_body)
        self.assertIn(response_body, str(exception.exception))

    def test_create_invalid_authorization(self):
        """Tests that a 401 failure response without a payment result will throw an ApiException"""
        client = Factory.create_client_from_communicator(self.communicator)
        response_body = read_resource("invalid_authorization.json")
        request_body = create_request()

        def receive_post(uri, request_headers, body):
            def generate_response():
                for start in range(0, len(response_body), 1024):
                    yield response_body[start: start + 1024].encode('utf-8')

            return 401, None, generate_response()

        self.mock_connection.post.side_effect = receive_post

        with self.assertRaises(ApiException) as exception:
            client.merchant("merchantId").payments().create_payment(request_body)
        self.assertIn(response_body, str(exception.exception))

    def test_create_reference_error(self):
        """Tests that a 409 failure response with a duplicate request code
        but without an idempotence key will throw a ReferenceException
        """
        client = Factory.create_client_from_communicator(self.communicator)
        response_body = read_resource("duplicate_request.json")
        request_body = create_request()

        def receive_post(uri, request_headers, body):
            def generate_response():
                for start in range(0, len(response_body), 1024):
                    yield response_body[start: start + 1024].encode('utf-8')

            return 409, None, generate_response()

        self.mock_connection.post.side_effect = receive_post

        with self.assertRaises(ReferenceException) as exception:
            client.merchant("merchantId").payments().create_payment(request_body)
        self.assertIn(response_body, str(exception.exception))

    def test_create_idempotence_error(self):
        """Tests that a 409 failure response with a duplicate request code
        and an idempotence key will throw an IdempotenceException
        """
        client = Factory.create_client_from_communicator(self.communicator)
        response_body = read_resource("duplicate_request.json")
        request_body = create_request()
        context = CallContext("key")

        def receive_post(uri, request_headers, body):
            def generate_response():
                for start in range(0, len(response_body), 1024):
                    yield response_body[start: start + 1024].encode('utf-8')

            return 409, None, generate_response()

        self.mock_connection.post.side_effect = receive_post

        with self.assertRaises(IdempotenceException) as exception:
            client.merchant("merchantId").payments().create_payment(request_body, context)
        self.assertIn(response_body, str(exception.exception))
        self.assertEqual(context.idempotence_key, exception.exception.idempotence_key)

    def test_create_not_found(self):
        """Tests that a 404 response with a non-JSON response will throw an NotFoundException
        """
        client = Factory.create_client_from_communicator(self.communicator)
        response_body = read_resource("not_found.html")
        request_body = create_request()

        def receive_post(uri, request_headers, body):
            def generate_response():
                for start in range(0, len(response_body), 1024):
                    yield response_body[start: start + 1024].encode('utf-8')

            return 404, {"content-type": "text/html"}, generate_response()

        self.mock_connection.post.side_effect = receive_post

        with self.assertRaises(NotFoundException) as exception:
            client.merchant("merchantId").payments().create_payment(request_body)
            self.assertIsNotNone(exception.exception.cause)
        self.assertIsInstance(exception.exception.cause, ResponseException)
        self.assertIn(response_body, str(exception.exception.cause))

    def test_create_method_not_allowed(self):
        """Tests that a 405 response with a non-JSON response will throw a CommunicationException
        """
        client = Factory.create_client_from_communicator(self.communicator)
        response_body = read_resource("method_not_allowed.html")
        request_body = create_request()

        def receive_post(uri, request_headers, body):
            def generate_response():
                for start in range(0, len(response_body), 1024):
                    yield response_body[start: start + 1024].encode('utf-8')

            return 405, {"content-type": "text/html"}, generate_response()

        self.mock_connection.post.side_effect = receive_post

        with self.assertRaises(CommunicationException) as exception:
            client.merchant("merchantId").payments().create_payment(request_body)
        self.assertIsNotNone(exception.exception.cause)
        self.assertIsInstance(exception.exception.cause, ResponseException)
        self.assertIn(response_body, str(exception.exception.cause))


def create_request():
    body = CreatePaymentRequest()
    order = Order()
    amount_of_money = AmountOfMoney()
    amount_of_money.amount = 2345
    amount_of_money.currency_code = "CAD"
    customer = Customer()
    billing_address = Address()
    billing_address.county_code = "CA"
    customer.billing_address = billing_address
    order.customer = customer
    card_payment_method_specific_input = CardPaymentMethodSpecificInput()
    card_payment_method_specific_input.payment_product_id = 1
    card = Card()
    card.cvv = "123"
    card.card_number = "4567350000427977"
    card.expiry_date = "1220"
    card_payment_method_specific_input.card = card
    body.card_payment_method_specific_input = card_payment_method_specific_input
    return body


def read_resource(relative_path): return file_utils.read_file(os.path.join("payment", relative_path))


if __name__ == '__main__':
    unittest.main()
