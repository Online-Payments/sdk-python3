import logging
import unittest

from onlinepayments.sdk.log.python_communicator_logger import PythonCommunicatorLogger


class TestHandler(logging.NullHandler):

    def __init__(self):
        super(TestHandler, self).__init__()
        self.records = []

    def handle(self, record):
        self.records.append(record)


class PythonCommunicatorLoggerTest(unittest.TestCase):

    def setUp(self):
        self.logger = logging.Logger(self.__class__.__name__)
        self.handler = TestHandler()
        self.logger.addHandler(self.handler)

    def tearDown(self):
        self.logger.removeHandler(self.handler)

    def test_ConstructingWithTwoParameters_DefaultScenario_CreateInstanceWithSingleLevel(self):
        communicator_logger = PythonCommunicatorLogger(self.logger, logging.DEBUG)
        self.assertIsNotNone(communicator_logger)

    def test_ConstructingWithTwoParameters_DefaultScenario_UseSameLevelForBothLogAndLogWithThrowable(self):
        communicator_logger = PythonCommunicatorLogger(self.logger, logging.DEBUG)
        communicator_logger.log("Message 1")
        communicator_logger.log("Message 2", Exception())

        self.assertEqual(2, len(self.handler.records))
        self.assertEqual(logging.DEBUG, self.handler.records[0].levelno)
        self.assertEqual(logging.DEBUG, self.handler.records[1].levelno)

    def test_ConstructingWithNullParameters_DefaultScenario_ThrowExceptionWhenLoggerIsNull(self):
        with self.assertRaises(ValueError):
            PythonCommunicatorLogger(None, logging.INFO, logging.WARNING)

    def test_ConstructingWithNullParameters_DefaultScenario_ThrowExceptionWhenLogLevelIsNull(self):
        with self.assertRaises(ValueError):
            PythonCommunicatorLogger(self.logger, None, logging.WARNING)

    def test_ConstructingWithNullParameters_DefaultScenario_CreatesLoggerWhenErrorLogLevelIsNull(self):
        communicator_logger = PythonCommunicatorLogger(self.logger, logging.INFO, None)
        communicator_logger.log("Hello world")

        self.assertEqual(1, len(self.handler.records))
        record = self.handler.records[0]
        self.assertEqual("Hello world", record.msg)
        self.assertEqual("INFO", record.levelname)

    def test_LoggingMessageOnly_DefaultScenario_CreateInfoLogRecord(self):
        communicator_logger = PythonCommunicatorLogger(self.logger, logging.INFO, logging.WARNING)
        communicator_logger.log("Hello world")

        self.assertEqual(1, len(self.handler.records))
        record = self.handler.records[0]
        self.assertEqual("Hello world", record.msg)
        self.assertEqual("INFO", record.levelname)
        self.assertEqual(self.__class__.__name__, record.name)
        self.assertEqual("log", record.funcName)
        self.assertIsNone(record.exc_info)

    def test_LoggingMessageWithException_DefaultScenario_CreateWarningLogRecordWithThrownException(self):
        communicator_logger = PythonCommunicatorLogger(self.logger, logging.INFO, logging.WARNING)
        exception = Exception("foo")
        communicator_logger.log("Hello world", exception)

        self.assertEqual(1, len(self.handler.records))
        record = self.handler.records[0]
        self.assertEqual("Hello world", record.msg)
        self.assertEqual("WARNING", record.levelname)
        self.assertEqual(self.__class__.__name__, record.name)
        self.assertEqual("log", record.funcName)
        self.assertIs(exception, record.args[0])


if __name__ == '__main__':
    unittest.main()
