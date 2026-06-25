import unittest

from onlinepayments.sdk.declined_payment_exception import DeclinedPaymentException
from onlinepayments.sdk.domain.payment_error_response import PaymentErrorResponse
from onlinepayments.sdk.domain.create_payment_response import CreatePaymentResponse


class DeclinedPaymentExceptionTest(unittest.TestCase):

    def test_DeclinedPaymentExceptionIsCreated_NullResponse_ReturnDefaultMessage(self):
        exception = DeclinedPaymentException(402, "body", None)
        self.assertIn("the payment platform returned a declined payment response", str(exception))

    def test_DeclinedPaymentExceptionIsCreated_ValidPaymentErrorResponse_ExposeExpectedProperties(self):
        payment_result = CreatePaymentResponse()
        response = PaymentErrorResponse()
        response.payment_result = payment_result
        exception = DeclinedPaymentException(402, '{"error":"declined"}', response)

        self.assertEqual(402, exception.status_code)
        self.assertEqual('{"error":"declined"}', exception.response_body)
        self.assertIs(payment_result, exception.create_payment_response)

    def test_GettingCreatePaymentResponse_NullResponse_ReturnNullCreatePaymentResponse(self):
        exception = DeclinedPaymentException(402, "body", None)
        self.assertIsNone(exception.create_payment_response)

    def test_GettingCreatePaymentResponse_NullPaymentResult_ReturnNullCreatePaymentResponse(self):
        response = PaymentErrorResponse()
        response.payment_result = None
        exception = DeclinedPaymentException(402, "body", response)
        self.assertIsNone(exception.create_payment_response)


if __name__ == '__main__':
    unittest.main()
