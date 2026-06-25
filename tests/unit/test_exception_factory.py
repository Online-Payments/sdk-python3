import unittest

from onlinepayments.sdk import exception_factory
from onlinepayments.sdk.api_exception import ApiException
from onlinepayments.sdk.authorization_exception import AuthorizationException
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.declined_payment_exception import DeclinedPaymentException
from onlinepayments.sdk.declined_payout_exception import DeclinedPayoutException
from onlinepayments.sdk.declined_refund_exception import DeclinedRefundException
from onlinepayments.sdk.idempotence_exception import IdempotenceException
from onlinepayments.sdk.platform_exception import PlatformException
from onlinepayments.sdk.reference_exception import ReferenceException
from onlinepayments.sdk.validation_exception import ValidationException
from onlinepayments.sdk.domain.api_error import APIError
from onlinepayments.sdk.domain.create_payment_response import CreatePaymentResponse
from onlinepayments.sdk.domain.error_response import ErrorResponse
from onlinepayments.sdk.domain.payment_error_response import PaymentErrorResponse
from onlinepayments.sdk.domain.payout_error_response import PayoutErrorResponse
from onlinepayments.sdk.domain.payout_result import PayoutResult
from onlinepayments.sdk.domain.refund_error_response import RefundErrorResponse
from onlinepayments.sdk.domain.refund_response import RefundResponse


def _error_response(error_id, errors):
    r = ErrorResponse()
    r.error_id = error_id
    r.errors = errors
    return r


def _make_api_error(error_code):
    e = APIError()
    e.error_code = error_code
    return e


class ExceptionFactoryTest(unittest.TestCase):

    def test_CreatingExceptionFromPaymentErrorResponse_DefaultScenario_ReturnDeclinedPaymentExceptionWhenPaymentResultIsPresent(self):
        payment_result = CreatePaymentResponse()
        response = PaymentErrorResponse()
        response.error_id = "payment-error-id"
        response.errors = []
        response.payment_result = payment_result

        exc = exception_factory.create_exception(402, '{"error":"declined"}', response, None)

        self.assertIsInstance(exc, DeclinedPaymentException)
        self.assertEqual(402, exc.status_code)
        self.assertEqual('{"error":"declined"}', exc.response_body)
        self.assertIs(payment_result, exc.create_payment_response)

    def test_CreatingExceptionFromPaymentErrorResponse_DefaultScenario_ReturnValidationExceptionWhenPaymentResultIsAbsentAndStatusCodeIs400(self):
        errors = []
        response = PaymentErrorResponse()
        response.error_id = "payment-error-id"
        response.errors = errors
        response.payment_result = None

        exc = exception_factory.create_exception(400, '{"error":"bad request"}', response, None)

        self.assertIsInstance(exc, ValidationException)
        self.assertEqual(400, exc.status_code)
        self.assertEqual('{"error":"bad request"}', exc.response_body)
        self.assertEqual("payment-error-id", exc.error_id)
        self.assertIs(errors, exc.errors)

    def test_CreatingExceptionFromPayoutErrorResponse_DefaultScenario_ReturnDeclinedPayoutExceptionWhenPayoutResultIsPresent(self):
        payout_result = PayoutResult()
        payout_result.id = "payout-id"
        payout_result.status = "REJECTED"
        response = PayoutErrorResponse()
        response.error_id = "payout-error-id"
        response.errors = []
        response.payout_result = payout_result

        exc = exception_factory.create_exception(402, '{"error":"declined"}', response, None)

        self.assertIsInstance(exc, DeclinedPayoutException)
        self.assertEqual(402, exc.status_code)
        self.assertEqual('{"error":"declined"}', exc.response_body)
        self.assertIs(payout_result, exc.payout_result)

    def test_CreatingExceptionFromPayoutErrorResponse_DefaultScenario_ReturnValidationExceptionWhenPayoutResultIsAbsentAndStatusCodeIs400(self):
        errors = []
        response = PayoutErrorResponse()
        response.error_id = "payout-error-id"
        response.errors = errors
        response.payout_result = None

        exc = exception_factory.create_exception(400, '{"error":"bad request"}', response, None)

        self.assertIsInstance(exc, ValidationException)
        self.assertEqual(400, exc.status_code)
        self.assertEqual('{"error":"bad request"}', exc.response_body)
        self.assertEqual("payout-error-id", exc.error_id)
        self.assertIs(errors, exc.errors)

    def test_CreatingExceptionFromRefundErrorResponse_DefaultScenario_ReturnDeclinedRefundExceptionWhenRefundResultIsPresent(self):
        refund_result = RefundResponse()
        refund_result.id = "refund-id"
        refund_result.status = "REJECTED"
        response = RefundErrorResponse()
        response.error_id = "refund-error-id"
        response.errors = []
        response.refund_result = refund_result

        exc = exception_factory.create_exception(402, '{"error":"declined"}', response, None)

        self.assertIsInstance(exc, DeclinedRefundException)
        self.assertEqual(402, exc.status_code)
        self.assertEqual('{"error":"declined"}', exc.response_body)
        self.assertIs(refund_result, exc.refund_response)

    def test_CreatingExceptionFromRefundErrorResponse_DefaultScenario_ReturnValidationExceptionWhenRefundResultIsAbsentAndStatusCodeIs400(self):
        errors = []
        response = RefundErrorResponse()
        response.error_id = "refund-error-id"
        response.errors = errors
        response.refund_result = None

        exc = exception_factory.create_exception(400, '{"error":"bad request"}', response, None)

        self.assertIsInstance(exc, ValidationException)
        self.assertEqual(400, exc.status_code)
        self.assertEqual('{"error":"bad request"}', exc.response_body)
        self.assertEqual("refund-error-id", exc.error_id)
        self.assertIs(errors, exc.errors)

    def test_CreatingExceptionFromGenericErrorResponse_DefaultScenario_ReturnValidationExceptionFor400(self):
        exc = exception_factory.create_exception(
            400, '{"error":"bad request"}', _error_response("error-id", []), None
        )
        self.assertIsInstance(exc, ValidationException)

    def test_CreatingExceptionFromGenericErrorResponse_DefaultScenario_ReturnAuthorizationExceptionFor403(self):
        exc = exception_factory.create_exception(
            403, '{"error":"forbidden"}', _error_response("error-id", []), None
        )
        self.assertIsInstance(exc, AuthorizationException)

    def test_CreatingExceptionFromGenericErrorResponse_DefaultScenario_ReturnReferenceExceptionFor404(self):
        exc = exception_factory.create_exception(
            404, '{"error":"not found"}', _error_response("error-id", []), None
        )
        self.assertIsInstance(exc, ReferenceException)

    def test_CreatingExceptionFromGenericErrorResponse_DefaultScenario_ReturnReferenceExceptionFor409WhenIdempotenceConditionsAreNotMet(self):
        exc = exception_factory.create_exception(
            409, '{"error":"conflict"}', _error_response("error-id", []), None
        )
        self.assertIsInstance(exc, ReferenceException)

    def test_CreatingExceptionFromGenericErrorResponse_DefaultScenario_ReturnIdempotenceExceptionFor409WhenIdempotenceConditionsAreMet(self):
        api_error = _make_api_error("1409")
        errors = [api_error]
        context = CallContext(idempotence_key="idempotence-key")
        context.idempotence_request_timestamp = 123456789

        exc = exception_factory.create_exception(
            409, '{"error":"duplicate"}', _error_response("error-id", errors), context
        )

        self.assertIsInstance(exc, IdempotenceException)
        self.assertEqual("idempotence-key", exc.idempotence_key)
        self.assertEqual(123456789, exc.idempotence_request_timestamp)

    def test_CreatingExceptionFromGenericErrorResponse_DefaultScenario_ReturnReferenceExceptionFor409WhenContextIsNone(self):
        api_error = _make_api_error("1409")
        errors = [api_error]

        exc = exception_factory.create_exception(
            409, '{"error":"duplicate"}', _error_response("error-id", errors), None
        )
        self.assertIsInstance(exc, ReferenceException)

    def test_CreatingExceptionFromGenericErrorResponse_DefaultScenario_ReturnReferenceExceptionFor409WhenIdempotenceKeyIsMissing(self):
        api_error = _make_api_error("1409")
        errors = [api_error]
        context = CallContext()

        exc = exception_factory.create_exception(
            409, '{"error":"duplicate"}', _error_response("error-id", errors), context
        )
        self.assertIsInstance(exc, ReferenceException)

    def test_CreatingExceptionFromGenericErrorResponse_DefaultScenario_ReturnReferenceExceptionFor410(self):
        exc = exception_factory.create_exception(
            410, '{"error":"gone"}', _error_response("error-id", []), None
        )
        self.assertIsInstance(exc, ReferenceException)

    def test_CreatingExceptionFromGenericErrorResponse_DefaultScenario_ReturnPlatformExceptionFor500(self):
        exc = exception_factory.create_exception(
            500, '{"error":"platform"}', _error_response("error-id", []), None
        )
        self.assertIsInstance(exc, PlatformException)

    def test_CreatingExceptionFromGenericErrorResponse_DefaultScenario_ReturnPlatformExceptionFor502(self):
        exc = exception_factory.create_exception(
            502, '{"error":"platform"}', _error_response("error-id", []), None
        )
        self.assertIsInstance(exc, PlatformException)

    def test_CreatingExceptionFromGenericErrorResponse_DefaultScenario_ReturnPlatformExceptionFor503(self):
        exc = exception_factory.create_exception(
            503, '{"error":"platform"}', _error_response("error-id", []), None
        )
        self.assertIsInstance(exc, PlatformException)

    def test_CreatingExceptionFromGenericErrorResponse_DefaultScenario_ReturnApiExceptionForUnexpectedStatusCode(self):
        exc = exception_factory.create_exception(
            418, '{"error":"teapot"}', _error_response("error-id", []), None
        )
        self.assertIsInstance(exc, ApiException)
        self.assertNotIsInstance(exc, (ValidationException, AuthorizationException, ReferenceException, PlatformException))

    def test_CreatingExceptionFromNullErrorObject_DefaultScenario_ReturnApiException(self):
        exc = exception_factory.create_exception(418, '{"error":"unknown"}', None, None)
        self.assertIsInstance(exc, ApiException)


    def test_CreatingExceptionFromUnsupportedErrorObject_DefaultScenario_RaiseValueError(self):
        with self.assertRaises(ValueError):
            exception_factory.create_exception(400, '{"error":"unsupported"}', object(), None)

    def test_CreatingExceptionFromUnsupportedErrorObject_DefaultScenario_RaiseValueErrorDescribingUnsupportedType(self):
        class MyCustomObject:
            pass
        try:
            exception_factory.create_exception(400, "body", MyCustomObject(), None)
            self.fail("Expected ValueError")
        except ValueError as e:
            self.assertIn("MyCustomObject", str(e))


if __name__ == '__main__':
    unittest.main()
