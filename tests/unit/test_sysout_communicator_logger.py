import io
import re
import sys
import unittest

from onlinepayments.sdk.log.sys_out_communicator_logger import SysOutCommunicatorLogger


class SysOutCommunicatorLoggerTest(unittest.TestCase):

    def setUp(self):
        self.stdout = sys.stdout
        sys.stdout = self.mock_io = io.StringIO()

    def tearDown(self):
        sys.stdout = self.stdout
        self.mock_io.close()

    def test_LoggingMessageOnly_DefaultScenario_WriteMessageToSystemOut(self):
        logger = SysOutCommunicatorLogger.instance()
        logger.log("test 123")

        text = self.mock_io.getvalue()
        self.assertMessage(text, "test 123")

    def test_LoggingMessageWithException_DefaultScenario_WriteMessageAndExceptionStringToSystemOut(self):
        logger = SysOutCommunicatorLogger.instance()
        exception = Exception("something terrible happened /jk")
        logger.log("test 112", exception)

        text = self.mock_io.getvalue()
        self.assertMessage(text, "test 112", exception)

    def test_LoggingMessageWithExceptionWithCause_DefaultScenario_WriteMessageAndExceptionExcludingCauseToSystemOut(self):
        logger = SysOutCommunicatorLogger.instance()
        cause = Exception("Root cause")
        exception = Exception("Top level")
        exception.__cause__ = cause
        logger.log("test cause", exception)

        text = self.mock_io.getvalue()
        self.assertMessage(text, "test cause", exception)
        self.assertNotIn("Root cause", text)
        self.assertNotIn("Caused by", text)

    def test_LoggingEmptyMessage_DefaultScenario_WriteEmptyMessageToSystemOut(self):
        logger = SysOutCommunicatorLogger.instance()
        logger.log("")

        text = self.mock_io.getvalue()
        self.assertMessage(text, "")

    def assertMessage(self, content, message, exception=None):
        message_pattern = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2} (.*)", re.DOTALL)

        expected = message + "\n"
        if exception is not None:
            expected += str(exception) + "\n"
        matcher = message_pattern.match(content)

        self.assertIsNotNone(matcher, "content does not match pattern " + message_pattern.pattern)
        self.assertEqual(expected, matcher.group(1))


if __name__ == '__main__':
    unittest.main()
