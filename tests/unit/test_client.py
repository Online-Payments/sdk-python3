import base64
import unittest

from datetime import timedelta
from unittest.mock import Mock, MagicMock

from tests.unit.test_factory import PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY

from onlinepayments.sdk.client import Client
from onlinepayments.sdk.factory import Factory
from onlinepayments.sdk.i_communicator import ICommunicator
from onlinepayments.sdk.communication.connection import Connection
from onlinepayments.sdk.communication.pooled_connection import PooledConnection
from onlinepayments.sdk.communication.request_header import RequestHeader
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller
from onlinepayments.sdk.log.body_obfuscator import BodyObfuscator
from onlinepayments.sdk.log.communicator_logger import CommunicatorLogger
from onlinepayments.sdk.log.header_obfuscator import HeaderObfuscator
from onlinepayments.sdk.merchant.merchant_client import MerchantClient


class ClientTest(unittest.TestCase):

    def test_ClientMetaInfoIsAddedUpdatedAndRemoved_DefaultScenario_ReturnExpectedClientInstances(self):

        client1 = Factory.create_client_from_file(PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)
        client2 = client1.with_client_meta_info(None)
        client3 = client1.with_client_meta_info("")
        client_meta_info = DefaultMarshaller.instance().marshal({"test": "test"})
        client4 = client1.with_client_meta_info(client_meta_info)
        client5 = client4.with_client_meta_info(client_meta_info)
        client6 = client4.with_client_meta_info(None)

        self.assertIsNone(client1._client_headers)
        self.assertIs(client1, client2)
        self.assertIsNot(client1, client3)
        self.assertClientHeaders(client3, "")
        self.assertIsNot(client1, client4)
        self.assertClientHeaders(client4, client_meta_info)
        self.assertIs(client4, client5)
        self.assertIsNot(client4, client6)
        self.assertIsNone(client6._client_headers)

    def test_ClosingIdleConnections_NonPooledConnection_NotThrow(self):
        mock = MagicMock(spec=Connection)
        function_mock = Mock(name="close_idle_connections_mock")
        mock.attach_mock(function_mock, "close_idle_connections")
        communicator = Factory.create_communicator_from_file(configuration_file_name=PROPERTIES_URI,
                                                             api_key_id=API_KEY_ID, secret_api_key=SECRET_API_KEY,
                                                             connection=mock)
        client = Factory.create_client_from_communicator(communicator)
        client.close_idle_connections(timedelta(seconds=5))

        function_mock.assert_not_called()

    def test_ClosingIdleConnections_PooledConnection_DelegateToPooledConnection(self):
        pooled_mock = MagicMock(spec=PooledConnection)
        function_mock = Mock(name="close_idle_connections_mock")
        pooled_mock.attach_mock(function_mock, "close_idle_connections")
        communicator = Factory.create_communicator_from_file(configuration_file_name=PROPERTIES_URI,
                                                             api_key_id=API_KEY_ID, secret_api_key=SECRET_API_KEY,
                                                             connection=pooled_mock)
        client = Factory.create_client_from_communicator(communicator)
        client.close_idle_connections(timedelta(seconds=5))

        function_mock.assert_called_once_with(timedelta(seconds=5))

    def test_ClosingExpiredConnections_NonPooledConnection_NotThrow(self):
        mock = MagicMock(spec=Connection)
        function_mock = Mock(name="close_expired_connections_mock")
        mock.attach_mock(function_mock, "close_expired_connections")
        communicator = Factory.create_communicator_from_file(configuration_file_name=PROPERTIES_URI,
                                                             api_key_id=API_KEY_ID, secret_api_key=SECRET_API_KEY,
                                                             connection=mock)
        client = Factory.create_client_from_communicator(communicator)
        client.close_expired_connections()

        function_mock.assert_not_called()

    def test_ClosingExpiredConnections_PooledConnection_DelegateToPooledConnection(self):
        pooled_mock = MagicMock(spec=PooledConnection)
        function_mock = Mock(name="close_expired_connections_mock")
        pooled_mock.attach_mock(function_mock, "close_expired_connections")
        communicator = Factory.create_communicator_from_file(configuration_file_name=PROPERTIES_URI,
                                                             api_key_id=API_KEY_ID, secret_api_key=SECRET_API_KEY,
                                                             connection=pooled_mock)
        client = Factory.create_client_from_communicator(communicator)
        client.close_expired_connections()

        function_mock.assert_called_once_with()

    def test_EnablingLogging_DefaultScenario_DelegateToCommunicatorWithValidLogger(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        client = Client(mock_communicator)
        mock_logger = MagicMock(spec=CommunicatorLogger)
        client.enable_logging(mock_logger)

        mock_communicator.enable_logging.assert_called_once_with(mock_logger)

    def test_DisablingLogging_DefaultScenario_DelegateToCommunicator(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        client = Client(mock_communicator)
        client.disable_logging()

        mock_communicator.disable_logging.assert_called_once_with()

    def test_EnablingAndDisablingLoggingMultipleTimes_DefaultScenario_DelegateEachCallToCommunicator(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        client = Client(mock_communicator)
        mock_logger1 = MagicMock(spec=CommunicatorLogger)
        mock_logger2 = MagicMock(spec=CommunicatorLogger)

        client.enable_logging(mock_logger1)
        client.disable_logging()
        client.enable_logging(mock_logger2)
        client.disable_logging()

        self.assertEqual(2, mock_communicator.enable_logging.call_count)
        self.assertEqual(2, mock_communicator.disable_logging.call_count)
        mock_communicator.enable_logging.assert_any_call(mock_logger1)
        mock_communicator.enable_logging.assert_any_call(mock_logger2)

    def test_ConstructingClient_DefaultScenario_CreateValidInstanceWithCommunicator(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        client = Client(mock_communicator)

        self.assertIsNotNone(client)
        self.assertIsInstance(client, Client)

    def test_ConstructingClient_DefaultScenario_InheritCommunicatorFromConstructor(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        client = Client(mock_communicator)

        self.assertIs(mock_communicator, client._communicator)

    def test_SettingBodyObfuscator_DefaultScenario_DelegateToCommunicator(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        client = Client(mock_communicator)
        mock_obfuscator = MagicMock(spec=BodyObfuscator)
        client.set_body_obfuscator(mock_obfuscator)

        mock_communicator.set_body_obfuscator.assert_called_once_with(mock_obfuscator)

    def test_SettingBodyObfuscator_DefaultScenario_DelegateNullBodyObfuscator(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        client = Client(mock_communicator)
        client.set_body_obfuscator(None)

        mock_communicator.set_body_obfuscator.assert_called_once_with(None)

    def test_SettingHeaderObfuscator_DefaultScenario_DelegateToCommunicator(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        client = Client(mock_communicator)
        mock_obfuscator = MagicMock(spec=HeaderObfuscator)
        client.set_header_obfuscator(mock_obfuscator)

        mock_communicator.set_header_obfuscator.assert_called_once_with(mock_obfuscator)

    def test_SettingHeaderObfuscator_DefaultScenario_DelegateNullHeaderObfuscator(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        client = Client(mock_communicator)
        client.set_header_obfuscator(None)

        mock_communicator.set_header_obfuscator.assert_called_once_with(None)

    def test_ClosingClient_DefaultScenario_DelegateToCommunicator(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        client = Client(mock_communicator)
        client.close()

        mock_communicator.close.assert_called_once_with()

    def test_ClosingClient_DefaultScenario_HandleIOException(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        mock_communicator.close.side_effect = IOError("connection closed")
        client = Client(mock_communicator)

        with self.assertRaises(IOError):
            client.close()

    def test_ClosingClient_DefaultScenario_BeCloseable(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        client = Client(mock_communicator)

        with client:
            pass

        mock_communicator.close.assert_called_once_with()

    def test_CreatingMerchantClient_DefaultScenario_ReturnMerchantClientInstance(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        client = Client(mock_communicator)
        merchant_client = client.merchant("merchantId")

        self.assertIsNotNone(merchant_client)
        self.assertIsInstance(merchant_client, MerchantClient)

    def test_CreatingMerchantClient_DefaultScenario_CreateMerchantClientWithValidMerchantId(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        client = Client(mock_communicator)
        merchant_client = client.merchant("merchant1")

        self.assertEqual("merchant1", merchant_client._ApiResource__path_context.get("merchantId"))

    def test_CreatingMerchantClient_DefaultScenario_CreateDifferentInstancesForDifferentMerchantIds(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        client = Client(mock_communicator)
        merchant_client1 = client.merchant("merchant1")
        merchant_client2 = client.merchant("merchant2")

        self.assertIsNot(merchant_client1, merchant_client2)

    def test_CreatingMerchantClient_DefaultScenario_HandleEmptyMerchantId(self):
        mock_communicator = MagicMock(spec=ICommunicator)
        client = Client(mock_communicator)
        merchant_client = client.merchant("")

        self.assertIsNotNone(merchant_client)
        self.assertIsInstance(merchant_client, MerchantClient)

    def assertClientHeaders(self, client, client_meta_info):
        headers = client._client_headers
        header_value = base64.b64encode(client_meta_info.encode("utf-8")).decode("utf-8")
        expected = RequestHeader("X-GCS-ClientMetaInfo", header_value)
        found = False
        for header in headers:
            if str(expected) == str(header):
                found = True
                break
        self.assertTrue(found, "header {0} was not found in {1}".format(expected, headers))


if __name__ == '__main__':
    unittest.main()
