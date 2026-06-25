import unittest

from onlinepayments.sdk.declined_refund_exception import DeclinedRefundException
from onlinepayments.sdk.domain.refund_error_response import RefundErrorResponse
from onlinepayments.sdk.domain.refund_response import RefundResponse


class DeclinedRefundExceptionTest(unittest.TestCase):

    def test_DeclinedRefundExceptionIsCreated_NullResponse_ReturnDefaultMessage(self):
        exception = DeclinedRefundException(402, "body", None)
        self.assertIn("the payment platform returned a declined refund response", str(exception))

    def test_DeclinedRefundExceptionIsCreated_ValidRefundErrorResponse_ExposeExpectedProperties(self):
        refund_result = RefundResponse()
        response = RefundErrorResponse()
        response.refund_result = refund_result
        exception = DeclinedRefundException(402, '{"error":"declined"}', response)

        self.assertEqual(402, exception.status_code)
        self.assertEqual('{"error":"declined"}', exception.response_body)
        self.assertIs(refund_result, exception.refund_response)

    def test_GettingRefundResponse_NullResponse_ReturnNullRefundResponse(self):
        exception = DeclinedRefundException(402, "body", None)
        self.assertIsNone(exception.refund_response)

    def test_GettingRefundResponse_NullRefundResult_ReturnNullRefundResponse(self):
        response = RefundErrorResponse()
        response.refund_result = None
        exception = DeclinedRefundException(402, "body", response)
        self.assertIsNone(exception.refund_response)

    def test_DeclinedRefundExceptionIsCreated_ValidRefundResult_ReturnExpectedMessage(self):
        refund_result = RefundResponse()
        refund_result.id = "refund-id"
        refund_result.status = "REJECTED"
        response = RefundErrorResponse()
        response.refund_result = refund_result
        exception = DeclinedRefundException(402, "body", response)

        self.assertIn("declined refund 'refund-id' with status 'REJECTED'", str(exception))


if __name__ == '__main__':
    unittest.main()
