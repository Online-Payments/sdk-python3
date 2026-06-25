import unittest

from onlinepayments.sdk.api_exception import ApiException
from onlinepayments.sdk.problem_details_exception import ProblemDetailsException
from onlinepayments.sdk.domain.problem_details_response import ProblemDetailsResponse


def _build(status_code=400, response_body='body', response=None):
    if response is None:
        response = ProblemDetailsResponse()
    return ProblemDetailsException(status_code, response_body, response)


class ProblemDetailsExceptionTest(unittest.TestCase):

    def test_Construction_WithStatusCode_StoreStatusCode(self):
        ex = _build(status_code=422)
        self.assertEqual(422, ex.status_code)

    def test_Construction_WithResponseBody_StoreResponseBody(self):
        ex = _build(response_body='{"type":"problem"}')
        self.assertEqual('{"type":"problem"}', ex.response_body)

    def test_Construction_WithResponseObject_StoreResponseObject(self):
        response = ProblemDetailsResponse()
        ex = ProblemDetailsException(400, 'body', response)
        self.assertIs(response, ex.response)

    def test_Construction_WithNullResponseBody_StoreNullResponseBody(self):
        ex = _build(response_body=None)
        self.assertIsNone(ex.response_body)

    def test_Construction_WithNullResponseObject_StoreNullResponseObject(self):
        ex = ProblemDetailsException(400, 'body', None)
        self.assertIsNone(ex.response)

    def test_GettingResponse_DefaultScenario_ReturnResponsePassedAtConstruction(self):
        response = ProblemDetailsResponse()
        ex = ProblemDetailsException(400, 'body', response)
        self.assertIs(response, ex.response)

    def test_ConvertingToString_DefaultScenario_IncludeProblemDetailsInMessage(self):
        ex = _build()
        self.assertIn('problem details', str(ex))

    def test_Inheritance_DefaultScenario_IsInstanceOfProblemDetailsException(self):
        ex = _build()
        self.assertIsInstance(ex, ProblemDetailsException)

    def test_Inheritance_DefaultScenario_IsInstanceOfApiException(self):
        ex = _build()
        self.assertIsInstance(ex, ApiException)

    def test_Inheritance_DefaultScenario_IsInstanceOfRuntimeError(self):
        ex = _build()
        self.assertIsInstance(ex, RuntimeError)

    def test_Inheritance_DefaultScenario_IsCatchableAsApiException(self):
        ex = _build(500, 'error')
        with self.assertRaises(ApiException):
            raise ex


if __name__ == '__main__':
    unittest.main()
