import pickle
import unittest
from unittest.mock import MagicMock, PropertyMock

from onlinepayments.sdk import exception_factory
from onlinepayments.sdk.api_exception import ApiException
from onlinepayments.sdk.authentication.authenticator import Authenticator
from onlinepayments.sdk.authorization_exception import AuthorizationException
from onlinepayments.sdk.client import Client
from onlinepayments.sdk.communication.communication_exception import CommunicationException
from onlinepayments.sdk.communication.connection import Connection
from onlinepayments.sdk.communication.i_metadata_provider import IMetadataProvider
from onlinepayments.sdk.communication.not_found_exception import NotFoundException
from onlinepayments.sdk.communication.response_exception import ResponseException
from onlinepayments.sdk.communicator import Communicator
from onlinepayments.sdk.declined_payment_exception import DeclinedPaymentException
from onlinepayments.sdk.declined_payout_exception import DeclinedPayoutException
from onlinepayments.sdk.declined_refund_exception import DeclinedRefundException
from onlinepayments.sdk.domain.api_error import APIError
from onlinepayments.sdk.domain.error_response import ErrorResponse
from onlinepayments.sdk.domain.payment_error_response import PaymentErrorResponse
from onlinepayments.sdk.domain.payout_error_response import PayoutErrorResponse
from onlinepayments.sdk.domain.problem_details_response import ProblemDetailsResponse
from onlinepayments.sdk.domain.refund_error_response import RefundErrorResponse
from onlinepayments.sdk.domain.share_payment_link_request import SharePaymentLinkRequest
from onlinepayments.sdk.idempotence_exception import IdempotenceException
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller
from onlinepayments.sdk.json.marshaller_syntax_exception import MarshallerSyntaxException
from onlinepayments.sdk.platform_exception import PlatformException
from onlinepayments.sdk.problem_details_exception import ProblemDetailsException
from onlinepayments.sdk.reference_exception import ReferenceException
from onlinepayments.sdk.validation_exception import ValidationException

JSON_HEADERS = {"Content-Type": "application/json"}
DECLINED_PAYMENT_BODY = ('{"errorId":"error-id","errors":[{"errorCode":"30511001"}],'
                         '"paymentResult":{"payment":{"id":"payment-id","status":"REJECTED"}}}')


def _api_error(error_code: str) -> APIError:
    return APIError(error_code=error_code)


def _all_api_exceptions() -> list[ApiException]:
    errors = [_api_error("1234")]
    return [
        ApiException(400, '{"cvv":"123"}', "error-id", errors),
        AuthorizationException(403, "body", "error-id", errors),
        ValidationException(400, "body", "error-id", errors),
        ReferenceException(404, "body", "error-id", errors),
        PlatformException(500, "body", "error-id", errors),
        IdempotenceException("key", 123, 409, "body", "error-id", errors),
        DeclinedPaymentException(402, DECLINED_PAYMENT_BODY,
                                 DefaultMarshaller.instance().unmarshal(DECLINED_PAYMENT_BODY, PaymentErrorResponse)),
        DeclinedPayoutException(402, "body", PayoutErrorResponse(error_id="error-id")),
        DeclinedRefundException(402, "body", RefundErrorResponse(error_id="error-id")),
        ProblemDetailsException(400, "body", ProblemDetailsResponse(title="title")),
    ]


class ApiExceptionTest(unittest.TestCase):

    def test_GettingErrors_DefaultScenario_ReturnListWhenErrorsAreNone(self):
        exception = ApiException(400, "body", "error-id", None)
        self.assertEqual([], exception.errors)
        self.assertIsInstance(exception.errors, list)

    def test_GettingErrors_DefaultScenario_ReturnListWhenErrorsAreTuple(self):
        error = _api_error("1234")
        exception = ApiException(400, "body", "error-id", (error,))
        self.assertEqual([error], exception.errors)
        self.assertIsInstance(exception.errors, list)

    def test_Pickling_DefaultScenario_PreserveAllFieldsForEveryApiException(self):
        for exception in _all_api_exceptions():
            with self.subTest(exception=type(exception).__name__):
                restored = pickle.loads(pickle.dumps(exception))
                self.assertIs(type(exception), type(restored))
                self.assertEqual(str(exception), str(restored))
                self.assertEqual(exception.status_code, restored.status_code)
                self.assertEqual(exception.response_body, restored.response_body)
                self.assertEqual(exception.error_id, restored.error_id)
                self.assertEqual([e.to_dictionary() for e in exception.errors],
                                 [e.to_dictionary() for e in restored.errors])

    def test_Pickling_DefaultScenario_PreserveSubclassSpecificFields(self):
        idempotence_exception = IdempotenceException("key", 123, 409, "body", "error-id", None)
        restored = pickle.loads(pickle.dumps(idempotence_exception))
        self.assertEqual("key", restored.idempotence_key)
        self.assertEqual(123, restored.idempotence_request_timestamp)

        payment_error_response = DefaultMarshaller.instance().unmarshal(DECLINED_PAYMENT_BODY, PaymentErrorResponse)
        declined_payment_exception = DeclinedPaymentException(402, DECLINED_PAYMENT_BODY, payment_error_response)
        restored = pickle.loads(pickle.dumps(declined_payment_exception))
        self.assertEqual("payment-id", restored.create_payment_response.payment.id)

    def test_Pickling_DefaultScenario_PreserveCommunicationExceptions(self):
        response_exception = ResponseException(500, '{"cvv":"123"}', JSON_HEADERS)
        restored = pickle.loads(pickle.dumps(response_exception))
        self.assertEqual(500, restored.status_code)
        self.assertEqual('{"cvv":"123"}', restored.body)
        self.assertEqual("application/json", restored.get_header_value("content-type"))
        self.assertEqual(str(response_exception), str(restored))

        not_found_exception = NotFoundException(response_exception, "not found")
        restored = pickle.loads(pickle.dumps(not_found_exception))
        self.assertEqual("not found", str(restored))
        self.assertEqual(500, restored.cause.status_code)

        communication_exception = CommunicationException(ValueError("connection reset"))
        restored = pickle.loads(pickle.dumps(communication_exception))
        self.assertIsInstance(restored.cause, ValueError)

        restored = pickle.loads(pickle.dumps(MarshallerSyntaxException(ValueError("invalid json"))))
        self.assertIsInstance(restored, MarshallerSyntaxException)


class ExceptionFactoryStatusCode429Test(unittest.TestCase):

    def test_CreatingException_StatusCode429_ReturnApiException(self):
        error_response = ErrorResponse(error_id="error-id", errors=[_api_error("1234")])
        exception = exception_factory.create_exception(429, "body", error_response, None)
        self.assertIs(ApiException, type(exception))
        self.assertEqual(429, exception.status_code)
        self.assertEqual("error-id", exception.error_id)


class MerchantClientStatusCode429Test(unittest.TestCase):

    def setUp(self):
        self.connection = MagicMock(spec=Connection)
        metadata_provider = MagicMock(spec=IMetadataProvider)
        type(metadata_provider).metadata_headers = PropertyMock(return_value=[])
        authenticator = MagicMock(spec=Authenticator)
        authenticator.get_authorization.return_value = "authorization"
        communicator = Communicator(api_endpoint="https://payment.preprod.online-payments.com",
                                    connection=self.connection, authenticator=authenticator,
                                    metadata_provider=metadata_provider, marshaller=DefaultMarshaller.instance())
        self.client = Client(communicator)

    def test_SharingPaymentLink_StatusCode429_RaiseApiException(self):
        body = '{"errorId":"error-id","errors":[{"errorCode":"1234","message":"Request rate threshold exceeded"}]}'
        self.connection.post.return_value = (429, JSON_HEADERS, [body.encode("utf-8")])

        with self.assertRaises(ApiException) as ctx:
            self.client.merchant("merchant-id").payment_links().share("link-id", SharePaymentLinkRequest())

        self.assertIs(ApiException, type(ctx.exception))
        self.assertEqual(429, ctx.exception.status_code)
        self.assertEqual("error-id", ctx.exception.error_id)


if __name__ == '__main__':
    unittest.main()
