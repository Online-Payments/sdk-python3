import unittest

from onlinepayments.sdk.declined_payout_exception import DeclinedPayoutException
from onlinepayments.sdk.domain.payout_error_response import PayoutErrorResponse
from onlinepayments.sdk.domain.payout_result import PayoutResult


class DeclinedPayoutExceptionTest(unittest.TestCase):

    def test_DeclinedPayoutExceptionIsCreated_NullResponse_ReturnDefaultMessage(self):
        exception = DeclinedPayoutException(402, "body", None)
        self.assertIn("the payment platform returned a declined payout response", str(exception))

    def test_DeclinedPayoutExceptionIsCreated_ValidPayoutErrorResponse_ExposeExpectedProperties(self):
        payout_result = PayoutResult()
        response = PayoutErrorResponse()
        response.payout_result = payout_result
        exception = DeclinedPayoutException(402, '{"error":"declined"}', response)

        self.assertEqual(402, exception.status_code)
        self.assertEqual('{"error":"declined"}', exception.response_body)
        self.assertIs(payout_result, exception.payout_result)

    def test_GettingPayoutResult_NullResponse_ReturnNullPayoutResult(self):
        exception = DeclinedPayoutException(402, "body", None)
        self.assertIsNone(exception.payout_result)

    def test_GettingPayoutResult_NullPayoutResult_ReturnNullPayoutResult(self):
        response = PayoutErrorResponse()
        response.payout_result = None
        exception = DeclinedPayoutException(402, "body", response)
        self.assertIsNone(exception.payout_result)

    def test_DeclinedPayoutExceptionIsCreated_ValidPayoutResult_ReturnExpectedMessage(self):
        payout_result = PayoutResult()
        payout_result.id = "payout-id"
        payout_result.status = "REJECTED"
        response = PayoutErrorResponse()
        response.payout_result = payout_result
        exception = DeclinedPayoutException(402, "body", response)

        self.assertIn("declined payout 'payout-id' with status 'REJECTED'", str(exception))


if __name__ == '__main__':
    unittest.main()
