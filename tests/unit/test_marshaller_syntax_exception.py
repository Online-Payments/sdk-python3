import unittest

from onlinepayments.sdk.json.marshaller_syntax_exception import MarshallerSyntaxException


class MarshallerSyntaxExceptionTest(unittest.TestCase):

    def test_CreatedWithDefaultConstructor_DefaultScenario_HaveNoMessageOrCause(self):
        exception = MarshallerSyntaxException()
        self.assertIsInstance(exception, RuntimeError)
        self.assertEqual("", str(exception))
        self.assertEqual((), exception.args)

    def test_CreatedWithCauseConstructor_DefaultScenario_StoreCause(self):
        cause = ValueError("Invalid JSON")
        exception = MarshallerSyntaxException(cause)

        self.assertIsInstance(exception, RuntimeError)
        self.assertIs(cause, exception.args[0])

    def test_CreatedWithCauseConstructor_DefaultScenario_PropagateCauseAsMessage(self):
        cause = ValueError("Invalid JSON")
        exception = MarshallerSyntaxException(cause)

        self.assertEqual(str(cause), str(exception))


if __name__ == '__main__':
    unittest.main()
